#==================================
#MEDIA BIAS
#Script análise descritiva 
#==================================

# Definir diretorio

setwd("C:/Users/usuario/Downloads/Base duplas 20-05-15")
getwd()

#Carregando dados

#Bia e Natália
bn= read.csv("Base_de_Dadas os_Media_Bias_Natália_e_Beatriz.csv", sep = ",", header=T , encoding = "UTF-8")
head(bn)

#Marina e Marcos
mm=read.csv("Base_de_dados_Marina_e_MarcosDamasceno - Dados.csv", sep = ",", header=T , encoding = "UTF-8")
head(mm)

# Bia, Barbara e pedro
bbp=read.csv("Base_de_Dados_Media_Bias_Bárbara_Pedro.csv", sep = ",", header=T , encoding = "UTF-8")
head(bbp)

#Bia, Barbara e Virgilio
bbv=read.csv("Base_de_Dados_Media_Bias_Bárbara_Virgilio.csv", sep = ",", header=T , encoding = "UTF-8")
head(bbv)

# Alysson e Florencia
af=read.csv("_Base_de_dados_Florencia_e_Alyson - Dados.csv", sep = ",", header=T , encoding = "UTF-8")
head(af)


