#!/usr/bin/env python3
"""
organize_pdfs.py — pdfs/ の重複削除・リネーム・カテゴリ分類

使い方:
  python3 organize_pdfs.py --dry-run   # プレビューのみ（変更なし）
  python3 organize_pdfs.py             # 実行
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

BASE = Path(__file__).parent
PDFS_DIR = BASE / "pdfs"
REF_DIR = BASE / "Reference"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_reference_index() -> dict[str, tuple[str, str]]:
    """Reference/ 以下を再帰的にスキャンし {hash: (category, filename)} を返す"""
    index = {}
    for cat_dir in sorted(REF_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        cat_name = cat_dir.name
        for pdf in sorted(cat_dir.glob("*.pdf")):
            h = sha256(pdf)
            index[h] = (cat_name, pdf.name)
    return index


def collect_pdfs(directory: Path) -> list[Path]:
    """ディレクトリ直下のすべてのファイルを取得（サブディレクトリ除く）"""
    return sorted(f for f in directory.iterdir() if f.is_file())


def log(msg: str):
    print(msg)


def move_or_dry(src: Path, dst: Path):
    if DRY_RUN:
        log(f"  [DRY] MOVE: {src.name!r:<60} → {dst.relative_to(PDFS_DIR)}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        log(f"  MOVED: {src.name!r:<60} → {dst.relative_to(PDFS_DIR)}")


def delete_or_dry(path: Path, reason: str):
    if DRY_RUN:
        log(f"  [DRY] DELETE ({reason}): {path.name!r}")
    else:
        path.unlink()
        log(f"  DELETED ({reason}): {path.name!r}")


def main():
    mode = "DRY-RUN" if DRY_RUN else "EXECUTE"
    log(f"\n{'='*70}")
    log(f"organize_pdfs.py — {mode}")
    log(f"{'='*70}\n")

    # Step 1: Reference/ インデックス構築
    log("[Step 1] Reference/ インデックス構築中...")
    ref_index = build_reference_index()
    log(f"  {len(ref_index)} 件のリファレンスファイルをインデックス化")

    # Reference/ で使われているカテゴリ一覧を収集
    ref_categories = sorted({cat for cat, _ in ref_index.values()})
    log(f"  カテゴリ: {', '.join(ref_categories)}\n")

    # Step 2: カテゴリサブディレクトリ作成
    log("[Step 2] カテゴリディレクトリ作成")
    all_dirs = ref_categories + ["_UNMATCHED"]
    for cat in all_dirs:
        cat_path = PDFS_DIR / cat
        if not DRY_RUN:
            cat_path.mkdir(exist_ok=True)
        log(f"  {'[DRY] ' if DRY_RUN else ''}mkdir: pdfs/{cat}/")

    # Step 3: pdfs/ 直下のファイルを収集
    log("\n[Step 3] pdfs/ 直下のファイルを収集")
    all_files = collect_pdfs(PDFS_DIR)
    pdf_files = [f for f in all_files if f.name != ".gitkeep"]
    log(f"  {len(pdf_files)} 件のファイルを検出（.gitkeep除く）\n")

    # Step 4: ハッシュ計算・マッチング・重複検出
    log("[Step 4] ハッシュ照合・重複検出・移動\n")

    matched = 0
    duplicate_moved = 0
    unmatched = 0

    # 既に使用済みのデスティネーションを追跡（同一ファイルの重複コピーを検出）
    used_destinations: set[str] = set()

    for f in pdf_files:
        log(f"  処理中: {f.name!r}")

        try:
            h = sha256(f)
        except Exception as e:
            log(f"    ERROR: {e}")
            continue

        if h in ref_index:
            cat, ref_name = ref_index[h]
            dst_rel = f"{cat}/{ref_name}"

            if dst_rel in used_destinations:
                # 同内容のファイルが既に処理済み → 重複として削除
                delete_or_dry(f, f"重複コピー（{dst_rel}）")
                duplicate_moved += 1
            else:
                dst = PDFS_DIR / cat / ref_name
                move_or_dry(f, dst)
                used_destinations.add(dst_rel)
                matched += 1
        else:
            # アンマッチ → _UNMATCHED/ へ
            dst_name = f.name if f.suffix else f.name + ".pdf"
            dst = PDFS_DIR / "_UNMATCHED" / dst_name
            move_or_dry(f, dst)
            log(f"    ※ Reference/ にマッチなし → _UNMATCHED/")
            unmatched += 1

    # Step 5: サマリ
    log(f"\n{'='*70}")
    log(f"完了サマリ ({mode})")
    log(f"{'='*70}")
    log(f"  マッチ（リネーム）  : {matched} 件")
    log(f"  重複削除            : {duplicate_moved} 件")
    log(f"  未マッチ            : {unmatched} 件 (_UNMATCHED/ に移動)")
    total = matched + duplicate_moved + unmatched
    log(f"  処理合計            : {total} 件")
    log(f"{'='*70}\n")

    if unmatched > 0:
        log("⚠  _UNMATCHED/ のファイルは手動で paper_list.md と照合してください。")
        log("   pdfinfo <file> または pdftotext <file> - で内容確認できます。\n")


if __name__ == "__main__":
    main()
