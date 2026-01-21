from typing import List
from entidades.vaga import Vaga


class GerarVagaFactory:
    def __init__(self):
        pass

    def gerar_todas_vagas(self):
        vagas_disponiveis: List = []
        vagas_disponiveis.extend(self._gerar_vaga_por_intervalo_positiva(1, 49, 0))
        vagas_disponiveis.extend(self._gerar_vaga_por_intervalo_positiva(98, 50, 4))
        vagas_disponiveis.extend(self._gerar_vaga_por_intervalo_positiva(99, 147, 6))
        vagas_disponiveis.extend(self._gerar_vaga_por_intervalo_positiva(189, 148, 10))
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_coluna_negativa(203, 211, 10)
        )
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_coluna_negativa(223, 212, 14)
        )
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_coluna_negativa(224, 236, 16)
        )
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_coluna_negativa(248, 237, 20)
        )
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_coluna_negativa(249, 258, 22)
        )
        vagas_disponiveis.extend(
            self._gerar_vaga_por_intervalo_linha(190, 202, 0, coluna_incial=11)
        )
        return vagas_disponiveis

    def _gerar_vaga_por_intervalo_positiva(
        self,
        numero_vaga_inicial,
        numero_vaga_final,
        coluna,
    ) -> List[Vaga]:
        vagas_disponiveis: List[Vaga] = []
        if numero_vaga_inicial > numero_vaga_final:
            offset = [o for o in range(numero_vaga_inicial - numero_vaga_final + 1)]
            for vaga in zip(
                offset, range(numero_vaga_inicial, numero_vaga_final - 2, -1)
            ):
                vagas_disponiveis.append(Vaga(vaga[1], (coluna, vaga[0])))
        else:
            offset = [o for o in range(numero_vaga_final - numero_vaga_inicial + 1)]
            for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final + 1)):
                vagas_disponiveis.append(Vaga(vaga[1], (coluna, vaga[0])))
        return vagas_disponiveis

    def _gerar_vaga_por_intervalo_coluna_negativa(
        self,
        numero_vaga_inicial,
        numero_vaga_final,
        coluna,
    ) -> List[Vaga]:
        vagas_disponiveis: List[Vaga] = []
        if numero_vaga_inicial > numero_vaga_final:
            offset = [o + 1 for o in range(numero_vaga_inicial - numero_vaga_final + 1)]
            for vaga in zip(
                offset, range(numero_vaga_inicial, numero_vaga_final - 2, -1)
            ):
                vagas_disponiveis.append(Vaga(vaga[1], (coluna, -vaga[0])))
        else:
            offset = [o + 1 for o in range(numero_vaga_final - numero_vaga_inicial + 1)]
            for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final + 1)):
                vagas_disponiveis.append(Vaga(vaga[1], (coluna, -vaga[0])))
        return vagas_disponiveis

    def _gerar_vaga_por_intervalo_linha(
        self, numero_vaga_inicial, numero_vaga_final, linha_fixa, coluna_incial=0
    ):
        vagas_disponiveis: List[Vaga] = []
        for vaga in enumerate(
            range(numero_vaga_inicial, numero_vaga_final + 1), start=coluna_incial
        ):
            vagas_disponiveis.append(Vaga(vaga[1], (vaga[0], linha_fixa)))
        return vagas_disponiveis
