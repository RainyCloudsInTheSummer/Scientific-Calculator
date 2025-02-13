import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica - By RainyCloudsInTheSummer")
        self.root.geometry("638x390")
        self.root.configure(bg="black")
        
        self.equacao = "0"
        self.entrada_texto = tk.StringVar(value=self.equacao)
        
        entrada = tk.Entry(root, textvariable=self.entrada_texto, font=("Arial", 40), bd=10, relief=tk.FLAT, justify='right', bg="black", fg="white")
        entrada.grid(row=0, column=0, columnspan=4, ipadx=8, padx=10, pady=10, sticky="nsew")
        
        botoes = [
            ('C', '+/-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', ',', '=', '√')
        ]
        
        frame_principal = tk.Frame(root, bg="black")
        frame_principal.grid(row=1, column=0, columnspan=4, sticky="nsew")
        
        for i, linha in enumerate(botoes):
            for j, botao in enumerate(linha):
                cor = "#4169e1" if botao in ('/', '*', '-', '+', '=', '√') else "#333"
                btn = tk.Button(frame_principal, text=botao, font=("Arial", 22), relief=tk.FLAT, bg=cor, fg="white", borderwidth=1, highlightbackground="black", command=lambda b=botao: self.clicar(b))
                btn.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        
        for i in range(5):
            frame_principal.rowconfigure(i, weight=1)
        for j in range(4):
            frame_principal.columnconfigure(j, weight=1)
        
        self.root.bind('<Key>', self.teclado)
                
    def clicar(self, botao):
        if botao == "C":
            self.equacao = "0"
        elif botao == "=":
            try:
                self.equacao = str(eval(self.equacao))
            except Exception as e:
                messagebox.showerror("Erro", "Entrada inválida")
                self.equacao = "0"
        elif botao == "√":
            try:
                self.equacao = str(math.sqrt(float(self.equacao)))
            except:
                messagebox.showerror("Erro", "Entrada inválida")
                self.equacao = "0"
        elif botao == "+/-":
            try:
                self.equacao = str(-float(self.equacao))
            except:
                messagebox.showerror("Erro", "Entrada inválida")
                self.equacao = "0"
        elif botao == "0":
            if self.equacao != "0":
                self.equacao += "0"
        else:
            if self.equacao == "0":
                self.equacao = botao if botao != ',' else '.'
            else:
                self.equacao += botao if botao != ',' else '.'
        
        self.entrada_texto.set(self.equacao)
    
    def teclado(self, event):
        tecla = event.keysym
        teclas_validas = {'Return': '=', 'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/', 'period': '.', 'comma': ','}
        
        if tecla.isdigit() or tecla in teclas_validas:
            self.clicar(teclas_validas.get(tecla, tecla))
        elif tecla == 'BackSpace':
            self.equacao = self.equacao[:-1] if len(self.equacao) > 1 else "0"
            self.entrada_texto.set(self.equacao)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
