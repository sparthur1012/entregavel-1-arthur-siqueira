## Codigo para calcular viabilidade energetica da missão
## importando bibliotecas
import sys

## definindo Robo, suas caracteristicas e da sua missao
class Robo:
    ### definindo caracteristicas do Robo
    def __init__(self, bateria, tempo, consumo_p_min):
        self.bateria = bateria # porcentagem de energia da bateria (0 a 100)
        self.tempo = tempo # em minutos
        self.consumo_p_min = consumo_p_min # em porcentagem por minuto
       
    ### definindo metodos para calcular energia necessaria e restante
    def energia_necessaria(self):
        return self.tempo * self.consumo_p_min

    def energia_restante(self):
        return self.bateria - self.energia_necessaria()
    
    ### definindo metodo para calcular se a missao é viavel
    def missao_viavel(self):
        return self.energia_restante() >= 0

## definindo função para buscar informacoes do Robo
def buscar_informacoes():
    try:
        bateria = float(input("Digite a porcentagem da bateria do robô (0 a 100): "))
        tempo = float(input("Digite o tempo da missão em minutos: "))
        consumo_p_min = float(input("Digite o consumo de energia em porcentagem por minuto: "))
        
        if bateria < 0 or bateria > 100:
            raise ValueError("Valor invalido (bateria)")
        if tempo <= 0:
            raise ValueError("Valor invalido (tempo)")
        if consumo_p_min <= 0:
            raise ValueError("Valor invalido (consumo por minuto)")

        return Robo(bateria, tempo, consumo_p_min)
    
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

def entregar_informacoes(meuRobo):
    restante = meuRobo.energia_restante()
    if meuRobo.missao_viavel():
        print(f"Missão viável.")
        print(f" Bateria restante: {restante:.2f}%")
        print(f" Consumo total: {meuRobo.energia_necessaria():.2f}%.")
    else:
        faltam = -restante
        print(f"Missão inviável.")
        print(f" Consumo total: {meuRobo.energia_necessaria():.2f}%.")
        print(f" Faltam {faltam:.2f} pontos percentuais.")

def main():
    meuRobo = buscar_informacoes()
    entregar_informacoes(meuRobo)


if __name__ == "__main__":
    main()