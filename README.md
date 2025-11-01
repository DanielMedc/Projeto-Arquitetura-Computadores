Esse Projeto tem duas partes
	
1. Binario --> ASCII
  1.0 enconded.txt : arquivo binário, fornecido pelo professor
  1.1 bi_to_ascii.py : recebe arquivo binario, devolve ASCII
   1.1.0 Recebe Binario , passa para inteiro , passa para ASCII
  1.2 saidatrue.txt : arquivo de texto devolvido
3. ASCII criptografado --> ASCII descriptografado
   3.0 english_quadgrams.txt : dicionário para o calculo de fitness, quanto menor valor negativo, melhor o fitness de uma certa palavra, ou seja ,
   mais "humana" == "descriptografada" o texto
   3.1 ngram_score.py : definição da função fitness, fornecido pelo professor
   3.4 resposta_final.txt : well, o texto final descriptografado
   3.2 Solver_True.py *

-- SOLVER --
Decifrador de Cifra de Substituição com Hill Climbing
Este projeto é um script em Python que decifra automaticamente um texto criptografado com uma cifra de substituição simples.

Ele utiliza um algoritmo de otimização chamado Hill Climbing (Subida de Encosta) combinado com análise de n-gramas (especificamente quadgramas) para avaliar a "qualidade" ou "fitness" de um texto decifrado.

A premissa é que um texto em inglês corretamente decifrado terá uma pontuação de fitness muito mais alta (baseada na frequência de quadgramas comuns como 'TION', 'THER', 'OUGH', etc.) do que um texto embaralhado.

🚀 Como Funciona
O algoritmo funciona de forma iterativa para "escalar" em direção à melhor solução possível (a chave de decriptação correta):

Inicialização: O script começa com uma chave de mapeamento inicial (A→A, B→B, C→C...) e calcula seu "fitness score" usando o texto cifrado. Este se torna o "pai".

Geração de "Filho": Em um loop, ele cria uma chave "filha" pegando a chave "pai" e trocando aleatoriamente o mapeamento de duas letras (ex: se A→Q e B→W, a chave filha pode ter A→W e B→Q).

Avaliação: O script decifra o texto com esta nova chave "filha" e calcula seu fitness score.

Seleção:

Se o score da "filha" for maior que o do "pai", a "filha" se torna o novo "pai". Isso indica que encontramos uma melhora, e o processo continua a partir desse novo ponto. Um contador de "paciência" é reiniciado.

Se o score da "filha" for menor, ela é descartada.

Convergência (Máximo Local): Se o script não conseguir encontrar uma chave "filha" melhor por um número definido de iterações (MAX_ITERATIONS = 1000), ele assume que encontrou a melhor solução que podia (um "máximo local") e para a execução.

Resultado: O script guarda e exibe a melhor chave (e o melhor score) encontrada durante todo o processo.

Bibliotecas Python
matplotlib
numpy
random
form math import log10

📊 Saída (Output)
Ao ser executado, o script produzirá o seguinte:

No Console
O script imprimirá no console a chave inicial e, em seguida, mostrará cada "NOVO RECORDE" de pontuação e a chave correspondente à medida que os encontra.

Ao final, ele exibirá:

A Melhor Chave Encontrada.

O número total de Chaves testadas (quantas vezes um recorde foi quebrado).

O número total de Decriptações realizadas.

O Texto Descriptografado completo.
