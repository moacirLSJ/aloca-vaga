from typing import List
from alocvx.entidades.morador import Morador
from alocvx.entidades.vaga import Vaga
import numpy as np


class MoradorVagaFactory:
    def __init__(self):
        pass

    def gerar_alocacao(self, vagas_disponiveis: List[Vaga]) -> List[Morador]:
        moradores: List[Morador] = []
        np.random.shuffle(vagas_disponiveis)

        for bloco in range(1, 8):
            for a in range(1, 15):
                numero_vaga = vagas_disponiveis.pop()
                moradores.append(
                    Morador.criar_morador(a, bloco, vaga_alocada=numero_vaga)
                )
        # alocando moradores dos blocos 4 apartamentos por 4 andares
        for bloco in range(8, 18):
            for a in range(1, 17):
                numero_vaga = vagas_disponiveis.pop()
                moradores.append(
                    Morador.criar_morador(a, bloco, vaga_alocada=numero_vaga)
                )
        return moradores
