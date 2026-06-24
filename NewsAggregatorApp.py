"""
COMPLETE NEWS AGGREGATOR APPLICATION
Combines GET/POST requests, Web Scraping, and News API
Features: Search, Filter, Save, Display News
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

print("=" * 100)
print("WELCOME TO NEWS AGGREGATOR APP")
print("=" * 100)
print("""
This application demonstrates:
✓ GET requests (fetch data)
✓ POST requests (send data)
✓ Web scraping with BeautifulSoup
✓ API integration
✓ Data processing and display
✓ File operations (save/read)
""")


class NewsAggregator:
    """Complete News Aggregator with multiple sources"""
    
    def __init__(self):
        self.news_data = []
        self.saved_articles = []
        self.api_key = "d135ac35a3b0441a9a35562bb4cc315e"  # Replace with real key from newsapi.org
        
    def get_top_headlines(self):
        """GET Request - Fetch top headlines"""
        print("\n" + "=" * 100)
        print("FETCHING TOP HEADLINES (GET REQUEST)")
        print("=" * 100)
        
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": "us",
            "apiKey": self.api_key
        }
        
        print(f"URL: {url}")
        print(f"Parameters: {params}\n")
        
        try:
            response = requests.get(url, params=params, timeout=10)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Success! Found {data['totalResults']} headlines\n")
                
                # Process and store articles
                for article in data['articles'][:5]:
                    self.news_data.append({
                        'title': article['title'],
                        'source': article['source']['name'],
                        'url': article['url'],
                        'published': article['publishedAt'],
                        'category': 'Top Headlines'
                    })
                
                # Display headlines
                self.display_articles(self.news_data[-5:])
            else:
                print(f"Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def search_news(self, keyword):
        """GET Request - Search news by keyword"""
        print("\n" + "=" * 100)
        print(f"SEARCHING NEWS FOR: '{keyword}' (GET REQUEST)")
        print("=" * 100)
        
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": keyword,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 5,
            "apiKey": self.api_key
        }
        
        print(f"URL: {url}")
        print(f"Search Keyword: {keyword}\n")
        
        try:
            response = requests.get(url, params=params, timeout=10)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {data['totalResults']} articles\n")
                
                # Store search results
                for article in data['articles'][:5]:
                    self.news_data.append({
                        'title': article['title'],
                        'source': article['source']['name'],
                        'url': article['url'],
                        'published': article['publishedAt'],
                        'category': f'Search: {keyword}'
                    })
                
                self.display_articles(self.news_data[-5:])
            else:
                print(f"Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def scrape_hindustan_times(self):
        """Web Scraping - Extract news from Hindustan Times"""
        print("\n" + "=" * 100)
        print("SCRAPING HINDUSTAN TIMES (WEB SCRAPING)")
        print("=" * 100)
        
        url = "https://www.hindustantimes.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        print(f"URL: {url}")
        print("Making GET request to Hindustan Times...\n")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find all headlines/links
                links = soup.find_all('a', limit=10)
                
                print(f"✓ Found {len(links)} links\n")
                print("EXTRACTED HEADLINES:\n")
                
                for i, link in enumerate(links[:5], 1):
                    text = link.get_text(strip=True)
                    href = link.get('href', '#')
                    
                    if text and len(text) > 5:
                        print(f"{i}. {text[:80]}")
                        print(f"   URL: {href}\n")
                        
                        self.news_data.append({
                            'title': text[:100],
                            'source': 'Hindustan Times',
                            'url': href,
                            'published': datetime.now().isoformat(),
                            'category': 'Web Scrape'
                        })
            else:
                print(f"Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def submit_comment(self, article_title, comment_text, rating):
        """POST Request - Submit comment on article"""
        print("\n" + "=" * 100)
        print("SUBMITTING COMMENT (POST REQUEST)")
        print("=" * 100)
        
        url = "https://httpbin.org/post"  # Using public test endpoint
        
        comment_data = {
            "articleTitle": article_title,
            "commentText": comment_text,
            "rating": rating,
            "timestamp": datetime.now().isoformat()
        }
        
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        
        print(f"URL: {url}")
        print(f"Article: {article_title}")
        print(f"Comment: {comment_text}")
        print(f"Rating: {'⭐' * rating}\n")
        
        try:
            response = requests.post(url, json=comment_data, headers=headers, timeout=10)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                print("✓ Comment submitted successfully!")
                print(f"Response: {json.dumps(response.json(), indent=2)[:200]}...")
            else:
                print(f"Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def save_article(self, article):
        """Save article to favorites"""
        print("\n" + "=" * 100)
        print("SAVING ARTICLE TO FAVORITES")
        print("=" * 100)
        
        self.saved_articles.append({
            **article,
            'saved_date': datetime.now().isoformat()
        })
        
        print(f"✓ Saved: {article['title'][:60]}...")
        print(f"Total saved: {len(self.saved_articles)}")
    
    def display_articles(self, articles):
        """Display articles in formatted output"""
        print("=" * 100)
        print("ARTICLES:")
        print("=" * 100 + "\n")
        
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']}")
            print(f"   Category: {article['category']}")
            print(f"   Published: {article['published']}")
            print(f"   URL: {article['url'][:70]}...")
            print()
    
    def filter_by_source(self, source):
        """Filter articles by source"""
        print("\n" + "=" * 100)
        print(f"FILTERING ARTICLES BY SOURCE: {source}")
        print("=" * 100 + "\n")
        
        filtered = [a for a in self.news_data if a['source'].lower() == source.lower()]
        
        if filtered:
            print(f"Found {len(filtered)} articles from {source}\n")
            self.display_articles(filtered)
        else:
            print(f"No articles found from {source}")
    
    def filter_by_category(self, category):
        """Filter articles by category"""
        print("\n" + "=" * 100)
        print(f"FILTERING ARTICLES BY CATEGORY: {category}")
        print("=" * 100 + "\n")
        
        filtered = [a for a in self.news_data if category.lower() in a['category'].lower()]
        
        if filtered:
            print(f"Found {len(filtered)} articles in {category}\n")
            self.display_articles(filtered)
        else:
            print(f"No articles found in {category}")
    
    def export_to_json(self, filename="news_data.json"):
        """Export news data to JSON file"""
        print("\n" + "=" * 100)
        print(f"EXPORTING DATA TO {filename}")
        print("=" * 100)
        
        data = {
            'total_articles': len(self.news_data),
            'total_saved': len(self.saved_articles),
            'exported_at': datetime.now().isoformat(),
            'articles': self.news_data,
            'saved_articles': self.saved_articles
        }
        
        filepath = os.path.join(os.getcwd(), filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Data exported to: {filepath}")
        print(f"  - Total articles: {len(self.news_data)}")
        print(f"  - Saved articles: {len(self.saved_articles)}")
    
    def display_summary(self):
        """Display application summary"""
        print("\n" + "=" * 100)
        print("APPLICATION SUMMARY")
        print("=" * 100)
        print(f"""
