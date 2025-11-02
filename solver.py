import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from ngram_score import ngram_score # Importa a classe do seu outro arquivo

random.seed(1337)
# --- FUNÇÕES AUXILIARES ---

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
contador_decriptação = 0 # Movido para o escopo global

def decrypt(ciphertext, key_map):
    """
    Descriptografa o texto (ciphertext) usando o mapa de chaves (key_map).
    """
    global contador_decriptação
    contador_decriptação = contador_decriptação +  1
    return "".join(key_map[c] for c in ciphertext)

def get_key():
    """Cria um mapa de chave incial."""
    key_list = list(ALPHABET)
    # Mapeia o alfabeto padrão (A-Z)
    # Ex: {'A': 'Q', 'B': 'W', 'C': 'E', ...}
    return dict(zip(ALPHABET, key_list))

# --- CONFIGURAÇÃO ---

try:
    fitness = ngram_score('english_quadgrams.txt')
except FileNotFoundError:
    print("ERRO: Arquivo 'english_quadgrams.txt' não encontrado.")
    sys.exit()

# Carrega e limpa o texto cifrado
try:
    with open('saidatrue.txt', 'r', encoding='utf-8') as f:
        original_text = f.read()
except FileNotFoundError:
    print("ERRO: Arquivo 'saidatrue.txt' não encontrado.")
    print("Por favor, rode o script 'converter_binario_ascii.py' primeiro.")
    sys.exit()

#texto limpo (A-Z, maiúsculas)
ciphertext = "".join(c for c in original_text.upper() if c in ALPHABET)

print("-----------------------------------------------------------\n")

MAX_ITERATIONS = 1000
# Paciência do programa

# Gera a chave "pai" inicial
contador_chave = 0
contador_chave_ruim =0
# contador_decriptação = 0 # Já foi inicializado globalmente

parent_key = get_key()
print("Primeira chave: " + "".join(parent_key[c] for c in ALPHABET))
decrypted_text = decrypt(ciphertext, parent_key)
parent_score = fitness.score(decrypted_text)
best_key = parent_key
best_score = parent_score

# --- Listas para o gráfico ---
fitness_history = [best_score]
iteration_history = [contador_decriptação] # Guarda o ponto inicial

# Loop principal de otimização
i = 0
while i < MAX_ITERATIONS:
    # Cria uma chave filha
    child_key = parent_key.copy()
    
    # Escolhe duas letras aleatórias do alfabeto
    l1, l2 = random.sample(ALPHABET, 2)
    
    # troca seus valores de destino
    child_key[l1], child_key[l2] = child_key[l2], child_key[l1]

    # Pontua a chave filha
    decrypted_text = decrypt(ciphertext, child_key)
    child_score = fitness.score(decrypted_text)

    # Comparação
    if child_score > parent_score:
        #Melhora
        parent_key = child_key
        parent_score = child_score
        i = 0 # Reinicia o contador de iterações, já que achamos uma melhora
        
        # Atualiza o melhor resultado geral
        if parent_score > best_score:
            best_score = parent_score
            best_key = parent_key
            print(f"NOVO RECORDE | Pontuação: {best_score:.2f}")
            print("NOVA CHAVE: "+ "".join(best_key[c] for c in ALPHABET))
            contador_chave +=1
            
            # --- GRÁFICO ---
            fitness_history.append(best_score)
            iteration_history.append(contador_decriptação) # Adiciona o ponto atual
            # ---  ---
    else:
        i += 1
        contador_chave_ruim +=1

# --- RESULTADOS ---

print("\n-----------------------------------------------------------")

# Imprime a melhor chave encontrada
print("\nMelhor Chave Encontrada (Cifra -> Plaintext):")
plain_str = "Chave: " + "".join(best_key[c] for c in ALPHABET)
print(f"Chaves melhores testadas: {contador_chave}")
print(f"Chaves piores testadas: {contador_chave_ruim}")
print(f"Decriptações no total: {contador_decriptação}")
print(plain_str)

# Descriptografa o texto original usando a melhor chave encontrada.
final_text = "".join(best_key.get(c.upper(), c) for c in original_text)
print("\n--- Texto Descriptografado ---")
print(final_text)
with open("resposta_final.txt", "w", encoding="utf-8") as f:
    f.write(final_text)
print("Arquivo salvo como: resposta_final.txt")


# --- GERAR GRÁFICO ---
plt.figure(figsize=(12, 7)) # Tamanho
plt.plot(iteration_history, fitness_history, marker='.', linestyle='-', markersize=5, label='Melhor Fitness')

# Adiciona títulos e rótulos
plt.title("Evolução do Fitness Score (Hill Climbing)")
plt.xlabel("Número Total de Decriptações (Iterações)")
plt.ylabel("Melhor Fitness Score Encontrado")

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Salva o gráfico em um arquivo
plt.savefig("evolucao_fitness.png")
plt.show()
