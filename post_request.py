"""
POST REQUEST - Complete Understanding Guide
Learn what POST is and how to use it
"""

import requests
import json

print("=" * 80)
print("WHAT IS A POST REQUEST?")
print("=" * 80)
print("""
POST is used to SEND/SUBMIT DATA to a server

Key Differences:
┌─────────────────────────────────────────────────────────────┐
│ GET Request                  │ POST Request                  │
├──────────────────────────────┼───────────────────────────────┤
│ Retrieves data               │ Sends data                    │
│ Data in URL (visible)        │ Data in body (hidden)         │
│ Limited data size (~2KB)     │ Large data support            │
│ Can be cached                │ Not cached                    │
│ Bookmark-able                │ Not bookmark-able             │
│ Use: Get articles            │ Use: Submit form, login       │
└─────────────────────────────────────────────────────────────┘
""")


print("\n" + "=" * 80)
print("EXAMPLE 1: SIMPLE POST REQUEST - Send JSON Data")
print("=" * 80)

# URL where we send data
url = "https://jsonplaceholder.typicode.com/posts"

# DATA we want to send
data = {
    'title': 'Python Tutorial',
    'body': 'Learning POST requests',
    'userId': 1
}

# HEADERS to tell server what type of data we're sending
headers = {
    'Content-Type': 'application/json'
}

print(f"URL: {url}")
print(f"Data to send: {data}")
print(f"Headers: {headers}")

try:
    # Make POST request
    response = requests.post(url, json=data, headers=headers, timeout=10)
    
    print(f"\nResponse Status Code: {response.status_code}")
    print(f"Response Content:")
    print(json.dumps(response.json(), indent=2))
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 2: POST with FORM DATA (not JSON)")
print("=" * 80)

url = "https://httpbin.org/post"

# Form data (key-value pairs like HTML form)
form_data = {
    'username': 'john_doe',
    'password': '12345',
    'remember': 'on'
}

headers = {
    'User-Agent': 'Mozilla/5.0'
}

print(f"URL: {url}")
print(f"Form Data: {form_data}")

try:
    # POST with form data (not json)
    response = requests.post(url, data=form_data, headers=headers, timeout=10)
    
    print(f"\nResponse Status Code: {response.status_code}")
    print(f"Response Received: {response.ok}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 3: POST REQUEST - Search on Website")
print("=" * 80)

url = "https://httpbin.org/post"

