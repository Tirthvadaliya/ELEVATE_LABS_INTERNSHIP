#  News Headlines Data Collection

This Python script (`datacollection.py`) collects the latest news headlines from the [BBC News](https://www.bbc.com/news) website and saves them to a text file.

## Features

- Fetches the BBC News homepage
- Extracts all headlines inside `<h2>` tags
- Saves the headlines to `headlines.txt` in the same folder

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:
```sh
pip install requests beautifulsoup4
```

## Usage

1. Run the script:
   ```sh
   python datacollection.py
   ```
2. After running, check the `headlines.txt` file in the same directory for the list of headlines.

## File Structure

- `datacollection.py` : Script to fetch and save BBC News headlines
- `headlines.txt` : Output file containing