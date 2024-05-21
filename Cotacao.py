import requests
from tkinter import *


def pegar_cotacao(moeda_origem, moeda_destino):
    """"""
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)
    dic_resposta = requisicao.json()
    cotacao = dic_resposta[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao


print(pegar_cotacao("USD", "BRL"))

janela = Tk()
janela.title("Cotação de Moedas")
texto_orientacao = Label(
    janela, text="Clique no botão para ver as cotações das moedas "
)
texto_orientacao.grid(column=0, row=0)

Button = Button(
    janela,
)
janela.mainloop()
