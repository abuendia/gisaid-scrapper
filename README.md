# GISAID scrapper
Scrapping tool for GISAID data regarding SARS-CoV-2. You need an active account in order to use it. 

## Preparations
Install all requirements for the scrapper.
```
pip install -r requirements.txt
```
You need to download a ![Firefox WebDriver](https://github.com/mozilla/geckodriver/releases) for your operating system and place it in script's directory.

Your login and password should be provided in `credentials.txt` file in format:
```
login
password
```

## Usage
`python3 gisaid_scrapper_headless.py` should run the scrapper in headless mode. If you need a browser window, you can specify it 
by changing `True` to `False` in the line `scrapper = GisaidCoVScrapper(False)`

## Result
The whole genom sequences from GISAID will be downloaded into `fastas/` directory.

The tool was written for personal use, so little to no maintenance is to be expected.
