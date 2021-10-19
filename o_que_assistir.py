#importação de lib
import time
import random
from tkinter.font import BOLD
from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime
import pandas as pd
 
class TelaPython:
    sg.theme('Dark')
    
    def __init__(self):
        layout = [
            [sg.Text('FILMES        ❤️    COMIDAS        ❤️    BEBIDAS', font=("Arial", 20, BOLD), text_color='red')],    
            [sg.Text('                                                              '),
                sg.Button('SORTEAR', font=("Arial", 20, BOLD),
                button_color=('White', 'Red'))],
            [sg.Output(size=(45,7.6), font=("Comic Sans", 20, BOLD), key='_OUTPUT_')]
        ]

        #Janela
        self.janela = sg.Window("O que assistir ❤️", icon='Icones/icon.ico').layout(layout)

    def Iniciar(self):
        while True:
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == sg.WINDOW_CLOSED:
                break
            if self.eventos == 'SORTEAR':
                self.janela['_OUTPUT_'].update(value='')
                
                lista_opcoes_filmes = pd.read_excel(r"lista_opcoes.xlsx", usecols='A')
                lista_opcoes_comidas = pd.read_excel(r"lista_opcoes.xlsx", usecols='B')
                lista_opcoes_bebidas = pd.read_excel(r"lista_opcoes.xlsx", usecols='C')
                
                lista_opcoes_filmes.dropna(subset = ["filmes"],inplace=True)
                lista_opcoes_comidas.dropna(subset = ["comidas"], inplace=True)
                lista_opcoes_bebidas.dropna(subset = ["bebidas"], inplace=True)
                
                tamanho_filmes = len(lista_opcoes_filmes['filmes'])
                tamanho_comidas = len(lista_opcoes_comidas['comidas'])
                tamanho_bebidas = len(lista_opcoes_bebidas['bebidas'])

                num_aleat = random.randint(0,tamanho_filmes-1)
                filme = (lista_opcoes_filmes["filmes"][num_aleat])

                num_aleat = random.randint(0,tamanho_comidas-1)
                comida = (lista_opcoes_comidas["comidas"][num_aleat])

                num_aleat = random.randint(0,tamanho_bebidas-1)
                bebida = (lista_opcoes_bebidas["bebidas"][num_aleat])
                
                separador_1 = '   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️\n'
                separador_2 = '\n\n   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️'
                frase_1 = 'Você irá assistir'
                frase_2 = ', comendo'
                frase_3 = 'e bebendo'

                print(separador_1, frase_1, filme, frase_2, comida, frase_3, bebida, separador_2) 

tela = TelaPython()
tela.Iniciar()

