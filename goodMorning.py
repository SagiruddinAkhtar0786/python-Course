# =============================================================================
# TIME MODULE - WORKING WITH TIME
# =============================================================================
# The time module provides functions to work with time and dates

import time

print("=" * 60)
print("WORKING WITH TIME MODULE")
print("=" * 60)

# ===== 1. GET CURRENT LOCAL TIME =====
print("\n1. GET CURRENT LOCAL TIME\n")

# Get current time as a time struct
Time = time.localtime()
Hour = Time.tm_hour
minute = Time.tm_min

print(f"Current local time:")
print(f"  Hour: {Hour}")
print(f"  Minute: {minute}")
print(f"  Time: {Hour}:{minute:02d}")  # :02d pads with zero


# ===== 2. TIME ZONE CONVERSION =====
print("\n" + "=" * 60)
print("2. TIME ZONE CONVERSION (UTC to IST)")
print("=" * 60 + "\n")

# Convert UTC time to Indian Standard Time (IST)
# IST is UTC + 5:30
indianTime = (Hour + 5) % 24  # Add 5 hours
indianMinute = (minute + 30) % 60  # Add 30 minutes

print(f"Local (UTC) time: {Hour}:{minute:02d}")
print(f"Indian (IST) time: {indianTime}:{indianMinute:02d}")
print(f"IST offset from UTC: +5:30")


# ===== 3. FORMATTED TIMESTAMP =====
print("\n" + "=" * 60)
print("3. FORMATTED TIMESTAMP")
print("=" * 60 + "\n")

# Get current timestamp in formatted string
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Current timestamp: {timestamp}")

# More format examples
print("\nOther timestamp formats:")
print(f"  Date only: {time.strftime('%Y-%m-%d', time.localtime())}")
print(f"  Time only: {time.strftime('%H:%M:%S', time.localtime())}")
print(f"  Day of week: {time.strftime('%A', time.localtime())}")
print(f"  Month name: {time.strftime('%B', time.localtime())}")
print(f"  Full date-time: {time.strftime('%c', time.localtime())}")


# ===== 4. TIME COMPONENTS =====
print("\n" + "=" * 60)
print("4. TIME COMPONENTS")
print("=" * 60 + "\n")

t = time.localtime()
print(f"""
Time Components:
  Year (tm_year): {t.tm_year}
  Month (tm_mon): {t.tm_mon}
  Day (tm_mday): {t.tm_mday}
  Hour (tm_hour): {t.tm_hour}
  Minute (tm_min): {t.tm_min}
  Second (tm_sec): {t.tm_sec}
  Weekday (tm_wday): {t.tm_wday} (0=Monday, 6=Sunday)
  Year day (tm_yday): {t.tm_yday} (day of year)
  DST flag (tm_isdst): {t.tm_isdst}
""")