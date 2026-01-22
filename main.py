"""
Esse sistema se destina a distribuição automática de vagas entre os moradores de um condominio.
A ordenção se da pela menor distancia percorrida para chegar a vaga.
regras para localização:
    a vaga ideal é a mais próxima possível do bloco do morador, na direção da portaria;
    a distancia entre as vagas adjacentes é de 1 passo;
    a distancia entre as vagas separadas por pavimento são 2 passos;
    O layout do estacionamento é um grid não-simetrico de 8 colunas e 49 linhas.
"""

from typing import List
from alocvx.fabricas.gera_troca_vaga import TrocaVagaEngrenagemFabrica
from alocvx.fabricas.gerar_vaga import GerarVagaFactory
from alocvx.entidades.vaga import Vaga
from alocvx.entidades.morador import Morador
from alocvx.fabricas.morador_vaga import MoradorVagaFactory
# criando as vagas disponiveis e suas localizações5
# mapas das vagas por bloco


def main():
    total_vagas = 258
    MAIOR_NUMERO_PASSOS_POR_APARTAMENTO = 80
    MENOR_NUMERO_PASSOS_POR_APARTAMENTO = 0
    TOTAL_MAXIMO_PASSOS = 7500
    TOTAL_MINIMO_PASSOS = 6100
    moradores: List[Morador] = []
    vagas_disponiveis = GerarVagaFactory().gerar_todas_vagas()
    Vaga.vagas = vagas_disponiveis
    vaga = list(filter(lambda v: v.numero == 30, vagas_disponiveis))[0]
    print('vaga encontrada:',vaga)
    for te in [1]:
        total_epocas = te
        moradores = MoradorVagaFactory().gerar_alocacao(vagas_disponiveis)
        for epoca in range(total_epocas):
            moradores = TrocaVagaEngrenagemFabrica.criar_troca_vaga('VizinhoMaisDistanteEngrenagem', moradores).otimizar_alocacao()
            print(f'total passos ao final: {Morador.calcular_passos_moradores(moradores)}')
    print( Morador.obter_detalhes_morador(7,5, moradores)['data'])
    print( Morador.obter_detalhes_morador(1,5, moradores)['data'])
    print( Morador.obter_detalhes_morador(8,3, moradores)['data'])
    print( Morador.obter_detalhes_morador(10,1, moradores)['data'])
    print( Morador.obter_detalhes_morador(12,16, moradores)['data'])
    print( Morador.obter_detalhes_morador(15,10, moradores)['data'])
    print( Morador.obter_detalhes_morador(17,1, moradores)['data'])
if __name__ == "__main__":
    main()
