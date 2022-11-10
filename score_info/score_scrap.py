from selenium import webdriver
from bs4 import BeautifulSoup as bs



options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('score_info\chromedriver.exe', options=options)
url = 'https://ipsi.jinhak.or.kr/subList/20000000095'
driver.get(url)
driver.implicitly_wait(time_to_wait=1000)
driver.find_element(by='id', value='pass').click()
driver.find_element(by='id', value='srchbtn').click()




school_score = {}


def scrap_10_page():
    for page_count in range(3,13):
        element = driver.find_element(by='css selector', value=f'#list_area > ul > li:nth-child({page_count}) > a')
        driver.execute_script("arguments[0].click();", element)
        html = driver.page_source
        soup = bs(html, "html.parser")
        for i in range(1,16):
            school_name = soup.select_one(f'#list_area > div > table > tbody > tr:nth-child({i}) > td:nth-child(4)').text
            score_info = float(soup.select_one(f'#list_area > div > table > tbody > tr:nth-child({i}) > td:nth-child(11)').text)
            try:
                school_score[school_name][0] += 1
                school_score[school_name][1] += score_info
            except:
                school_score[school_name] = [1, score_info]


scrap_10_page()
for school, score in school_score.items():
    print(school+':'+str(round(score[1]/score[0], 2)))
driver.quit()
