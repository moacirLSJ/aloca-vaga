from typing import List
from entidades.morador import Morador
from entidades.vaga import Vaga
import numpy as np


class MoradorVagaFactory:
    def __init__(self):
        pass

    def gerar_alocacao(self, vagas_disponiveis: List[Vaga]) -> List[Morador]:
        moradores: List[Morador] = []
        vagas_embaralhadas = vagas_disponiveis[:]
        np.random.shuffle(vagas_embaralhadas)
        Vaga.vagas = vagas_disponiveis
        for bloco in range(1, 8):
            for a in range(1, 15):
                numero_vaga = vagas_embaralhadas.pop()
                moradores.append(
                    Morador.criar_morador(a, bloco, vaga_alocada=numero_vaga)
                )
        # alocando moradores dos blocos 4 apartamentos por 4 andares
        for bloco in range(8, 18):
            for a in range(1, 17):
                numero_vaga = vagas_embaralhadas.pop()
                moradores.append(
                    Morador.criar_morador(a, bloco, vaga_alocada=numero_vaga)
                )
        return moradores
