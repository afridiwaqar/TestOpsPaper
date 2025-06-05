from splinter import Browser

def test_login():
    with Browser('chrome') as browser:
        browser.visit("http://127.0.0.1:5000/auth/login")
        browser.fill('email', 'admin@helloflask.com')
        browser.fill('password', 'helloflask')
        browser.find_by_name('submit').click()
        assert "Home - Albumy" in browser.title
