"""AsyncIO examples for concurrent programming."""

import asyncio
import time

# Example 1: Simple async function with await
# async defines a coroutine, await pauses execution until the coroutine completes

async def greet(name, delay):
    print(f"Hello {name}! Starting...")
    await asyncio.sleep(delay)  # Simulate waiting for I/O (like network request)
    print(f"Hello {name}! Done!")
    return f"Greeted {name}"


# Example 2: Run multiple tasks concurrently
# gather() waits for all tasks to complete and returns results

async def main():
    print("=== Concurrent Execution ===")
    # Create multiple tasks that run at the same time
    result1 = asyncio.create_task(greet("Alice", 2))
    result2 = asyncio.create_task(greet("Bob", 1))
    result3 = asyncio.create_task(greet("Charlie", 3))

    # Wait for all tasks to complete
    results = await asyncio.gather(result1, result2, result3)
    print("All results:", results)


# Example 3: Simulating concurrent file operations
async def fetch_data(user_id, delay):
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Data for user {user_id} received!")
    return f"User {user_id} data"


async def fetch_multiple_users():
    print("\n=== Fetching Multiple Users Concurrently ===")
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3),
    ]
    results = await asyncio.gather(*tasks)
    return results


# Example 4: Using asyncio.run() to execute async functions

if __name__ == "__main__":
    # Measure time for sequential execution
    print("Sequential time reference:")
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Execution time: {end - start:.2f} seconds\n")

    # Fetch multiple users concurrently
    start = time.perf_counter()
    results = asyncio.run(fetch_multiple_users())
    end = time.perf_counter()
    print(f"Concurrent execution time: {end - start:.2f} seconds")
    print("Fetched data:", results)
