from alocvx.entidades.morador import Morador
from alocvx.utilidades.progressbar import progress_bar
from alocvx.engrenagens.troca_vaga_contrato import TrocaVagaEngrenagem


class FullScanEngrenagem(TrocaVagaEngrenagem):
    def __init__(self, moradores: list["Morador"]):
        self.moradores = moradores

    def otimizar_alocacao(self) -> list["Morador"]:
        # implementar a lógica de troca de vagas entre moradores
        # para minimizar a soma total dos passos
        # estratégia simples: tentar trocar vagas entre pares de moradores todos com todos
        melhor_moradores = self.moradores[:]
        melhor_passos = Morador.calcular_passos_moradores(melhor_moradores)
        melhor_encontrado = True

        while melhor_encontrado:
            melhor_encontrado = False
            for i in range(len(melhor_moradores)):
                for j in range(i + 1, len(melhor_moradores)):
                    progress_bar(
                        i * len(melhor_moradores) + j,
                        len(melhor_moradores) * len(melhor_moradores),
                    )
                    morador1 = melhor_moradores[i]
                    morador2 = melhor_moradores[j]

                    # Trocar as vagas alocadas
                    morador1.vaga_alocada, morador2.vaga_alocada = (
                        morador2.vaga_alocada,
                        morador1.vaga_alocada,
                    )

                    novos_passos = Morador.calcular_passos_moradores(melhor_moradores)

                    if novos_passos < melhor_passos:
                        melhor_passos = novos_passos
                        melhor_encontrado = True
                    else:
                        # Reverter a troca se não melhorar
                        morador1.vaga_alocada, morador2.vaga_alocada = (
                            morador2.vaga_alocada,
                            morador1.vaga_alocada,
                        )
        return melhor_moradores
