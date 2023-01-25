from django.shortcuts import render
import os
import time
from datetime import datetime
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium. webdriver. common. keys import Keys
import json
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from selenium import webdriver
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

# from openpyxl import Workbook
# import openpyxl
# from openpyxl.styles import Font, colors, Color, PatternFill, Alignment
from urllib.parse import urlsplit
# Create your views here.
from django.http import HttpResponse
from selenium import webdriver

class Master_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)

        map_url = urlsplit(mainURL).netloc
        print (map_url)



        url = "https://wheregoes.com/"
        print ("Performing Redirection Test on "+ clean_url)
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(clean_url) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_1 = mainURL

                    else:
                        redirection_result_1 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ clean_url)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ url_with_www)
            if search_input:
                time.sleep(1)
                search_input.send_keys(url_with_www) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_2 = mainURL
                    else:
                        redirection_result_2 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ url_with_www)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_1)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_1) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_3 = mainURL
                    else:
                        redirection_result_3 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_1)    
                except:
                    print ("Redirection Test Failed on "+ alternate_url_1)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_2)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_2) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_4 = mainURL
                    else:
                        redirection_result_4 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_2)
                    if redirection_result_1 != "Failed":
                        redirection_result_1_score = 100
                    else:
                        redirection_result_1_score = 0
                    if redirection_result_2 != "Failed":
                        redirection_result_2_score = 100
                    else:
                        redirection_result_2_score = 0
                    if redirection_result_3 != "Failed":
                        redirection_result_3_score = 100
                    else:
                        redirection_result_3_score = 0
                    if redirection_result_4 != "Failed":
                        redirection_result_4_score = 100
                    else:
                        redirection_result_4_score = 0

                    
                    site_redirection_score = round((redirection_result_1_score + redirection_result_2_score + redirection_result_3_score + redirection_result_4_score) / 4)
                    site_redirection_score = int(site_redirection_score)
                    print(site_redirection_score)
                    # driver.close()
                except:
                    print ("Redirection Test Failed on "+ alternate_url_2)
                    # driver.close()
                
        except:
            print("Redirection Test Failed Completely")
            # driver.close()


    # def google_index1():
        print ("Performing Google Index test on "+ "site:"+clean_url)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()    
        # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index = (google_index.split()[1])
                print (google_index)

                google_index_current_url = driver.current_url
                # print (google_index_current_url)
                if google_index != 0:
                    google_index_score = 100
                else:
                    google_index_score = 0
                print ("Successfully Completed Google Index test on "+ "site:"+clean_url)
                # driver.close()
            else:
                print ("Google Index test Failed on "+ "site:"+clean_url)
                # driver.close()
        except:
            print ("Google Index test Failed on "+ "site:"+clean_url)
            # driver.close()


    # def google_index2():
        print ("Performing Google Index test on "+ "site:"+url_with_www)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)

        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+url_with_www)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index_2 = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index_2 = (google_index_2.split()[1])
                print (google_index_2)

                google_index_2_current_url = driver.current_url
                # print (google_index_2_current_url)
                if google_index_2 != 0:
                    google_index_2_score = 100
                else:
                    google_index_2_score = 0
                
                page_indexed_in_google_score = round((google_index_score + google_index_2_score)/2)
                page_indexed_in_google_score = int(page_indexed_in_google_score)
                print ("Successfully Completed Google Index test on "+ "site:"+url_with_www)
                # driver.close()

            else:
                print ("Google Index test Failed on "+ "site:"+url_with_www)
                # driver.close()
            

        except:
            print ("Google Index test Failed on "+ "site:"+url_with_www)
            # driver.close()

    # def gtmetrix_test():
        print ("Performing GTMetrix test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].IntoView();", search_input)
        search_input.send_keys("https://gtmetrix.com/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/section[1]/div/form/div[1]/div[1]/div/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                gtmetrix_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[1]/i"))).get_attribute('class')
                gtmetrix_grade = gtmetrix_grade[-1]
                print (gtmetrix_grade)

                gtmetrix_performance =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[2]/span/span"))).get_attribute('textContent')
                gtmetrix_performance = gtmetrix_performance.replace("%","")
                gtmetrix_performance = int(gtmetrix_performance)
                print (gtmetrix_performance)

                gtmetrix_structure =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[3]/span/span"))).get_attribute('textContent')
                gtmetrix_structure = gtmetrix_structure.replace("%","")
                gtmetrix_structure = int(gtmetrix_structure)
                print (gtmetrix_structure)

                gtmetrix_lcp =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[1]/span"))).get_attribute('textContent')
                print (gtmetrix_lcp)

                gtmetrix_tbt =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[2]/span"))).get_attribute('textContent')
                print (gtmetrix_tbt)

                gtmetrix_cls =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[3]/span"))).get_attribute('textContent')
                print (gtmetrix_cls)

                gtmetrix_current_url = driver.current_url
                # print (gtmetrix_current_url)
                if gtmetrix_grade == "A":
                    grade_score = 100
                if gtmetrix_grade == "B":
                    grade_score = 80
                if gtmetrix_grade == "C":
                    grade_score = 60
                if gtmetrix_grade == "D":
                    grade_score = 40
                if gtmetrix_grade == "E":
                    grade_score = 20
                if gtmetrix_grade == "F":
                    grade_score = 0
                # print (grade_score)
                gtmetrix_result_score = round((grade_score + gtmetrix_performance + gtmetrix_structure)/3)
                gtmetrix_result_score = int(gtmetrix_result_score)
                # print (gtmetrix_result_score)
                print ("Successfully Completed GTMetrix test on "+ mainURL)
                # driver.close()
            else:
                print ("GTMetrix Test Failed on "+ mainURL)
                # driver.close()
            

        except:
            print ("GTMetrix Test Failed on "+ mainURL)
            # driver.close()


    # def ssl_lab():
        print ("Performing Secure Server and Web Application test on "+ mainURL)
        url = "https://www.ssllabs.com/ssltest/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[1]/center/form/table/tbody/tr[1]/td[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    find_table= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@id = 'multiTable']")))
                    if find_table:
                        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[4]/div")))  
                        driver.find_element(By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[2]/span[1]/b/a").click()
                except:pass
                ssl_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='gradeA']"))).text
                print (ssl_grade)
                certificate = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Certificate']//following::div").get_attribute("class")
                certificate=list(certificate)
                certificate =certificate[-3]+certificate[-2]+certificate[-1]
                if certificate == "300":
                    certificate = 100

                elif certificate == "270":
                    certificate = 90

                elif certificate == "240":
                    certificate = 80

                elif certificate == "210":
                    certificate = 70

                elif certificate == "180":
                    certificate = 60

                elif certificate == "150":
                    certificate = 50

                elif certificate == "120":
                    certificate = 40

                elif certificate == "_90":
                    certificate = 30

                elif certificate == "_60":
                    certificate = 20

                elif certificate == "_30":
                    certificate = 10

                elif certificate == "h_1":
                    certificate = 0
                print (certificate)

                protocol_support = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Protocol Support']//following::div").get_attribute("class")
                protocol_support=list(protocol_support)
                protocol_support =protocol_support[-3]+protocol_support[-2]+protocol_support[-1]
                if protocol_support == "300":
                    protocol_support = 100

                elif protocol_support == "270":
                    protocol_support = 90

                elif protocol_support == "240":
                    protocol_support = 80

                elif protocol_support == "210":
                    protocol_support = 70

                elif protocol_support == "180":
                    protocol_support = 60

                elif protocol_support == "150":
                    protocol_support = 50

                elif protocol_support == "120":
                    protocol_support = 40

                elif protocol_support == "_90":
                    protocol_support = 30

                elif protocol_support == "_60":
                    protocol_support = 20

                elif protocol_support == "_30":
                    protocol_support = 10

                elif protocol_support == "h_1":
                    protocol_support = 0
                print (protocol_support)

                key_exchange = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Key Exchange']//following::div").get_attribute("class")
                key_exchange=list(key_exchange)
                key_exchange =key_exchange[-3]+key_exchange[-2]+key_exchange[-1]
                if key_exchange == "300":
                    key_exchange = 100

                elif key_exchange == "270":
                    key_exchange = 90

                elif key_exchange == "240":
                    key_exchange = 80

                elif key_exchange == "210":
                    key_exchange = 70

                elif key_exchange == "180":
                    key_exchange = 60

                elif key_exchange == "150":
                    key_exchange = 50

                elif key_exchange == "120":
                    key_exchange = 40

                elif key_exchange == "_90":
                    key_exchange = 30

                elif key_exchange == "_60":
                    key_exchange = 20

                elif key_exchange == "_30":
                    key_exchange = 10

                elif key_exchange == "h_1":
                    key_exchange = 0
                print (key_exchange)   

                ciper_strength = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Cipher Strength']//following::div").get_attribute("class")
                ciper_strength=list(ciper_strength)
                ciper_strength =ciper_strength[-3]+ciper_strength[-2]+ciper_strength[-1]
                if ciper_strength == "300":
                    ciper_strength = 100

                elif ciper_strength == "270":
                    ciper_strength = 90

                elif ciper_strength == "240":
                    ciper_strength = 80

                elif ciper_strength == "210":
                    ciper_strength = 70

                elif ciper_strength == "180":
                    ciper_strength = 60

                elif ciper_strength == "150":
                    ciper_strength = 50

                elif ciper_strength == "120":
                    ciper_strength = 40

                elif ciper_strength == "_90":
                    ciper_strength = 30

                elif ciper_strength == "_60":
                    ciper_strength = 20

                elif ciper_strength == "_30":
                    ciper_strength = 10

                elif ciper_strength == "h_1":
                    ciper_strength = 0

                else:
                    pass
                print (ciper_strength)
                ssl_lab_current_url = driver.current_url
                # print (ssl_lab_current_url)
                if ssl_grade == "A+":
                    ssl_grade_score = 100
                if ssl_grade == "A":
                    ssl_grade_score = 90
                if ssl_grade == "B":
                    ssl_grade_score = 80
                if ssl_grade == "C":
                    ssl_grade_score = 60
                if ssl_grade == "D":
                    ssl_grade_score = 40
                if ssl_grade == "E":
                    ssl_grade_score = 20
                if ssl_grade == "F":
                    ssl_grade_score = 10
                if ssl_grade == "T":
                    ssl_grade_score = 0
                ssl_lab_test_score = round((ssl_grade_score + certificate + protocol_support + key_exchange + ciper_strength)/5)
                ssl_lab_test_score  = int(ssl_lab_test_score)
                print ("Successfully Completed Secure Server and Web Application test on "+ mainURL)
                # driver.close()


            else:
                print ("Secure Server and Web Application test Failed on "+ mainURL)
                # driver.close()


        except:
            print ("Secure Server and Web Application test Failed on "+ mainURL)
            # driver.close()


    # def webpage_test():
        print ("Performing Webpage Performance test on "+ mainURL)
        url = "https://www.webpagetest.org/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='analytical-review']")))
            search_view = driver.execute_script("arguments[0].scrollIntoView();", search_view)
            time.sleep(1)
            search_input =driver.find_element(By.XPATH, "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.submit()
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result']")))
                time.sleep(2)
                current_page = driver.current_url
                print (current_page)
                time.sleep(2)
                modified_url = current_page+"/2/performance_optimization/"
                print (modified_url)
                time.sleep(2)
                driver.get(modified_url)
                time.sleep(2)
                result_grade=WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='grades']")))
                result_grade =driver.execute_script("arguments[0].scrollIntoView();", result_grade)
                time.sleep(2)
                performance_grade = driver.find_element(By.XPATH, "//li[@class='security']/a/h2").text
                print (performance_grade)
                first_byte_time = driver.find_element(By.XPATH, "//li[@class='first_byte_time']/a/h2").text
                print (first_byte_time)
                keep_alive = driver.find_element(By.XPATH, "//li[@class='keep_alive_enabled']/a/h2").text
                print (keep_alive)
                compress_trf = driver.find_element(By.XPATH, "//li[@class='compress_text']/a/h2").text
                print (compress_trf)
                compress_img = driver.find_element(By.XPATH, "//li[@class='compress_images']/a/h2").text
                print (compress_img)
                cache_static = driver.find_element(By.XPATH, "//li[@class='cache_static_content']/a/h2").text
                print (cache_static)
                effective_cdn = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").text
                print (effective_cdn)
                effective_cdn_colour = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").get_attribute("class")
                print (effective_cdn_colour)
                time.sleep(1)
                webpage_test_current_url = driver.current_url
                # print (webpage_test_current_url)
                if performance_grade == "A+":
                    performance_score = 100
                if performance_grade == "A":
                    performance_score = 90
                if performance_grade == "B":
                    performance_score = 80
                if performance_grade == "C":
                    performance_score = 60
                if performance_grade == "D":
                    performance_score = 40
                if performance_grade == "E":
                    performance_score = 20
                if performance_grade == "F":
                    performance_score = 0

                if first_byte_time == "A+":
                    first_byte_time_score = 100
                if first_byte_time == "A":
                    first_byte_time_score = 90
                if first_byte_time == "B":
                    first_byte_time_score = 80
                if first_byte_time == "C":
                    first_byte_time_score = 60
                if first_byte_time == "D":
                    first_byte_time_score = 40
                if first_byte_time == "E":
                    first_byte_time_score = 20
                if first_byte_time == "F":
                    first_byte_time_score = 0

                if keep_alive == "A+":
                    keep_alive_score = 100
                if keep_alive == "A":
                    keep_alive_score = 90
                if keep_alive == "B":
                    keep_alive_score = 80
                if keep_alive == "C":
                    keep_alive_score = 60
                if keep_alive == "D":
                    keep_alive_score = 40
                if keep_alive == "E":
                    keep_alive_score = 20
                if keep_alive == "F":
                    keep_alive_score = 0

                if compress_trf == "A+":
                    compress_trf_score = 100
                if compress_trf == "A":
                    compress_trf_score = 90
                if compress_trf == "B":
                    compress_trf_score = 80
                if compress_trf == "C":
                    compress_trf_score = 60
                if compress_trf == "D":
                    compress_trf_score = 40
                if compress_trf == "E":
                    compress_trf_score = 20
                if compress_trf == "F":
                    compress_trf_score = 0

                if compress_img == "A+":
                    compress_img_score = 100
                if compress_img == "A":
                    compress_img_score = 90
                if compress_img == "B":
                    compress_img_score = 80
                if compress_img == "C":
                    compress_img_score = 60
                if compress_img == "D":
                    compress_img_score = 40
                if compress_img == "E":
                    compress_img_score = 20
                if compress_img == "F":
                    compress_img_score = 0


                if cache_static == "A+":
                    cache_static_score = 100
                if cache_static == "A":
                    cache_static_score = 90
                if cache_static == "B":
                    cache_static_score = 80
                if cache_static == "C":
                    cache_static_score = 60
                if cache_static == "D":
                    cache_static_score = 40
                if cache_static == "E":
                    cache_static_score = 20
                if cache_static == "F":
                    cache_static_score = 0

                if effective_cdn_colour == "A" and effective_cdn == "✓":
                    effective_cdn_score = 100
                if effective_cdn_colour == "B" and effective_cdn == "✓":
                    effective_cdn_score = 80
                if effective_cdn_colour == "C" and effective_cdn == "✓":
                    effective_cdn_score = 60
                if effective_cdn_colour == "D" and effective_cdn == "✓":
                    effective_cdn_score = 40
                if effective_cdn_colour == "E" and effective_cdn == "✓":
                    effective_cdn_score = 20
                if effective_cdn_colour == "F" and effective_cdn == "✓":
                    effective_cdn_score = 10
                if effective_cdn == "X":
                    effective_cdn_score = 0
                webpage_performance_test_score = round((performance_score + first_byte_time_score + keep_alive_score + compress_trf_score + compress_img_score + cache_static_score + effective_cdn_score )/7)
                webpage_performance_test_score = int(webpage_performance_test_score)
                print ("Successfully Completed Webpage Performance test on "+ mainURL)
                
                # driver.close()    
            else:
                print ("Webpage Performance Test Failed on "+ mainURL)
                # driver.close()
            

        except:
            print ("Webpage Performance Test Failed on "+ mainURL)
            # driver.close()


    # def website_audit_test():
        print ("Performing Website Audit test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("https://www.seobility.net/en/seocheck/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='cookieoptin_saveall']"))).click()
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='bigassform']/div[1]/div/form/div[1]/div[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row analysisheading']")))
                time.sleep(4)
                seo_score = driver.find_element(By.XPATH, "//*[@id='pieLabel0']/div").text
                seo_score = int(seo_score.replace("%", ""))
                print (seo_score)
                meta_information = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/div").text
                meta_information = int(meta_information.replace("%", ""))
                print (meta_information)
                page_quality = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div").text
                page_quality = int(page_quality.replace("%", ""))
                print (page_quality)
                page_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[3]/div[2]/div/div").text
                page_structure = int(page_structure.replace("%", ""))
                print (page_structure)
                link_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div/div").text
                link_structure = int(link_structure.replace("%", ""))
                print (link_structure)
                server = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div[2]/div/div").text
                server = int(server.replace("%", ""))
                print (server)
                external_factors = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[6]/div[2]/div/div").text
                external_factors = int(external_factors.replace("%", ""))
                print (external_factors)
                response_time = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[2]/span").text
                print (response_time)
                file_size = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span").text
                print (file_size)
                text_words = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/span").text
                print (text_words)
                media_files = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[4]/div/div[2]/span").text
                print (media_files)
                no_of_links = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[5]/div/div[2]/span").text
                print (no_of_links)
                website_audit_current_url = driver.current_url
                # print (website_audit_current_url)
                website_audit_score = round((seo_score + meta_information + page_quality + page_structure + link_structure + server + external_factors)/7)
                website_audit_score = int(website_audit_score)
                print ("Successfully Completed Website Audit test on "+ mainURL)
                # driver.close()


            else:
                print ("Website Audit Test Failed on "+ mainURL)
                # driver.close()
        except:
            print ("Website Audit Test Failed on "+ mainURL)
            # driver.close()


    # def google_domain_index():
        print ("Performing SERP Link - Domain Index test on Google for "+ clean_url)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(1)
                try:
                  google_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                  google_serp_result = (google_serp_result.split()[1])
                  print (google_serp_result)
                except:
                  google_serp_result = "No Results Found"
                print (google_serp_result)
                google_serp_current_url = driver.current_url
                # print (google_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Google for "+ clean_url)
                # driver.close()

            else:
                print ("SERP Link - Domain Index test on Google Failed for "+ clean_url)
                # driver.close()


        except:
            print ("SERP Link - Domain Index test on Google Failed for "+ clean_url)
            # driver.close()


    # def yahoo_domain_index():
        print ("Performing SERP Link - Domain Index test on Yahoo for "+ clean_url)
        url = "https://in.search.yahoo.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='sbq']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(1)
                try:
                  yahoo_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class=' fz-14 lh-22']"))).text
                  yahoo_serp_result = (yahoo_serp_result.split()[1])
                except:
                  yahoo_serp_result = "No Results Found"
                print (yahoo_serp_result)
                yahoo_serp_current_url = driver.current_url
                # print (yahoo_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Yahoo for "+ clean_url)
                # driver.close()

            else:
                print ("SERP Link - Domain Index test on Yahoo Failed for "+ clean_url)
                # driver.close()

        except:
            print ("SERP Link - Domain Index test on Yahoo Failed for "+ clean_url)
            # driver.close()


    # def bing_domain_index():
        print ("Performing SERP Link - Domain Index test on Bing for "+ clean_url)
        url = "https://www.bing.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@id='sb_form_q']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(3)
                try:
                  bing_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class='sb_count']"))).text
                # bing_serp_result = (bing_serp_result.split()[0])
                  bing_serp_result = bing_serp_result.replace("About", "").replace("Results", "").replace("results", "")      
                except:
                  bing_serp_result = "No Result Found"     
                print (bing_serp_result)
                bing_serp_current_url = driver.current_url
                # print (bing_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Bing for "+ clean_url)
                # driver.close()

            else:
                print ("SERP Link - Domain Index test on Bing Failed for "+ clean_url)
                # driver.close()

        except:
            print ("SERP Link - Domain Index test on Bing Failed for "+ clean_url)
            # driver.close()


    # def pingdom_tools_test()
        print ("Performing Pingdom Tools test for "+ mainURL)
        url = "https://tools.pingdom.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='urlInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH , "//div[@class='grid ng-star-inserted']")))
                time.sleep(10)
                performance_grade = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/app-grade-badge/span").text
                performance_score = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/div[2]").text
                pingdom_performance = performance_grade+performance_score
                print (pingdom_performance)
                pingdom_page_size = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[2]/app-metric/div[2]").text
                print (pingdom_page_size)
                pingdom_load_time = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[3]/app-metric/div[2]").text
                print (pingdom_load_time)
                pingdom_request = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[4]/app-metric/div[2]").text
                print (pingdom_request)

                pingdom_tools_current_url = driver.current_url
                # print (pingdom_tools_current_url)
                pingdom_test_score = performance_score
                pingdom_test_score = int(pingdom_test_score)
                print ("Successfully Completed Pingdom Tools test for "+ mainURL)
                # driver.close()
            else:
                print ("Pingdom Tools Test Failed for "+ mainURL)
                # driver.close()
        except:
            print ("Pingdom Tools Test Failed for "+ mainURL)
            # driver.close()

    # def on_map():
        print ("Performing Google Map Location Test for "+ mainURL)
        url = "https://www.google.com/maps"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='searchboxinput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(map_url)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                time.sleep(1)
                try:
                    time.sleep(5)
                    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Io6YTe fontBodyMedium']")))
                    if result :
                        time.sleep(1)
                        map_result = "Map Location Found"
                        print (map_result)
                        on_map_current_url = driver.current_url
                        # print (on_map_current_url)
                        print ("Successfully Completed Google Map Location test for "+ mainURL)
                        # driver.close()

                except:
                    time.sleep(1)
                    map_result = "Map Location Not Found"
                    print (map_result)
                    on_map_current_url = driver.current_url
                    # print (on_map_current_url)
                    print ("Google Map Location Test Failed for "+ mainURL)
                    # driver.close()
        except:
            print ("Google Map Location Test Failed for "+ mainURL)
            # driver.close()

    # def mobile():
        print ("Performing Mobile Friendly Test for "+ mainURL)
        url = "https://technicalseo.com/tools/mobile-friendly/"
        # options = uc.ChromeOptions()
        # # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/section/div/div[1]/div/form/div/div[1]/md-input-container/div[1]/textarea")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                driver.find_element(By.XPATH, "//*[@id='mobile_friendly_form']/div/div[2]/md-input-container/button").click()
                mobile_friendly_result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i")))
                try:
                    mobile_friendly_result = driver.find_element(By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i").get_attribute("class")
                    if mobile_friendly_result == "mdi mdi-check-circle mdi-cell":
                        mobile_friendly_result = "YES"
                    else:
                        mobile_friendly_result = "NO"
                    mobile_friendly_current_url = driver.current_url
                    if mobile_friendly_result == "Yes":
                        mobile_friendly_test_score = 100
                    else:
                        mobile_friendly_test_score = 0
                    mobile_friendly_test_score = int(mobile_friendly_test_score)
                    print ("Successfully Completed Mobile Friendly test for "+ mainURL)
                    # driver.close()
                except:
                  print ("Mobile Friendly Test Failed for "+ mainURL)
                #   driver.close()
        except:
          print ("Mobile Friendly Test Failed for "+ mainURL)
        #   driver.close()


    
    # def dns_test():
        print ("Performing DNS Health Test for "+ mainURL)
        url = "https://mxtoolbox.com/domain/"
        # options = uc.ChromeOptions()

        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'txtToolInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//span[@id = 'spanTestsRemaining'][text()='Complete']")))
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'tilesResults']")))
                problem_errors =driver.find_element(By.XPATH, "//span[@id='spanNumErrors']").text
                print (problem_errors)
                problem_warnings =driver.find_element(By.XPATH, "//span[@id='spanNumWarnings']").text
                print (problem_warnings)
                blacklist_errors =driver.find_element(By.XPATH, "//span[@id='blacklistNumFailed']").text
                print (blacklist_errors)
                blacklist_warnings =driver.find_element(By.XPATH, "//span[@id='blacklistNumWarning']").text
                print (blacklist_warnings)
                mail_server_errors =driver.find_element(By.XPATH, "//span[@id='smtpNumFailed']").text
                print (mail_server_errors)
                mail_server_warnings =driver.find_element(By.XPATH, "//span[@id='smtpNumWarning']").text
                print (mail_server_warnings)
                web_server_errors =driver.find_element(By.XPATH, "//span[@id='webNumFailed']").text
                print (web_server_errors)
                web_server_warnings =driver.find_element(By.XPATH, "//span[@id='webNumWarning']").text
                print (web_server_warnings)
                dns_errors =driver.find_element(By.XPATH, "//span[@id='dnsNumFailed']").text
                print (dns_errors)
                dns_warnings =driver.find_element(By.XPATH, "//span[@id='dnsNumWarning']").text
                print (dns_warnings)
                dns_test_current_url = driver.current_url
                # print (dns_test_current_url)
                dns_test_score = 60
                print ("Successfully Completed DNS Health test for "+ mainURL)
                time.sleep(1)
                # driver.close()

        except:
            print ("DNS Health test Failed for "+ mainURL)
            # driver.close()



    # def HTML_Validation_test()        
        print ("Performing W3 NU HTML VALIDATOR test for "+ mainURL)
        url = "https://html5.validator.nu/"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='doc']")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='results']/ol")))
                markup_warning = len(driver.find_elements(By.XPATH, "//div[@id='results']//following::li[@class='info warning']"))
                print (markup_warning)
                markup_error = len(driver.find_elements(By.XPATH, ("//div[@id='results']//following::li[@class='error']") ))
                print (markup_error)
                time.sleep(3)
                markup_validation_current_url = driver.current_url
                # print (markup_validation_current_url)
                html_validation_test_score = 80
                print ("Successfully Completed W3 NU HTML VALIDATOR test for "+ mainURL)
                driver.close()
            else:
                print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
                driver.close()

        except:
            print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
            driver.close()

        webvital_basic_score = round((site_redirection_score + page_indexed_in_google_score + gtmetrix_result_score)/3)
        webvital_advanced_score = round((mobile_friendly_test_score + webpage_performance_test_score + ssl_lab_test_score + pingdom_test_score + dns_test_score + html_validation_test_score)/6)
        seo_final_score = (website_audit_score)
        overall_bar_report_score = round((webvital_basic_score + webvital_advanced_score + seo_final_score)/3)

        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = {"Result":[  {"Date" : current_date},
      
                            {"Site URL" : site_url},



                            {"Dashboard Data" :                      [{     "Overall Bar Report Score" : overall_bar_report_score,
                                                                            "Webvital Basic" : [{"Webvital Basic Score" : webvital_basic_score,
                                                                                                "Site Redirection Score" : site_redirection_score,
                                                                                                "Page Indexed by Google Score" : page_indexed_in_google_score,
                                                                                                "GTMetrix Result Score" :gtmetrix_result_score,  }],
                                                                                                
                                                                            "Webvital Advanced" : [{"Webvital Advance Score" : webvital_advanced_score,
                                                                                                "Site Redirection Score" : site_redirection_score,
                                                                                                "Page Indexed by Google Score" : page_indexed_in_google_score,
                                                                                                "GTMetrix Result Score" :gtmetrix_result_score,  }],

                                                                            "SEO" :             [{"SEO Score" : seo_final_score,
                                                                                                "Website Audit Test" : website_audit_score,}]}]},


                        {"Site Redirection Test" :                      [{  "Site Redirection Score" : site_redirection_score,
                                                                            clean_url : redirection_result_1,
                                                                            url_with_www : redirection_result_2,
                                                                            alternate_url_1 : redirection_result_3,
                                                                            alternate_url_2 : redirection_result_4}]},
        
        
        
        
        
                        {"Page Indexed by Google":                      [{  "Page Indexed by Google Score" : page_indexed_in_google_score,
                                                                            "google_index_url" : "site:"+clean_url,
                                                                            "google_index_result" : google_index,
                                                                            "google_index_result_page" : google_index_current_url,

                                                                            "google_index_url2" : "site:"+url_with_www,
                                                                            "google_index_result2" : google_index_2,
                                                                            "google_index_result2_page" : google_index_2_current_url}]},


                            {"GTMetri Test Result":                     [{  "GTMetrix Result Score" :gtmetrix_result_score,           
                                                                            "Grade" : gtmetrix_grade,
                                                                            "Performance" : gtmetrix_performance,
                                                                            "Structure" :gtmetrix_structure,
                                                                            "Largest Contentful Paint (LCP)" : gtmetrix_lcp,
                                                                            "Total Blocking Time (TBT)" : gtmetrix_tbt,
                                                                            "Cumulative Layout Shift (CLS)" : gtmetrix_cls,
                                                                            "GTMetrix Result Page": gtmetrix_current_url }]},
        
                            {"SSL Lab Test Result":                     [{  "Secure Server and Web Application Score" : ssl_lab_test_score,
                                                                            "Overall" : ssl_grade,
                                                                            "Certificate" : certificate,
                                                                            "Protocol" : protocol_support,
                                                                            "Key Exchange" : key_exchange,
                                                                            "Cipher Strength" : ciper_strength,
                                                                            "SSL Lab Test Result Page": ssl_lab_current_url }]},
                                
                        {"Webpage Performance Test Result":             [{  "Webpage Performance Test Score" : webpage_performance_test_score,
                                                                            "Security Score" : performance_grade,
                                                                            "First Byte time" : first_byte_time,
                                                                            "Keep Alive" : keep_alive,
                                                                            "Compress Transfer" : compress_trf,
                                                                            "Compress Image" : compress_img,
                                                                            "Cache Static Content" : cache_static,
                                                                            "Effective use of CDN" : effective_cdn,
                                                                            "Webpage Performance Test Result Page": webpage_test_current_url }]},
                                
                        {"Website Audit Test Result":                   [{  "Website Audit Test" : website_audit_score,
                                                                            "SEO Score" : seo_score,
                                                                            "Meta Information" : meta_information,
                                                                            "Page Quality" : page_quality,
                                                                            "Page Structure" : page_structure,
                                                                            "Link Structure" : link_structure,
                                                                            "Server" : server,
                                                                            "External Factors" : external_factors,
                                                                            "Response Time" : response_time,
                                                                            "File Size" : file_size,
                                                                            "Text Words" : text_words,
                                                                            "Media Files" : media_files,
                                                                            "Number Of Links" : no_of_links,
                                                                            "Website Audit Test Result Page": website_audit_current_url }]},
        
                        {"SERP Links - Domain Index Test Result":       [{  "Google" : google_serp_result,
                                                                            "Google Test Page" : google_serp_current_url,
                                                                            "Yahoo" : yahoo_serp_result,
                                                                            "Yahoo Test Page" : yahoo_serp_current_url,
                                                                            "Bing" : bing_serp_result,
                                                                            "Bing Test Page" : bing_serp_current_url}]},
                                                                    
                        {"W3 NU HTML VALIDATOR Test Result":            [{  "W3 NU HTML VALIDATOR Test Score" : html_validation_test_score,
                                                                            "Warnings" : markup_warning,
                                                                            "Errors" : markup_error,
                                                                            "W3 NU HTML VALIDATOR Test Result Page" : markup_validation_current_url}]},

                        {"DNS Health Test Result":                      [{  "DNS Health Test Score" : dns_test_score},
                                                                            {  "Problems"                      : [{ "Warnings" :problem_warnings,
                                                                                                                    "Errors" : problem_errors}]},
                                                                            {  "Blacklist"                     : [{ "Warnings" : blacklist_warnings,
                                                                                                                    "Errors" :  blacklist_errors}]},
                                                                            {  "Mail Server"                   : [{ "Warnings" : mail_server_warnings,
                                                                                                                    "Errors" :  mail_server_errors}]},
                                                                            {  "Web Server"                    : [{ "Warnings" : web_server_warnings,
                                                                                                                    "Errors" :  web_server_errors}]},
                                                                            {  "DNS"                           : [{ "Warnings" : dns_warnings,
                                                                                                                   "Errors" :  dns_errors}]},
                                                                            {  "DNS Health Test Result Page"   : dns_test_current_url}]},
                                                                                    
                        {"Pingdom Tools Test Result":                   [{  "Pingdom Tools Test Score" : performance_score,
                                                                            "Performance grade" : pingdom_performance,
                                                                            "Page size" : pingdom_page_size,
                                                                            "Load time" : pingdom_load_time,
                                                                            "Requests" : pingdom_request,
                                                                            "Pingdom Tools Test Result Page" : pingdom_tools_current_url}]},


                        {"Google Map Test Result":                      [{  "Google Map" : map_result,
                                                                            "Google Map Test Result Page" : on_map_current_url}]},

                        {"Mobile Friendly Test Result":                 [{  "Mobile Friendly Test Score" : mobile_friendly_test_score,
                                                                            "Mobile Friendly" : mobile_friendly_result,
                                                                            "Mobile Friendly Test Result Page" : mobile_friendly_current_url}]}
                                                                                    
                                                        
            ]}
        
        return Response(data)


