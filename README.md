

# Build

```
nix-shell -p python3Package.virtualenv geckodriver
virtualenv venv
source venv/bin/activate
pip3 install selenium beautifulsoup4 pyperclip
```

# Run

```
python3 get_cves.py
```
