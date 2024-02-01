import time
import pygame
import random
from midiutil import MIDIFile
import tkinter.messagebox as mb

#Métodos para tratar os casos de string que mudam o tom da musica
class StringOitava:
    __CHARAUMENTA = "+"
    __CHARDIMINUI = "-"
    __CHARFIXO = "R"
    __CARACTERESEFEITO = __CHARAUMENTA,__CHARDIMINUI
    __OITAVA = 12
    __MAXTOM = 3 * __OITAVA

    @staticmethod
    def cmpString( stringMusica, i):
        if i + 1 < len(stringMusica) and stringMusica[i: i + 1] == StringOitava.__CHARFIXO and stringMusica[i + 1] in StringOitava.__CARACTERESEFEITO:
             return True
        else:
            return False
        
    @staticmethod
    def setOitava(tomAtual, stringMusica, i):
        caractere = stringMusica[i + 1]
        match caractere:
            case "+":       
                if tomAtual < StringOitava.__MAXTOM:
                    return tomAtual + StringOitava.__OITAVA
                else:
                    return tomAtual
            case "-":
                if tomAtual > -StringOitava.__MAXTOM:
                     return tomAtual - StringOitava.__OITAVA 
                else:
                     return tomAtual
                
#Método para mudar o BPM da Música a partir de uma String                
class StringBPM():
    __STRINGFIXA = "BPM+"
    __INCREMENTOBPM = 80

    @staticmethod
    def cmpString(stringMusica, i):
        if stringMusica[i: i + len(StringBPM.__STRINGFIXA)] == StringBPM.__STRINGFIXA:
             return True
        else:
            return False

    @staticmethod
    def setBPM(bpmAtual):
        return bpmAtual + StringBPM.__INCREMENTOBPM

# Super Classe de Notas, para organizar os métodos e definicoes comuns entre elas
class Notas:

    LA = 69
    RE = 62
    MI = 64
    FA = 63
    SOL = 67
    DO = 60
    SI = 71
    CaractereLa = "A"
    CaractereSi = "B"
    CaractereDo = "C"
    CaractereRe = "D"
    CaractereMi = "E"
    CaractereFa = "F"
    CaractereSol = "G"
     

    def __init__(self, caracteresEfeito):
        self.caracteresEfeito = caracteresEfeito
    def verificarCaractereConjunto(self, caractereMusica):
         return caractereMusica.lower() in self.caracteresEfeito.lower()

#Clase para selecionar o caso em que a nota tocada deve ser a anterior
class NotasRepetidas(Notas):
    __NOTAS = [Notas.CaractereLa, Notas.CaractereSi, Notas.CaractereDo, Notas.CaractereRe, Notas.CaractereMi, Notas.CaractereFa, Notas.CaractereSol]

    def verifUltimoCharNota(self, caractereMusica):
        if caractereMusica in self.__NOTAS:
            return True
        else:
            return False    
    
    def getNota(self, caractereMusica):
        match caractereMusica.upper():
            case self.CaractereDo:
                return self.DO
            case self.CaractereRe:
                return self.RE
            case self.CaractereMi:
                return self.MI
            case self.CaractereFa:
               return self.FA
            case self.CaractereSol:
                return self.SOL
            case self.CaractereLa:
                return self.LA
            case self.CaractereSi:                    
                return self.SI
    

# Classe para selecionar as notas                 
class NotasBasicas(Notas):
    __SEMSOM = 128
    __CaractereSemSom = " "

    def getNota(self, caractereMusica):
        match caractereMusica.upper():
            case self.CaractereDo:
                return self.DO
            case self.CaractereRe:
                return self.RE
            case self.CaractereMi:
                return self.MI
            case self.CaractereFa:
                return self.FA
            case self.CaractereSol:
                return self.SOL
            case self.CaractereLa:
                return self.LA
            case self.CaractereSi:
                return self.SI
            case self.__CaractereSemSom:
                return self.__SEMSOM  

# Classe para selecionar as notas aleatórias da música
class NotaAleatoria(Notas):
    def getNota(self):
        return random.choice([self.LA, self.RE, self.MI, self.FA, self.SOL, self.DO, self.SI])

#Método para alterar o volume
class Volume():
    __AUMENTARVOLUME = "+"
    __DIMINUIRVOLUME = '-'

    @staticmethod
    def verificarCaractereConjunto(caractereMusica):
         return caractereMusica in [Volume.__AUMENTARVOLUME, Volume.__DIMINUIRVOLUME]
    @staticmethod
    def setVolume(caractereVolume, volume, volumePadrao, volumeMax):
        if caractereVolume == Volume.__AUMENTARVOLUME:
            volume = volume * 2
            if volume > volumeMax:
                return volumeMax
            else:
                return volume
        elif caractereVolume == Volume.__DIMINUIRVOLUME:
            return volumePadrao

class Instrumentos():

    @staticmethod
    def verificarCaractereConjunto(caractereMusica):
         return caractereMusica == "\n"   
    
    @staticmethod
    def getInstrumentos():
          return random.randint(1,127)

class BPM():
    @staticmethod
    def verificarCaractereConjunto(caractereMusica):
         return caractereMusica == ";" 
    
    @staticmethod
    def setBPM():
         return random.randint(1,1000)
      
