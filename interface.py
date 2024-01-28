import tkinter as tk
import actions as actions

# Create the main window
window = tk.Tk(className="Pepper MP")

# Frame para o campo de texto
frameText_Field = tk.Frame(window)
frameText_Field.grid(row=0, column=1, padx=5, pady=5)

#Label de titulo
titulo = tk.Label(frameText_Field, text="Pepper Music Player", font=("Arial", 10))
titulo.grid(row=0, padx=5, pady=5)

# Create a text field
text_field = tk.Text(frameText_Field, height=10, width=50)
text_field.grid(row=1, padx=5, pady=5)

# Volume
volume = tk.Scale(frameText_Field, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
volume.grid(row=2, padx=5, pady=5)

# Frame para os botões
frameButtons = tk.Frame(window)
frameButtons.grid(row=1, column=1, padx=5, pady=5)

# Create five buttons
text = text_field.get("1.0",'end-1c')
playButton = tk.Button(frameButtons, text="▶", command=lambda: actions.play(text_field.get("1.0","end")), width=2, height=1)
playButton.grid(row=2, column=0, padx=5, pady=5)

resetButton = tk.Button(frameButtons, text="⏺️", command=actions.reset, width=2, height=1)
resetButton.grid(row=2, column=1, padx=5, pady=5)

doisxButton = tk.Button(frameButtons, text="2x", command=actions.doisX, width=2, height=1)
doisxButton.grid(row=2, column=2, padx=5, pady=5)

oitavaButton = tk.Button(frameButtons, text="#", command=actions.oitava, width=2, height=1)
oitavaButton.grid(row=2, column=3, padx=5, pady=5)

ajudaButton = tk.Button(frameButtons, text="?", command=actions.ajuda, width=2, height=1)
ajudaButton.grid(row=2, column=4, padx=5, pady=5)

salvarMidiButton = tk.Button(frameButtons, text="⬇", command=lambda: actions.salvarMidi(text_field.get("1.0","end")), width=2, height=1)
salvarMidiButton.grid(row=2, column=5, padx=5, pady=5)

# Start the main loop
window.mainloop()
