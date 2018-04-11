from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import requests
from fake_useragent import UserAgent
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import re


#________Requests pagina inicial____________
url = 'http://g1.globo.com/minas-gerais/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
response = requests.get(url, headers=headers)

#print(response.content)


#________Definindo Classes e Funçoes___________


class Reportagem(object):
    v1=  'G1 - Minas Gerais'
    v2 = 3
    
    def set_v3(self, titulo):
        if len(titulo)>5:
            self.v3 = titulo
        else:
            print ('Erro: Titulo tem menos que cinco caracteres.')
            
    def set_v4(self, subtitulo):
        su


titulo = 'Eu sou Deus'
titulo    
teste = Reportagem()
teste.set_v3(titulo)

teste.v3

#________Mineirando dados pagina inicial____________

soup = BeautifulSoup(response.content, 'html.parser')
dadosBrutos = soup.find_all("div", class_="feed-post-body")

for i in dadosBrutos:
    print('\n \n')
    titulo = (i.find_all("p", class_="feed-post-body-title gui-color-primary gui-color-hover"))[0].text
    subtitulo = i.find_all("p", class_="feed-post-body-resumo")[0].text
    try:
        tema = (i.find_all("span", class_="feed-post-header-chapeu"))[0].text
    except:
        tema = ""
    urlReportagem = i.a.attrs['href']
    
    print(titulo)
    print(tema)
    



dadosBrutos[0].find_all ("span", class_="feed-post-header-chapeu")[0].text
dadosBrutos[3].(i.find_all ("span", class_="feed-post-header-chapeu"))[0].text

responseReportagem = requests.get(urlReportagem, headers=headers)
soupReportagem = BeautifulSoup(responseReportagem.content, 'html.parser')

# DATA | HORA -> [1]data DD/MM/AAAA [2]hora 10h03
dataHoraReportagem = ((soupReportagem.find("time")).text.split(' '))

#autor
autor = (((soupReportagem.find("p", class_="content-publication-data__from")).text).split(' Por '))[1].rstrip(' ')

textCoder = soupReportagem.find_all("p", class_="content-text__container ")

text = ""
for i in textCoder:
    text = text + i.text
text

imagens = soupReportagem.find_all('img', class_='image content-media__image')

if imagens:
    print ('não há imagens')

#___________Limpando e formatando as Variaveis___________
data = dataHoraReportagem[1]
hora = re.sub(u'h', ':', dataHoraReportagem[2])
V1 = 'G1 - Minas Gerais'
V2 = 3
V3 = titulo
V4 = subtitulo
V5 = text
#V6 = (tema aberto?)
V7 = tema
#V8 = Relacionamento | Gerar lista de nomes
#V9= Personagem | Gerar listas de nomes

if imagens:
    V10 = 'Sim'
else:
    V10 = 'Não'
    
#11 = Tamanho do espaço da notícia
V12 = autor



print(data, hora, V1, V2, V3, V4, V7, V10, V12)

#dir