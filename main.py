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
from dataclasses import dataclass
import numpy as np


@dataclass
class Vaga:
    numero: int
    localizacao: tuple


@dataclass
class Morador:
    bloco: int
    apt: int
    vaga_ideal: Vaga
    vaga_alocada: Vaga


# criando as vagas disponiveis e suas localizações
# mapas das vagas por bloco
mapa_vagas_ideal = [
    [
        # BLOCO 1
        Vaga(20, (0, 19)),
    ],
    [
        # BLOCO 2
        Vaga(30, (0, 30)),
    ],
    [
        # BLOCO 3
        Vaga(30, (0, 30)),
    ],
    [
        # BLOCO 4
        Vaga(39, (0, 39)),
    ],
    [
        # BLOCO 5
        Vaga(39, (0, 39)),
    ],
    [
        # BLOCO 6
        Vaga(48, (0, 48)),
    ],
    [
        # BLOCO 7
        Vaga(48, (0, 48)),
    ],
    [
        # BLOCO 8
        Vaga(148, (3, 48)),
    ],
    [
        # BLOCO 9
        Vaga(157, (3, 39)),
    ],
    [
        # BLOCO 10
        Vaga(166, (3, 30)),
    ],
    [
        # BLOCO 11
        Vaga(175, (3, 21)),
    ],
    [
        # BLOCO 12
        Vaga(184, (3, 8)),
    ],
    [
        # BLOCO 13
        Vaga(196, (7, 0)),
    ],
    [
        # BLOCO 14
        Vaga(179, (3, 17)),
    ],
    [
        # BLOCO 15
        Vaga(179, (3, 17)),
    ],
    [
        # BLOCO 16
        Vaga(162, (3, 34)),
    ],
    [
        # BLOCO 17
        Vaga(162, (3, 34)),
    ],
]


def gerar_vaga_por_intervalo_positiva(
    numero_vaga_inicial,
    numero_vaga_final,
    coluna,
) -> List[Vaga]:
    vagas_disponiveis: List[Vaga] = []
    if numero_vaga_inicial > numero_vaga_final:
        offset = [o for o in range(numero_vaga_inicial - numero_vaga_final + 1)]
        for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final - 2, -1)):
            vagas_disponiveis.append(Vaga(vaga[1], (coluna, vaga[0])))
    else:
        offset = [o for o in range(numero_vaga_final - numero_vaga_inicial + 1)]
        for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final + 1)):
            vagas_disponiveis.append(Vaga(vaga[1], (coluna, vaga[0])))
    return vagas_disponiveis


def gerar_vaga_por_intervalo_coluna_negativa(
    numero_vaga_inicial,
    numero_vaga_final,
    coluna,
) -> List[Vaga]:
    vagas_disponiveis: List[Vaga] = []
    if numero_vaga_inicial > numero_vaga_final:
        offset = [o + 1 for o in range(numero_vaga_inicial - numero_vaga_final + 1)]
        for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final - 2, -1)):
            vagas_disponiveis.append(Vaga(vaga[1], (coluna, -vaga[0])))
    else:
        offset = [o + 1 for o in range(numero_vaga_final - numero_vaga_inicial + 1)]
        for vaga in zip(offset, range(numero_vaga_inicial, numero_vaga_final + 1)):
            vagas_disponiveis.append(Vaga(vaga[1], (coluna, -vaga[0])))
    return vagas_disponiveis


def gerar_vaga_por_intervalo_linha(
    numero_vaga_inicial, numero_vaga_final, linha_fixa, coluna_incial=0
):
    vagas_disponiveis: List[Vaga] = []
    for vaga in enumerate(
        range(numero_vaga_inicial, numero_vaga_final + 1), start=coluna_incial
    ):
        vagas_disponiveis.append(Vaga(vaga[1], (vaga[0], linha_fixa)))
    print(vagas_disponiveis)
    return vagas_disponiveis


def main():
    total_vagas = 256
    vagas_ocupadas: List[int] = []
    moradores: List[Morador] = []
    # gerando todas as vagas disponiveis]
    vagas_disponiveis: List[Vaga] = []
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_positiva(1, 49, 0))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_positiva(98, 50, 4))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_positiva(99, 147, 6))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_positiva(148, 189, 10))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_coluna_negativa(203, 211, 10))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_coluna_negativa(223, 212, 14))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_coluna_negativa(224, 236, 16))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_coluna_negativa(248, 237, 20))
    vagas_disponiveis.extend(gerar_vaga_por_intervalo_coluna_negativa(249, 256, 22))
    vagas_disponiveis.extend(
        gerar_vaga_por_intervalo_linha(190, 202, 0, coluna_incial=8)
    )
    print(len(vagas_disponiveis))
    vaga = filter(lambda v: v.numero == 256, vagas_disponiveis)
    print(list(vaga))
    exit()
    # definindo os moradores e suas vagas ideais
    for bloco in range(0, 7):
        for apt in range(1, 15):
            moradores.append(
                Morador(
                    bloco,
                    apt,
                    vaga_ideal=mapa_vagas_ideal[bloco],
                    vaga_alocada=Vaga(0, (0, 0)),
                )
            )
    print("moradores blocos 1 a 7: ", moradores)
    # alocando moradores dos blocos 7 apartamentos por 2 andares
    for bloco in range(1, 8):
        for a in range(1, 15):
            numero_vaga = np.random.choice(total_vagas, size=1, replace=False)
            while numero_vaga in vagas_ocupadas:
                numero_vaga = np.random.choice(total_vagas, size=1, replace=False)
            vagas_ocupadas.append(numero_vaga)
            moradores.append(Morador(bloco, a, (0, 0), Vaga(numero_vaga, (0, 49))))
    # alocando moradores dos blocos 4 apartamentos por 4 andares
    for bloco in range(8, 17):
        for a in range(1, 16):
            numero_vaga = np.random.choice(total_vagas, size=1, replace=False)
            while numero_vaga in vagas_ocupadas:
                numero_vaga = np.random.choice(total_vagas, size=1, replace=False)
            vagas_ocupadas.append(numero_vaga)
            moradores.append(Morador(bloco, a, (1, 1), Vaga(numero_vaga, (1, 1))))

    print(moradores)


def passos_ate_vaga(morador: Morador, vaga: Vaga):
    passos = 3
    return passos


if __name__ == "__main__":
    main()