class URL_Test(generics.ListAPIView):
     def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)

        map_url = urlsplit(mainURL).netloc
        print (map_url)



        url = "https://wheregoes.com/"
        print ("Performing Redirection Test on "+ clean_url)
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(clean_url) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_1 = mainURL

                    else:
                        redirection_result_1 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ clean_url)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ url_with_www)
            if search_input:
                time.sleep(1)
                search_input.send_keys(url_with_www) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_2 = mainURL
                    else:
                        redirection_result_2 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ url_with_www)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_1)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_1) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_3 = mainURL
                    else:
                        redirection_result_3 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_1)    
                except:
                    print ("Redirection Test Failed on "+ alternate_url_1)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_2)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_2) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_4 = mainURL
                    else:
                        redirection_result_4 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_2)
                    if redirection_result_1 != "Failed":
                        redirection_result_1_score = 100
                    else:
                        redirection_result_1_score = 0
                    if redirection_result_2 != "Failed":
                        redirection_result_2_score = 100
                    else:
                        redirection_result_2_score = 0
                    if redirection_result_3 != "Failed":
                        redirection_result_3_score = 100
                    else:
                        redirection_result_3_score = 0
                    if redirection_result_4 != "Failed":
                        redirection_result_4_score = 100
                    else:
                        redirection_result_4_score = 0

                    site_redirection_score = round((redirection_result_1_score + redirection_result_2_score + redirection_result_3_score + redirection_result_4_score) / 4)
                    print(site_redirection_score)
                    driver.close()
                except:
                    print ("Redirection Test Failed on "+ alternate_url_2)
                    driver.close()
                
        except:
            print("Redirection Test Failed Completely")
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = {"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},
                            

                            {"Site Redirection Test" :                  [{  "Site Redirection" : site_redirection_score,
                                                                            clean_url : redirection_result_1,
                                                                            url_with_www : redirection_result_2,
                                                                            alternate_url_1 : redirection_result_3,
                                                                            alternate_url_2 : redirection_result_4}]}
        ]}
        return Response(data)

