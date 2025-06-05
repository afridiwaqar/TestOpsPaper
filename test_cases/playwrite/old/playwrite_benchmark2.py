import asyncio
from playwright.async_api import async_playwright
import psutil
import time
import cProfile
import pstats

def get_system_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    cpu_times = process.cpu_times()
    memory_usage = memory_info.rss / (1024 ** 2)  # Convert bytes to MB
    cpu_usage = process.cpu_percent(interval=1)
    return memory_usage, cpu_usage

async def run(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    # Benchmark the home page load time
    start = time.time()
    await page.goto('http://127.0.0.1:5000')
    end = time.time()
    home_load_time = end - start
    memory_usage, cpu_usage = get_system_usage()
    print(f"Home page load time: {home_load_time:.2f} seconds, Memory usage: {memory_usage:.2f} MB, CPU usage: {cpu_usage:.2f}%")

    # Register a new user
    await page.goto('http://127.0.0.1:5000/register')
    await page.fill('input[name="username"]', 'testuser')
    await page.fill('input[name="email"]', 'testuser@example.com')
    await page.fill('input[name="password"]', 'password123')
    start = time.time()
    await page.click('button[type="submit"]')
    end = time.time()
    register_time = end - start
    memory_usage, cpu_usage = get_system_usage()
    print(f"User registration time: {register_time:.2f} seconds, Memory usage: {memory_usage:.2f} MB, CPU usage: {cpu_usage:.2f}%")

    # Login with the new user
    await page.goto('http://127.0.0.1:5000/login')
    await page.fill('input[name="username"]', 'testuser')
    await page.fill('input[name="password"]', 'password123')
    start = time.time()
    await page.click('button[type="submit"]')
    end = time.time()
    login_time = end - start
    memory_usage, cpu_usage = get_system_usage()
    print(f"User login time: {login_time:.2f} seconds, Memory usage: {memory_usage:.2f} MB, CPU usage: {cpu_usage:.2f}%")

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    asyncio.run(main())

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
