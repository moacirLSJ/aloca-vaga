from dataclasses import dataclass
from entidades.vaga import Vaga


@dataclass
class Morador:
    bloco: int
    apt: int
    vaga_ideal: Vaga
    vaga_alocada: Vaga
    MAPA_VAGAS_IDEAL = [
        [
            # BLOCO 1
            (0, 19),
        ],
        [
            # BLOCO 2
            (0, 30),
        ],
        [
            # BLOCO 3
            (0, 30),
        ],
        [
            # BLOCO 4
            (0, 39),
        ],
        [
            # BLOCO 5
            (0, 39),
        ],
        [
            # BLOCO 6
            (0, 48),
        ],
        [
            # BLOCO 7
            (0, 48),
        ],
        [
            # BLOCO 8
            (10, 48),
        ],
        [
            # BLOCO 9
            (10, 39),
        ],
        [
            # BLOCO 10
            (10, 30),
        ],
        [
            # BLOCO 11
            (10, 21),
        ],
        [
            # BLOCO 12
            (10, 8),
        ],
        [
            # BLOCO 13
            (10, 0),
        ],
        [
            # BLOCO 14
            (10, 28),
        ],
        [
            # BLOCO 15
            (10, 28),
        ],
        [
            # BLOCO 16
            (10, 34),
        ],
        [
            # BLOCO 17
            (10, 34),
        ],
    ]

    @staticmethod
    def criar_morador(apartamento: int, bloco: int, vaga_alocada: Vaga):
        localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
        resultado = Vaga.obter_vaga_pela_localizacao(localizacao_ideal)
        if resultado['ok'] is False:
            return resultado
        vaga_ideal = resultado['data']['vaga']
        return Morador(
            bloco,
            apartamento,
            vaga_ideal=vaga_ideal,
            vaga_alocada=vaga_alocada,
        )
    def calcular_passo
 