# Search data
search_data = {
    'query': 'Python Programming',
    'category': 'tutorial',
    'page': 1,
    'sort': 'latest'
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

print(f"URL: {url}")
print(f"Search Parameters: {search_data}")

try:
    response = requests.post(url, json=search_data, headers=headers, timeout=10)
    
    print(f"\nResponse Status Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Search submitted successfully!")
        print(f"Response Data: {json.dumps(response.json(), indent=2)[:300]}...")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 4: POST REQUEST - User Login")
print("=" * 80)

url = "https://httpbin.org/post"

# Login credentials
login_data = {
    'email': 'user@example.com',
    'password': 'mypassword123'
}

headers = {
    'Content-Type': 'application/json'
}

print(f"URL: {url}")
print(f"Login Data: {login_data}")

try:
    response = requests.post(url, json=login_data, headers=headers, timeout=10)
    
    print(f"\nResponse Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    if response.status_code == 200:
        print("✓ Login request sent!")
        # In real scenario, server would return token/session
        print("(In real scenario, server would return auth token)")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 5: POST REQUEST - Comment/Comment Submission")
print("=" * 80)

url = "https://httpbin.org/post"

# Comment data
comment_data = {
    'article_id': 123,
    'user_id': 456,
    'comment': 'This is a great article!',
    'rating': 5
}

print(f"URL: {url}")
print(f"Comment Data: {comment_data}")

try:
    response = requests.post(url, json=comment_data)
    
    print(f"\nResponse Status Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Comment submitted successfully!")
        result = response.json()
        print(f"Submitted Data: {result.get('json', {})}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 6: POST REQUEST - Newsletter Subscription")
print("=" * 80)

url = "https://httpbin.org/post"

# Subscription data
subscription = {
    'email': 'subscriber@example.com',
    'name': 'John Doe',
    'categories': ['Politics', 'Sports', 'Technology'],
    'frequency': 'daily'
}

print(f"URL: {url}")
print(f"Subscription Data: {json.dumps(subscription, indent=2)}")

try:
    response = requests.post(url, json=subscription)
    
    print(f"\nResponse Status Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ Newsletter subscription successful!")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 7: POST REQUEST - File Upload")
print("=" * 80)

url = "https://httpbin.org/post"

# File upload
files = {
    'file': open(__file__, 'rb'),  # Read this file
    'document_type': (None, 'Python Script')
}

print(f"URL: {url}")
print(f"Uploading file: {__file__}")

try:
    response = requests.post(url, files=files)
    
    print(f"\nResponse Status Code: {response.status_code}")
    if response.status_code == 200:
        print("✓ File uploaded successfully!")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 8: CHECKING POST RESPONSE")
print("=" * 80)

url = "https://httpbin.org/post"
data = {'test': 'data', 'value': 123}

try:
    response = requests.post(url, json=data)
    
    print("Response Attributes:")
    print(f"  status_code: {response.status_code}")      # HTTP status
    print(f"  headers: {response.headers}")               # Response headers
    print(f"  content: {type(response.content)}")         # Raw bytes
    print(f"  text: {type(response.text)}")               # As text
    print(f"  json(): {type(response.json())}")           # As JSON
    print(f"  ok: {response.ok}")                         # True if status < 400
    print(f"  url: {response.url}")                       # Final URL
    print(f"  history: {response.history}")               # Redirects
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 80)
print("EXAMPLE 9: ERROR HANDLING IN POST")
print("=" * 80)

urls = [
    "https://httpbin.org/post",          # Valid
    "https://httpbin.org/status/404",    # Not found
    "https://httpbin.org/status/500",    # Server error
    "https://invalid-url-that-does-not-exist.com/post"  # Connection error
]

for test_url in urls[:3]:  # Test first 3
    print(f"\nTesting: {test_url}")
    try:
        response = requests.post(test_url, json={'test': 'data'}, timeout=5)
        
        if response.ok:
            print("  ✓ SUCCESS (200)")
        elif response.status_code == 404:
            print("  ✗ NOT FOUND (404)")
        elif response.status_code == 500:
            print("  ✗ SERVER ERROR (500)")
        else:
            print(f"  ✗ ERROR ({response.status_code})")
            
    except requests.exceptions.Timeout:
        print("  ✗ TIMEOUT - Server took too long")
    except requests.exceptions.ConnectionError:
        print("  ✗ CONNECTION ERROR - Can't reach server")
    except requests.exceptions.RequestException as e:
        print(f"  ✗ ERROR: {e}")


print("\n" + "=" * 80)
print("QUICK REFERENCE - POST REQUEST SYNTAX")
print("=" * 80)
print("""
BASIC SYNTAX:
    requests.post(url, json=data, headers=headers, timeout=10)

DIFFERENT WAYS TO SEND DATA:

1. JSON Data:
    response = requests.post(url, json={'key': 'value'})

2. Form Data:
    response = requests.post(url, data={'key': 'value'})

3. Raw String:
    response = requests.post(url, data='raw string')

4. File Upload:
    files = {'file': open('file.txt', 'rb')}
    response = requests.post(url, files=files)

5. With Headers:
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

6. With Timeout:
    response = requests.post(url, json=data, timeout=10)

RESPONSE HANDLING:

    response.status_code    # HTTP status (200, 404, 500, etc.)
    response.ok             # True if status < 400
    response.json()         # Parse as JSON
    response.text           # As plain text
    response.content        # As bytes
    response.headers        # Response headers
    response.cookies        # Cookies from response
""")


print("\n" + "=" * 80)
print("COMMON HTTP STATUS CODES")
print("=" * 80)
print("""
2xx - SUCCESS
  200 OK - Request successful
  201 Created - New resource created
  204 No Content - Success but no response body

3xx - REDIRECT
  301 Moved Permanently
  302 Found
  304 Not Modified

4xx - CLIENT ERROR
  400 Bad Request - Invalid data
  401 Unauthorized - Login required
  403 Forbidden - Access denied
  404 Not Found - Resource doesn't exist

5xx - SERVER ERROR
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable
""")
