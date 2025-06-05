import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    # Benchmark the home page load time
    start = time.time()
    await page.goto('http://127.0.0.1:5000')
    end = time.time()
    home_load_time = end - start
    print(f"Home page load time: {home_load_time:.2f} seconds")

    # Register a new user
    await page.goto('http://127.0.0.1:5000/register')
    await page.fill('input[name="username"]', 'testuser')
    await page.fill('input[name="email"]', 'testuser@example.com')
    await page.fill('input[name="password"]', 'password123')
    start = time.time()
    await page.click('button[type="submit"]')
    end = time.time()
    register_time = end - start
    print(f"User registration time: {register_time:.2f} seconds")

    # Login with the new user
    await page.goto('http://127.0.0.1:5000/login')
    await page.fill('input[name="username"]', 'testuser')
    await page.fill('input[name="password"]', 'password123')
    start = time.time()
    await page.click('button[type="submit"]')
    end = time.time()
    login_time = end - start
    print(f"User login time: {login_time:.2f} seconds")

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    import time
    import cProfile
    import pstats

    profiler = cProfile.Profile()
    profiler.enable()

    asyncio.run(main())

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
