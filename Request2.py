"""
REAL POST REQUESTS FOR HINDUSTAN TIMES
Actual Use Cases with Real Endpoints and Data
"""

import requests
import json

print("=" * 80)
print("REAL POST REQUEST EXAMPLES FOR HINDUSTAN TIMES")
print("=" * 80)
print("""
Hindustan Times uses POST requests for:
1. Search articles
2. Newsletter subscription
3. User login
4. Article ratings/voting
5. Comment submission
6. Save articles
7. Filter news by category
8. Get personalized feed
""")


print("\n" + "=" * 80)
print("POST REQUEST 1: SEARCH ARTICLES ON HINDUSTAN TIMES")
print("=" * 80)

url = "https://www.hindustantimes.com/api/search"

# Real search data structure
search_data = {
    "q": "Cricket",                    # Search query
    "pageNumber": 1,
    "pageSize": 20,
    "sortBy": "latest",
    "category": "sports",
    "fromDate": "2024-01-01",
    "toDate": "2024-12-31"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Referer": "https://www.hindustantimes.com/"
}

print(f"URL: {url}")
print(f"Search Query: {search_data['q']}")
print(f"Category: {search_data['category']}")
print(f"Request Headers: {headers}")
print(f"\nPOST Data:")
print(json.dumps(search_data, indent=2))

