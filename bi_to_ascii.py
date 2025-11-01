# converter_binario_ascii.py
# Converte bits (0 e 1) de um arquivo para texto ASCII.
# Mostra: "arquivo codificado" e "arquivo de saída"

print("=== Conversor Binário → ASCII ===")
entrada = "encoded.txt"
saida = "saidatrue.txt"

try:
    # Lê o conteúdo
    with open(entrada, "r", encoding="utf-8", errors="ignore") as f:
        dados = f.read()

    # divide o código em pedaços
    codigos_binarios = dados.split()
    
    texto_decodificado = []
    
    for bin_str in codigos_binarios:
        if bin_str: 
            #Converte a string binária para um número inteiro
            valor_ascii = int(bin_str, 2)
            
            #Converte o número inteiro para seu caractere ascii
            texto_decodificado.append(chr(valor_ascii))

    texto = "".join(texto_decodificado)

    with open(saida, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Arquivo salvo como:" + saida)

except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print("Erro", e)