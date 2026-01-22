from dataclasses import dataclass
from .vaga import Vaga


@dataclass
class Morador:
    bloco: int
    apt: int
    vaga_ideal: Vaga
    vaga_alocada: Vaga
    MAPA_VAGAS_IDEAL = [
        [
            # BLOCO 1
            20,
        ],
        [
            # BLOCO 2
            31,
        ],
        [
            # BLOCO 3
            31,
        ],
        [
            # BLOCO 4
            39,
        ],
        [
            # BLOCO 5
            39,
        ],
        [
            # BLOCO 6
            49,
        ],
        [
            # BLOCO 7
            49,
        ],
        [
            # BLOCO 8
            149,
        ],
        [
            # BLOCO 9
            158,
        ],
        [
            # BLOCO 10
            167,
        ],
        [
            # BLOCO 11
            176,
        ],
        [
            # BLOCO 12
            185,
        ],
        [
            # BLOCO 13
            195,
        ],
        [
            # BLOCO 14
            172,
        ],
        [
            # BLOCO 15
            172,
        ],
        [
            # BLOCO 16
            163,
        ],
        [
            # BLOCO 17
            163,
        ],
    ]

    @staticmethod
    def obter_detalhes_morador(
        bloco: int, apt: int, moradores: list["Morador"]
    ) -> dict:
        morador = next(
            filter(lambda m: m.bloco == bloco and m.apt == apt, moradores), None
        )
        if morador is None:
            return {
                "ok": False,
                "message": "Morador não encontrado",
                "data": None,
            }
        return {"ok": True, "message": "Morador encontrado", "data": morador}

    @staticmethod
    def criar_morador(apartamento: int, bloco: int, vaga_alocada: Vaga):
        localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
        resultado = Vaga.obter_vaga_pelo_numero(localizacao_ideal)
        if resultado["ok"] is False:
            return resultado
        vaga_ideal = resultado["data"]["vaga"]
        return Morador(
            bloco,
            apartamento,
            vaga_ideal=vaga_ideal,
            vaga_alocada=vaga_alocada,
        )

    @staticmethod
    def calcular_passos_moradores(moradores: list["Morador"]) -> int:
        total_passos = 0
        for morador in moradores:
            resultado = morador.calcular_distancia_passos()
            if resultado["ok"]:
                total_passos += resultado["data"]
        return total_passos

    def calcular_distancia_passos(self):
        try:
            pos_ideal = self.vaga_ideal.localizacao
            pos_alocada = self.vaga_alocada.localizacao

            distancia_colunas = abs(pos_ideal[1] - pos_alocada[1])
            distancia_linhas = abs(pos_ideal[0] - pos_alocada[0])

            total_passos = distancia_colunas + distancia_linhas

            return {
                "ok": True,
                "mensagem": "Distância calculada com sucesso",
                "data": total_passos,
            }
        except Exception as e:
            return {
                "ok": False,
                "mensagem": f"Erro ao calcular distância: {str(e)}",
                "data": None,
            }

    def __repr__(self) -> str:
        return f"Morador(bl={self.bloco}, apt={self.apt}, vi={self.vaga_ideal}, va={self.vaga_alocada} passos={self.calcular_distancia_passos()['data']})"
