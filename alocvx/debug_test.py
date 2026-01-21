"""
Simple integration test to debug factory issues.
"""

from fabricas.gerar_vaga import GerarVagaFactory
from fabricas.morador_vaga import MoradorVagaFactory
from entidades.vaga import Vaga
from entidades.morador import Morador


def test_simple_workflow():
    """Simple test to debug factory workflow."""
    Vaga.vagas.clear()

    # Step 1: Generate all vagas
    vaga_factory = GerarVagaFactory()
    morador_factory = MoradorVagaFactory()

    vagas = vaga_factory.gerar_todas_vagas()
    print(f"Step 1: Generated {len(vagas)} vagas")

    # Step 2: Add generated vagas to class variable
    Vaga.vagas.extend(vagas)
    print(f"Step 2: Class variable now has {len(Vaga.vagas)} vagas")

    # Step 3: Setup ideal vagas
    for bloco in range(1, 18):
        localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
        vaga_ideal = Vaga(2000 + bloco, localizacao_ideal)
        Vaga.vagas.append(vaga_ideal)

    print(f"Step 3: After adding ideal vagas, class has {len(Vaga.vagas)} vagas")

    # Step 4: Try allocation
    try:
        moradores = morador_factory.gerar_alocacao(vagas)
        print(f"Step 4: Created {len(moradores)} moradores")
        return True
    except Exception as e:
        print(f"Step 4: Error in allocation: {e}")
        return False


if __name__ == "__main__":
    success = test_simple_workflow()
    print(f"Test {'PASSED' if success else 'FAILED'}")