Total Articles Fetched: {len(self.news_data)}
Saved Articles: {len(self.saved_articles)}

Sources:
  {', '.join(set([a['source'] for a in self.news_data]))}

Categories:
  {', '.join(set([a['category'] for a in self.news_data]))}

Methods Used:
  ✓ GET requests (fetch headlines, search)
  ✓ POST requests (submit comments)
  ✓ Web scraping (Hindustan Times)
  ✓ Data filtering and processing
  ✓ File export (JSON)
""")


# ============================================================================
# MAIN APPLICATION - RUN ALL DEMONSTRATIONS
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    
    # Create news aggregator instance
    app = NewsAggregator()
    
    print("\n" + "=" * 100)
    print("STARTING NEWS AGGREGATOR APPLICATION")
    print("=" * 100)
    
    # Example 1: Get top headlines (GET)
    print("\n[1/6] Fetching top headlines...")
    app.get_top_headlines()
    
    # Example 2: Search news (GET)
    print("\n[2/6] Searching for 'Python'...")
    app.search_news("Python")
    
    # Example 3: Scrape Hindustan Times (Web Scraping)
    print("\n[3/6] Scraping Hindustan Times...")
    app.scrape_hindustan_times()
    
    # Example 4: Submit comment (POST)
    print("\n[4/6] Submitting comment...")
    app.submit_comment(
        article_title="AI News Article",
        comment_text="Very informative article about artificial intelligence!",
        rating=5
    )
    
    # Example 5: Save article
    print("\n[5/6] Saving article...")
    if app.news_data:
        app.save_article(app.news_data[0])
    
    # Example 6: Display summary and export
    print("\n[6/6] Generating summary...")
    app.display_summary()
    
    # Export to JSON
    app.export_to_json()
    
    # Filter demonstrations
    print("\n" + "=" * 100)
    print("FILTER DEMONSTRATIONS")
    print("=" * 100)
    
    app.filter_by_category("Top Headlines")
    app.filter_by_source("BBC News")
    
    # Completion message
    print("\n" + "=" * 100)
    print("APPLICATION COMPLETED SUCCESSFULLY!")
    print("=" * 100)
    print("""
What was demonstrated:
1. ✓ GET Requests - Fetch data from APIs
2. ✓ POST Requests - Submit data to servers
3. ✓ Web Scraping - Extract data from websites
4. ✓ Data Processing - Filter, organize, display
5. ✓ File Operations - Export data to JSON
6. ✓ Error Handling - Handle exceptions gracefully

Key Concepts Learned:
• HTTP Methods (GET, POST)
• API Integration
• BeautifulSoup Web Scraping
• JSON Data Format
• Error Handling with try-except
• Data Filtering and Transformation
""")


if __name__ == "__main__":
    main()
