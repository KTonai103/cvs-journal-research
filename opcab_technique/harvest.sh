#!/usr/bin/env bash
# Comprehensive OPCAB technique-paper harvest: CrossRef (per journal) + PubMed (per angle)
set -u
cd "$(dirname "$0")"
RAW=raw
MAIL="ktonai.cs@gmail.com"
UA="OPCAB-research/1.0 (mailto:$MAIL)"

cr() { # crossref: $1=issn $2=label $3=qid $4=query
  curl -s --max-time 40 -A "$UA" \
    "https://api.crossref.org/journals/$1/works?query=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$4")&rows=100&select=DOI,title,published,type,container-title,author,volume,issue,page&mailto=$MAIL" \
    -o "$RAW/cr_${2}_${3}.json"
  n=$(jq -r '.message.items|length' "$RAW/cr_${2}_${3}.json" 2>/dev/null)
  echo "CR $2/$3: ${n:-ERR}"
  sleep 1
}

# ----- CrossRef per journal -----
# technique-focused journals: cast wide
for q in "off-pump coronary artery bypass:opcab" "beating heart coronary:beating" "anaortic coronary:anaortic" "minimally invasive coronary bypass:midcab" "coronary anastomosis technique:anast"; do
  qq="${q%%:*}"; id="${q##*:}"
  cr 2666-2507 jtcvsTech  "$id" "$qq"   # JTCVS Techniques
  cr 2225-319X annCTS     "$id" "$qq"   # Annals of Cardiothoracic Surgery
  cr 1813-9175 mmcts      "$id" "$qq"   # Multimedia Manual CTS
  cr 1522-2942 operTech   "$id" "$qq"   # Operative Techniques Thorac CV Surg
  cr 1559-0879 innov      "$id" "$qq"   # Innovations
done
# general journals: OPCAB-specific queries only
for q in "off-pump coronary artery bypass:opcab" "anaortic no-touch aorta coronary:anaortic"; do
  qq="${q%%:*}"; id="${q##*:}"
  cr 0022-5223 jtcvs   "$id" "$qq"
  cr 0003-4975 ats     "$id" "$qq"
  cr 1010-7940 ejcts   "$id" "$qq"
  cr 1569-9293 icvts   "$id" "$qq"
  cr 1540-8191 jcs     "$id" "$qq"
  cr 1749-8090 jcts    "$id" "$qq"
done

# ----- PubMed per technique angle -----
pm() { # $1=pid $2=query
  ids=$(curl -s --max-time 40 -A "$UA" \
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=80&retmode=json&term=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$2")&email=$MAIL" \
    | jq -r '.esearchresult.idlist|join(",")')
  if [ -n "$ids" ]; then
    curl -s --max-time 40 -A "$UA" \
      "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=$ids&email=$MAIL" \
      -o "$RAW/pm_${1}.json"
    n=$(jq -r '.result.uids|length' "$RAW/pm_${1}.json" 2>/dev/null)
    echo "PM $1: ${n:-ERR}"
  else echo "PM $1: 0"; fi
  sleep 1
}

pm techn 'off-pump coronary artery bypass[Mesh] AND (technique[ti] OR "how I do it"[tiab] OR "operative technique"[tiab] OR "surgical technique"[tiab] OR "how to do it"[tiab])'
pm anaortic '(anaortic[tiab] OR "no touch aorta"[tiab] OR "no-touch aorta"[tiab] OR clampless[tiab]) AND (coronary bypass OR off-pump)'
pm exposure '(deep pericardial[tiab] OR "apical suction"[tiab] OR stabilizer[tiab] OR "heart positioning"[tiab] OR verticalization[tiab] OR enucleation[tiab]) AND off-pump'
pm midcab '(MIDCAB[tiab] OR "minimally invasive direct coronary"[tiab] OR "left anterior small thoracotomy"[tiab] OR LAST[tiab]) AND coronary'
pm roboendo '(robotic[tiab] OR endoscopic[tiab] OR "totally endoscopic"[tiab] OR TECAB[tiab]) AND coronary artery bypass'
pm shunt '(intracoronary shunt[tiab] OR "coronary occlusion"[tiab] OR "blower mister"[tiab] OR mister[tiab]) AND off-pump'
pm flow '(transit time flow[tiab] OR "graft assessment"[tiab] OR "graft patency"[tiab]) AND off-pump coronary'
pm bita 'bilateral internal thoracic[tiab] AND off-pump'
pm hybrid 'hybrid coronary revascularization[tiab]'
pm video '(video[ti] OR multimedia[tiab] OR "video tutorial"[tiab]) AND (off-pump OR coronary artery bypass)'
pm grafts '(sequential[tiab] OR composite[tiab] OR "Y graft"[tiab] OR "T graft"[tiab] OR "I graft"[tiab]) AND off-pump coronary'
pm multivessel '(multivessel[tiab] OR "total arterial"[tiab] OR "complete revascularization"[tiab]) AND off-pump coronary'
pm review 'off-pump coronary artery bypass[Mesh] AND (review[pt] OR systematic[ti] OR meta-analysis[pt])'
pm convert '("conversion to"[tiab] OR bailout[tiab] OR emergency[tiab]) AND off-pump coronary'
pm special '(redo[tiab] OR reoperative[tiab] OR "left main"[tiab] OR "porcelain aorta"[tiab] OR "high risk"[tiab]) AND off-pump coronary bypass'

echo "DONE harvest"
