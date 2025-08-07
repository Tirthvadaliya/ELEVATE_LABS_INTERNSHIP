import requests
from bs4 import BeautifulSoup
import os


url = "https://www.bbc.com/news" 


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


headlines = soup.find_all('h2')
headline_texts = [headline.get_text(strip=True) for headline in headlines]


folder_path = r"d:\work\git\GitDemo\ELEVATE_LABS_INTERNSHIP\DAY-3_TASK" 
os.makedirs(folder_path, exist_ok=True)


file_path = os.path.join(folder_path, "headlines.txt")


with open(file_path, "w", encoding="utf-8") as file:
    for line in headline_texts:
        file.write(line + "\n")

print(f"✅ Headlines saved to: {file_path}")