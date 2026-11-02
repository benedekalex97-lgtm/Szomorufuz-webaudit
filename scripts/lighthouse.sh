#!/usr/bin/env bash
# Lighthouse futtatás (mobil és desktop) a kulcsoldalakra, egymás után, szünetekkel.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/data/lighthouse"; mkdir -p "$OUT"
CHROME="$(node -e "console.log(require('playwright').chromium.executablePath())")"
export CHROME_PATH="$CHROME"
FLAGS="--headless=new --no-sandbox --disable-gpu --ignore-certificate-errors"
for slug in "" "hamvasztas-urnakiadas/" "koporsos-temetes/" "arajanlat-keres-itt/" "elerhetoseg/" "teendok-halaleset-utan/"; do
  name="${slug%/}"; name="${name:-home}"
  for ff in mobile desktop; do
    preset=""; [ "$ff" = desktop ] && preset="--preset=desktop"
    lighthouse "https://www.budapest-temetkezes.hu/$slug" $preset --quiet \
      --chrome-flags="$FLAGS" --output=json --output=html \
      --output-path="$OUT/$name-$ff" --max-wait-for-load=60000 || echo "FAIL $name $ff"
    sleep 5
  done
done
