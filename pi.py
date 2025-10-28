# testar_pontuacao.py

# 1. Importe a classe do arquivo ngram_score.py
from ngram_score import ngram_score

with open('saidatrue.txt', 'r', encoding='utf-8') as f:
    meu_texto = f.read()

fitness = ngram_score('english_quadgrams.txt')

# 5. Chame o método .score() no seu texto limpo
pontuacao = fitness.score(meu_texto)

print(f"--- Texto Original (limpo) ---")
print(meu_texto[:200] + "...")
print("\n--------------------------------")
print(f"Pontuação de 'Fitness' do texto: {pontuacao}")