"""
GET and POST Requests Example using requests library
"""

import requests

print("=" * 70)
print("1. GET REQUEST - Fetch content from Hindustan Times")
print("=" * 70)

try:
    # Simple GET request
    url = "https://www.hindustantimes.com/"
    response = requests.get(url, timeout=10)
    
    print(f"Status Code: {response.status_code}")
    print(f"Content Type: {response.headers.get('Content-Type')}")
    print(f"URL: {response.url}")
    print(f"Content Length: {len(response.content)} bytes")
    
    # Print first 500 characters of content
    print("\nFirst 500 characters of page:")
    print(response.text[:500])
    
except requests.exceptions.RequestException as e:
    print(f"Error during GET request: {e}")


print("\n" + "=" * 70)
print("2. GET REQUEST with HEADERS")
print("=" * 70)

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get("https://www.hindustantimes.com/", headers=headers, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 70)
print("3. GET REQUEST with PARAMETERS")
print("=" * 70)

try:
    params = {
        'page': 1,
        'sort': 'latest'
    }
    
    response = requests.get("https://www.hindustantimes.com/", params=params, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Final URL: {response.url}")
    print(f"Response received: {response.status_code == 200}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 70)
print("4. POST REQUEST - Example (if API endpoint exists)")
print("=" * 70)

try:
    # Example POST request with JSON data
    url = "https://www.hindustantimes.com/"
    
    data = {
        'search': 'Python',
        'category': 'technology'
    }
    
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Note: This might not work if the website doesn't accept POST at root
    response = requests.post(url, json=data, headers=headers, timeout=10)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:300]}")
    
except requests.exceptions.RequestException as e:
    print(f"Error during POST request: {e}")


print("\n" + "=" * 70)
print("5. POST REQUEST - Form Data Example")
print("=" * 70)

try:
    url = "https://www.hindustantimes.com/"
    
    form_data = {
        'username': 'user@example.com',
        'password': 'password123'
    }
    
    response = requests.post(url, data=form_data, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response Length: {len(response.content)} bytes")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 70)
print("6. CHECK RESPONSE STATUS")
print("=" * 70)

try:
    response = requests.get("https://www.hindustantimes.com/", timeout=10)
    
    # Status code checks
    if response.status_code == 200:
        print("✓ Success - Page loaded successfully")
    elif response.status_code == 404:
        print("✗ Not Found - Page doesn't exist")
    elif response.status_code == 500:
        print("✗ Server Error")
    else:
        print(f"Status: {response.status_code}")
    
    # Check if successful
    print(f"Successful: {response.ok}")  # True if status < 400
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


print("\n" + "=" * 70)
print("COMMON STATUS CODES")
print("=" * 70)
print("""
200 - OK (Success)
201 - Created
204 - No Content
301 - Moved Permanently
302 - Found (Redirect)
304 - Not Modified
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Internal Server Error
502 - Bad Gateway
503 - Service Unavailable
""")


print("\n" + "=" * 70)
print("COMMON REQUEST METHODS")
print("=" * 70)
print("""
GET    - Fetch data (no body)
POST   - Submit data (with body)
PUT    - Update entire resource
PATCH  - Partial update
DELETE - Remove resource
HEAD   - Like GET but no response body
""")
