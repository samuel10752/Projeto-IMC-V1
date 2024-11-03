import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100  # Converter cm para metros
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)

        # Determinar a categoria de IMC com base no valor
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_text.set(f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")


# Função para resetar todos os campos
def reset_fields():
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    result_text.set("")


# Função para sair da aplicação
def exit_application():
    root.destroy()


# Inicializar janela principal
root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")

# Fixar o tamanho da janela para impedir redimensionamento
root.resizable(False, False)  # Desativa o redimensionamento da janela

# Nome do Paciente
tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = tk.Entry(root, width=53, bd=2, relief="solid", bg="#F0F0F0")
entry_name.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Endereço Completo
tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_address = tk.Entry(root, width=53, bd=2, relief="solid", bg="#F0F0F0")
entry_address.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Altura
tk.Label(root, text="Altura (cm)").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_height = tk.Entry(root, width=15, bd=2, relief="solid", bg="#F0F0F0")
entry_height.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Peso
tk.Label(root, text="Peso (Kg)").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_weight = tk.Entry(root, width=15, bd=2, relief="solid", bg="#F0F0F0")
entry_weight.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Exibição do Resultado ao lado direito dos campos de altura e peso, com tamanho fixo
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, width=30, height=4, bd=2, relief="solid", anchor="w", justify="left", bg="#F0F0F0")
result_label.grid(row=2, column=2, rowspan=2, padx=(7, 5), pady=5, sticky="w")  # Ajuste de padx para simular largura entre 29 e 30
# Botões
tk.Button(root, text="Calcular", command=calculate_bmi).grid(row=4, column=0, padx=5, pady=10, sticky="w")
tk.Button(root, text="Reiniciar", command=reset_fields).grid(row=4, column=1, padx=5, pady=10, sticky="w")
tk.Button(root, text="Sair", command=exit_application).grid(row=4, column=2, padx=5, pady=10, sticky="w")

# Executar a aplicação
root.mainloop()
