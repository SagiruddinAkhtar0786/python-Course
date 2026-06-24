"""
NEWS API - Fetch Daily News from Different Topics
Using NewsAPI.org and requests module
Website: https://newsapi.org/
"""

import requests
import json
from datetime import datetime, timedelta

print("=" * 80)
print("NEWS API - FETCH DAILY NEWS BY TOPIC")
print("=" * 80)
print("""
What is NewsAPI?
- Free API to access news articles worldwide
- Get news by keywords, categories, countries, etc.
- Real-time news data from 50,000+ sources
- Documentation: https://newsapi.org/docs

Features:
✓ Search news by keyword
✓ Filter by category (business, sports, technology, etc.)
✓ Filter by country
✓ Sort by relevance, popularity, publishedAt
✓ Get headlines from specific news sources
""")


print("\n" + "=" * 80)
print("STEP 1: GET YOUR API KEY")
print("=" * 80)
print("""
To use NewsAPI:
1. Visit https://newsapi.org/
2. Sign up (free plan available)
3. Copy your API key
4. Replace 'your_api_key_here' with your actual API key below
""")

# Get your free API key from https://newsapi.org/
API_KEY = "your_api_key_here"  # Replace with your actual API key
BASE_URL = "https://newsapi.org/v2"

print(f"API Key: {API_KEY if API_KEY != 'your_api_key_here' else '*** Not configured ***'}")
print(f"Base URL: {BASE_URL}")


print("\n" + "=" * 80)
print("EXAMPLE 1: GET TOP HEADLINES")
print("=" * 80)

url = f"{BASE_URL}/top-headlines"

# Parameters for top headlines
params = {
    "country": "us",      # Country code (us, in, gb, etc.)
    "apiKey": API_KEY
}

print(f"URL: {url}")
print(f"Parameters:")
print(f"  - country: {params['country']}")
print(f"  - Get latest headlines from US\n")

