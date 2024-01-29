import functions
import pygame
import tkinter.messagebox as mb

def play(text,volume,oitava,doisx):
    musica = functions.Musica(volume, oitava, doisx)
    musica.criarMusica(text)
    functions.tocar_musica("output.mid")
    print("play")

def reset():
    pygame.mixer.music.stop()
    print("reset")

def ajuda():
    mb.showinfo("Ajuda", "O campo de texto serve para você digitar a música que deseja tocar.\n\nO botão ▶ serve para tocar a música.\n\nO botão ⏺️ serve para parar a música.\n\nO checkbox 2x serve para tocar a música duas vezes mais rápido.\n\nO checkbox +# serve para tocar a música uma oitava acima.\n\nO botão ? serve para mostrar essa mensagem de ajuda.\n\nO botão ⬇ serve para salvar a música em um arquivo midi.")
    print("?")

def salvarMidi(text):
    musica = functions.Musica()
    musica.criarMusica(text)
    print("salvarMidi")

