"""
GET Request from Hindustan Times
Extracting and Printing Navbar
"""

import requests
from bs4 import BeautifulSoup

print("=" * 70)
print("EXTRACTING NAVBAR FROM HINDUSTAN TIMES")
print("=" * 70)

try:
    # Make GET request
    url = "https://www.hindustantimes.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    print(f"URL Requested: {url}")
    print(f"Headers Sent: {headers}")
    print(f"Response : {response}")
    print(f"Status Code: {response.status_code}")
    print(f"Request Successful: {response.ok}\n")
    
    if response.ok:
        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print("=" * 70)
        print("METHOD 1: Find <nav> Tags")
        print("=" * 70)
        
        # Find all nav elements
        navs = soup.find_all('nav')
        print(f"Found {len(navs)} nav elements\n")
        
        for i, nav in enumerate(navs[:2]):  # Print first 2 navs
            print(f"Nav {i+1}:")
            print(nav.prettify()[:300])  # Print first 300 chars
            print("...\n")
        
        print("=" * 70)
        print("METHOD 2: Find Navigation Links")
        print("=" * 70)
        
        # Find all links in navigation
        links = soup.find_all('a', class_='')
        navbar_links = []
        
        for link in links[:15]:  # Get first 15 links
            href = link.get('href')
            text = link.get_text(strip=True)
            if text and href:
                navbar_links.append({'text': text, 'href': href})
        
        print("Navigation Links:")
        for link in navbar_links[:10]:
            print(f"  • {link['text']}: {link['href']}")
        
        print(f"\nTotal links found: {len(navbar_links)}")
        
        print("\n" + "=" * 70)
        print("METHOD 3: Find Header Section")
        print("=" * 70)
        
        # Find header
        header = soup.find('header')
        if header:
            print("Header found!")
            header_text = header.get_text(strip=True)[:200]
            print(f"Header content (first 200 chars): {header_text}\n")
        
        print("=" * 70)
        print("METHOD 4: Extract Menu Items by Class")
        print("=" * 70)
        
        # Find elements with specific classes
        menu_items = soup.find_all(['a', 'span', 'li'], limit=20)
        
        print("Menu elements:")
        for item in menu_items[:10]:
            text = item.get_text(strip=True)
            if text:
                print(f"  • {text}")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")

except ImportError:
    print("ERROR: BeautifulSoup not installed!")
    print("Install it with: pip install beautifulsoup4")
except Exception as e:
    print(f"Error parsing HTML: {e}")
 