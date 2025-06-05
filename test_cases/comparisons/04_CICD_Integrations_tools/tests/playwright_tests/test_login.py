from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:5000/auth/login")
        page.fill('input[name="email"]', 'admin@helloflask.com')
        page.fill('input[name="password"]', 'helloflask')
        page.click('input[name="submit"]')
        assert "Home - Albumy" in page.title()
        browser.close()
