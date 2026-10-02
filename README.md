# Entregável 1 - Teste de Bateria para Robôs 🤖

O programa um programa para analise da viabilidade de bateria de um robô de acordo com os seguintes Critérios:

1. Bateria atual, em porcentagem.🔋
2. Tempo de missão, em Minutos.🕦
3. Consumo pro minuto, em percentuais da bateria.📊

## ESTRUTURA DO CÓDIGO 🧬

- Robo é uma classe com:
	- Energia: inteiro (varia entre 0-100).
	- Tempo de missão: inteiro (verificar se existem bibliotecas para tempo).
	- Consumo por minuto: float.
- CheckBat é uma função que verificar se o valor de bateria passado é plausível.
- CalcCons é uma função para calcular quanta bateria vai ser consumida na missão e se a bateria atual é suficiente.
- GetData é a função que vai solicitar os dados para o Robô.
- GiveData é a função que vai entregar os dados para o piloto.
- Main é a função principal, que servirá como base, interligando e organizando as demais funções do código.

## TO-DO ✅

- [x] Estruturar o programa.
- [x] Criar a classe Robo.
- [x] Criar funções específicas.
- [x] Criar função principal.
- [x] Testar funcionamento do programa.