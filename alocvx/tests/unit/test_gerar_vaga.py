"""
Unit tests for GerarVagaFactory.
"""

import pytest
from fabricas.gerar_vaga import GerarVagaFactory
from entidades.vaga import Vaga


class TestGerarVagaFactory:
    """Test GerarVagaFactory functionality."""

    def setup_method(self):
        """Setup test data before each test."""
        self.factory = GerarVagaFactory()
        Vaga.vagas.clear()

    def test_factory_initialization(self):
        """Test factory initialization."""
        factory = GerarVagaFactory()
        assert factory is not None

    def test_gerar_todas_vagas_returns_list(self):
        """Test that gerar_todas_vagas returns a list."""
        vagas = self.factory.gerar_todas_vagas()
        assert isinstance(vagas, list)
        assert len(vagas) > 0

    def test_gerar_todas_vagas_all_vaga_objects(self):
        """Test that all returned objects are Vaga instances."""
        vagas = self.factory.gerar_todas_vagas()
        for vaga in vagas:
            assert isinstance(vaga, Vaga)

    def test_gerar_todas_vagas_unique_numbers(self):
        """Test that all generated vagas have unique numbers."""
        vagas = self.factory.gerar_todas_vagas()
        numbers = [vaga.numero for vaga in vagas]
        assert len(numbers) == len(set(numbers))

    def test_gerar_vaga_por_intervalo_positiva_ascending(self):
        """Test positive interval generation with ascending numbers."""
        vagas = self.factory._gerar_vaga_por_intervalo_positiva(1, 5, 0)

        assert len(vagas) == 5
        assert vagas[0].numero == 1
        assert vagas[-1].numero == 5
        for vaga in vagas:
            assert vaga.localizacao[0] == 0  # coluna
            assert vaga.localizacao[1] >= 0  # offset (non-negative)

    def test_gerar_vaga_por_intervalo_positiva_descending(self):
        """Test positive interval generation with descending numbers."""
        vagas = self.factory._gerar_vaga_por_intervalo_positiva(5, 1, 2)

        assert len(vagas) == 5
        assert vagas[0].numero == 5
        assert vagas[-1].numero == 1
        for vaga in vagas:
            assert vaga.localizacao[0] == 2  # coluna
            assert vaga.localizacao[1] >= 0  # offset (non-negative)

    def test_gerar_vaga_por_intervalo_positiva_single_value(self):
        """Test positive interval generation with single value."""
        vagas = self.factory._gerar_vaga_por_intervalo_positiva(10, 10, 5)

        assert len(vagas) == 1
        assert vagas[0].numero == 10
        assert vagas[0].localizacao == (5, 0)

    def test_gerar_vaga_por_intervalo_coluna_negativa_ascending(self):
        """Test negative column interval generation with ascending numbers."""
        vagas = self.factory._gerar_vaga_por_intervalo_coluna_negativa(1, 3, 1)

        assert len(vagas) == 3
        assert vagas[0].numero == 1
        assert vagas[-1].numero == 3
        for vaga in vagas:
            assert vaga.localizacao[0] == 1  # coluna
            assert vaga.localizacao[1] <= 0  # offset (negative)

    def test_gerar_vaga_por_intervalo_coluna_negativa_descending(self):
        """Test negative column interval generation with descending numbers."""
        vagas = self.factory._gerar_vaga_por_intervalo_coluna_negativa(3, 1, 2)

        assert len(vagas) == 3
        assert vagas[0].numero == 3
        assert vagas[-1].numero == 1
        for vaga in vagas:
            assert vaga.localizacao[0] == 2  # coluna
            assert vaga.localizacao[1] <= 0  # offset (negative)

    def test_gerar_vaga_por_intervalo_coluna_negativa_single_value(self):
        """Test negative column interval generation with single value."""
        vagas = self.factory._gerar_vaga_por_intervalo_coluna_negativa(20, 20, 3)

        assert len(vagas) == 1
        assert vagas[0].numero == 20
        assert vagas[0].localizacao == (3, -1)

    def test_gerar_vaga_por_intervalo_linha_default(self):
        """Test line interval generation with default column start."""
        vagas = self.factory._gerar_vaga_por_intervalo_linha(10, 12, 5)

        assert len(vagas) == 3
        assert vagas[0].numero == 10
        assert vagas[-1].numero == 12
        for i, vaga in enumerate(vagas):
            assert vaga.localizacao[0] == i  # coluna (starts at 0)
            assert vaga.localizacao[1] == 5  # linha fixa

    def test_gerar_vaga_por_intervalo_linha_custom_column(self):
        """Test line interval generation with custom column start."""
        vagas = self.factory._gerar_vaga_por_intervalo_linha(15, 17, 8, coluna_incial=3)

        assert len(vagas) == 3
        assert vagas[0].numero == 15
        assert vagas[-1].numero == 17
        for i, vaga in enumerate(vagas):
            assert vaga.localizacao[0] == i + 3  # coluna (starts at 3)
            assert vaga.localizacao[1] == 8  # linha fixa

    def test_gerar_vaga_por_intervalo_linha_single_value(self):
        """Test line interval generation with single value."""
        vagas = self.factory._gerar_vaga_por_intervalo_linha(
            100, 100, 10, coluna_incial=5
        )

        assert len(vagas) == 1
        assert vagas[0].numero == 100
        assert vagas[0].localizacao == (5, 10)

    def test_gerar_todas_vagas_first_interval(self):
        """Test first interval in gerar_todas_vagas."""
        vagas = self.factory.gerar_todas_vagas()

        # First interval should be (1, 49, 0)
        first_interval_vagas = [
            v for v in vagas if 1 <= v.numero <= 49 and v.localizacao[0] == 0
        ]
        assert len(first_interval_vagas) == 49

    def test_gerar_todas_vagas_second_interval(self):
        """Test second interval in gerar_todas_vagas."""
        vagas = self.factory.gerar_todas_vagas()

        # Second interval should be (98, 50, 4) - descending
        second_interval_vagas = [
            v for v in vagas if 50 <= v.numero <= 98 and v.localizacao[0] == 4
        ]
        assert len(second_interval_vagas) == 49

    def test_gerar_todas_vagas_contains_specific_vaga(self):
        """Test that specific vaga exists in generated list."""
        vagas = self.factory.gerar_todas_vagas()

        # Check for vaga number 1 with location (0, 0)
        vaga_1 = next((v for v in vagas if v.numero == 1), None)
        assert vaga_1 is not None
        assert vaga_1.localizacao == (0, 0)

    def test_gerar_todas_vagas_contains_high_number_vaga(self):
        """Test that high number vaga exists in generated list."""
        vagas = self.factory.gerar_todas_vagas()

        # Check for a high number vaga
        high_vaga = next((v for v in vagas if v.numero >= 250), None)
        assert high_vaga is not None

    def test_offset_calculation_ascending_positive(self):
        """Test offset calculation for ascending positive interval."""
        vagas = self.factory._gerar_vaga_por_intervalo_positiva(1, 3, 0)

        expected_offsets = [0, 1, 2]
        actual_offsets = [v.localizacao[1] for v in vagas]

        assert actual_offsets == expected_offsets

    def test_offset_calculation_descending_positive(self):
        """Test offset calculation for descending positive interval."""
        vagas = self.factory._gerar_vaga_por_intervalo_positiva(3, 1, 0)

        expected_offsets = [0, 1, 2]
        actual_offsets = [v.localizacao[1] for v in vagas]

        assert actual_offsets == expected_offsets

    def test_offset_calculation_ascending_negative(self):
        """Test offset calculation for ascending negative interval."""
        vagas = self.factory._gerar_vaga_por_intervalo_coluna_negativa(1, 3, 0)

        expected_offsets = [-1, -2, -3]
        actual_offsets = [v.localizacao[1] for v in vagas]

        assert actual_offsets == expected_offsets

    def test_offset_calculation_descending_negative(self):
        """Test offset calculation for descending negative interval."""
        vagas = self.factory._gerar_vaga_por_intervalo_coluna_negativa(3, 1, 0)

        expected_offsets = [-1, -2, -3]
        actual_offsets = [v.localizacao[1] for v in vagas]

        assert actual_offsets == expected_offsets
