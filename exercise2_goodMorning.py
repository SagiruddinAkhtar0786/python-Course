# =============================================================================
# EXERCISE 2: GOOD MORNING - TIME-BASED GREETINGS
# =============================================================================
# This program demonstrates:
# 1. Functions with delays (time.sleep)
# 2. Current time extraction
# 3. Conditional greetings based on time

import time

print("=" * 60)
print("EXERCISE 2: TIME-BASED GREETING")
print("=" * 60)

# ===== 1. SIMPLE GREETING WITH DELAY =====
print("\n1. SIMPLE GREETING WITH DELAY\n")

def good_morning():
    """Function that says good morning with a delay"""
    print("Good morning!")
    time.sleep(2)  # Wait for 2 seconds (reduced from 10 for testing)
    print("Have a great day!")

print("Calling good_morning()...")
good_morning()


# ===== 2. GET CURRENT TIME =====
print("\n" + "=" * 60)
print("2. GET CURRENT TIME")
print("=" * 60 + "\n")

# Get current time as formatted string
t = time.strftime("%H:%M:%S", time.localtime())
print(f"Current time: {t}")

# Extract hour as integer
hour_from_system = int(time.strftime("%H", time.localtime()))
print(f"Current hour: {hour_from_system}")


# ===== 3. TIME-BASED GREETING =====
print("\n" + "=" * 60)
print("3. TIME-BASED GREETING")
print("=" * 60 + "\n")

hour = int(input("Enter the current hour (0-23): "))

# Determine greeting based on hour
if 5 <= hour < 12:
    greeting = "Good morning!"
elif 12 <= hour < 17:
    greeting = "Good afternoon!"
elif 17 <= hour < 21:
    greeting = "Good evening!"
else:
    greeting = "Good night!"

print(greeting)

# More detailed greeting
if hour < 5:
    print("  It's still early, go back to sleep!")
elif hour < 12:
    print("  Time for breakfast!")
elif hour < 17:
    print("  Hope you're having a productive day!")
elif hour < 21:
    print("  Enjoy your evening!")
else:
    print("  Time to rest!")
elif 17 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")