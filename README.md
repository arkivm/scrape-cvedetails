# Scrape CVEs from cvedetails.com

The old interface of cvedetails.com had a way to export data as a CSV, but it
is no longer the case. To avoid the boring work of clicking copy from every
page and pasting it into a csv file, this script automates scraping the webpage
to save the CVEs as a csv.

It uses selenium framework to invoke a browser and click the copy button. There
should be a way in javascript/tampermonkey to do it too.

# Build

```
nix-shell -p python3Packages.virtualenv geckodriver
virtualenv venv
source venv/bin/activate
pip3 install selenium beautifulsoup4 pyperclip
```

# Run

```
python3 get_cves.py
```

# Extract CVEs (year, total CVEs, driver CVEs)
```
./get_cves.sh
```
