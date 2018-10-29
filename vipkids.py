from splinter.browser import Browser
import time

class SuperApply():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = Browser(driver_name="chrome")
        self.url = "https://www.vipkid.com.cn/login"

    def login(self):
        self.browser.visit(self.url)
        self.browser.find_by_xpath("//input[@type='text']").first.fill(self.username)
        self.browser.find_by_xpath("//input[@type='password']").first.fill(self.password)
        login_button = self.browser.find_by_xpath("//span[@class='login-button']")
        login_button.click()

    def close_popup(self):
        try:
            close_button = self.browser.find_by_xpath("//div[@class='user-task-modal-close']")
            print(type(close_button))
            print(dir(close_button))
            close_button.click()
        except:
            pass

    def book(self):
        book_link = self.browser.find_link_by_href("/parent/preschedule")
        book_link.click()


print("StartTime:" + time.strftime("%H:%M:%S", time.localtime(int(time.time()))))
s = SuperApply(18018065563, 817129)
s.login()
s.close_popup()
s.book()
print("EndTime:" + time.strftime("%H:%M:%S", time.localtime(int(time.time()))))