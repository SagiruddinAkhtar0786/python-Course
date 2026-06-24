"""
EXACT SEARCHING ON HINDUSTAN TIMES
Understanding HTML Structure & How to Find Elements
URL: https://www.hindustantimes.com/
"""

import requests
from bs4 import BeautifulSoup
import json

# Step 1: Make the request
url = "https://www.hindustantimes.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("=" * 80)
print("STEP 1: FETCH THE PAGE")
print("=" * 80)
print(f"URL: {url}")
print(f"Headers: {headers}")

response = requests.get(url, headers=headers, timeout=10)
print(f"Status Code: {response.status_code}")
print(f"Response OK: {response.ok}")
print(f"Content Length: {len(response.content)} bytes")

if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Page Title: {soup.title.string if soup.title else 'No title'}\n")
    
    # ========== SEARCH METHOD 1: By TAG ==========
    print("=" * 80)
    print("SEARCH METHOD 1: Find by HTML TAG")
    print("=" * 80)
    print("What: Find all <div> tags")
    print("Code: soup.find_all('div')")
    print("Result:")
    
    divs = soup.find_all('div', limit=5)
    print(f"  • Found {len(soup.find_all('div'))} total <div> elements")
    print(f"  • First 5 <div> tags:")
    for i, div in enumerate(divs):
        print(f"    {i+1}. {str(div)[:100]}...")
    
    # ========== SEARCH METHOD 2: By CLASS ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 2: Find by CLASS attribute")
    print("=" * 80)
    print("What: Find all elements with class 'navbar'")
    print("Code: soup.find_all(class_='navbar')")
    print("Result:")
    
    navbar_elements = soup.find_all(class_='navbar')
    print(f"  • Found {len(navbar_elements)} elements with class 'navbar'")
    if navbar_elements:
        for i, elem in enumerate(navbar_elements[:3]):
            print(f"    {i+1}. {str(elem)[:150]}...")
    else:
        print("  • None found. Trying different class names...")
        # Try other common navbar classes
        for class_name in ['nav', 'header', 'menu', 'top-nav']:
            elements = soup.find_all(class_=class_name)
            if elements:
                print(f"  • Found {len(elements)} elements with class '{class_name}'")
    
    # ========== SEARCH METHOD 3: By ID ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 3: Find by ID attribute")
    print("=" * 80)
    print("What: Find element with id 'header'")
    print("Code: soup.find(id='header')")
    print("Result:")
    
    header = soup.find(id='header')
    if header:
        print(f"  • Found element with id='header'")
        print(f"  • Content (first 200 chars): {str(header)[:200]}...")
    else:
        print("  • Not found. Searching for other common IDs...")
        for id_name in ['main', 'content', 'nav', 'menu', 'navigation']:
            elem = soup.find(id=id_name)
            if elem:
                print(f"  • Found element with id='{id_name}'")
    
    # ========== SEARCH METHOD 4: By TAG + CLASS ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 4: Find by TAG + CLASS combination")
    print("=" * 80)
    print("What: Find all <a> tags with class containing 'link'")
    print("Code: soup.find_all('a', class_='link')")
    print("Result:")
    
    links = soup.find_all('a', limit=10)
    print(f"  • Found {len(soup.find_all('a'))} total <a> (links)")
    print(f"  • First 10 links:")
    for i, link in enumerate(links):
        href = link.get('href', 'No href')
        text = link.get_text(strip=True)[:50]
        print(f"    {i+1}. Text: '{text}' | URL: {href}")
    
    # ========== SEARCH METHOD 5: By ATTRIBUTE ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 5: Find by ATTRIBUTE")
    print("=" * 80)
    print("What: Find elements with href containing 'sports'")
    print("Code: soup.find_all('a', href=lambda x: x and 'sports' in x.lower())")
    print("Result:")
    
    sports_links = soup.find_all('a', href=lambda x: x and 'sports' in x.lower() if x else False)
    print(f"  • Found {len(sports_links)} links with 'sports' in URL")
    for i, link in enumerate(sports_links[:5]):
        print(f"    {i+1}. {link.get_text(strip=True)}: {link.get('href')}")
    
    # ========== SEARCH METHOD 6: By TEXT CONTENT ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 6: Find by TEXT CONTENT")
    print("=" * 80)
    print("What: Find all elements containing text 'Sports'")
    print("Code: soup.find_all(string=lambda text: text and 'Sports' in text)")
    print("Result:")
    
    sports_text = soup.find_all(string=lambda text: text and 'Sports' in str(text) if text else False)
    print(f"  • Found {len(sports_text)} elements containing 'Sports'")
    for i, text in enumerate(sports_text[:5]):
        print(f"    {i+1}. {str(text.strip())[:100]}")
    
    # ========== SEARCH METHOD 7: HIERARCHICAL SEARCH ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 7: HIERARCHICAL SEARCH (Parent > Child)")
    print("=" * 80)
    print("What: Find <nav> then find all <a> inside it")
    print("Code: nav = soup.find('nav'); links = nav.find_all('a') if nav else []")
    print("Result:")
    
    nav = soup.find('nav')
    if nav:
        nav_links = nav.find_all('a', limit=5)
        print(f"  • Found <nav> element")
        print(f"  • Found {len(nav_links)} links inside nav:")
        for i, link in enumerate(nav_links):
            print(f"    {i+1}. {link.get_text(strip=True)}")
    else:
        print("  • <nav> element not found on page")
    
    # ========== SEARCH METHOD 8: SELECT (CSS SELECTOR) ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 8: CSS SELECTOR (Advanced)")
    print("=" * 80)
    print("What: Find all <a> tags with class 'article-link'")
    print("Code: soup.select('a.article-link')")
    print("Result:")
    
    articles = soup.select('a.article-link', limit=5)
    if articles:
        print(f"  • Found {len(articles)} article links")
        for i, article in enumerate(articles):
            print(f"    {i+1}. {article.get_text(strip=True)[:50]}")
    else:
        print("  • No elements found with 'a.article-link'")
        print("  • Trying alternative selectors...")
        alternatives = ['a.link', 'a[href]', 'div.article']
        for selector in alternatives:
            results = soup.select(selector, limit=3)
            if results:
                print(f"  • Found {len(soup.select(selector))} with '{selector}'")
    
    # ========== SEARCH METHOD 9: GET ATTRIBUTES ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 9: EXTRACT SPECIFIC ATTRIBUTES")
    print("=" * 80)
    print("What: Get all href and title from links")
    print("Code: link.get('href'), link.get('title')")
    print("Result:")
    
    all_links = soup.find_all('a', limit=8)
    print(f"  • Extracting attributes from {len(all_links)} links:")
    for i, link in enumerate(all_links):
        href = link.get('href', 'N/A')
        title = link.get('title', 'N/A')
        data_attr = link.get('data-id', 'N/A')
        print(f"    {i+1}. href='{href}' | title='{title}' | data-id='{data_attr}'")
    
    # ========== SEARCH METHOD 10: FILTER WITH FUNCTIONS ==========
    print("\n" + "=" * 80)
    print("SEARCH METHOD 10: CUSTOM FILTER FUNCTIONS")
    print("=" * 80)
    print("What: Find links that have both href and text")
    print("Code: soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get_text())")
    print("Result:")
    
    valid_links = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get_text(strip=True), limit=5)
    print(f"  • Found {len(valid_links)} valid links (with href AND text)")
    for i, link in enumerate(valid_links):
        print(f"    {i+1}. {link.get_text(strip=True)[:40]} -> {link.get('href')[:50]}")
    
    # ========== SUMMARY TABLE ==========
    print("\n" + "=" * 80)
    print("QUICK REFERENCE - ALL SEARCH METHODS")
    print("=" * 80)
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║ METHOD                              │ SYNTAX                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║ 1. Find by TAG                      │ soup.find_all('div')               ║
║ 2. Find by CLASS                    │ soup.find_all(class_='navbar')     ║
║ 3. Find by ID                       │ soup.find(id='header')             ║
║ 4. Find by TAG + CLASS              │ soup.find_all('a', class_='link')  ║
║ 5. Find by ATTRIBUTE                │ soup.find_all('a', href='...')     ║
║ 6. Find by TEXT                     │ soup.find_all(string='Sports')     ║
║ 7. Hierarchical (Parent > Child)    │ parent.find_all('child')           ║
║ 8. CSS SELECTOR                     │ soup.select('a.link')              ║
║ 9. Get ATTRIBUTES                   │ element.get('href')                ║
║ 10. Custom FILTER                   │ soup.find_all(lambda tag: ...)     ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    # ========== PRACTICAL EXAMPLE: GET ALL HEADLINES ==========
    print("\n" + "=" * 80)
    print("PRACTICAL EXAMPLE: Extract ALL HEADLINES")
    print("=" * 80)
    
    headlines = []
    
    # Method 1: Look for common headline tags
    for tag in ['h1', 'h2', 'h3']:
        elements = soup.find_all(tag, limit=10)
        for elem in elements:
            text = elem.get_text(strip=True)
            if text and len(text) > 5:
                headlines.append({
                    'tag': tag,
                    'text': text[:80]
                })
    
    print(f"Found {len(headlines)} headlines:")
    for i, headline in enumerate(headlines[:10]):
        print(f"  {i+1}. [{headline['tag']}] {headline['text']}")

else:
    print(f"Failed to fetch page. Status: {response.status_code}")
