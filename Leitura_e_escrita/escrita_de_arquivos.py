file = open("arquivo.txt", mode="w")  # ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")
# também podemos escrever em um arquivo através do print
print("Túlio 22", file=file)
# Para escrever múltiplas linhas podemos utilizar a função writelines
LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)

# Abrimos o arquivo e escrevemos seu conteúdo. Vamos então fechá-lo:

file.close()
