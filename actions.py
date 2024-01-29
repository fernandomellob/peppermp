import functions
import pygame

def play(text,volume,oitava,doisx):
    musica = functions.Musica(volume, oitava, doisx)
    musica.criarMusica(text)
    functions.tocar_musica("output.mid")
    print("play")

def reset():
    pygame.mixer.music.stop()
    print("reset")

def ajuda():
    print("?")

def salvarMidi(text):
    musica = functions.Musica()
    musica.criarMusica(text)
    print("salvarMidi")

