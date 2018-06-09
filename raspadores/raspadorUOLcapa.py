from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
from fake_useragent import UserAgent
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import re
import requests

#________Requests pagina inicial____________
url = 'https://noticias.uol.com.br/minas-gerais/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

response = requests.get(url, headers=headers)


#________Mineirando dados pagina inicial____________

soup = BeautifulSoup(response.content, 'html.parser')
dadosBrutos = soup.find_all("div","modulos-topo")

titulo = []
#subtitulo = []
#tema = []
#urlReportagem = []
#dataHoraReportagem = []
#data = []
#hora = []
#autor = []
#texto = []
#imagens = []
#textCoder = []
#soupReportagem = []
cont=0
for i in dadosBrutos:
    print('\n \nteste')
    titulo.append((i.find_all("h2", class_="h-opacity65 transition-025")))
    cont = cont + 1