"""
LESSON 1: Web Scraping with BeautifulSoup
Web scraping extracts data directly from HTML pages when no public API exists.
"""

from bs4 import BeautifulSoup
import requests

# HTML content simulating a blog or news feed
sample_html = """
<html>
  <body>
    <div class="article">
      <h2 class="title">Python 3.12 Released</h2>
      <p class="author">By Alex</p>
    </div>
    <div class="article">
      <h2 class="title">Building Web Bots</h2>
      <p class="author">By Sam</p>
    </div>
  </body>
</html>
"""

# Parse HTML string using BeautifulSoup
soup = BeautifulSoup(sample_html, "html.parser")

# Find all elements matching a CSS class
articles = soup.find_all("div", class_="article")

print("--- Scraped Articles ---")
for art in articles:
    title = art.find("h2", class_="title").text
    author = art.find("p", class_="author").text
    print(f"📖 {title} ({author})")

# Live Web Scraping Example (Scraping quotes site)
print("\n--- Scraping Live Quotes Page ---")
try:
    res = requests.get("https://quotes.toscrape.com/", timeout=5)
    live_soup = BeautifulSoup(res.text, "html.parser")
    
    first_quote = live_soup.find("span", class_="text").text
    quote_author = live_soup.find("small", class_="author").text
    
    print(f"Quote: {first_quote}")
    print(f"Author: {quote_author}")
except Exception as e:
    print(f"❌ Scraping error: {e}")

# ✏️ PRACTICE EXERCISE:
# Modify the live scrape block to loop through and print the top 3 quotes instead of just the first one!
