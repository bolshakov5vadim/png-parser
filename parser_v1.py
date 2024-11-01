from selenium.webdriver.common.keys import Keys#websocket
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import random, string#для названий файлов
import time#для ожидания подзагрузки
import os#для записи файлов


def download(url, path):

    # если путь не существует, сделать этот путь
    if not os.path.isdir(path):
        os.makedirs(path)
        
    letters = string.ascii_lowercase#имя файла
    filename = ''.join(random.choice(letters) for i in range(10))
    filename =  path+'/'+filename+'.png'
    response = requests.get(url)
    with open(filename, "wb") as f:
            f.write(response.content)
    



#chromedriver.exe ДОЛЖЕН СОВПАДАТЬ С ВЕРСИЕЙ БРАУЗЕРА

print("Pinterest_parser_v1.0. Yandex flag-1, Pin flag-2")
print("Print ENG ask.")
ask=input()
urls=[]

print("Print parsing limit.")
limit=input()
limit=int(limit)


for letter in ask:
        	if letter==' ':
                  letter='+'
#нормализация запроса в яндекс-запрос

if ask.find('1') != -1:#эмулятор яндекс
        url='https://www.yandex.ru/images/search?text='+ask

        

if ask.find('2') != -1:#эмулятор pinterest
    url = 'https://www.pinterest.co.uk/search/pins/?q='+ask   


driver = webdriver.Chrome()#что написано в скобках НЕ ВОСПРИНИМАЕТ
driver.get(url)#настроили эмулятор yandex
        
i=0#ломает цикл если конец страницы
old=0

while True:#цикл PAGE_DOWN
        
            html = driver.page_source#код страницы
            soup = BeautifulSoup(html, "html.parser")#код страницы

            img_tags = soup.findAll('img')#иногда ничего не находит
            for obj in img_tags:
                    str_img=str(obj.get("src"))
                    if str_img.find('https:')==-1:str_img='https:'+str_img
                    if str_img not in urls: urls.append(str_img)


            html = driver.find_element(By.TAG_NAME, 'html')
            html.send_keys(Keys.PAGE_DOWN)
            # Прыжок вниз.
            
            #ожидание загрузки
            time.sleep(0.5)

            #нажатие кнопки яндекс
            #button = driver.find_element_by_class_name("button2 button2_size_l button2_theme_action button2_type_link button2_view_classic more__button i-bem button2_js_inited")
            #if (button.size() > 0 && button.get(0).isDisplayed()): button.click()
            #JavascriptExecutor executor = (JavascriptExecutor)driver;
            #executor.executeScript("arguments[0].click();", element);

            print(f"Links: {len(urls)}")

            i += 1#ломает цикл если конец страницы
            if (len(urls)>limit):
                print("len(urls) stabled")
                break
            
            if i % 8 == 0: 
                if (len(urls) == old):
                    print("len(urls) stabled")
                    break
                old = len(urls)



      
    
log=0
for url in urls:
    download(url, "folder")
    log+=1
    print(f"Downloaded {log}/{len(urls)} images")