import random
import sys
from ngram_score import ngram_score # Importa a classe do seu outro arquivo

random.seed(1337)
# --- 0.1 FUNÇÕES AUXILIARES ---

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(ciphertext, key_map):
    """
    Descriptografa o texto (ciphertext) usando o mapa de chaves (key_map).
    """
    return "".join(key_map[c] for c in ciphertext)

def get_random_key():
    """Cria um mapa de chaves aleatório."""
    key_list = list(ALPHABET)
    random.shuffle(key_list)
    # Mapeia o alfabeto padrão (A-Z) para a lista embaralhada
    # Ex: {'A': 'Q', 'B': 'W', 'C': 'E', ...}
    return dict(zip(ALPHABET, key_list))

# --- 0.2 CONFIGURAÇÃO ---

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



MAX_ITERATIONS = 10000
# Paciência do programa

# 1. Gera a chave "pai" inicial
parent_key = get_random_key()
primeira_key = parent_key
decrypted_text = decrypt(ciphertext, parent_key)
parent_score = fitness.score(decrypted_text)
best_key = parent_key
best_score = parent_score

print(f"Iteração 0 | Pontuação: {best_score:.2f}")

# 2. Loop principal de otimização
i = 0
while i < MAX_ITERATIONS:
    # 3. Cria uma chave "filha" trocando duas letras da chave "pai"
    child_key = parent_key.copy()
    
    # Escolhe duas letras aleatórias do *alfabeto cifrado* (A-Z)
    l1, l2 = random.sample(ALPHABET, 2)
    
    # E troca seus *valores* de destino (plaintext)
    child_key[l1], child_key[l2] = child_key[l2], child_key[l1]

    # 4. Pontua a chave "filha"
    decrypted_text = decrypt(ciphertext, child_key)
    child_score = fitness.score(decrypted_text)

    # 5. Compara as pontuações
    if child_score > parent_score:
        # Achamos uma melhora
        parent_key = child_key
        parent_score = child_score
        i = 0 # Reinicia o contador de iterações, já que achamos uma melhora
        
        # Atualiza o melhor resultado geral
        if parent_score > best_score:
            best_score = parent_score
            best_key = parent_key
            print(f"NOVO RECORDE | Pontuação: {best_score:.2f}")
    
    i += 1

# --- 4. RESULTADOS ---

print("\n-----------------------------------------------------------")

# Imprime a melhor chave encontrada
print("\nMelhor Chave Encontrada (Cifra -> Plaintext):")
plain_str = "Chave: " + "".join(best_key[c] for c in ALPHABET)
print(plain_str)

# Descriptografa o texto *original* (com espaços e pontuação)
# usando a melhor chave encontrada.
# .get(c, c) passa caracteres desconhecidos (como ' ') sem alterá-los.
final_text = "".join(best_key.get(c.upper(), c) for c in original_text)
print("\n--- Texto Descriptografado ---")
print(final_text)
with open("resposta_final.txt", "w", encoding="utf-8") as f:
    f.write(final_text)
print("Arquivo salvo como: resposta_final.txt")