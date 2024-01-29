import tkinter as tk
import actions as actions
from tkinter import Tk, Label
from PIL import Image, ImageTk 

# Create the main window
window = tk.Tk(className="Pepper MP")
window.configure(bg='#E35335')  # Define a cor de fundo da janela principal

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)


# Frame para o campo de texto
frameText_Field = tk.Frame(window)
frameText_Field.grid(row=0, column=1, padx=5, pady=5)
frameText_Field.configure(bg='#E35335')

#Label de titulo
titulo = tk.Label(frameText_Field, text="Pepper Music Player™", font=("Arial", 10), highlightbackground='black', highlightcolor='black', highlightthickness=1)
titulo.grid(row=4, column=0, columnspan=1)  
titulo.configure(bg='#90ee90')

# Função para limpar o placeholder ao clicar
def on_entry_click(event):
    if text_field.get("1.0", "end-1c") == 'Escreva sua linda música aqui':
        text_field.delete("1.0", "end")  # Deleta o conteúdo da caixa de texto
        text_field.unbind('<FocusIn>', on_focus_id)  # Desvincula o evento após o primeiro clique

# Função para adicionar o placeholder se a caixa estiver vazia
def on_focusout(event):
    if not text_field.get("1.0", "end-1c").strip():
        text_field.insert("1.0", 'Escreva sua linda música aqui', font=("Comic Sans MS", 10))
        # Revincula o evento de focus in para que o placeholder possa reaparecer
        global on_focus_id
        on_focus_id = text_field.bind('<FocusIn>', on_entry_click)




# Create a text field
text_field = tk.Text(frameText_Field, height=10, width=50, highlightbackground='black', highlightcolor='black', highlightthickness=1)
text_field.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
text_field.configure(bg='#90ee90')
text_field.insert("1.0", 'Escreva sua linda música aqui')  # Insere o texto padrão
on_focus_id = text_field.bind('<FocusIn>', on_entry_click)  # Vincula o evento de foco
text_field.bind('<FocusOut>', on_focusout)  # Vincula o evento de foco fora

# Volume
volume = tk.Scale(frameText_Field, from_=0, to=100, orient=tk.HORIZONTAL, length=200, troughcolor='white', bg='white', highlightbackground='black', highlightcolor='black', highlightthickness=1)
volume.set(50)
volume.grid(row=2, column=0, padx=5, pady=5)
volume.configure(bg='#90ee90')


# Frame para os botões
frameButtons = tk.Frame(window,  highlightbackground='black', highlightcolor='black', highlightthickness=2)
frameButtons.grid(row=1, column=1, padx=5, pady=5)
frameButtons.configure(bg='#90ee90')

# Create five buttons
text = text_field.get("1.0",'end-1c')
playButton = tk.Button(frameButtons, text="▶", command=lambda: actions.play(text_field.get("1.0","end"),volume.get(),oitava_state.get(),doisx_state.get()), width=2, height=1)
playButton.grid(row=2, column=0, padx=5, pady=5)
playButton.configure(bg='#ffc3a0')

resetButton = tk.Button(frameButtons, text="⏺️", command=actions.reset, width=2, height=1)
resetButton.grid(row=2, column=1, padx=5, pady=5)
resetButton.configure(bg='yellow')

ajudaButton = tk.Button(frameButtons, text="?", command=actions.ajuda, width=2, height=1)
ajudaButton.grid(row=2, column=2, padx=5, pady=5)
ajudaButton.configure(bg='orange')

salvarMidiButton = tk.Button(frameButtons, text="⬇", command=lambda: actions.salvarMidi(text_field.get("1.0","end")), width=2, height=1)
salvarMidiButton.grid(row=2, column=3, padx=5, pady=5)
salvarMidiButton.configure(bg='#0097FF')

doisx_state = tk.BooleanVar()
doisxButton = tk.Checkbutton(frameButtons, text="2x", variable = doisx_state, width=2, height=1, onvalue = True, offvalue= False)
doisxButton.grid(row=2, column=4, padx=5, pady=5)
doisxButton.configure(bg='#891289')

oitava_state = tk.BooleanVar()
oitavaButton = tk.Checkbutton(frameButtons, text="+#", variable = oitava_state, width=2, height=1, onvalue = True, offvalue= False)
oitavaButton.grid(row=2, column=5, padx=5, pady=5)
oitavaButton.configure(bg='grey')


# Carregando e redimensionando a imagem do logotipo
image = Image.open(r"C:\Users\bener\pimenta\FinalTrabapimenta\logo.png")
image = image.resize((80 , 80), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Adicionando a imagem a um Label e posicionando centralizado no topo

label_logo = Label(frameText_Field, image=photo)
label_logo.image = photo
label_logo.grid(row=0, column=0, columnspan=1)  
label_logo.configure(bg='#E35335')

# Função chamada quando o botão do logotipo é pressionado
def on_logo_press(event):
    global label_text
    label_text = tk.Label(frameText_Field, text="GL Nogueira.", bg='#E35335', fg='black')
    label_text.grid(row=0, column=0, sticky='w')

# Função chamada quando o botão do logotipo é solto
def on_logo_release(event):
    label_text.destroy()


# Cria o botão com a imagem do logotipo
logo_button = tk.Button(frameText_Field, image=photo, borderwidth=0, highlightthickness=0, bg='#E35335')
logo_button.image = photo  # Mantenha uma referência!
logo_button.grid(row=0, column=0)
logo_button.bind('<ButtonPress>', on_logo_press)  # Bind do evento de pressionar o botão
logo_button.bind('<ButtonRelease>', on_logo_release)  # Bind do evento de soltar o botão



# Start the main loop
window.mainloop()
