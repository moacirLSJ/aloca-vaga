from alocvx.engrenagems.troca_vaga_contrato import TrocaVagaEngrenagem
from alocvx.entidades.morador import Morador
from typing import List


class TrocaVagaEngrenagemFabrica:
    @staticmethod
    def criar_troca_vaga(tipo_engrenagem,moradores: List[Morador]) -> TrocaVagaEngrenagem:
        match tipo_engrenagem:
            case 'FullScanEngrenagem':
                classe = __import__('alocvx.engrenagems.full_scan', fromlist=[tipo_engrenagem]) 
                return classe.FullScanEngrenagem(moradores)
            case 'VizinhoMaisDistanteEngrenagem':
                classe = __import__('alocvx.engrenagems.vizinho_mais_distante', fromlist=[tipo_engrenagem]) 
                return classe.VizinhoMaisDistanteEngrenagem(moradores)
            case _:
                raise ValueError(f'Tipo de engrenagem desconhecido: {tipo_engrenagem}')
            