class Musica:
#Classe geral da música, responsável por gerar o arquivo de música
# A Classe solicita informações sobre o caractere para a classe TraducaoCaratereMIDI e faz as devidas alteracoes no arquivo de musica
    __TRACK = 0
    __CANAL = 0
    __DURACAO = 1
    __BPMBASE = 120
    __VOLUMEBASE = 50
    __VOLUMEMAX = 127
    __TELEFONE = 124
    __NOTAMAX = 127
    __NOTAMIN = 0
    __OITAVA = 12
    notaBase = NotasBasicas("ABCDEFG ")
    notaAleatoria = NotaAleatoria("?")
    notaRepetida = NotasRepetidas("OIU")

    def __init__(self, volumeInicial, estadoOitava, estado2x):
        self.midi = MIDIFile(1)
        self.volume = volumeInicial
        self.tempo_musica = 0
        self.instrumento = 0

        if estadoOitava == True:
            self.tom = self.__OITAVA
        else:
            self.tom = 0

        if estado2x == True:
            self.bpm = self.__BPMBASE * 2
        else:
            self.bpm = self.__BPMBASE

       
    #Salva arquivo
    def criarArquivoMidi(self):
        midi_file = "output.mid"

        with open(midi_file, "wb") as midi_output:
            self.midi.writeFile(midi_output)

    #Adiciona a nota e corrige o tempo
    def adicionarNota(self, numeroNota):
        self.midi.addNote(self.__TRACK, self.__CANAL, numeroNota + self.tom,  self.tempo_musica, self.__DURACAO, self.volume)
        self.tempo_musica = self.tempo_musica + 1
  
    #Função para adicionar o som do telefone, que nao encontrei como fazer
    def adicionarTelefone(self):
        instrumentoAnterior = self.instrumento
        self.alteraInstrumento(self.__TELEFONE)
        self.adicionarNota(random.randint(self.__NOTAMIN, self.__NOTAMAX))
        self.alteraInstrumento(instrumentoAnterior)

    def alteraVolume(self, novoVolume):
        self.volume = novoVolume

    def alteraBPM(self, novoBPM):
        self.bpm = novoBPM
        self.midi.addTempo(self.__TRACK, self.tempo_musica, self.bpm)

    def alteraTom(self, novoTom):
        self.tom = novoTom

    def alteraInstrumento(self, novoInstrumento):
        self.instrumento = novoInstrumento
        self.midi.addProgramChange(self.__TRACK, self.__CANAL,  self.tempo_musica, self.instrumento)

    def criarMusica(self, stringNotas):

        self.midi.addTempo(self.__TRACK, 0 , self.bpm)
        caracteresParaPular = 0

        for i, caractere in enumerate(stringNotas):
            if caracteresParaPular > 0:
                caracteresParaPular = caracteresParaPular - 1     

            elif StringBPM.cmpString(stringNotas, i):
                self.alteraBPM(StringBPM.setBPM(self.bpm))
                caracteresParaPular = 3

            elif StringOitava.cmpString(stringNotas, i):
                self.alteraTom(StringOitava.setOitava(self.tom, stringNotas, i))
                caracteresParaPular = 1

            elif self.notaRepetida.verificarCaractereConjunto(caractere):
                if self.notaRepetida.verifUltimoCharNota(ultimoCaractere) == True: 
                    self.adicionarNota(self.notaRepetida.getNota(ultimoCaractere))
                else:
                    self.adicionarTelefone()

            elif self.notaBase.verificarCaractereConjunto(caractere):
                self.adicionarNota(self.notaBase.getNota(caractere))

            elif self.notaAleatoria.verificarCaractereConjunto(caractere):
                self.adicionarNota(self.notaAleatoria.getNota())      

            elif Volume.verificarCaractereConjunto(caractere):
                self.alteraVolume(Volume.setVolume(caractere, self.volume, self.__VOLUMEBASE, self.__VOLUMEMAX))
            
            elif Instrumentos.verificarCaractereConjunto(caractere):
                self.alteraInstrumento(Instrumentos.getInstrumentos())
            
            elif BPM.verificarCaractereConjunto(caractere):
                self.alteraBPM(BPM.setBPM())
            
            ultimoCaractere = caractere

        self.criarArquivoMidi()



class Player:
    @staticmethod
    def tocarMusica(midi_file):
        #Funcao para tocar o arquivo
        pygame.init()
        pygame.mixer.init()

        try:
            pygame.mixer.music.load(midi_file)
            pygame.mixer.music.play() 
        except pygame.error as e:
            print("Pygame error:", e)
    @staticmethod
    def pararMusica():
        pygame.mixer.music.stop()
    

def mensagemAjuda():
    mb.showinfo("Ajuda", "O campo de texto serve para você digitar a música que deseja tocar.\n\nO botão ▶ serve para tocar a música.\n\nO botão ⏺️ serve para parar a música.\n\nO checkbox 2x serve para tocar a música duas vezes mais rápido.\n\nO checkbox +# serve para tocar a música uma oitava acima.\n\nO botão ? serve para mostrar essa mensagem de ajuda.\n\nO botão ⬇ serve para salvar a música em um arquivo midi.")
