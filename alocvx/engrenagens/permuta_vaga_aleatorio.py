from alocvx.engrenagens.troca_vaga_contrato import TrocaVagaEngrenagem
from typing import List
from alocvx.entidades.morador import Morador
import numpy as np


class PermutaVagaAleatorio(TrocaVagaEngrenagem):
    def __init__(self, moradores: List[Morador]):
        self.moradores = moradores[:]

    def otimizar_alocacao(self) -> List[Morador]:
        for contagem_troca in range(len(self.moradores) // 2):
            passos_morador1 = self.moradores[
                contagem_troca
            ].calcular_distancia_passos()["data"]
            passos_morador2 = self.moradores[
                np.random.randint(contagem_troca + 1, len(self.moradores))
            ].calcular_distancia_passos()["data"]
            print(f"passos morador 1: {passos_morador1}")
            print(f"passos morador 2: {passos_morador2}")
            probabilidade_troca = np.abs(passos_morador1 - passos_morador2) / 80
            print(f"probabilidade de troca: {probabilidade_troca}")
            if np.random.rand() < probabilidade_troca:
                (
                    self.moradores[contagem_troca].vaga_alocada,
                    self.moradores[
                        np.random.randint(contagem_troca + 1, len(self.moradores))
                    ].vaga_alocada,
                ) = (
                    self.moradores[
                        np.random.randint(contagem_troca + 1, len(self.moradores))
                    ].vaga_alocada,
                    self.moradores[contagem_troca].vaga_alocada,
                )
        return self.moradores

    def _sigmoid(self, x) -> float:
        return 1 / (1 + np.exp(-x))