class PageIndex_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def google_index1():
        print ("Performing Google Index test on "+ "site:"+clean_url)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()    
        # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)
        try:
            time.sleep(1)
            remove_button = driver.find_element(By.XPATH, "//button[@id='L2AGLb']").click()
        except:
            pass
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index = (google_index.split()[1])
                print (google_index)

                google_index_current_url = driver.current_url
                # print (google_index_current_url)
                if google_index != 0:
                    google_index_score = 100
                else:
                    google_index_score = 0
                print ("Successfully Completed Google Index test on "+ "site:"+clean_url)
                # driver.close()
            else:
                print ("Google Index test Failed on "+ "site:"+clean_url)
                # driver.close()
        except:
            print ("Google Index test Failed on "+ "site:"+clean_url)
            # driver.close()


    # def google_index2():
        print ("Performing Google Index test on "+ "site:"+url_with_www)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)
        try:
            time.sleep(1)
            remove_button = driver.find_element(By.XPATH, "//button[@id='L2AGLb']").click()
        except:
            pass
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+url_with_www)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index_2 = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index_2 = (google_index_2.split()[1])
                print (google_index_2)

                google_index_2_current_url = driver.current_url
                # print (google_index_2_current_url)
                if google_index_2 != 0:
                    google_index_2_score = 100
                else:
                    google_index_2_score = 0
                page_indexed_in_google_score = round((google_index_score + google_index_2_score)/2)
                print ("Successfully Completed Google Index test on "+ "site:"+url_with_www)
                driver.close()

            else:
                print ("Google Index test Failed on "+ "site:"+url_with_www)
                driver.close()


        except:
            print ("Google Index test Failed on "+ "site:"+url_with_www)
            driver.close()

        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
                            {"Site URL" : site_url},
                            {"Page Indexed by Google":                  [{ 
                                  "Page Indexed In Google Score" : page_indexed_in_google_score,
                                                                            "google_index_url" : "site:"+clean_url,
                                                                            "google_index_result" : google_index,
                                                                            "google_index_result_page" : google_index_current_url,
                                                                            "google_index_url2" : "site:"+url_with_www,
                                                                            "google_index_result2" : google_index_2,
                                                                            "google_index_result2_page" : google_index_2_current_url}]},
        ]})
        return Response(data)

class GTMetrix_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)
        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)
        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)
        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)
        else:
            url_with_www = clean_url
            print (url_with_www)
        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")
        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")
        print(alternate_url_1)
        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url
        print(alternate_url_2)
    # def gtmetrix_test():
        print ("Performing GTMetrix test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("https://gtmetrix.com/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/section[1]/div/form/div[1]/div[1]/div/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                gtmetrix_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[1]/i"))).get_attribute('class')
                gtmetrix_grade = gtmetrix_grade[-1]
                print (gtmetrix_grade)

                gtmetrix_performance =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[2]/span/span"))).get_attribute('textContent')
                gtmetrix_performance = gtmetrix_performance.replace("%","")
                gtmetrix_performance = int(gtmetrix_performance)
                print (gtmetrix_performance)

                gtmetrix_structure =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[3]/span/span"))).get_attribute('textContent')
                gtmetrix_structure = gtmetrix_structure.replace("%","")
                gtmetrix_structure = int(gtmetrix_structure)
                print (gtmetrix_structure)

                gtmetrix_lcp =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[1]/span"))).get_attribute('textContent')
                print (gtmetrix_lcp)

                gtmetrix_tbt =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[2]/span"))).get_attribute('textContent')
                print (gtmetrix_tbt)

                gtmetrix_cls =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[3]/span"))).get_attribute('textContent')
                print (gtmetrix_cls)

                gtmetrix_current_url = driver.current_url
                # print (gtmetrix_current_url)
                if gtmetrix_grade == "A":
                    grade_score = 100
                if gtmetrix_grade == "B":
                    grade_score = 80
                if gtmetrix_grade == "C":
                    grade_score = 60
                if gtmetrix_grade == "D":
                    grade_score = 40
                if gtmetrix_grade == "E":
                    grade_score = 20
                if gtmetrix_grade == "F":
                    grade_score = 0
                # print (grade_score)
                gtmetrix_result_score = round((grade_score + gtmetrix_performance + gtmetrix_structure)/3)
                # print (gtmetrix_result_score)
                print ("Successfully Completed GTMetrix test on "+ mainURL)
                driver.close()
            else:
                print ("GTMetrix Test Failed on "+ mainURL)
                driver.close()
            

        except:
            print ("GTMetrix Test Failed on "+ mainURL)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
    
                            {"Site URL" : site_url},
                            
                            {"GTMetrix Test Result":     [{  "GTMetrix Results" :gtmetrix_result_score,           
                                                            "Grade" : gtmetrix_grade,
                                                            "Performance" : gtmetrix_performance,
                                                            "Structure" :gtmetrix_structure,
                                                            "Largest Contentful Paint (LCP)" : gtmetrix_lcp,
                                                            "Total Blocking Time (TBT)" : gtmetrix_tbt,
                                                            "Cumulative Layout Shift (CLS)" : gtmetrix_cls,
                                                            "GTMetrix Result Page": gtmetrix_current_url }]}
        ]})
        return Response(data)



class SSL_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def ssl_lab():
        print ("Performing Secure Server and Web Application test on "+ mainURL)
        url = "https://www.ssllabs.com/ssltest/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[1]/center/form/table/tbody/tr[1]/td[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    find_table= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@id = 'multiTable']")))
                    if find_table:
                        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[4]/div")))  
                        driver.find_element(By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[2]/span[1]/b/a").click()
                except:pass
                ssl_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='gradeA']"))).text
                print (ssl_grade)
                certificate = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Certificate']//following::div").get_attribute("class")
                certificate=list(certificate)
                certificate =certificate[-3]+certificate[-2]+certificate[-1]
                if certificate == "300":
                    certificate = 100

                elif certificate == "270":
                    certificate = 90

                elif certificate == "240":
                    certificate = 80

                elif certificate == "210":
                    certificate = 70

                elif certificate == "180":
                    certificate = 60

                elif certificate == "150":
                    certificate = 50

                elif certificate == "120":
                    certificate = 40

                elif certificate == "_90":
                    certificate = 30

                elif certificate == "_60":
                    certificate = 20

                elif certificate == "_30":
                    certificate = 10

                elif certificate == "h_1":
                    certificate = 0
                print (certificate)

                protocol_support = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Protocol Support']//following::div").get_attribute("class")
                protocol_support=list(protocol_support)
                protocol_support =protocol_support[-3]+protocol_support[-2]+protocol_support[-1]
                if protocol_support == "300":
                    protocol_support = 100

                elif protocol_support == "270":
                    protocol_support = 90

                elif protocol_support == "240":
                    protocol_support = 80

                elif protocol_support == "210":
                    protocol_support = 70

                elif protocol_support == "180":
                    protocol_support = 60

                elif protocol_support == "150":
                    protocol_support = 50

                elif protocol_support == "120":
                    protocol_support = 40

                elif protocol_support == "_90":
                    protocol_support = 30

                elif protocol_support == "_60":
                    protocol_support = 20

                elif protocol_support == "_30":
                    protocol_support = 10

                elif protocol_support == "h_1":
                    protocol_support = 0
                print (protocol_support)

                key_exchange = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Key Exchange']//following::div").get_attribute("class")
                key_exchange=list(key_exchange)
                key_exchange =key_exchange[-3]+key_exchange[-2]+key_exchange[-1]
                if key_exchange == "300":
                    key_exchange = 100

                elif key_exchange == "270":
                    key_exchange = 90

                elif key_exchange == "240":
                    key_exchange = 80

                elif key_exchange == "210":
                    key_exchange = 70

                elif key_exchange == "180":
                    key_exchange = 60

                elif key_exchange == "150":
                    key_exchange = 50

                elif key_exchange == "120":
                    key_exchange = 40

                elif key_exchange == "_90":
                    key_exchange = 30

                elif key_exchange == "_60":
                    key_exchange = 20

                elif key_exchange == "_30":
                    key_exchange = 10

                elif key_exchange == "h_1":
                    key_exchange = 0
                print (key_exchange)   

                ciper_strength = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Cipher Strength']//following::div").get_attribute("class")
                ciper_strength=list(ciper_strength)
                ciper_strength =ciper_strength[-3]+ciper_strength[-2]+ciper_strength[-1]
                if ciper_strength == "300":
                    ciper_strength = 100

                elif ciper_strength == "270":
                    ciper_strength = 90

                elif ciper_strength == "240":
                    ciper_strength = 80

                elif ciper_strength == "210":
                    ciper_strength = 70

                elif ciper_strength == "180":
                    ciper_strength = 60

                elif ciper_strength == "150":
                    ciper_strength = 50

                elif ciper_strength == "120":
                    ciper_strength = 40

                elif ciper_strength == "_90":
                    ciper_strength = 30

                elif ciper_strength == "_60":
                    ciper_strength = 20

                elif ciper_strength == "_30":
                    ciper_strength = 10

                elif ciper_strength == "h_1":
                    ciper_strength = 0

                else:
                    pass
                print (ciper_strength)
                ssl_lab_current_url = driver.current_url
                # print (ssl_lab_current_url)
                if ssl_grade == "A+":
                    ssl_grade_score = 100
                if ssl_grade == "A":
                    ssl_grade_score = 90
                if ssl_grade == "B":
                    ssl_grade_score = 80
                if ssl_grade == "C":
                    ssl_grade_score = 60
                if ssl_grade == "D":
                    ssl_grade_score = 40
                if ssl_grade == "E":
                    ssl_grade_score = 20
                if ssl_grade == "F":
                    ssl_grade_score = 10
                if ssl_grade == "T":
                    ssl_grade_score = 0
                ssl_lab_test_score = round((ssl_grade_score + certificate + protocol_support + key_exchange + ciper_strength)/5)
                print ("Successfully Completed Secure Server and Web Application test on "+ mainURL)
                driver.close()


            else:
                print ("Secure Server and Web Application test Failed on "+ mainURL)
                driver.close()


        except:
            print ("Secure Server and Web Application test Failed on "+ mainURL)
            driver.close()
        
        
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},


                            {"SSL Lab Test Result":                 [{ "Secure Server and Web Application" : ssl_lab_test_score,
                                                                        "Overall" : ssl_grade,
                                                                        "Certificate" : certificate,
                                                                        "Protocol" : protocol_support,
                                                                        "Key Exchange" : key_exchange,
                                                                        "Cipher Strength" : ciper_strength,
                                                                        "SSL Lab Test Result Page": ssl_lab_current_url }]},
        ]})
        return Response(data)


