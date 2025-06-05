import asyncio
from playwright.async_api import async_playwright
import psutil
import time
import matplotlib.pyplot as plt

total_runs = 5  # Number of times to run the test

def get_system_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_usage = memory_info.rss / (1024 ** 2)  # Convert bytes to MB
    cpu_usage = process.cpu_percent(interval=1)
    return memory_usage, cpu_usage

async def run(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    home_load_time = []
    register_time = []
    login_time = []
    cpu_usages = []
    memory_usages = []
    successes = []

    for _ in range(total_runs):
        try:
            # Benchmark the home page load time
            start = time.time()
            await page.goto('http://127.0.0.1:5000')
            end = time.time()
            home_load_time.append(end - start)
            memory_usage, cpu_usage = get_system_usage()
            memory_usages.append(memory_usage)
            cpu_usages.append(cpu_usage)

            # Register a new user
            await page.goto('http://127.0.0.1:5000/register')
            await page.fill('input[name="username"]', f'testuser{_}')
            await page.fill('input[name="email"]', f'testuser{_}@example.com')
            await page.fill('input[name="password"]', 'password123')
            start = time.time()
            await page.click('button[type="submit"]')
            end = time.time()
            register_time.append(end - start)
            memory_usage, cpu_usage = get_system_usage()
            memory_usages.append(memory_usage)
            cpu_usages.append(cpu_usage)

            # Login with the new user
            await page.goto('http://127.0.0.1:5000/login')
            await page.fill('input[name="username"]', f'testuser{_}')
            await page.fill('input[name="password"]', 'password123')
            start = time.time()
            await page.click('button[type="submit"]')
            end = time.time()
            login_time.append(end - start)
            memory_usage, cpu_usage = get_system_usage()
            memory_usages.append(memory_usage)
            cpu_usages.append(cpu_usage)

            successes.append(1)  # Assuming success if no exception
        except Exception as e:
            successes.append(0)  # Failure if any exception occurs
            print(f"An error occurred: {e}")

    await browser.close()

    avg_cpu_usage = sum(cpu_usages) / len(cpu_usages)
    avg_memory_usage = sum(memory_usages) / len(memory_usages)
    success_rates = [sum(successes[:i+1]) / (i+1) * 100 for i in range(total_runs)]

    # Plotting CPU Usage
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(cpu_usages)), cpu_usages, align='center')
    plt.xticks(range(len(cpu_usages)), [f'Run {i+1}' for i in range(len(cpu_usages))])
    plt.title('CPU Usage per Test Run')
    plt.xlabel('Run')
    plt.ylabel('CPU Usage (%)')
    plt.show()

    # Plotting Memory Usage
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(memory_usages)), memory_usages, align='center')
    plt.xticks(range(len(memory_usages)), [f'Run {i+1}' for i in range(len(memory_usages))])
    plt.title('Memory Usage per Test Run')
    plt.xlabel('Run')
    plt.ylabel('Memory Usage (MB)')
    plt.show()

    # Plotting Success Rates Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(success_rates)), success_rates)
    plt.title('Reliability Over Time')
    plt.xlabel('Run')
    plt.ylabel('Success Rate (%)')
    plt.grid(True)
    plt.show()

    print(f"Average CPU Usage: {avg_cpu_usage:.2f}%")
    print(f"Average Memory Usage: {avg_memory_usage:.2f} MB")
    print(f"Overall Success Rate: {sum(successes) / len(successes) * 100:.2f}%")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
