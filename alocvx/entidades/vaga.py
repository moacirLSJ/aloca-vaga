from dataclasses import dataclass
from typing import List, ClassVar


@dataclass
class Vaga:
    numero: int
    localizacao: tuple
    vagas: ClassVar[List["Vaga"]] = []

    @staticmethod
    def obter_vaga_pelo_numero(numero: int) -> dict:
        for vaga in Vaga.vagas:
            if vaga.numero == numero:
                return {
                    "ok": True,
                    "message": "Vaga encontrada",
                    "data": {"vaga": vaga},
                }
        return {"ok": False, "message": "Vaga não encontrada"}

    @classmethod
    def obter_vaga_pela_localizacao(cls,localizacao: tuple) -> dict:
        for vaga in Vaga.vagas:
            if vaga.localizacao == localizacao:
                return {
                    "ok": True,
                    "message": "Vaga encontrada",
                    "data": {"vaga": vaga},
                }
        return {"ok": False, "message": "Vaga não encontrada pela localização"}

    @staticmethod
    def calcular_distancia(vaga1: "Vaga", vaga2: "Vaga") -> dict:
        return {
            "ok": True,
            "message": "Distância calculada",
            "data": {
                "distancia": abs(vaga1.localizacao[0] - vaga2.localizacao[0])
                + abs(vaga1.localizacao[1] - vaga2.localizacao[1])
            },
        }
