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
url = 'http://g1.globo.com/minas-gerais/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

response = requests.get(url, headers=headers)

#print(response.content)


#________Mineirando dados pagina inicial____________

soup = BeautifulSoup(response.content, 'html.parser')
dadosBrutos = soup.find_all("div", class_="feed-post-body")

titulo = []
subtitulo = []
tema = []
urlReportagem = []
dataHoraReportagem = []
data = []
hora = []
autor = []
texto = []
imagens = []

textCoder = []
soupReportagem = []


for i in dadosBrutos:
    print('\n \n')
    titulo.append((i.find_all("p", class_="feed-post-body-title gui-color-primary gui-color-hover")))
    
    try:
        subtitulo.append(i.find_all("p", class_="feed-post-body-resumo")[0].text)
    except:
        subtitulo.append('')
    try:
        tema.append((i.find_all("span", class_="feed-post-header-chapeu"))[0].text)
    except:
        tema.append('')
    urlReportagem.append (i.a.attrs['href'])

cont = 0
for i in urlReportagem:
    print(cont)
    responseReportagem = requests.get(i, headers=headers)
    soupReportagem.append (BeautifulSoup(responseReportagem.content, 'html.parser'))

    # DATA | HORA -> [1]data DD/MM/AAAA [2]hora 10h03
    try:
        dataHoraReportagem.append(((soupReportagem[cont].find("time", itemprop="datePublished" )).text.split(' ')))
    except:
        dataHoraReportagem.append('')
        print('Erro: Data não encontrada')
        
    #autor
    try:
        autor.append ((((soupReportagem[cont].find("p", class_="content-publication-data__from")).text).split(' Por '))[1].rstrip(' '))
    except:
        autor.append('')
        print('Erro: Data não encontrada')
        
    textCoder = soupReportagem[cont].find_all("p", class_="content-text__container")
    #textCoder = soupReportagem[cont].find_all("p", class_="content-text__container theme-color-primary-first-letter")
    text = ''
    
    for i in textCoder:
        text = text + i.text
    
    texto.append(text)

    img = soupReportagem[cont].find_all('img', class_='image content-media__image')
    
    if img:
        imagens.append('Sim')
    else:
        imagens.append('Não')
        
    cont = cont + 1
    
#___________Transferindo as variáveis data e hora para variáveis separadas
for i in range(len(dataHoraReportagem)):
    try:
        data.append(dataHoraReportagem[i][1])
    except:
        data.append ('')
for i in range(len(dataHoraReportagem)):
    try:
        hora.append(re.sub(u'h', ':', dataHoraReportagem[i][2]))
    except:
        hora.append ('')

#_________Remove texto em branco e suas variáveis
i = 0
for j in range(len(texto)):
    try:
        if not texto[i]:
            print(titulo[i])
            texto.pop(i)
            autor.pop(i)
            dataHoraReportagem.pop(i)
            imagens.pop(i)
            subtitulo.pop(i)
            tema.pop(i)
            titulo.pop(i)
            urlReportagem.pop(i)
            data.pop(i)
            hora.pop(i)
            i = i - 1
    except:
        print(data, hora, titulo, subtitulo)
    i = i +1
        

            
#___________Limpando e formatando as Variaveis (parte antiga. tem que adequar ao novo codigo)___________
        
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

