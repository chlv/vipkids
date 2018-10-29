from splinter.browser import Browser

browser = Browser(driver_name="chrome")
url = "file:///C:/Users/lc/Desktop/vipkids/%E9%A2%84%E7%BA%A6%E8%AF%BE%E7%A8%8B%20-%20VIPKID%E5%9C%A8%E7%BA%BF%E5%B0%91%E5%84%BF%E8%8B%B1%E8%AF%AD.html"
browser.visit(url)
row = browser.find_by_xpath("//tr[th='15:30']/td")
print(type(row[0]))
# row[0].click()