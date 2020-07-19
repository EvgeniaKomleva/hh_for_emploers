
import time
import io
import csv
import json
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options

def auth():
    options = Options()
    user_name = 'komle'  # впишите ваше имя компьютера
    profile_path = r'C:\Users\{}\AppData\Local\Google\Chrome\User Data'.format(user_name)
    options.add_argument("user-data-dir={}".format(profile_path))
    return options


def base(myurl, auth_status):
    options = ''
    if auth_status == 1:
        options = auth()
    driver = webdriver.Chrome(executable_path='C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver.exe',
                              chrome_options=options)

    driver.get(myurl)
    time.sleep(1)

    #all_vacansu = driver.find_elements_by_xpath('//div[@class="resume-search-item__content"]')
    all_vacansu = driver.find_elements_by_xpath(
        '//a[@class="bloko-link bloko-link_dimmed HH-VacancyResponsePopup-Link"]')

    last_page = 0
    try:
        last_page = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div[4]/div/div[2]/div/div[7]/div/span[3]/a').text
        #print(len(buttons))

        #last_page = str(buttons)[len(buttons) - 8:-6].replace('...', '')
        #print(last_page)
    except:
        last_page = 1

    print(last_page)
    print(len(all_vacansu))
    i, j, k = 0, 0, 0

    while i < int(last_page):

        i = i + 1  # номер текущей страницы парсинга
        for vacansu in all_vacansu:
            j = j + 1  # Номер текущего резюме

            try:
                vacansu.click()
                #driver.find_element_by_xpath('//input[@class="bloko-radio__input HH-VacancyResponsePopup-Resume-Radio HH-InconsistencyChecker-Radio"]')
                #print("find resume ")
                v_button = driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/form/div[4]/div/button/span[1]')#.click()
                v_button.click()
                print(v_button.text)
                print("find otklic")
                driver.implicitly_wait(50)
            except:
                k = k+1
                print("-"*k)


        # блок перехода на следующую страницу
        page = driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div/div[2]/div/div[4]/div/div[2]/div/div[8]/div/a')  # Для перехода на след страницу (кроме последней!)
        print(page)
        page.click()
        driver.implicitly_wait(5)
        # try:
        #     page = driver.find_element_by_xpath(
        #         '/html/body/div[6]/div/div/div/div[2]/div/div[4]/div/div[2]/div/div[8]/div/a')  # Для перехода на след страницу (кроме последней!)
        #     print(page)
        #     page.click()
        #     driver.implicitly_wait(5)
        # except:
        #     print('last page done')

        all_vacansu = driver.find_elements_by_xpath(
            '//a[@class="bloko-link bloko-link_dimmed HH-VacancyResponsePopup-Link"]')

        if len(all_vacansu) == 0:
            print('AAAAAAAAAAAAAAAAA')
            print(i)

    for vacansu in all_vacansu:
        j = j + 1  # Номер текущего резюме

        try:
            vacansu.click()
            # driver.find_element_by_xpath('//input[@class="bloko-radio__input HH-VacancyResponsePopup-Resume-Radio HH-InconsistencyChecker-Radio"]')
            # print("find resume ")
            v_button = driver.find_element_by_xpath(
                '/html/body/div[9]/div[1]/div/form/div[4]/div/button/span[1]')  # .click()
            v_button.click()
            print(v_button.text)
            print("find otklic")
            driver.implicitly_wait(50)
        except:
            k = k + 1
            print("-" * k)

    #print(last_page)
    print("count_error {}".format(k))
    print("count good vacancy {}".format(j))


if __name__ == '__main__':
    auth_status = 1
    #url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&resume=55273996ff07e206ce0039ed1f5761364e5042&specialization=1&showClusters=true'
    #url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&resume=55273996ff07e206ce0039ed1f5761364e5042&specialization=1&only_with_salary=true&salary=220000&from=cluster_compensation&showClusters=false'
    #url = 'https://hh.ru/search/vacancy?clusters=true&specialization=1&resume=55273996ff07e206ce0039ed1f5761364e5042&enable_snippets=true&salary=&st=searchVacancy&fromSearch=true&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post'
    #url = 'https://hh.ru/search/vacancy?resume=55273996ff07e206ce0039ed1f5761364e5042&from=resumelist'
    #url = 'https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_field=name&text=data+scientist&experience=noExperience&from=cluster_experience&showClusters=true'
    url = 'https://hh.ru/vacancies/data-scientist'
    base(url, auth_status)