class Webpage_Perfomance_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def webpage_test():
        print ("Performing Webpage Performance test on "+ mainURL)
        url = "https://www.webpagetest.org/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='analytical-review']")))
            search_view = driver.execute_script("arguments[0].scrollIntoView();", search_view)
            time.sleep(1)
            search_input =driver.find_element(By.XPATH, "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.submit()
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result']")))
                time.sleep(2)
                current_page = driver.current_url
                print (current_page)
                time.sleep(2)
                modified_url = current_page+"/2/performance_optimization/"
                print (modified_url)
                time.sleep(2)
                driver.get(modified_url)
                time.sleep(2)
                result_grade=WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='grades']")))
                result_grade =driver.execute_script("arguments[0].scrollIntoView();", result_grade)
                time.sleep(2)
                performance_grade = driver.find_element(By.XPATH, "//li[@class='security']/a/h2").text
                print (performance_grade)
                first_byte_time = driver.find_element(By.XPATH, "//li[@class='first_byte_time']/a/h2").text
                print (first_byte_time)
                keep_alive = driver.find_element(By.XPATH, "//li[@class='keep_alive_enabled']/a/h2").text
                print (keep_alive)
                compress_trf = driver.find_element(By.XPATH, "//li[@class='compress_text']/a/h2").text
                print (compress_trf)
                compress_img = driver.find_element(By.XPATH, "//li[@class='compress_images']/a/h2").text
                print (compress_img)
                cache_static = driver.find_element(By.XPATH, "//li[@class='cache_static_content']/a/h2").text
                print (cache_static)
                effective_cdn = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").text
                print (effective_cdn)
                effective_cdn_colour = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").get_attribute("class")
                print (effective_cdn_colour)
                time.sleep(1)
                webpage_test_current_url = driver.current_url
                # print (webpage_test_current_url)
                if performance_grade == "A+":
                    performance_score = 100
                if performance_grade == "A":
                    performance_score = 90
                if performance_grade == "B":
                    performance_score = 80
                if performance_grade == "C":
                    performance_score = 60
                if performance_grade == "D":
                    performance_score = 40
                if performance_grade == "E":
                    performance_score = 20
                if performance_grade == "F":
                    performance_score = 0

                if first_byte_time == "A+":
                    first_byte_time_score = 100
                if first_byte_time == "A":
                    first_byte_time_score = 90
                if first_byte_time == "B":
                    first_byte_time_score = 80
                if first_byte_time == "C":
                    first_byte_time_score = 60
                if first_byte_time == "D":
                    first_byte_time_score = 40
                if first_byte_time == "E":
                    first_byte_time_score = 20
                if first_byte_time == "F":
                    first_byte_time_score = 0

                if keep_alive == "A+":
                    keep_alive_score = 100
                if keep_alive == "A":
                    keep_alive_score = 90
                if keep_alive == "B":
                    keep_alive_score = 80
                if keep_alive == "C":
                    keep_alive_score = 60
                if keep_alive == "D":
                    keep_alive_score = 40
                if keep_alive == "E":
                    keep_alive_score = 20
                if keep_alive == "F":
                    keep_alive_score = 0

                if compress_trf == "A+":
                    compress_trf_score = 100
                if compress_trf == "A":
                    compress_trf_score = 90
                if compress_trf == "B":
                    compress_trf_score = 80
                if compress_trf == "C":
                    compress_trf_score = 60
                if compress_trf == "D":
                    compress_trf_score = 40
                if compress_trf == "E":
                    compress_trf_score = 20
                if compress_trf == "F":
                    compress_trf_score = 0

                if compress_img == "A+":
                    compress_img_score = 100
                if compress_img == "A":
                    compress_img_score = 90
                if compress_img == "B":
                    compress_img_score = 80
                if compress_img == "C":
                    compress_img_score = 60
                if compress_img == "D":
                    compress_img_score = 40
                if compress_img == "E":
                    compress_img_score = 20
                if compress_img == "F":
                    compress_img_score = 0


                if cache_static == "A+":
                    cache_static_score = 100
                if cache_static == "A":
                    cache_static_score = 90
                if cache_static == "B":
                    cache_static_score = 80
                if cache_static == "C":
                    cache_static_score = 60
                if cache_static == "D":
                    cache_static_score = 40
                if cache_static == "E":
                    cache_static_score = 20
                if cache_static == "F":
                    cache_static_score = 0

                if effective_cdn_colour == "A" and effective_cdn == "✓":
                    effective_cdn_score = 100
                if effective_cdn_colour == "B" and effective_cdn == "✓":
                    effective_cdn_score = 80
                if effective_cdn_colour == "C" and effective_cdn == "✓":
                    effective_cdn_score = 60
                if effective_cdn_colour == "D" and effective_cdn == "✓":
                    effective_cdn_score = 40
                if effective_cdn_colour == "E" and effective_cdn == "✓":
                    effective_cdn_score = 20
                if effective_cdn_colour == "F" and effective_cdn == "✓":
                    effective_cdn_score = 10
                if effective_cdn == "X":
                    effective_cdn_score = 0
                webpage_performance_test_score = round((performance_score + first_byte_time_score + keep_alive_score + compress_trf_score + compress_img_score + cache_static_score + effective_cdn_score )/7)
                print ("Successfully Completed Webpage Performance test on "+ mainURL)
                
                driver.close()    
            else:
                print ("Webpage Performance Test Failed on "+ mainURL)
                driver.close()
            

        except:
            print ("Webpage Performance Test Failed on "+ mainURL)
            driver.close()
        
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                            

                            {"Webpage Performance Test Result":         [{  "Webpage Performance Test" : webpage_performance_test_score,
                                                                            "Security Score" : performance_grade,
                                                                            "First Byte time" : first_byte_time,
                                                                            "Keep Alive" : keep_alive,
                                                                            "Compress Transfer" : compress_trf,
                                                                            "Compress Image" : compress_img,
                                                                            "Cache Static Content" : cache_static,
                                                                            "Effective use of CDN" : effective_cdn,
                                                                            "Webpage Performance Test Result Page": webpage_test_current_url }]},
        ]})
        return Response(data)


class Website_Audit_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def website_audit_test():
        print ("Performing Website Audit test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("https://www.seobility.net/en/seocheck/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='cookieoptin_saveall']"))).click()
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='bigassform']/div[1]/div/form/div[1]/div[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row analysisheading']")))
                time.sleep(4)
                seo_score = driver.find_element(By.XPATH, "//*[@id='pieLabel0']/div").text
                seo_score = int(seo_score.replace("%", ""))
                print (seo_score)
                meta_information = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/div").text
                meta_information = int(meta_information.replace("%", ""))
                print (meta_information)
                page_quality = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div").text
                page_quality = int(page_quality.replace("%", ""))
                print (page_quality)
                page_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[3]/div[2]/div/div").text
                page_structure = int(page_structure.replace("%", ""))
                print (page_structure)
                link_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div/div").text
                link_structure = int(link_structure.replace("%", ""))
                print (link_structure)
                server = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div[2]/div/div").text
                server = int(server.replace("%", ""))
                print (server)
                external_factors = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[6]/div[2]/div/div").text
                external_factors = int(external_factors.replace("%", ""))
                print (external_factors)
                response_time = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[2]/span").text
                response_time = response_time.replace("s","")
                print (response_time)
                file_size = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span").text
                file_size = file_size.replace("kB", "")
                print (file_size)
                text_words = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/span").text
                print (text_words)
                media_files = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[4]/div/div[2]/span").text
                print (media_files)
                no_of_links = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[5]/div/div[2]/span").text
                no_of_links = no_of_links.split("/")
                internal_links = no_of_links[0].replace("internal", "")
                external_links = no_of_links[1].replace("external", "")
                print (internal_links)
                print (external_links)
            
                website_audit_current_url = driver.current_url
                # print (website_audit_current_url)
                website_audit_score = seo_score
                print ("Successfully Completed Website Audit test on "+ mainURL)
                driver.close()


            else:
                print ("Website Audit Test Failed on "+ mainURL)
                driver.close()
        except:
            print ("Website Audit Test Failed on "+ mainURL)
            driver.close()

        
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},
                            

                            {"Website Audit Test Result":               [{  "Website Audit" : website_audit_score,
                                                                            "SEO Score" : seo_score,
                                                                            "Meta Information" : meta_information,
                                                                            "Page Quality" : page_quality,
                                                                            "Page Structure" : page_structure,
                                                                            "Link Structure" : link_structure,
                                                                            "Server" : server,
                                                                            "External Factors" : external_factors,
                                                                            "Response Time in Seconds" : response_time,
                                                                            "File Size in KB" : file_size,
                                                                            "Text Words" : text_words,
                                                                            "Media Files" : media_files,
                                                                            "Number Of Internal Links" : internal_links,
                                                                            "Number Of External Links" : external_links,
                                                                            "Website Audit Test Result Page": website_audit_current_url }]},
        ]})
        return Response(data)



class Domain_Index_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def google_domain_index():
        print ("Performing SERP Link - Domain Index test on Google for "+ clean_url)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(1)
                try:
                  google_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                  google_serp_result = (google_serp_result.split()[1])
                  print (google_serp_result)
                except:
                  google_serp_result = "No Results Found"
                print (google_serp_result)
                google_serp_current_url = driver.current_url
                # print (google_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Google for "+ clean_url)
                # driver.close()

            else:
                print ("SERP Link - Domain Index test on Google Failed for "+ clean_url)
                # driver.close()


        except:
            print ("SERP Link - Domain Index test on Google Failed for "+ clean_url)
            # driver.close()


    # def yahoo_domain_index():
        print ("Performing SERP Link - Domain Index test on Yahoo for "+ clean_url)
        url = "https://in.search.yahoo.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='sbq']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(1)
                try:
                  yahoo_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class=' fz-14 lh-22']"))).text
                  yahoo_serp_result = (yahoo_serp_result.split()[1])
                except:
                  yahoo_serp_result = "No Results Found"
                print (yahoo_serp_result)
                yahoo_serp_current_url = driver.current_url
                # print (yahoo_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Yahoo for "+ clean_url)
                # driver.close()

            else:
                print ("SERP Link - Domain Index test on Yahoo Failed for "+ clean_url)
                # driver.close()

        except:
            print ("SERP Link - Domain Index test on Yahoo Failed for "+ clean_url)
            # driver.close()


    # def bing_domain_index():
        print ("Performing SERP Link - Domain Index test on Bing for "+ clean_url)
        url = "https://www.bing.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@id='sb_form_q']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.submit()
                time.sleep(3)
                try:
                  bing_serp_result = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class='sb_count']"))).text
                # bing_serp_result = (bing_serp_result.split()[0])
                  bing_serp_result = bing_serp_result.replace("About", "").replace("Results", "").replace("results", "")      
                except:
                  bing_serp_result = "No Result Found"     
                print (bing_serp_result)
                bing_serp_current_url = driver.current_url
                # print (bing_index_current_url)
                print ("Successfully Completed SERP Link - Domain Index test on Bing for "+ clean_url)
                driver.close()

            else:
                print ("SERP Link - Domain Index test on Bing Failed for "+ clean_url)
                driver.close()

        except:
            print ("SERP Link - Domain Index test on Bing Failed for "+ clean_url)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                            {"SERP Links - Domain Index Test Result":       [{  "Google" : google_serp_result,
                                                                                "Google Test Page" : google_serp_current_url,
                                                                                "Yahoo" : yahoo_serp_result,
                                                                                "Yahoo Test Page" : yahoo_serp_current_url,
                                                                                "Bing" : bing_serp_result,
                                                                                "Bing Test Page" : bing_serp_current_url}]},
        ]})
        return Response(data)


class Pingdom_Tools_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def pingdom_tools_test()
        print ("Performing Pingdom Tools test for "+ mainURL)
        url = "https://tools.pingdom.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='urlInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH , "//div[@class='grid ng-star-inserted']")))
                time.sleep(10)
                performance_grade = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/app-grade-badge/span").text
                performance_score = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/div[2]").text
                pingdom_performance = performance_grade+performance_score
                print (pingdom_performance)
                pingdom_page_size = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[2]/app-metric/div[2]").text
                print (pingdom_page_size)
                pingdom_load_time = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[3]/app-metric/div[2]").text
                print (pingdom_load_time)
                pingdom_request = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[4]/app-metric/div[2]").text
                print (pingdom_request)

                pingdom_tools_current_url = driver.current_url
                # print (pingdom_tools_current_url)
                pingdom_test_score = performance_score
                pingdom_test_score = int(pingdom_test_score)
                print ("Successfully Completed Pingdom Tools test for "+ mainURL)
                driver.close()
            else:
                print ("Pingdom Tools Test Failed for "+ mainURL)
                driver.close()
        except:
            print ("Pingdom Tools Test Failed for "+ mainURL)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                            {"Pingdom Tools Test Result":           [{  "Pingdom Tools Test" : performance_score,
                                                                        "Performance grade" : pingdom_performance,
                                                                        "Page size" : pingdom_page_size,
                                                                        "Load time" : pingdom_load_time,
                                                                        "Requests" : pingdom_request,
                                                                        "Pingdom Tools Test Result Page" : pingdom_tools_current_url}]},
        ]})
        return Response(data)



class Map_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
        map_url = urlsplit(mainURL).netloc
        print (map_url)
    # def on_map():
        print ("Performing Google Map Location Test for "+ mainURL)
        url = "https://www.google.com/maps"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='searchboxinput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(map_url)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                time.sleep(1)
                try:
                    time.sleep(5)
                    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Io6YTe fontBodyMedium']")))
                    if result :
                        time.sleep(1)
                        map_result = "Map Location Found"
                        print (map_result)
                        on_map_current_url = driver.current_url
                        # print (on_map_current_url)
                        print ("Successfully Completed Google Map Location test for "+ mainURL)
                        driver.close()

                except:
                    time.sleep(1)
                    map_result = "Map Location Not Found"
                    print (map_result)
                    on_map_current_url = driver.current_url
                    # print (on_map_current_url)
                    print ("Google Map Location Test Failed for "+ mainURL)
                    driver.close()
        except:
            print ("Google Map Location Test Failed for "+ mainURL)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                            {"Google Map Test Result":              [{  "Google Map" : map_result,
                                                                        "Google Map Test Result Page" : on_map_current_url}]},
        ]})
        return Response(data)


