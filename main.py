import tkinter as tk
from tkinter import messagebox
import functions

class GeradorSenhasGUI:
    def __init__(self, root):
        #Organização dos elementos
        self.root = root
        self.root.title("Gerador de Senhas")
        self.root.geometry("400x300")

        self.comprimento_label = tk.Label(root, text="Comprimento da Senha:")
        self.comprimento_label.pack(pady=10)

        self.comprimento_entry = tk.Entry(root)
        self.comprimento_entry.pack(pady=10)
        self.comprimento_entry.insert(tk.END, "8")

        self.letras_var = tk.BooleanVar(value=True)
        self.letras_checkbox = tk.Checkbutton(root, text="Incluir Letras", variable=self.letras_var)
        self.letras_checkbox.pack(pady=10)

        self.numeros_var = tk.BooleanVar(value=False)
        self.numeros_checkbox = tk.Checkbutton(root, text="Incluir Números", variable=self.numeros_var)
        self.numeros_checkbox.pack(pady=10)

        self.especiais_var = tk.BooleanVar(value=False)
        self.especiais_checkbox = tk.Checkbutton(root, text="Incluir Caracteres Especiais", variable=self.especiais_var)
        self.especiais_checkbox.pack(pady=10)

        self.gerar_button = tk.Button(root, text="Gerar Senha", command=self.gerarSenhaClicked)
        self.gerar_button.pack(pady=10)

        self.senha_text = tk.Text(root, height=5, width=15)
        self.senha_text.pack(pady=10)
        self.senha_text.config(state=tk.DISABLED)  # Impede a edição do texto


    def gerarSenhaClicked(self): #Função executada ao clicar no botão de gerar senha
        comprimento = self.comprimento_entry.get()
        letras = self.letras_var.get()
        numeros = self.numeros_var.get()
        especiais = self.especiais_var.get()

        #Validação dos parametros
        if (not functions.validarComprimento(comprimento) or
            not functions.validarParametros(letras, numeros, especiais)):
            messagebox.showerror("Erro", "Parâmetros inválidos!")
            return

        #Geração da senha
        senha = functions.gerarSenha(int(comprimento), letras, numeros, especiais)
        self.senha_text.config(state=tk.NORMAL)  # Permite a edição do texto
        self.senha_text.delete("1.0", tk.END)  # Limpa o texto anterior
        self.senha_text.insert(tk.END, senha)  # Insere a nova senha
        self.senha_text.config(state=tk.DISABLED)  # Impede a edição do texto


def main():
    root = tk.Tk()
    app = GeradorSenhasGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
