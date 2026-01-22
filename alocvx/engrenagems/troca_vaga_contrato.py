from alocvx.entidades.morador import Morador
from alocvx.utilidades.progressbar import progress_bar
from abc import ABC, abstractmethod
from typing import List


class TrocaVagaEngrenagem(ABC):
    @abstractmethod
    def __init__(self, moradores: List[Morador]):
        pass

    @abstractmethod
    def otimizar_alocacao(self) -> List[Morador]:
        pass
