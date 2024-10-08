#Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui é uma biblioteca que baixa no terminal com pip install pyautogui
#pyautogui.write -> escreve um texto
#pyautogui.click -> clicar com o mouse
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho de teclado (ctrl, c por ex)
#pyautogui.PAUSE -> define uma pausa, vai definir uma pausa a cada comando pyautogui
#pyautogui.drag -> arrasta algo

import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")#vai apertar a tecla windows
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#quero dar uma pausa pra carregar a pagina da web, por isso a biblioteca time

#Passo 2: fazer o login no sistemas

time.sleep(2)
pyautogui.click(x=2151, y=295)#peguei a posição no arquivo auxiliar, a posição altera com o tamanho da tela, se for duas telas etc
pyautogui.write("agathacduarte@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=2161, y=451)

time.sleep(2)

#Passo 3: Importar a base de dados

import pandas #pacote que trabalha com base de dados em varios formatos, excel sql etc, instala com pip install pandas

tabela = pandas.read_csv("produtos.csv") #variavel, vai ler a tabela do arquivo
print(tabela)



#Passo 4: Cadastrar um produto e repetir ate acabar os produtos
linha = 0 #da tabela

for linha in tabela.index: #para cada linha da tabela, usa o tab ao inves de {}, faz linha++ automatico
    #o python sabe que a variavel linha é de fato uma linha por conta do .index, indice

    #codigo
    pyautogui.click(x=2140, y=179)

    codigo = tabela.loc[linha, "codigo"]#ta pegando a linha e coluna certa
    pyautogui.write(str(codigo))#pra pegar o valor e escrever em formato de texto
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco
    preco = tabela.loc[linha, "preco_unitario"]

    pyautogui.write(str(preco))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    #verificar se a informação n ta vazia pra poder escrever
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("enter")

    pyautogui.scroll(5000) #sobe a tela, positivo vai pra cima, negativo pra baixo