try:
    response = requests.get(url, params=params, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Success! Found {data['totalResults']} headlines\n")
        
        # Print first 5 headlines
        print("TOP 5 HEADLINES:\n")
        for i, article in enumerate(data['articles'][:5], 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.json().get('message', 'Unknown error')}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 2: SEARCH NEWS BY KEYWORD")
print("=" * 80)

url = f"{BASE_URL}/everything"

params = {
    "q": "technology",           # Search keyword
    "sortBy": "publishedAt",     # Sort by published date
    "language": "en",            # English articles
    "pageSize": 5,               # Get 5 results
    "apiKey": API_KEY
}

print(f"URL: {url}")
print(f"Parameters:")
print(f"  - Keyword: {params['q']}")
print(f"  - Language: {params['language']}")
print(f"  - Sort By: {params['sortBy']}")
print(f"  - Results: {params['pageSize']}\n")

try:
    response = requests.get(url, params=params, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Success! Found {data['totalResults']} articles\n")
        
        print("TECHNOLOGY NEWS:\n")
        for i, article in enumerate(data['articles'][:5], 1):
            print(f"{i}. {article['title']}")
            print(f"   Author: {article.get('author', 'Unknown')}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")
    else:
        print(f"Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 3: NEWS BY CATEGORY")
print("=" * 80)

url = f"{BASE_URL}/top-headlines"

categories = ["business", "sports", "entertainment", "health"]

print(f"Fetching top news from multiple categories:\n")

for category in categories:
    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }
    
    print(f"Category: {category.upper()}")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data['articles']:
                # Print top article from this category
                article = data['articles'][0]
                print(f"  ✓ Top Story: {article['title'][:60]}...")
                print(f"  Source: {article['source']['name']}")
            else:
                print(f"  No articles found")
        else:
            print(f"  Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
    
    print()


print("\n" + "=" * 80)
print("EXAMPLE 4: NEWS FROM SPECIFIC SOURCES")
print("=" * 80)

url = f"{BASE_URL}/top-headlines"

sources_list = ["bbc-news", "cnn", "reuters"]

print(f"Fetching news from multiple sources:\n")

for source in sources_list:
    params = {
        "sources": source,
        "apiKey": API_KEY
    }
    
    print(f"Source: {source.upper()}")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"  ✓ Found {len(data['articles'])} articles")
            
            if data['articles']:
                article = data['articles'][0]
                print(f"  Latest: {article['title'][:50]}...")
        else:
            print(f"  Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
    
    print()


print("\n" + "=" * 80)
print("EXAMPLE 5: NEWS FROM SPECIFIC COUNTRY")
print("=" * 80)

url = f"{BASE_URL}/top-headlines"

countries = {
    "us": "United States",
    "in": "India",
    "gb": "United Kingdom",
    "au": "Australia"
}

print(f"Top headlines from different countries:\n")

for code, country_name in countries.items():
    params = {
        "country": code,
        "apiKey": API_KEY
    }
    
    print(f"{country_name}:")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"  ✓ {len(data['articles'])} headlines available")
            
            if data['articles']:
                article = data['articles'][0]
                print(f"  Top: {article['title'][:50]}...")
        else:
            print(f"  Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
    
    print()


print("\n" + "=" * 80)
print("EXAMPLE 6: SEARCH WITH DATE RANGE")
print("=" * 80)

url = f"{BASE_URL}/everything"

# Get news from last 7 days
today = datetime.now()
week_ago = today - timedelta(days=7)

params = {
    "q": "artificial intelligence",
    "from": week_ago.strftime("%Y-%m-%d"),
    "to": today.strftime("%Y-%m-%d"),
    "sortBy": "relevance",
    "language": "en",
    "pageSize": 5,
    "apiKey": API_KEY
}

print(f"URL: {url}")
print(f"Search: Artificial Intelligence news from last 7 days")
print(f"From: {params['from']}")
print(f"To: {params['to']}\n")

try:
    response = requests.get(url, params=params, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Found {data['totalResults']} articles about AI\n")
        
        for i, article in enumerate(data['articles'][:5], 1):
            print(f"{i}. {article['title']}")
            print(f"   Published: {article['publishedAt'][:10]}")
            print(f"   Source: {article['source']['name']}\n")
    else:
        print(f"Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("QUICK REFERENCE - NEWS API ENDPOINTS")
print("=" * 80)
print("""
ENDPOINT 1: Top Headlines
URL: https://newsapi.org/v2/top-headlines
Parameters:
  - country: Country code (us, in, gb, au, etc.)
  - category: business, entertainment, health, science, sports, technology
  - sources: Specific news source
Example: GET /top-headlines?country=us&category=sports&apiKey=KEY

ENDPOINT 2: Everything
URL: https://newsapi.org/v2/everything
Parameters:
  - q: Search keyword (required)
  - from: Start date (YYYY-MM-DD)
  - to: End date (YYYY-MM-DD)
  - language: Language code (en, es, fr, etc.)
  - sortBy: relevancy, popularity, publishedAt
  - pageSize: Number of articles (max 100)
Example: GET /everything?q=technology&language=en&apiKey=KEY

SORTING OPTIONS:
  - relevancy: Most relevant first
  - popularity: Most popular first
  - publishedAt: Most recent first

COMMON COUNTRY CODES:
  us = United States      in = India          gb = United Kingdom
  au = Australia          ca = Canada         fr = France
  de = Germany            it = Italy          es = Spain
  br = Brazil             mx = Mexico         jp = Japan
  ru = Russia             cn = China          in = India
""")


print("\n" + "=" * 80)
print("HOW TO GET YOUR API KEY")
print("=" * 80)
print("""
Step 1: Visit https://newsapi.org/
Step 2: Click "Register" or "Sign Up"
Step 3: Fill in your details (email, password, etc.)
Step 4: Verify your email
Step 5: Go to Dashboard
Step 6: Copy your API Key
Step 7: Replace 'your_api_key_here' in this script with your API key

Free Plan Includes:
✓ 100 requests per day
✓ All endpoints access
✓ Search up to 1 month old articles
✓ Basic sorting options
""")
