import pytest
from fabricas.gerar_vaga import GerarVagaFactory
from entidades.vaga import Vaga


def test_isolate_factory():
    """Isolate factory to see what's happening."""
    Vaga.vagas.clear()
    factory = GerarVagaFactory()
    vagas = factory.gerar_todas_vagas()

    print(f"Generated {len(vagas)} vagas")
    print(f"First vaga: {vagas[0] if vagas else 'No vagas'}")

    assert len(vagas) > 0
