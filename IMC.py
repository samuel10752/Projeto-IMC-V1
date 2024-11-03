import tkinter as tk
from tkinter import messagebox

# Largura padrão para os botões
largura_botao = 12

# Função para calcular o IMC
def calcular_imc():
    try:
        altura = float(campo_altura.get().replace(" cm", "")) / 100  # Converter cm para metros
        peso = float(campo_peso.get().replace(" Kg", ""))
        imc = peso / (altura ** 2)

        # Determinar a categoria de IMC com base no valor
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"

        texto_resultado.set(f"IMC: {imc:.2f}\nCategoria: {categoria}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos para altura e peso.")

# Função para resetar todos os campos
def limpar_campos():
    campo_nome.delete(0, tk.END)
    campo_endereco.delete(0, tk.END)
    campo_altura.delete(0, tk.END)
    campo_peso.delete(0, tk.END)
    texto_resultado.set("")

# Função para sair da aplicação
def sair_aplicacao():
    root.destroy()

# Função para aplicar formatação de altura
def formatar_altura(event):
    texto = campo_altura.get()
    try:
        altura = float(texto)
        campo_altura.delete(0, tk.END)
        campo_altura.insert(0, f"{altura:.1f} cm")  # Formato com uma casa decimal e "cm"
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira um número válido para altura.")

# Função para aplicar formatação de peso
def formatar_peso(event):
    texto = campo_peso.get()
    try:
        peso = float(texto)
        campo_peso.delete(0, tk.END)
        campo_peso.insert(0, f"{peso:.1f} Kg")  # Formato com uma casa decimal e "Kg"
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira um número válido para peso.")

# Função para validar entrada de letras e espaços apenas
def validar_letras(texto):
    return texto.isalpha() or texto == "" or all(c.isalpha() or c.isspace() for c in texto)

# Inicializar janela principal
root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")

# Nome do Paciente
tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
campo_nome = tk.Entry(root, width=53, bd=2, relief="solid", bg="#F0F0F0")
campo_nome.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Configura a validação para Nome do Paciente
validacao_nome = root.register(validar_letras)
campo_nome.config(validate="key", validatecommand=(validacao_nome, "%P"))

# Endereço Completo
tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
campo_endereco = tk.Entry(root, width=53, bd=2, relief="solid", bg="#F0F0F0")
campo_endereco.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Configura a validação para Endereço Completo
validacao_endereco = root.register(validar_letras)
campo_endereco.config(validate="key", validatecommand=(validacao_endereco, "%P"))

# Altura
tk.Label(root, text="Altura (cm)").grid(row=2, column=0, sticky="w", padx=5, pady=5)
campo_altura = tk.Entry(root, width=15, bd=2, relief="solid", bg="#F0F0F0")
campo_altura.grid(row=2, column=1, padx=5, pady=(0, 8), sticky="w")
campo_altura.bind("<FocusOut>", formatar_altura)  # Formata ao perder o foco

# Peso
tk.Label(root, text="Peso (Kg)").grid(row=3, column=0, sticky="w", padx=5, pady=(0, 50))
campo_peso = tk.Entry(root, width=15, bd=2, relief="solid", bg="#F0F0F0")
campo_peso.grid(row=3, column=1, padx=5, pady=(0, 50), sticky="w")
campo_peso.bind("<FocusOut>", formatar_peso)  # Formata ao perder o foco

# Exibição do Resultado com Texto Centralizado
texto_resultado = tk.StringVar()
rotulo_resultado = tk.Label(root, textvariable=texto_resultado, width=30, height=6, bd=2, relief="solid", anchor="center", justify="center", bg="#F0F0F0")
rotulo_resultado.grid(row=2, column=1, rowspan=2, padx=(113, 10), pady=(5, 0), sticky="e")

# Frame específico para os botões Calcular e Reiniciar
frame_botoes_centro = tk.Frame(root)
frame_botoes_centro.grid(row=5, column=0, columnspan=2, pady=10, sticky="w", padx=(70, 0))

# Botões estilizados em cinza claro
estilo_botao = {
    "bg": "#D3D3D3", "fg": "black",
    "activebackground": "#B0B0B0", "activeforeground": "black",
    "width": largura_botao, "bd": 2, "relief": "solid"
}

tk.Button(frame_botoes_centro, text="Calcular", command=calcular_imc, **estilo_botao).pack(side="left", padx=1)
tk.Button(frame_botoes_centro, text="Reiniciar", command=limpar_campos, **estilo_botao).pack(side="left", padx=1)

# Botão Sair, também estilizado em cinza claro
frame_botao_sair = tk.Frame(root)
frame_botao_sair.grid(row=5, column=1, sticky="e", padx=(10, 10))

tk.Button(frame_botao_sair, text="Sair", command=sair_aplicacao, **estilo_botao).pack()

# Executar a aplicação
root.mainloop()
