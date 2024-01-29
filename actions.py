import functions

def play(text,volume,oitava,doisx):
    musica = functions.Musica(volume, oitava, doisx)
    musica.criarMusica(text)
    functions.Player.tocarMusica("output.mid")

def reset():
    functions.Player.pararMusica()

def ajuda():
    functions.mensagemAjuda()

def salvarMidi(text):
    musica = functions.Musica()
    musica.criarMusica(text)

