from random import randint
import PySimpleGUI as sg


class Advinhe:
    def __init__(self):
        self.gerandonumero = 0
        self.valormin = 1
        self.valormax = 50
        self.usuario = 0
        self.total = 0

    def Iniciar1(self):
        layout = [
            [sg.Text('Bem vindo ao Ebony Simple Game', size=(40, 0), key='Titulo')],
            [sg.Text('Chute um número entre 1 e 50: ', size=(40, 0), key='tc')],
            [sg.Input(size=(6, 0), key='inputChute')],
            [sg.Button('Conferir!')],
            [sg.Output(size=(40, 15))]
        ]
        self.janela = sg.Window('Chute um número!', layout=layout)
        self.GerarNumeroAleatorio()
        self.Iniciar()

    def Iniciar(self):
        cont = 1
        try:
            while True:
                self.lernumero()
                if self.evento == 'Conferir!':
                    self.chutado = self.valores['inputChute']
                    while True:
                        self.total = cont
                        if int(self.chutado) <= 50:
                            if int(self.chutado) > self.numeroAleatorio:
                                print('Chute um número mais baixo!')
                                # self.lernumero()
                                cont += 1
                                break
                            elif int(self.chutado) < self.numeroAleatorio:
                                print('Chute um número mais alto!')
                                # self.lernumero()
                                cont += 1
                                break
                            else:
                                print('\nLegal, vc acertou!')
                                print(f'Tentativas válidas: {self.total}\n')
                                cont += 1
                                break
                        else:
                            print('\nOOOOh Burrooo! Eu disse, ENTRE 1 e 50\nTente novamente...\n')
                            self.lernumero()
                            cont += 1
                            break

        except ValueError:
            print('\nOooh Burro! Digite apenas números!\nTente novamente...\n')
            self.Iniciar()

    def lernumero(self):
        self.evento, self.valores = self.janela.Read()

    def pedirnumero(self):
        self.usuario = input('Chute um número entre 1 e 50: ')

    def GerarNumeroAleatorio(self):
        self.numeroAleatorio = randint(self.valormin, self.valormax)


comecar = Advinhe()
comecar.Iniciar1()
# @ebony.prog
