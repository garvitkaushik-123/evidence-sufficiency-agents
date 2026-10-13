#!/bin/sh
# Build docs/report.pdf from docs/report.md (needs pandoc and Google Chrome). Usage: sh docs/build_report.sh
set -e
cd "$(dirname "$0")"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
pandoc report.md -s --from markdown+smart --metadata pagetitle="When Is Enough Evidence Enough?" -c report.css -o report.html --resource-path=.
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/report.pdf" "file://$PWD/report.html" 2>/dev/null
pdfinfo report.pdf | grep Pages
