import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def escolher_origem():
    pasta = filedialog.askdirectory(title="Selecione a pasta de origem")
    if pasta:
        entrada_origem.delete(0, tk.END)
        entrada_origem.insert(0, pasta)

def escolher_destino():
    pasta = filedialog.askdirectory(title="Selecione a pasta de destino")
    if pasta:
        entrada_destino.delete(0, tk.END)
        entrada_destino.insert(0, pasta)

def copiar_pastas():
    pasta_origem = entrada_origem.get()
    pasta_destino = entrada_destino.get()
    pastas_selecionadas = entrada_pastas.get().split(",")  # Nomes separados por vírgula

    if not os.path.exists(pasta_origem):
        messagebox.showerror("Erro", "A pasta de origem não existe!")
        return
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    if not pastas_selecionadas:
        messagebox.showwarning("Aviso", "Nenhuma pasta foi informada!")
        return

    for pasta in pastas_selecionadas:
        origem = os.path.join(pasta_origem, pasta.strip())
        destino = os.path.join(pasta_destino, pasta.strip())

        if os.path.isdir(origem):
            try:
                shutil.copytree(origem, destino)
            except FileExistsError:
                messagebox.showerror("Erro", f"A pasta '{pasta.strip()}' já existe no destino!")
        else:
            messagebox.showerror("Erro", f"A pasta '{pasta.strip()}' não foi encontrada na origem!")
    
    messagebox.showinfo("Sucesso", "Pastas copiadas com sucesso!")

# Criando a interface gráfica
janela = tk.Tk()
janela.title("Copiador de Pastas")
janela.geometry("450x250")

# Organização com Frames
frame_topo = tk.Frame(janela, pady=10)
frame_topo.pack()
frame_meio = tk.Frame(janela, pady=10)
frame_meio.pack()
frame_inferior = tk.Frame(janela, pady=10)
frame_inferior.pack()

# Elementos na interface
tk.Label(frame_topo, text="Pasta de origem:", font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
entrada_origem = tk.Entry(frame_topo, width=40, font=("Arial", 10))
entrada_origem.grid(row=0, column=1, pady=5)
tk.Button(frame_topo, text="Selecionar", command=escolher_origem, font=("Arial", 10)).grid(row=0, column=2, padx=5)

tk.Label(frame_meio, text="Pasta de destino:", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
entrada_destino = tk.Entry(frame_meio, width=40, font=("Arial", 10))
entrada_destino.grid(row=1, column=1, pady=5)
tk.Button(frame_meio, text="Selecionar", command=escolher_destino, font=("Arial", 10)).grid(row=1, column=2, padx=5)

tk.Label(frame_meio, text="Nomes das pastas (separados por vírgula):", font=("Arial", 10)).grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=5)
entrada_pastas = tk.Entry(frame_meio, width=50, font=("Arial", 10))
entrada_pastas.grid(row=3, column=0, columnspan=3, pady=5)

tk.Button(frame_inferior, text="Copiar Pastas Informadas", command=copiar_pastas, font=("Arial", 10)).pack()

# Executar a interface
janela.mainloop()