class DNS_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def dns_test():
        print ("Performing DNS Health Test for "+ mainURL)
        url = "https://mxtoolbox.com/domain/"
        # options = uc.ChromeOptions()

        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'txtToolInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//span[@id = 'spanTestsRemaining'][text()='Complete']")))
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'tilesResults']")))
                problem_errors =driver.find_element(By.XPATH, "//span[@id='spanNumErrors']").text
                print (problem_errors)
                problem_warnings =driver.find_element(By.XPATH, "//span[@id='spanNumWarnings']").text
                print (problem_warnings)
                blacklist_errors =driver.find_element(By.XPATH, "//span[@id='blacklistNumFailed']").text
                print (blacklist_errors)
                blacklist_warnings =driver.find_element(By.XPATH, "//span[@id='blacklistNumWarning']").text
                print (blacklist_warnings)
                mail_server_errors =driver.find_element(By.XPATH, "//span[@id='smtpNumFailed']").text
                print (mail_server_errors)
                mail_server_warnings =driver.find_element(By.XPATH, "//span[@id='smtpNumWarning']").text
                print (mail_server_warnings)
                web_server_errors =driver.find_element(By.XPATH, "//span[@id='webNumFailed']").text
                print (web_server_errors)
                web_server_warnings =driver.find_element(By.XPATH, "//span[@id='webNumWarning']").text
                print (web_server_warnings)
                dns_errors =driver.find_element(By.XPATH, "//span[@id='dnsNumFailed']").text
                print (dns_errors)
                dns_warnings =driver.find_element(By.XPATH, "//span[@id='dnsNumWarning']").text
                print (dns_warnings)
                dns_test_current_url = driver.current_url
                # print (dns_test_current_url)
                dns_test_score = 60
                print ("Successfully Completed DNS Health test for "+ mainURL)
                time.sleep(1)
                driver.close()

        except:
            print ("DNS Health test Failed for "+ mainURL)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                            

                            {"DNS Health Test Result":             [ {"DNS Health" : dns_test_score},
                                                                     {  "Problems"                      : [{ "Warnings" :problem_warnings,
                                                                                                             "Errors" : problem_errors}]},
                                                                     {  "Blacklist"                     : [{ "Warnings" : blacklist_warnings,
                                                                                                             "Errors" :  blacklist_errors}]},
                                                                     {  "Mail Server"                   : [{ "Warnings" : mail_server_warnings,
                                                                                                             "Errors" :  mail_server_errors}]},
                                                                     {  "Web Server"                    : [{ "Warnings" : web_server_warnings,
                                                                                                             "Errors" :  web_server_errors}]},
                                                                     {  "DNS"                           : [{ "Warnings" : dns_warnings,
                                                                                                            "Errors" :  dns_errors}]},
                                                                     {  "DNS Health Test Result Page"   : dns_test_current_url}]},
        ]})
        return Response(data)



class Mobile_Friendly_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def mobile():
        print ("Performing Mobile Friendly Test for "+ mainURL)
        url = "https://technicalseo.com/tools/mobile-friendly/"
        # options = uc.ChromeOptions()
        # # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/section/div/div[1]/div/form/div/div[1]/md-input-container/div[1]/textarea")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                driver.find_element(By.XPATH, "//*[@id='mobile_friendly_form']/div/div[2]/md-input-container/button").click()
                mobile_friendly_result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i")))
                try:
                    mobile_friendly_result = driver.find_element(By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i").get_attribute("class")
                    if mobile_friendly_result == "mdi mdi-check-circle mdi-cell":
                        mobile_friendly_result = "YES"
                    else:
                        mobile_friendly_result = "NO"
                    mobile_friendly_current_url = driver.current_url
                    if mobile_friendly_result == "YES":
                        mobile_friendly_test_score = 100
                    else:
                        mobile_friendly_test_score = 0
                    print ("Successfully Completed Mobile Friendly test for "+ mainURL)
                    driver.close()
                except:
                  print ("Mobile Friendly Test Failed for "+ mainURL)
                  driver.close()
        except:
          print ("Mobile Friendly Test Failed for "+ mainURL)
          driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},
                            

                            {"Mobile Friendly Test Result":             [{  "Mobile Friendly Test" : mobile_friendly_test_score,
                                                                            "Mobile Friendly" : mobile_friendly_result,
                                                                            "Mobile Friendly Test Result Page" : mobile_friendly_current_url}]}
        ]})
        return Response(data)



class HTML_Validation_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)

        only_domain = clean_url.replace(".", " ")
        only_domain = (only_domain.split()[0])
        print (only_domain)
        
    # def HTML_Validation_test()        
        print ("Performing W3 NU HTML VALIDATOR test for "+ mainURL)
        url = "https://html5.validator.nu/"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='doc']")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='results']/ol")))
                markup_warning = len(driver.find_elements(By.XPATH, "//div[@id='results']//following::li[@class='info warning']"))
                print (markup_warning)
                markup_error = len(driver.find_elements(By.XPATH, ("//div[@id='results']//following::li[@class='error']") ))
                print (markup_error)
                time.sleep(3)
                markup_validation_current_url = driver.current_url
                # print (markup_validation_current_url)
                print ("Successfully Completed W3 NU HTML VALIDATOR test for "+ mainURL)
                driver.close()
            else:
                print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
                driver.close()

        except:
            print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
            driver.close()
        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        data = ({"Result" :[{"Date" : current_date},
      
                            {"Site URL" : site_url},

                        

                            {"W3 NU HTML VALIDATOR Test Result":        [{  "W3 NU HTML VALIDATOR" : 80,
                                                                            "Warnings" : markup_warning,
                                                                            "Errors" : markup_error,
                                                                            "W3 NU HTML VALIDATOR Test Result Page" : markup_validation_current_url}]},
        ]})
        return Response(data)

class Social_Profile_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('--mute-audio')
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        print (mainURL)
        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)
        only_domain = clean_url.replace(".", " ")
        only_domain = (only_domain.split()[0])
        print (only_domain)
        try:
            try:
                facebook_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://www.facebook.com/')]").get_attribute('href')
            except:
                facebook_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://facebook.com/')]").get_attribute('href')
            print (facebook_link)
            driver.get(facebook_link)
            try:
                facebook_link_type = driver.current_url
                print (facebook_link_type)
                if "/people" in facebook_link_type or "/profile" in facebook_link_type:
                    data_list = driver.find_elements(By.XPATH, ("//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w x1cy8zhl xyamay9']/span/a"))
                    # print (data_list)
                    for data in data_list:
                        print (data)
                        if "followers" in data.get_attribute("href"):
                            facebook_followers = data.get_attribute("textContent")
                            facebook_followers = facebook_followers.replace("followers", "")
                            print (facebook_followers)
                            facebook_rr = driver.find_element(By.XPATH, ("//a[contains(@href,'reviews')]/div/div/span")).text
                            clean = facebook_rr.replace("(" ,"")
                            # review = rating_data.replace("(" ,"")
                            rating = (clean.split()[2])
                            review = (clean.split()[3])
                            if rating =="rated":
                                rating = "N/A"
                    try:
                        if facebook_link:
                            pass
                        if facebook_followers:
                            pass
                        if rating:
                            pass
                        if review:
                            pass
                    except:
                        facebook_link = 0
                        facebook_followers = 0
                        rating = 0
                        review = 0
                else:
                    facebook_link = 0
                    facebook_followers = 0
                    rating = 0
                    review = 0
            except:
                facebook_link = 0
                facebook_followers = 0
                rating = 0
                review = 0
                # print ("No")
                    # data_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf xeuugli x1r8uery x1iyjqo2 xs83m0k x1swvt13 x1pi30zi xqdwrps x16i7wwg x1y5dvz6']")))
                    # data= driver.find_elements(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 xo1l8bm xi81zsa']//following::a").get_attribute('textContent')
                    # for datas in data:
                    #     print (data)
                    
        except:
            facebook_link = 0
            facebook_followers = 0
            rating = 0
            review = 0
            print ("No Facebook")
        
           
        try:
            driver.get(mainURL)
            try:
                insta_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://www.instagram.com/')]").get_attribute('href')   
                driver.get(insta_link)
                print (insta_link)
                data_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class=' x78zum5 x1q0g3np      xieb3on']"))).get_attribute('class')
                instagram_followers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class=' x78zum5 x1q0g3np      xieb3on']/li[2]/button/div/span/span"))).get_attribute('textContent')
                instagram_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class=' x78zum5 x1q0g3np      xieb3on']/li/button/div/span/span"))).get_attribute('textContent')
                # followers = driver.find_element(By.XPATH, "//span[@class='_ac2a' ]").get_attribute('title')
                print (instagram_followers)
                print (instagram_post) 
                
            except:
                insta_link = 0
                instagram_followers = 0
                instagram_post = 0
                print ("No insta Link")
            
                
        except:
            print ("No insta link")
        try:
            driver.get(mainURL)
            try:
                linked_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://in.linkedin.com/')]").get_attribute('href')  
            except:
                linked_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://www.linkedin.com/')]").get_attribute('href')
            print (linked_link)
            if linked_link:
                print (linked_link)
            #     driver.get(linked_link)
            #     data_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='before:middot']"))).text
            #     # instagram_followers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class=' x78zum5 x1q0g3np      xieb3on']/li[2]/button/div/span/span"))).get_attribute('textContent')
            #     # # followers = driver.find_element(By.XPATH, "//span[@class='_ac2a' ]").get_attribute('title')
            #     print (data_bar)
                
        except:
            linked_link = 0
            print ("No linkedin Link")
            
    
        try:
            driver.get(mainURL)
            try:
                twitter_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://twitter.com/')]").get_attribute('href')  
                driver.get(twitter_link)
                print (twitter_link)
                data_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj']")))
                time.sleep(1)
                twitter_tweets = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").get_attribute("textContent")
                
                twitter_followers = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj']/div[2]/a/span/span").get_attribute("textContent")
                # followers = driver.find_element(By.XPATH, "//span[@class='_ac2a' ]").get_attribute('title')
                twitter_tweets = twitter_tweets.replace("Tweets", "")
                print (twitter_tweets)
                print (twitter_followers)
                
            except:
                twitter_link = 0
                twitter_tweets = 0
                twitter_followers = 0
                print ("No Twitter Link")
            
                
        except:
            print ("No Twitter link")
        try:
            driver.get(mainURL)
            try:
                youtube_link=driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://www.youtube.com/channel/')]").get_attribute('href') 
                driver.get(youtube_link)
                print (youtube_link)
                youtube_follower = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//yt-formatted-string[@id='subscriber-count']"))).get_attribute('textContent')
                youtube_follower = youtube_follower.replace("subscribers" , "")
                # time.sleep(1)
                # twitter_followers = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj']/div[2]/a/span/span").get_attribute("textContent")
                # followers = driver.find_element(By.XPATH, "//span[@class='_ac2a' ]").get_attribute('title')
                print (youtube_follower)
                
            except:
                youtube_link = 0
                youtube_follower = 0
                print ("No Youtube Link")

            
                
        except:
            print ("No Youtube link")

        driver.get("https://www.google.com")
        try:
            time.sleep(1)
            remove_button = driver.find_element(By.XPATH, "//button[@id='L2AGLb']").click()
        except:
            pass

        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(only_domain)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    google_rating = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Ob2kfd']/div/span"))).get_attribute("textContent")
                    if google_rating:
                        google_link = driver.current_url
                    
                except:
                    google_rating = "N/A"
                    google_link = "N/A"
                try:
                    google_reviews = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Ob2kfd']/div/span[3]/span/a/span"))).get_attribute("textContent")       
                    google_reviews = google_reviews.replace("Google reviews", "")
                except:
                    google_reviews = "N/A"

                # google_link = driver.current_url
                print (google_rating)
                print (google_reviews)
                print (google_link)
        except:
            pass
        response = {
                    "Facebook" : [{"Facebook Followers" : facebook_followers,
                                   "Facebook Ratings" : rating,
                                   "Facebook Reviews" : review}],
                    "Linkedin Link" : linked_link,
                    "Instagram" :   [{"Instagram Followers" : instagram_followers,
                                      "Instagram Posts" : instagram_post,
                                      "Instagram Page Link" : insta_link}],
                    # "LinkedIn Link" : linked_link,
                    "Youtube" : [{"Youtube Followers" : youtube_follower,
                                  "Youtube Link": youtube_link}],
                    "Twitter Link" : [{"Twitter Tweets" : twitter_tweets,
                                       "Twitter Followers" : twitter_followers,
                                       "Twitter Page Link" : twitter_link}],
                    "Google" : [{"Google Ratings" : google_rating,
                                 "Google Reviews" : google_reviews,
                                 "Google Link" : google_link}]
                    }
        
        return Response(response)




class SEO_Report_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL
        try:
            url = mainURL
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            # Find all elements with the tag 'a'
            links = soup.find_all(['a','img','link','script','iframe','source','picture','video'])

            # Extract the 'href' attribute from each element and add it to the links list
            links_list = []
            for link in links:
                url = link.get("href") or link.get("src")
                if url and (url.startswith("http") or url.startswith("www")):
                    status_res = requests.head(url)
                    # status = "OK" if status_res.status_code == 200 else "Not OK"
                    reason = status_res.reason
                    links_list.append({'link' : url, 'status code': status_res.status_code, "status" : reason})
                total_links = len(links_list)
                current_date= datetime.now().strftime("%b-%d-%Y ")
                current_time= datetime.now().strftime("%H:%M:%S")
                current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
                print (current_date)
                print (current_time)
                print(current_date_time)
                response = ({"Result" :[{"Date" : current_date},
                                    {"Site URL" : site_url},
                                    {"total_links" : total_links},

                                    {"Result":        [{  "Links" : links_list }]},

                ]})
        except:
            current_date= datetime.now().strftime("%b-%d-%Y ")
            current_time= datetime.now().strftime("%H:%M:%S")
            current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
            print (current_date)
            print (current_time)
            print(current_date_time)
            response = ({"Result" :[{"Date" : current_date},
                                {"Site URL" : site_url},
                                {"error" : "Please check the URL or Internet Connection and Try Again"},
                                
            ]})

        return Response(response)





