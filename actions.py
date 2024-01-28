import functions

def play(text):
    musica = functions.Musica()
    musica.criarMusica(text)
    functions.tocar_musica("output.mid")
    print("play")

def reset():
    print("reset")

def doisX():
    print("2X")

def oitava():
    print("#")

def ajuda():
    print("?")

def salvarMidi(text):
    musica = functions.Musica()
    musica.criarMusica(text)
    print("salvarMidi")

