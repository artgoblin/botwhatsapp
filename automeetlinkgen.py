from selenium import webdriver 

def replya():

    driver = webdriver.Chrome("Chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get("https://meet.google.com/")

    #clicking the meeting tab
    Tosignin=driver.find_element_by_css_selector('#page-content > section.module-hero.glue-mod-spacer-6-top.glue-mod-spacer-6-bottom.hero > div > div:nth-child(1) > div.primary-meet-cta.hero-cta > div > a > button')
    Tosignin.click()
    driver.implicitly_wait(10)

    #to sign in
    password = "s1234DAS2000"
    email= "projectsmail768@gmail.com"
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
    driver.find_element_by_id('identifierNext').click()

    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()

    k=driver.current_url
    
    driver.close()
    driver.quit()
    return k