class Full_Test(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        site_url = mainURL
        print("Site URL===="+ site_url)
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)

        map_url = urlsplit(mainURL).netloc
        print (map_url)



        url = "https://wheregoes.com/"
        print ("Performing Redirection Test on "+ clean_url)
        driver.get(url)
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(clean_url) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_1 = mainURL

                    else:
                        redirection_result_1 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ clean_url)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ url_with_www)
            if search_input:
                time.sleep(1)
                search_input.send_keys(url_with_www) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_2 = mainURL
                    else:
                        redirection_result_2 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ url_with_www)
                except:
                    print ("Redirection Test Failed on "+ clean_url)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_1)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_1) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_3 = mainURL
                    else:
                        redirection_result_3 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_1)    
                except:
                    print ("Redirection Test Failed on "+ alternate_url_1)
            
            
            search_input = driver.find_element(By.XPATH , "//input[@id='url']")
            print ("Performing Redirection Test on "+ alternate_url_2)
            if search_input:
                time.sleep(1)
                search_input.send_keys(alternate_url_2) 
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='trace-results']")))
                try:
                    status = driver.find_elements(By.XPATH , "//a[text()='200']")
                    if status:
                        redirection_result_4 = mainURL
                    else:
                        redirection_result_4 = "Failed"
                    print ("Successfully Completed Redirection Test on "+ alternate_url_2)
                    if redirection_result_1 != "Failed":
                        redirection_result_1_score = 100
                    else:
                        redirection_result_1_score = 0
                    if redirection_result_2 != "Failed":
                        redirection_result_2_score = 100
                    else:
                        redirection_result_2_score = 0
                    if redirection_result_3 != "Failed":
                        redirection_result_3_score = 100
                    else:
                        redirection_result_3_score = 0
                    if redirection_result_4 != "Failed":
                        redirection_result_4_score = 100
                    else:
                        redirection_result_4_score = 0

                    
                    site_redirection_score = round((redirection_result_1_score + redirection_result_2_score + redirection_result_3_score + redirection_result_4_score) / 4)
                    site_redirection_score = int(site_redirection_score)
                    print(site_redirection_score)
                    # driver.close()
                except:
                    print ("Redirection Test Failed on "+ alternate_url_2)
                    # driver.close()
                
        except:
            print("Redirection Test Failed Completely")
            # driver.close()


    # def google_index1():
        print ("Performing Google Index test on "+ "site:"+clean_url)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()    
        # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)
        try:
            time.sleep(1)
            remove_button = driver.find_element(By.XPATH, "//button[@id='L2AGLb']").click()
        except:
            pass
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+clean_url)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index = (google_index.split()[1])
                print (google_index)

                google_index_current_url = driver.current_url
                # print (google_index_current_url)
                if google_index != 0:
                    google_index_score = 100
                else:
                    google_index_score = 0
                print ("Successfully Completed Google Index test on "+ "site:"+clean_url)
                # driver.close()
            else:
                print ("Google Index test Failed on "+ "site:"+clean_url)
                # driver.close()
        except:
            print ("Google Index test Failed on "+ "site:"+clean_url)
            # driver.close()


    # def google_index2():
        print ("Performing Google Index test on "+ "site:"+url_with_www)
        url = "https://www.google.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.get(url)
        try:
            time.sleep(1)
            remove_button = driver.find_element(By.XPATH, "//button[@id='L2AGLb']").click()
        except:
            pass
        try:
            time.sleep(1)
            search_input = driver.find_element(By.XPATH , "//input[@class='gLFyf']")
            if search_input:
                time.sleep(1)
                search_input.send_keys("site:"+url_with_www)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                google_index_2 = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result-stats']"))).text
                google_index_2 = (google_index_2.split()[1])
                print (google_index_2)

                google_index_2_current_url = driver.current_url
                # print (google_index_2_current_url)
                if google_index_2 != 0:
                    google_index_2_score = 100
                else:
                    google_index_2_score = 0
                page_indexed_in_google_score = round((google_index_score + google_index_2_score)/2)
                print ("Successfully Completed Google Index test on "+ "site:"+url_with_www)
                # driver.close()

            else:
                print ("Google Index test Failed on "+ "site:"+url_with_www)
                # driver.close()


        except:
            print ("Google Index test Failed on "+ "site:"+url_with_www)
            # driver.close()

    # def gtmetrix_test():
        print ("Performing GTMetrix test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("https://gtmetrix.com/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/section[1]/div/form/div[1]/div[1]/div/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                gtmetrix_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[1]/i"))).get_attribute('class')
                gtmetrix_grade = gtmetrix_grade[-1]
                print (gtmetrix_grade)

                gtmetrix_performance =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[2]/span/span"))).get_attribute('textContent')
                gtmetrix_performance = gtmetrix_performance.replace("%","")
                gtmetrix_performance = int(gtmetrix_performance)
                print (gtmetrix_performance)

                gtmetrix_structure =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div/div[3]/span/span"))).get_attribute('textContent')
                gtmetrix_structure = gtmetrix_structure.replace("%","")
                gtmetrix_structure = int(gtmetrix_structure)
                print (gtmetrix_structure)

                gtmetrix_lcp =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[1]/span"))).get_attribute('textContent')
                print (gtmetrix_lcp)

                gtmetrix_tbt =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[2]/span"))).get_attribute('textContent')
                print (gtmetrix_tbt)

                gtmetrix_cls =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/article/div[2]/div[2]/div/div[3]/span"))).get_attribute('textContent')
                print (gtmetrix_cls)

                gtmetrix_current_url = driver.current_url
                # print (gtmetrix_current_url)
                if gtmetrix_grade == "A":
                    grade_score = 100
                if gtmetrix_grade == "B":
                    grade_score = 80
                if gtmetrix_grade == "C":
                    grade_score = 60
                if gtmetrix_grade == "D":
                    grade_score = 40
                if gtmetrix_grade == "E":
                    grade_score = 20
                if gtmetrix_grade == "F":
                    grade_score = 0
                # print (grade_score)
                gtmetrix_result_score = round((grade_score + gtmetrix_performance + gtmetrix_structure)/3)
                gtmetrix_result_score = int(gtmetrix_result_score)
                # print (gtmetrix_result_score)
                print ("Successfully Completed GTMetrix test on "+ mainURL)
                # driver.close()
            else:
                print ("GTMetrix Test Failed on "+ mainURL)
                # driver.close()
            

        except:
            print ("GTMetrix Test Failed on "+ mainURL)
            # driver.close()


    # def ssl_lab():
        print ("Performing Secure Server and Web Application test on "+ mainURL)
        url = "https://www.ssllabs.com/ssltest/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[1]/center/form/table/tbody/tr[1]/td[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    find_table= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@id = 'multiTable']")))
                    if find_table:
                        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[4]/div")))  
                        driver.find_element(By.XPATH, "//*[@id='multiTable']/tbody/tr[3]/td[2]/span[1]/b/a").click()
                except:pass
                ssl_grade =WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='gradeA']"))).text
                print (ssl_grade)
                certificate = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Certificate']//following::div").get_attribute("class")
                certificate=list(certificate)
                certificate =certificate[-3]+certificate[-2]+certificate[-1]
                if certificate == "300":
                    certificate = 100

                elif certificate == "270":
                    certificate = 90

                elif certificate == "240":
                    certificate = 80

                elif certificate == "210":
                    certificate = 70

                elif certificate == "180":
                    certificate = 60

                elif certificate == "150":
                    certificate = 50

                elif certificate == "120":
                    certificate = 40

                elif certificate == "_90":
                    certificate = 30

                elif certificate == "_60":
                    certificate = 20

                elif certificate == "_30":
                    certificate = 10

                elif certificate == "h_1":
                    certificate = 0
                print (certificate)

                protocol_support = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Protocol Support']//following::div").get_attribute("class")
                protocol_support=list(protocol_support)
                protocol_support =protocol_support[-3]+protocol_support[-2]+protocol_support[-1]
                if protocol_support == "300":
                    protocol_support = 100

                elif protocol_support == "270":
                    protocol_support = 90

                elif protocol_support == "240":
                    protocol_support = 80

                elif protocol_support == "210":
                    protocol_support = 70

                elif protocol_support == "180":
                    protocol_support = 60

                elif protocol_support == "150":
                    protocol_support = 50

                elif protocol_support == "120":
                    protocol_support = 40

                elif protocol_support == "_90":
                    protocol_support = 30

                elif protocol_support == "_60":
                    protocol_support = 20

                elif protocol_support == "_30":
                    protocol_support = 10

                elif protocol_support == "h_1":
                    protocol_support = 0
                print (protocol_support)

                key_exchange = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Key Exchange']//following::div").get_attribute("class")
                key_exchange=list(key_exchange)
                key_exchange =key_exchange[-3]+key_exchange[-2]+key_exchange[-1]
                if key_exchange == "300":
                    key_exchange = 100

                elif key_exchange == "270":
                    key_exchange = 90

                elif key_exchange == "240":
                    key_exchange = 80

                elif key_exchange == "210":
                    key_exchange = 70

                elif key_exchange == "180":
                    key_exchange = 60

                elif key_exchange == "150":
                    key_exchange = 50

                elif key_exchange == "120":
                    key_exchange = 40

                elif key_exchange == "_90":
                    key_exchange = 30

                elif key_exchange == "_60":
                    key_exchange = 20

                elif key_exchange == "_30":
                    key_exchange = 10

                elif key_exchange == "h_1":
                    key_exchange = 0
                print (key_exchange)   

                ciper_strength = driver.find_element(By.XPATH, "//div[@class='chartLabel'][text()='Cipher Strength']//following::div").get_attribute("class")
                ciper_strength=list(ciper_strength)
                ciper_strength =ciper_strength[-3]+ciper_strength[-2]+ciper_strength[-1]
                if ciper_strength == "300":
                    ciper_strength = 100

                elif ciper_strength == "270":
                    ciper_strength = 90

                elif ciper_strength == "240":
                    ciper_strength = 80

                elif ciper_strength == "210":
                    ciper_strength = 70

                elif ciper_strength == "180":
                    ciper_strength = 60

                elif ciper_strength == "150":
                    ciper_strength = 50

                elif ciper_strength == "120":
                    ciper_strength = 40

                elif ciper_strength == "_90":
                    ciper_strength = 30

                elif ciper_strength == "_60":
                    ciper_strength = 20

                elif ciper_strength == "_30":
                    ciper_strength = 10

                elif ciper_strength == "h_1":
                    ciper_strength = 0

                else:
                    pass
                print (ciper_strength)
                ssl_lab_current_url = driver.current_url
                # print (ssl_lab_current_url)
                if ssl_grade == "A+":
                    ssl_grade_score = 100
                if ssl_grade == "A":
                    ssl_grade_score = 90
                if ssl_grade == "B":
                    ssl_grade_score = 80
                if ssl_grade == "C":
                    ssl_grade_score = 60
                if ssl_grade == "D":
                    ssl_grade_score = 40
                if ssl_grade == "E":
                    ssl_grade_score = 20
                if ssl_grade == "F":
                    ssl_grade_score = 10
                if ssl_grade == "T":
                    ssl_grade_score = 0
                ssl_lab_test_score = round((ssl_grade_score + certificate + protocol_support + key_exchange + ciper_strength)/5)
                ssl_lab_test_score  = int(ssl_lab_test_score)
                print ("Successfully Completed Secure Server and Web Application test on "+ mainURL)
                # driver.close()


            else:
                print ("Secure Server and Web Application test Failed on "+ mainURL)
                # driver.close()


        except:
            print ("Secure Server and Web Application test Failed on "+ mainURL)
            # driver.close()


    

    # def website_audit_test():
        print ("Performing Website Audit test on "+ mainURL)
        url = "https://www.croxyproxy.com/"
        driver.get(url)
        time.sleep(1)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='url']")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("https://www.seobility.net/en/seocheck/")
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='cookieoptin_saveall']"))).click()
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='bigassform']/div[1]/div/form/div[1]/div[2]/input")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row analysisheading']")))
                time.sleep(4)
                seo_score = driver.find_element(By.XPATH, "//*[@id='pieLabel0']/div").text
                seo_score = int(seo_score.replace("%", ""))
                print (seo_score)
                meta_information = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/div").text
                meta_information = int(meta_information.replace("%", ""))
                print (meta_information)
                page_quality = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div").text
                page_quality = int(page_quality.replace("%", ""))
                print (page_quality)
                page_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[3]/div[2]/div/div").text
                page_structure = int(page_structure.replace("%", ""))
                print (page_structure)
                link_structure = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div/div").text
                link_structure = int(link_structure.replace("%", ""))
                print (link_structure)
                server = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div[2]/div/div").text
                server = int(server.replace("%", ""))
                print (server)
                external_factors = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[6]/div[2]/div/div").text
                external_factors = int(external_factors.replace("%", ""))
                print (external_factors)
                response_time = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[2]/span").text
                response_time = response_time.replace("s", "")
                print (response_time)
                file_size = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span").text
                file_size = file_size.replace("kB", "")
                print (file_size)
                text_words = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/span").text
                print (text_words)
                media_files = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[4]/div/div[2]/span").text
                print (media_files)
                no_of_links = driver.find_element(By.XPATH, "//*[@id='accountback']/div[1]/div[2]/div[3]/div[1]/div[5]/div/div[2]/span").text
                no_of_links = no_of_links.split("/")
                internal_links = no_of_links[0].replace("internal", "")
                external_links = no_of_links[1].replace("external", "")
                print (internal_links)
                print (external_links)
                website_audit_current_url = driver.current_url
                # print (website_audit_current_url)
                website_audit_score = seo_score
                print ("Successfully Completed Website Audit test on "+ mainURL)
                # driver.close()


            else:
                print ("Website Audit Test Failed on "+ mainURL)
                # driver.close()
        except:
            print ("Website Audit Test Failed on "+ mainURL)
            # driver.close()


    # def pingdom_tools_test()
        print ("Performing Pingdom Tools test for "+ mainURL)
        url = "https://tools.pingdom.com/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='urlInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH , "//div[@class='grid ng-star-inserted']")))
                time.sleep(10)
                performance_grade = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/app-grade-badge/span").text
                performance_score = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[1]/app-metric/div[2]").text
                pingdom_performance = performance_grade+performance_score
                print (pingdom_performance)
                pingdom_page_size = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[2]/app-metric/div[2]").text
                print (pingdom_page_size)
                pingdom_load_time = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[3]/app-metric/div[2]").text
                print (pingdom_load_time)
                pingdom_request = driver.find_element(By.XPATH , "/html/body/app-root/main/app-report/section[1]/app-summary/div/div/app-summary-player/div/div[2]/div/div[4]/app-metric/div[2]").text
                print (pingdom_request)

                pingdom_tools_current_url = driver.current_url
                # print (pingdom_tools_current_url)
                pingdom_test_score = performance_score
                pingdom_test_score = int(pingdom_test_score)
                print ("Successfully Completed Pingdom Tools test for "+ mainURL)
                # driver.close()
            else:
                print ("Pingdom Tools Test Failed for "+ mainURL)
                # driver.close()
        except:
            print ("Pingdom Tools Test Failed for "+ mainURL)
            # driver.close()



    # def mobile():
        print ("Performing Mobile Friendly Test for "+ mainURL)
        url = "https://technicalseo.com/tools/mobile-friendly/"
        # options = uc.ChromeOptions()
        # # options.add_argument("--headless")
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/section/div/div[1]/div/form/div/div[1]/md-input-container/div[1]/textarea")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                driver.find_element(By.XPATH, "//*[@id='mobile_friendly_form']/div/div[2]/md-input-container/button").click()
                mobile_friendly_result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i")))
                try:
                    mobile_friendly_result = driver.find_element(By.XPATH, "//*[@id='mobile_friendly_results']/tbody/tr/td[2]/i").get_attribute("class")
                    if mobile_friendly_result == "mdi mdi-check-circle mdi-cell":
                        mobile_friendly_result = "YES"
                    else:
                        mobile_friendly_result = "NO"
                    mobile_friendly_current_url = driver.current_url
                    if mobile_friendly_result == "YES":
                        mobile_friendly_test_score = 100
                    else:
                        mobile_friendly_test_score = 0
                    mobile_friendly_test_score = int(mobile_friendly_test_score)
                    print ("Successfully Completed Mobile Friendly test for "+ mainURL)
                    # driver.close()
                except:
                  print ("Mobile Friendly Test Failed for "+ mainURL)
                #   driver.close()
        except:
          print ("Mobile Friendly Test Failed for "+ mainURL)
        #   driver.close()


    
    # def dns_test():
        print ("Performing DNS Health Test for "+ mainURL)
        url = "https://mxtoolbox.com/domain/"
        # options = uc.ChromeOptions()

        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'txtToolInput']")))
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//span[@id = 'spanTestsRemaining'][text()='Complete']")))
                WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'tilesResults']")))
                problem_errors =driver.find_element(By.XPATH, "//span[@id='spanNumErrors']").text
                print (problem_errors)
                problem_warnings =driver.find_element(By.XPATH, "//span[@id='spanNumWarnings']").text
                print (problem_warnings)
                blacklist_errors =driver.find_element(By.XPATH, "//span[@id='blacklistNumFailed']").text
                print (blacklist_errors)
                blacklist_warnings =driver.find_element(By.XPATH, "//span[@id='blacklistNumWarning']").text
                print (blacklist_warnings)
                mail_server_errors =driver.find_element(By.XPATH, "//span[@id='smtpNumFailed']").text
                print (mail_server_errors)
                mail_server_warnings =driver.find_element(By.XPATH, "//span[@id='smtpNumWarning']").text
                print (mail_server_warnings)
                web_server_errors =driver.find_element(By.XPATH, "//span[@id='webNumFailed']").text
                print (web_server_errors)
                web_server_warnings =driver.find_element(By.XPATH, "//span[@id='webNumWarning']").text
                print (web_server_warnings)
                dns_errors =driver.find_element(By.XPATH, "//span[@id='dnsNumFailed']").text
                print (dns_errors)
                dns_warnings =driver.find_element(By.XPATH, "//span[@id='dnsNumWarning']").text
                print (dns_warnings)
                dns_test_current_url = driver.current_url
                # print (dns_test_current_url)
                dns_test_score = 60
                print ("Successfully Completed DNS Health test for "+ mainURL)
                time.sleep(1)
                # driver.close()

        except:
            print ("DNS Health test Failed for "+ mainURL)
            # driver.close()



    # def HTML_Validation_test()        
        print ("Performing W3 NU HTML VALIDATOR test for "+ mainURL)
        url = "https://html5.validator.nu/"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='doc']")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='results']/ol")))
                markup_warning = len(driver.find_elements(By.XPATH, "//div[@id='results']//following::li[@class='info warning']"))
                print (markup_warning)
                markup_error = len(driver.find_elements(By.XPATH, ("//div[@id='results']//following::li[@class='error']") ))
                print (markup_error)
                time.sleep(3)
                markup_validation_current_url = driver.current_url
                # print (markup_validation_current_url)
                html_validation_test_score = 80
                print ("Successfully Completed W3 NU HTML VALIDATOR test for "+ mainURL)
                # driver.close()
            else:
                print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
                # driver.close()

        except:
            print ("W3 NU HTML VALIDATOR Test Failed for "+ mainURL)
            # driver.close()

    # def webpage_test():
        print ("Performing Webpage Performance test on "+ mainURL)
        url = "https://www.webpagetest.org/"
        # options = uc.ChromeOptions()
        # driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        # driver.maximize_window()
        driver.get(url)
        try:
            time.sleep(1)
            search_view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='analytical-review']")))
            search_view = driver.execute_script("arguments[0].scrollIntoView();", search_view)
            time.sleep(1)
            search_input =driver.find_element(By.XPATH, "//input[@id='url']")
            if search_input:
                time.sleep(1)
                search_input.send_keys(mainURL)
                time.sleep(1)
                search_input.submit()
                result = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='result']")))
                time.sleep(2)
                current_page = driver.current_url
                print (current_page)
                time.sleep(2)
                modified_url = current_page+"/2/performance_optimization/"
                print (modified_url)
                time.sleep(2)
                driver.get(modified_url)
                time.sleep(2)
                result_grade=WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//div[@id='grades']")))
                result_grade =driver.execute_script("arguments[0].scrollIntoView();", result_grade)
                time.sleep(2)
                performance_grade = driver.find_element(By.XPATH, "//li[@class='security']/a/h2").text
                print (performance_grade)
                first_byte_time = driver.find_element(By.XPATH, "//li[@class='first_byte_time']/a/h2").text
                print (first_byte_time)
                keep_alive = driver.find_element(By.XPATH, "//li[@class='keep_alive_enabled']/a/h2").text
                print (keep_alive)
                compress_trf = driver.find_element(By.XPATH, "//li[@class='compress_text']/a/h2").text
                print (compress_trf)
                compress_img = driver.find_element(By.XPATH, "//li[@class='compress_images']/a/h2").text
                print (compress_img)
                cache_static = driver.find_element(By.XPATH, "//li[@class='cache_static_content']/a/h2").text
                print (cache_static)
                effective_cdn = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").text
                print (effective_cdn)
                effective_cdn_colour = driver.find_element(By.XPATH, "//li[@class='use_of_cdn']/a/h2").get_attribute("class")
                print (effective_cdn_colour)
                time.sleep(1)
                webpage_test_current_url = driver.current_url
                # print (webpage_test_current_url)
                if performance_grade == "A+":
                    performance_score = 100
                if performance_grade == "A":
                    performance_score = 90
                if performance_grade == "B":
                    performance_score = 80
                if performance_grade == "C":
                    performance_score = 60
                if performance_grade == "D":
                    performance_score = 40
                if performance_grade == "E":
                    performance_score = 20
                if performance_grade == "F":
                    performance_score = 0

                if first_byte_time == "A+":
                    first_byte_time_score = 100
                if first_byte_time == "A":
                    first_byte_time_score = 90
                if first_byte_time == "B":
                    first_byte_time_score = 80
                if first_byte_time == "C":
                    first_byte_time_score = 60
                if first_byte_time == "D":
                    first_byte_time_score = 40
                if first_byte_time == "E":
                    first_byte_time_score = 20
                if first_byte_time == "F":
                    first_byte_time_score = 0

                if keep_alive == "A+":
                    keep_alive_score = 100
                if keep_alive == "A":
                    keep_alive_score = 90
                if keep_alive == "B":
                    keep_alive_score = 80
                if keep_alive == "C":
                    keep_alive_score = 60
                if keep_alive == "D":
                    keep_alive_score = 40
                if keep_alive == "E":
                    keep_alive_score = 20
                if keep_alive == "F":
                    keep_alive_score = 0

                if compress_trf == "A+":
                    compress_trf_score = 100
                if compress_trf == "A":
                    compress_trf_score = 90
                if compress_trf == "B":
                    compress_trf_score = 80
                if compress_trf == "C":
                    compress_trf_score = 60
                if compress_trf == "D":
                    compress_trf_score = 40
                if compress_trf == "E":
                    compress_trf_score = 20
                if compress_trf == "F":
                    compress_trf_score = 0

                if compress_img == "A+":
                    compress_img_score = 100
                if compress_img == "A":
                    compress_img_score = 90
                if compress_img == "B":
                    compress_img_score = 80
                if compress_img == "C":
                    compress_img_score = 60
                if compress_img == "D":
                    compress_img_score = 40
                if compress_img == "E":
                    compress_img_score = 20
                if compress_img == "F":
                    compress_img_score = 0


                if cache_static == "A+":
                    cache_static_score = 100
                if cache_static == "A":
                    cache_static_score = 90
                if cache_static == "B":
                    cache_static_score = 80
                if cache_static == "C":
                    cache_static_score = 60
                if cache_static == "D":
                    cache_static_score = 40
                if cache_static == "E":
                    cache_static_score = 20
                if cache_static == "F":
                    cache_static_score = 0

                if effective_cdn_colour == "A" and effective_cdn == "✓":
                    effective_cdn_score = 100
                if effective_cdn_colour == "B" and effective_cdn == "✓":
                    effective_cdn_score = 80
                if effective_cdn_colour == "C" and effective_cdn == "✓":
                    effective_cdn_score = 60
                if effective_cdn_colour == "D" and effective_cdn == "✓":
                    effective_cdn_score = 40
                if effective_cdn_colour == "E" and effective_cdn == "✓":
                    effective_cdn_score = 20
                if effective_cdn_colour == "F" and effective_cdn == "✓":
                    effective_cdn_score = 10
                if effective_cdn == "X":
                    effective_cdn_score = 0
                webpage_performance_test_score = round((performance_score + first_byte_time_score + keep_alive_score + compress_trf_score + compress_img_score + cache_static_score + effective_cdn_score )/7)
                webpage_performance_test_score = int(webpage_performance_test_score)
                print ("Successfully Completed Webpage Performance test on "+ mainURL)
                
                driver.close()    
            else:
                print ("Webpage Performance Test Failed on "+ mainURL)
                driver.close()
            

        except:
            print ("Webpage Performance Test Failed on "+ mainURL)
            driver.close()




        webvital_basic_score = round((site_redirection_score + page_indexed_in_google_score + gtmetrix_result_score)/3)
        webvital_advanced_score = round((mobile_friendly_test_score + webpage_performance_test_score + ssl_lab_test_score + pingdom_test_score + dns_test_score + html_validation_test_score)/6)
        seo_final_score = (website_audit_score)
        overall_bar_report_score = round((webvital_basic_score + webvital_advanced_score + seo_final_score)/3)

        current_date= datetime.now().strftime("%b-%d-%Y ")
        current_time= datetime.now().strftime("%H:%M:%S")
        current_date_time = str(current_date.replace(" ","-")+current_time.replace(":", "_"))
        print (current_date)
        print (current_time)
        print(current_date_time)
        response = {
                        "Result": [
                            {
                                "Date": current_date
                            },
                            {
                                "Site URL": site_url
                            },
                            {
                                "Dashboard Data": [
                                    {
                                        "Your Bar Score": overall_bar_report_score,
                                        "Webvital Basic": [
                                            {
                                                "Web Vitals Basic": webvital_basic_score,
                                                "Site Redirection": site_redirection_score,
                                                "Page Indexed In Google": page_indexed_in_google_score,
                                                "GTMetrix Results": gtmetrix_result_score
                                            }
                                        ],
                                        "Webvital Advance": [
                                            {   "Web Vitals Advanced": webvital_advanced_score,
                                                "Mobile Friendly Test": mobile_friendly_test_score,
                                                "Webpage Performance Test": webpage_performance_test_score,
                                                "Secure Server and Web Application": ssl_lab_test_score,
                                                "Pingdom Tools": pingdom_test_score,
                                                "DNS Health": dns_test_score,
                                                "W3 NU HTML VALIDATOR": html_validation_test_score
                                            }
                                        ],
                                        "Seo": [
                                            {
                                                "SEO": seo_final_score,
                                                "Website Audit": website_audit_score,
                    				            "Google Metrics": -0
                                            }
                                        ],
                                        "Social Media Presence": [
                                            {  
                                                "Social Media Presence Score" : -0,
                                                "Social Profile Strength": -0

                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Site Redirection Test": [
                                    {
                                        "Site Redirection": site_redirection_score,
                                        clean_url: redirection_result_1,
                                        url_with_www : redirection_result_2,
                                        alternate_url_1 : redirection_result_3,
                                        alternate_url_2 : redirection_result_4
                                    }
                                ]
                            },
                            {
                                "Page Indexed by Google": [
                                    {
                                        "Page Indexed In Google" : page_indexed_in_google_score,
                                                                        "google_index_url" : "site:"+clean_url,
                                                                        "google_index_result" : google_index,
                                                                        "google_index_result_page" : google_index_current_url,
                                                                        "google_index_url2" : "site:"+url_with_www,
                                                                        "google_index_result2" : google_index_2,
                                                                        "google_index_result2_page" : google_index_2_current_url
                                    }
                                ]
                            },
                            {
                                "GTMetrix Test Result": [
                                    {
                                        "GTMetrix Results" :gtmetrix_result_score,           
                                        "Grade" : gtmetrix_grade,
                                        "Performance" : gtmetrix_performance,
                                        "Structure" :gtmetrix_structure,
                                        "Largest Contentful Paint (LCP)" : gtmetrix_lcp,
                                        "Total Blocking Time (TBT)" : gtmetrix_tbt,
                                        "Cumulative Layout Shift (CLS)" : gtmetrix_cls,
                                        "GTMetrix Result Page": gtmetrix_current_url
                                    }
                                ]
                            },
                            {
                                "Mobile Friendly Test Result": [
                                    {
                                        "Mobile Friendly Test" : mobile_friendly_test_score,
                                        "Mobile Friendly" : mobile_friendly_result,
                                        "Mobile Friendly Test Result Page" : mobile_friendly_current_url
                                    }
                                ]
                            },
                            {
                                "Webpage Performance Test Result": [
                                    {
                                        "Webpage Performance Test" : webpage_performance_test_score,
                                        "Security Score" : performance_grade,
                                        "First Byte time" : first_byte_time,
                                        "Keep Alive" : keep_alive,
                                        "Compress Transfer" : compress_trf,
                                        "Compress Image" : compress_img,
                                        "Cache Static Content" : cache_static,
                                        "Effective use of CDN" : effective_cdn,
                                        "Webpage Performance Test Result Page": webpage_test_current_url
                                    }
                                ]
                            },
                            {
                                "SSL Lab Test Result": [
                                    {
                                        "Secure Server and Web Application" : ssl_lab_test_score,
                                        "Overall" : ssl_grade,
                                        "Certificate" : certificate,
                                        "Protocol" : protocol_support,
                                        "Key Exchange" : key_exchange,
                                        "Cipher Strength" : ciper_strength,
                                        "SSL Lab Test Result Page": ssl_lab_current_url
                                    }
                                ]
                            },
                            {
                                "Pingdom Tools Test Result": [
                                    {
                                        "Pingdom Tools Test" : performance_score,
                                        "Performance grade" : pingdom_performance,
                                        "Page size" : pingdom_page_size,
                                        "Load time" : pingdom_load_time,
                                        "Requests" : pingdom_request,
                                        "Pingdom Tools Test Result Page" : pingdom_tools_current_url
                                    }
                                ]
                            },
                            {"DNS Health Test Result" : [  {"DNS Health" : dns_test_score},
                                                    {  "Problems"                      : [{ "Warnings" :problem_warnings,
                                                                                            "Errors" : problem_errors}]},
                                                    {  "Blacklist"                     : [{ "Warnings" : blacklist_warnings,
                                                                                            "Errors" :  blacklist_errors}]},
                                                    {  "Mail Server"                   : [{ "Warnings" : mail_server_warnings,
                                                                                            "Errors" :  mail_server_errors}]},
                                                    {  "Web Server"                    : [{ "Warnings" : web_server_warnings,
                                                                                            "Errors" :  web_server_errors}]},
                                                    {  "DNS"                           : [{ "Warnings" : dns_warnings,
                                                                                           "Errors" :  dns_errors}]},
                                                    {  "DNS Health Test Result Page"   : dns_test_current_url}]
                                    
                                
                            },
                            {
                                "W3 NU HTML VALIDATOR Test Result":            [{  "W3 NU HTML VALIDATOR" : html_validation_test_score,
                                                                                    "Warnings" : markup_warning,
                                                                                    "Errors" : markup_error,
                                                                                    "W3 NU HTML VALIDATOR Test Result Page" : markup_validation_current_url
                                    }
                                ]
                            },   
                            {
                               "Website Audit Test Result":            [{  "Website Audit" : website_audit_score,
                                                                            "SEO Score" : seo_score,
                                                                            "Meta Information" : meta_information,
                                                                            "Page Quality" : page_quality,
                                                                            "Page Structure" : page_structure,
                                                                            "Link Structure" : link_structure,
                                                                            "Server" : server,
                                                                            "External Factors" : external_factors,
                                                                            "Response Time in Seconds" : response_time,
                                                                            "File Size in KB" : file_size,
                                                                            "Text Words" : text_words,
                                                                            "Media Files" : media_files,
                                                                            "Number Of Internal Links" : internal_links,
                                                                            "Number Of External Links" : external_links,
                                                                            "Website Audit Test Result Page": website_audit_current_url
                                    }
                                ]
                            },
                            {
                                "Google Metric": [
                                    {
                                        "Google Metrics": -0,
                                        "Pages Indexed in Google": google_index_2,
                                        "Organic Search for 'Speciality in Locality": -0,
                                        "Places Search Score for 'Speciality in Locality": -0
                                    }
                                ]
                            },
                            {
                                "Social profile strength": [
                                    {
                                        "Social Profile Strength": -0,
                                        "Facebook": [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "Google":   [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "Yelp":     [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "Instagram": [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "Youtube":  [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "LinkedIn": [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }],
                                        "Twitter": [{ "Rating" : -0,
                                                       "Reviews" : -0,
                                                       "Followers" : -0,
                                                       "Likes" : -0    }]


                                    }
                                ]
                            }    
                        ]
                    }
        return Response (response)
    

class Speciality_In_Locality(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        speciality = self.request.query_params.get('speciality')
        locality = self.request.query_params.get('locality')
        parameter = speciality + " in " + locality
        print (mainURL)
        print (speciality)
        print (parameter)
        
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def Speciality_In_Locality()        
        print ("Performing Speciality in Locality Places Search for "+ mainURL)
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    try:
                        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='wUrVib OSrXXb']"))).click()
                    except:
                        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Odp5De']/div/div/div[2]/div[1]/div[2]/g-more-link/a/div/span[2]"))).click()    
                    place_names = []
                    page_counter = 0
                    while page_counter <= 9 :
                        try:
                            name_element = driver.find_elements(By.XPATH, "//span[@class='OSrXXb']")
                            # rating_element = driver.find_elements(By.XPATH, "//span[@class='yi40Hd YrbPuc']")
                            for name_list in name_element:
                                place_names.append(name_list.text)
                            # for rating_list in rating_element:
                            #     rating.append(rating_list.text) 
                            time.sleep(2)
                            next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[2]")))
                            driver.execute_script("arguments[0].scrollIntoView();", next_button)
                            driver.execute_script("arguments[0].click();", next_button)
                            page_counter += 1
                            # print (page_counter)
                        except:
                            print ("No more pAges")
                            break
                    print (place_names)
                except:
                    print ("No Places Found")
        except:
            print ("Google Page Load Error")
        print ("Performing Speciality in Locality Organic Search for "+ mainURL)
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    organic_names = []
                    page_counter = 0
                    while page_counter <= 100 :
                        try:
                            name_element = driver.find_elements(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")
                            # rating_element = driver.find_elements(By.XPATH, "//span[@class='yi40Hd YrbPuc']")
                            for name_list in name_element:
                                organic_names.append(name_list.text)
                            # for rating_list in rating_element:
                            #     rating.append(rating_list.text) 
                            time.sleep(2)
                            next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[1]")))
                            driver.execute_script("arguments[0].scrollIntoView();", next_button)
                            driver.execute_script("arguments[0].click();", next_button)
                            page_counter += 1
                            # print (page_counter)
                        except:
                            print ("No more pAges")
                            break
                    print (organic_names)
                except:
                    print ("No Places Found")
        except: pass
        response = {"Result" : [{"Places Result" : place_names,
                                 "Organic Result " : organic_names}]
        }
        return Response(response)


class Speciality_Locality_Places(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        speciality = self.request.query_params.get('speciality')
        locality = self.request.query_params.get('locality')
        pages = self.request.query_params.get('pages')
        pages = int(pages)
        parameter = speciality + " in " + locality
        print (mainURL)
        print (speciality)
        print (parameter)
        print (pages)
        

        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def Speciality_Locality_Places()        
        print ("Performing Speciality in Locality Places Search for "+ mainURL)
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='wUrVib OSrXXb']"))).click()
                except:
                    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Odp5De']/div/div/div[2]/div[1]/div[2]/g-more-link/a/div/span[2]"))).click()     
                
                # try: 
                #     if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[2]"))):
                #         available_pages = driver.find_elements(By.XPATH, "//a[@class='fl']")
                #         last_page = available_pages[-1]
                #         last_page = last_page.get_attribute('aria-label')
                #         last_page = int(last_page[-1])
                # except:
                #     last_page = 0    
                # print ("last page " , last_page)   
                # if pages == "None":
                #     pages = 9
                 
                # else:
                #     pages = int(pages) 
                # print (pages)    
                place_names = []
                page_counter = 0
                rating = []
                
                while page_counter <= pages :
                    try:
                        name_element = driver.find_elements(By.XPATH, "//span[@class='OSrXXb']")
                        # rating_element = driver.find_elements(By.XPATH, "//span[@class='yi40Hd YrbPuc']")
                        for name_list in name_element:
                            place_names.append(name_list.text)
                        # for rating_list in rating_element:
                        #     rating.append(rating_list.text) 
                        time.sleep(2)
                        next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[2]")))
                        driver.execute_script("arguments[0].scrollIntoView();", next_button)
                        driver.execute_script("arguments[0].click();", next_button)
                        page_counter += 1
                        print (page_counter)
                    except:
                        print ("No more pAges")
                        break
                print (place_names)
                    

        except:
            print ('Error in Loading Google Page')
        response = {"Result": [{"Place Result" : place_names}]}
        return Response(response)
    



class Speciality_Locality_Organic(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        speciality = self.request.query_params.get('speciality')
        locality = self.request.query_params.get('locality')
        pages = self.request.query_params.get('pages')
        pages = int(pages)
        parameter = speciality + " in " + locality
        print (mainURL)
        print (speciality)
        print (parameter)
        print (pages)
        

        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def Speciality_Locality_Places()        
        print ("Performing Speciality in Locality Organic Search for "+ mainURL)
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    organic_links = []
                    organic_names = []
                    results = []
                    page_counter = 0
                    while page_counter < 5 :
                        try:
                            link_element = driver.find_elements(By.XPATH, "//div[@class='g Ww4FFb vt6azd tF2Cxc']/div/div/div/a")
                            # name_element = driver.find_elements(By.XPATH, "//div[@class='g Ww4FFb vt6azd tF2Cxc']/div/div/div/a/h3")
                            # for link_list in link_element:
                            #     link_list = link_list.get_attribute('href')
                            #     if not any(link_list.startswith(social_links) for social_links in ["https://www.facebook.com/", "https://www.facebook.in/", "https://www.instagram.com/", "https://www.instagram.in/" , "https://www.yelp.com/" , "https://in.linkedin.com/" , "https://www.linkedin.com/" , "https://twitter.com/" , "https://www.youtube.com/channel/" , "https://www.youtube.com/profile/"]):
                            #         results.append(link_list)
                            # for name_list in name_element:
                            #     name_list = name_list.text
                            #     if not "Yelp" in name_list :
                            #         organic_names.append(name_list)
                            
                            for link_list in link_element:
                                sites = link_list.get_attribute('href')
                                
                                if not any(sites.startswith(social_links) for social_links in ["https://www.facebook.com/", "https://www.facebook.in/", "https://www.instagram.com/", "https://www.instagram.in/" , "https://www.yelp.com/" , "https://in.linkedin.com/" , "https://www.linkedin.com/" , "https://twitter.com/" , "https://www.youtube.com/channel/" , "https://www.youtube.com/profile/"]):
                                    # name = list[name]
                                    # name = link_list.find_element(By.XPATH, "./h3").text
                                    results.append({"link" :sites})
                                         
                            time.sleep(2)
                            next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[1]")))
                            driver.execute_script("arguments[0].scrollIntoView();", next_button)
                            driver.execute_script("arguments[0].click();", next_button)
                            page_counter += 1
                            print (page_counter)
                        except:
                            print ("No more pAges")
                            break
                    print (results)
                except:
                    print ("No Places Found")
        except: pass
        response = {"Result" : [{
                                 "Organic Result " : results}]
        }
        return Response(response)
    


class Speciality_Locality_Organic_Score(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        speciality = self.request.query_params.get('speciality')
        locality = self.request.query_params.get('locality')
        parameter = speciality + " in " + locality
        print (mainURL)
        print (speciality)
        print (parameter)
        
        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def Speciality_Locality_Places()        
        print ("Performing Speciality in Locality Organic Search for "+ mainURL)
        
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    page_counter = 0
                    while page_counter <= 5 :
                        try:
                            link_element = driver.find_elements(By.XPATH, "//div[@class='g Ww4FFb vt6azd tF2Cxc']/div/div/div/a")
                            # rating_element = driver.find_elements(By.XPATH, "//span[@class='yi40Hd YrbPuc']")
                            for link in link_element:
                                driver.execute_script("arguments[0].scrollIntoView();", link)
                                link = link.get_attribute("href")
                                if link.startswith(mainURL):
                                    print (link)
                                    
                                    find_page = driver.find_element(By.XPATH, "//div[@id='result-stats']").get_attribute("textContent")
                                    page = find_page
                                    if "About" in page:
                                        page = (page.split()[0])
                                    if "Page" in page:
                                        page = (page.split()[1])
                                    break
                                    

                                else:
                                    pass
                            time.sleep(1)
                            next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[1]")))
                            driver.execute_script("arguments[0].scrollIntoView();", next_button)
                            driver.execute_script("arguments[0].click();", next_button)
                            page_counter += 1
                        except:
                            print ("No more pAges")
                            break
                    
                except:
                    print ("No results Found")
        except:
            print ("Error Loading Google Page")
        # print (page)
        try:
            if page == "About":
                organic_search_score = 100
            if page == "2":
                organic_search_score = 80
            if page == "3":
                organic_search_score = 60
            if page == "4":
                organic_search_score = 40
            if page == "5":
                organic_search_score = 20
           
        except: 
            organic_search_score = 0
            
            print ("NOt found link")
        print (organic_search_score)
        response = {"Result" : [{
                                 "Organic Result Score " : organic_search_score}]
        }
        return Response(response)
    

class Speciality_Locality_Places_Score(generics.ListAPIView):
    def get(self, request,*args,**kwargs):
        mainURL = self.request.query_params.get('url')
        speciality = self.request.query_params.get('speciality')
        locality = self.request.query_params.get('locality')
        parameter = speciality + " in " + locality
        print (mainURL)
        print (speciality)
        print (parameter)
        
        

        if mainURL.startswith("https://") or mainURL.startswith("http://") or mainURL.startswith("https://www") or mainURL.startswith("http://www"):
            pass

        else:
            mainURL = "https://" + mainURL

        url = mainURL
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome(service = Service(ChromeDriverManager().install()), options = options)
        driver.maximize_window()
        driver.get(url)
        current = driver.current_url
        mainURL = current
        if mainURL.endswith("/"):
            mainURL = mainURL[:-1]
        else:
            pass
        print(mainURL)


        if mainURL.startswith("https://") :
            clean_url = mainURL.replace("https://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)

        if mainURL.startswith("http://") :
            clean_url = mainURL.replace("http://","") 
            # print (clean_url)
            if clean_url.startswith("www."):
                clean_url = clean_url.replace("www.","")
            else:
                pass
            print (clean_url)


        if not clean_url.startswith("www."):
            url_with_www = "www." + clean_url
            print (url_with_www)

        else:
            url_with_www = clean_url
            print (url_with_www)


        if mainURL.startswith("https://"):
            alternate_url_1 = mainURL
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        if mainURL.startswith("http://"):
            alternate_url_1 = mainURL.replace("http://", "https://")
            if alternate_url_1.startswith("https://www."):
                alternate_url_1 = alternate_url_1.replace("https://www.", "https://")

        print(alternate_url_1)

        if mainURL.startswith("https://www."):
            alternate_url_2  = mainURL
        if mainURL.startswith("http://www."):
            alternate_url_2 = mainURL.replace("http://www.", "https://www.")
        if not mainURL.startswith("https://www."):
            alternate_url_2 = "https://www."+ clean_url

        print(alternate_url_2)
    # def Speciality_Locality_Places()        
        print ("Performing Speciality in Locality Places Search for "+ mainURL)
        url = "https://www.google.com"
        # options = uc.ChromeOptions()
        # options.add_argument("--headless")
        # driver = uc.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        try:
            if search_input:
                time.sleep(1)
                search_input.send_keys(parameter)
                time.sleep(1)
                search_input.send_keys(Keys.RETURN)
                try:
                    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='wUrVib OSrXXb']"))).click()
                except:
                    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Odp5De']/div/div/div[2]/div[1]/div[2]/g-more-link/a/div/span[2]"))).click()     
                place_names = [] 
                page_counter = 0
                while page_counter <= 5 :
                    try:
                        name_element = driver.find_elements(By.XPATH, "//span[@class='OSrXXb']")
                        # rating_element = driver.find_elements(By.XPATH, "//span[@class='yi40Hd YrbPuc']")
                        for name_list in name_element:
                            
                            # driver.execute_script("arguments[0].scrollIntoView();", name_list)
                            # driver.execute_script("arguments[0].click();", name_list)
                            # # place_names.append(name_list.text)
                            
                            name_list.click()
                            time.sleep(0.7)
                            
                            link = driver.find_element(By.XPATH, "//div[@class='hBPSMc qDBO2c']/a")
                            # link = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='hBPSMc qDBO2c']/a")))
                            link = link.get_attribute("href")
                            # if link.startswith(clean_url):
                            if clean_url in link:
                                print (link)
                            else:
                                pass
                           
                        time.sleep(2)
                        next_button =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']/span[1]")))
                        driver.execute_script("arguments[0].scrollIntoView();", next_button)
                        driver.execute_script("arguments[0].click();", next_button)
                        page_counter += 1
                        print (page_counter)
                        page = page_counter
                    except:
                        print ("No more pAges")
                        page = 1
                        break
                # print (place_names)
                    

        except:
            print ('Error in Loading Google Page')
        try:
            if page == 1:
                score = 100
        except:
            score = 0
        response = {"Result": [{"Place Result Score" : score}]}
        return Response(response)
                
                


