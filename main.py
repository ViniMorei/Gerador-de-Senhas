import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha(comprimento=8, letras=True, numeros=True, especiais=True):
    caracteres = ''
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def gerar_senha_clicked():
    comprimento = int(comprimento_entry.get())
    incluir_letras = letras_var.get()
    incluir_numeros = numeros_var.get()
    incluir_especiais = especiais_var.get()

    senha = gerar_senha(comprimento, incluir_letras, incluir_numeros, incluir_especiais)
    messagebox.showinfo("Senha Gerada", f"Sua senha gerada é:\n{senha}")

# Criar janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Criar e posicionar os elementos da interface
tk.Label(root, text="Comprimento da Senha:").pack()
comprimento_entry = tk.Entry(root)
comprimento_entry.pack()

tk.Label(root, text="Incluir Letras:").pack()
letras_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=letras_var).pack()

tk.Label(root, text="Incluir Números:").pack()
numeros_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=numeros_var).pack()

tk.Label(root, text="Incluir Caracteres Especiais:").pack()
especiais_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=especiais_var).pack()

gerar_button = tk.Button(root, text="Gerar Senha", command=gerar_senha_clicked)
gerar_button.pack()

# Iniciar o loop de eventos da interface gráfica
root.mainloop()