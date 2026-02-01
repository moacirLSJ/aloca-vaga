from alocvx.entidades.morador import Morador
from alocvx.utilidades.progressbar import progress_bar
from alocvx.engrenagens.troca_vaga_contrato import TrocaVagaEngrenagem


class VizinhoMaisDistanteEngrenagem(TrocaVagaEngrenagem):
    def __init__(self, moradores: list["Morador"]):
        self.moradores = moradores

    def otimizar_alocacao(self) -> list["Morador"]:
        # implementar a lógica de troca de vagas entre moradores
        # para minimizar a soma total dos passos
        # estratégia simples: tentar trocar vagas entre o morador mais distante e os outros
        melhor_moradores = self.moradores[:]
        melhor_passos = Morador.calcular_passos_moradores(melhor_moradores)
        melhor_encontrado = True

        while melhor_encontrado:
            melhor_encontrado = False
            # encontrar o morador com o maior número de passos
            morador_mais_distante = max(
                melhor_moradores, key=lambda m: m.calcular_distancia_passos()["data"]
            )

            progress_bar(
                morador_mais_distante.apt * len(melhor_moradores),
                len(melhor_moradores) * len(melhor_moradores),
            )
            for morador in melhor_moradores:
                if morador == morador_mais_distante:
                    continue

                # trocar as vagas alocadas entre os dois moradores
                morador_mais_distante.vaga_alocada, morador.vaga_alocada = (
                    morador.vaga_alocada,
                    morador_mais_distante.vaga_alocada,
                )

                passos_atuais = Morador.calcular_passos_moradores(melhor_moradores)

                if passos_atuais < melhor_passos:
                    melhor_passos = passos_atuais
                    melhor_encontrado = True
                else:
                    # desfazer a troca se não melhorar
                    morador_mais_distante.vaga_alocada, morador.vaga_alocada = (
                        morador.vaga_alocada,
                        morador_mais_distante.vaga_alocada,
                    )

        return melhor_moradores