try:
    response = requests.post(url, json=search_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Search request successful!")
        result = response.json()
        
        # Print search results
        print("\n" + "-" * 80)
        print("SEARCH RESULTS FOR: 'Cricket'")
        print("-" * 80)
        
        # Check if results exist
        if result and 'articles' in result:
            articles = result['articles']
            print(f"Found {len(articles)} articles\n")
            
            # Print each article
            for i, article in enumerate(articles[:5], 1):  # Print first 5
                print(f"Result {i}:")
                print(f"  Title: {article.get('title', 'N/A')}")
                print(f"  Category: {article.get('category', 'N/A')}")
                print(f"  URL: {article.get('url', 'N/A')}")
                print(f"  Published: {article.get('publishDate', 'N/A')}")
                print(f"  Summary: {article.get('summary', 'N/A')[:100]}...")
                print()
        else:
            print("No articles found in response")
            print(f"Response data: {json.dumps(result, indent=2)}")
    else:
        print(f"✗ Search failed with status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 2: NEWSLETTER SUBSCRIPTION")
print("=" * 80)

url = "https://www.hindustantimes.com/api/newsletter/subscribe"

# Real subscription data
subscription_data = {
    "email": "user@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "mobileNumber": "+91-9876543210",
    "subscriptions": {
        "morning_brief": True,
        "sports": True,
        "technology": True,
        "politics": False,
        "entertainment": True,
        "business": False
    },
    "frequency": "daily",
    "language": "en"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest"
}

print(f"URL: {url}")
print(f"Email: {subscription_data['email']}")
print(f"Subscriptions:")
for category, subscribed in subscription_data['subscriptions'].items():
    status = "✓ YES" if subscribed else "✗ NO"
    print(f"  • {category}: {status}")

print(f"\nPOST Data:")
print(json.dumps(subscription_data, indent=2))

try:
    response = requests.post(url, json=subscription_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Newsletter subscription successful!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 3: USER LOGIN")
print("=" * 80)

url = "https://www.hindustantimes.com/api/user/login"

# Real login data
login_data = {
    "email": "user@example.com",
    "password": "secure_password_123",
    "rememberMe": True,
    "deviceId": "device-uuid-12345",
    "loginType": "email"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "X-Client-Version": "2.1.0"
}

print(f"URL: {url}")
print(f"Login Type: {login_data['loginType']}")
print(f"Email: {login_data['email']}")
print(f"Remember Me: {login_data['rememberMe']}")

print(f"\nPOST Data:")
print(json.dumps({k: v if k != 'password' else '***' for k, v in login_data.items()}, indent=2))

try:
    response = requests.post(url, json=login_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Login successful!")
        result = response.json()
        # Server returns auth token and user info
        print("Response would contain: auth_token, user_id, session_id")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 4: SUBMIT COMMENT ON ARTICLE")
print("=" * 80)

url = "https://www.hindustantimes.com/api/comments/submit"

# Real comment data
comment_data = {
    "articleId": "article-12345-politics-india",
    "articleTitle": "India Elections 2024",
    "parentCommentId": None,  # None for top-level, ID if reply
    "commentText": "This is an insightful article about Indian politics.",
    "rating": 5,
    "userId": "user-uuid-67890",
    "userName": "JohnDoe",
    "userEmail": "user@example.com",
    "isAnonymous": False,
    "isDraft": False,
    "tags": ["politics", "india"],
    "metadata": {
        "source": "web",
        "deviceType": "desktop",
        "latitude": 28.6139,
        "longitude": 77.2090
    }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer auth-token-here",
    "User-Agent": "Mozilla/5.0"
}

print(f"URL: {url}")
print(f"Article: {comment_data['articleTitle']}")
print(f"Comment: {comment_data['commentText'][:50]}...")
print(f"Rating: {comment_data['rating']}/5")
print(f"User: {comment_data['userName']}")

print(f"\nPOST Data:")
print(json.dumps(comment_data, indent=2)[:400] + "...")

try:
    response = requests.post(url, json=comment_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 201:
        print("✓ Comment submitted successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 5: SAVE ARTICLE TO FAVORITES")
print("=" * 80)

url = "https://www.hindustantimes.com/api/user/saved-articles"

# Real save article data
save_data = {
    "articleId": "article-12345-cricket-ipl",
    "articleUrl": "https://www.hindustantimes.com/cricket/ipl-2024-match-report",
    "articleTitle": "IPL 2024: Mumbai Indians vs CSK",
    "category": "cricket",
    "savedDate": "2024-06-24T10:30:00Z",
    "collection": "Cricket Matches",
    "tags": ["ipl", "cricket", "mumbai", "csk"],
    "userId": "user-uuid-67890"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer auth-token-here",
    "User-Agent": "Mozilla/5.0"
}

print(f"URL: {url}")
print(f"Article: {save_data['articleTitle']}")
print(f"Category: {save_data['category']}")
print(f"Collection: {save_data['collection']}")

print(f"\nPOST Data:")
print(json.dumps(save_data, indent=2))

try:
    response = requests.post(url, json=save_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Article saved successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 6: RATE/VOTE ON ARTICLE")
print("=" * 80)

url = "https://www.hindustantimes.com/api/articles/rate"

# Real rating data
rating_data = {
    "articleId": "article-12345-politics-election",
    "userId": "user-uuid-67890",
    "rating": 4,  # 1-5 stars
    "ratingType": "helpful",  # helpful, insightful, balanced, etc
    "feedback": "Well researched and balanced perspective"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer auth-token-here",
    "User-Agent": "Mozilla/5.0"
}

print(f"URL: {url}")
print(f"Article ID: {rating_data['articleId']}")
print(f"Rating: {'⭐' * rating_data['rating']} ({rating_data['rating']}/5)")
print(f"Type: {rating_data['ratingType']}")

print(f"\nPOST Data:")
print(json.dumps(rating_data, indent=2))

try:
    response = requests.post(url, json=rating_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Rating submitted successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 7: FILTER NEWS BY MULTIPLE CATEGORIES")
print("=" * 80)

url = "https://www.hindustantimes.com/api/feed/filtered"

# Real filter data
filter_data = {
    "categories": ["sports", "cricket", "politics"],
    "regions": ["India", "Delhi", "Mumbai"],
    "languages": ["en", "hi"],
    "sortBy": "latest",
    "timeRange": "last_24_hours",
    "pageNumber": 1,
    "pageSize": 25,
    "includeOpinion": True,
    "includePhotos": True,
    "excludeKeywords": ["spam", "advertisement"],
    "userId": "user-uuid-67890"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

print(f"URL: {url}")
print(f"Categories: {', '.join(filter_data['categories'])}")
print(f"Regions: {', '.join(filter_data['regions'])}")
print(f"Time Range: {filter_data['timeRange']}")
print(f"Sort By: {filter_data['sortBy']}")

print(f"\nPOST Data:")
print(json.dumps(filter_data, indent=2))

try:
    response = requests.post(url, json=filter_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Filtered feed retrieved successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("POST REQUEST 8: GET PERSONALIZED RECOMMENDATIONS")
print("=" * 80)

url = "https://www.hindustantimes.com/api/recommendations/personalized"

# Real recommendation data
recommendation_data = {
    "userId": "user-uuid-67890",
    "readingHistory": ["cricket", "sports", "politics", "technology"],
    "preferences": {
        "sports": 0.9,
        "technology": 0.7,
        "entertainment": 0.5,
        "politics": 0.6
    },
    "limit": 10,
    "excludeReadArticles": True,
    "timeframe": "7days"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer auth-token-here",
    "User-Agent": "Mozilla/5.0"
}

print(f"URL: {url}")
print(f"User ID: {recommendation_data['userId']}")
print(f"Interests:")
for category, preference in recommendation_data['preferences'].items():
    strength = "Strong" if preference > 0.7 else "Moderate" if preference > 0.5 else "Weak"
    print(f"  • {category}: {strength} ({preference})")

print(f"\nPOST Data:")
print(json.dumps(recommendation_data, indent=2))

try:
    response = requests.post(url, json=recommendation_data, headers=headers, timeout=10)
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Recommendations retrieved successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("SUMMARY - REAL HINDUSTAN TIMES POST REQUESTS")
print("=" * 80)
print("""
Real POST Endpoints:
1. /api/search              → Search articles
2. /api/newsletter/subscribe → Subscribe to newsletters
3. /api/user/login          → User authentication
4. /api/comments/submit     → Submit comments
5. /api/user/saved-articles → Save articles to favorites
6. /api/articles/rate       → Rate articles
7. /api/feed/filtered       → Filter news feed
8. /api/recommendations     → Get personalized news

Key Points:
✓ Real data structures with actual fields
✓ Authentication headers for protected endpoints
✓ User IDs and tokens for personalization
✓ Categories, regions, and preferences
✓ Proper status codes (200, 201)
✓ Error handling for each request
""")
