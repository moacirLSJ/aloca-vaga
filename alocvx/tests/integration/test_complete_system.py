"""
Integration tests for the alocvx parking allocation system.
"""

import pytest
from fabricas.gerar_vaga import GerarVagaFactory
from fabricas.morador_vaga import MoradorVagaFactory
from entidades.vaga import Vaga
from entidades.morador import Morador


class TestParkingAllocationIntegration:
    """Integration tests for the complete parking allocation system."""

    def setup_method(self):
        """Setup test data before each test."""
        # Don't clear Vaga.vagas here - let tests manage it themselves
        self.vaga_factory = GerarVagaFactory()
        self.morador_factory = MoradorVagaFactory()

    def test_complete_allocation_workflow(self):
        """Test complete workflow from vaga generation to morador allocation."""
        # Step 1: Generate all vagas
        print(f"DEBUG: Factory instance: {self.vaga_factory}")
        print(f"DEBUG: Factory class: {type(self.vaga_factory)}")
        vagas = self.vaga_factory.gerar_todas_vagas()
        print(f"DEBUG: Generated {len(vagas)} vagas")

        # Store vagas count before modifying class variable
        vagas_count = len(vagas)
        print(f"DEBUG: About to add {vagas_count} vagas to class variable")

        # Store a copy to see if something modifies it
        vagas_backup = vagas[:]
        print(f"DEBUG: Backup has {len(vagas_backup)} items")

        # Add generated vagas to class variable for lookup operations
        Vaga.vagas.extend(vagas)
        print(f"DEBUG: After extending, local vagas still has {len(vagas)} items")
        print(f"DEBUG: Backup still has {len(vagas_backup)} items")

        # Check the assertion variable immediately
        print(f"DEBUG: About to assert, vagas has {len(vagas)} items")

        # Step 2: Setup ideal vagas for moradores
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(2000 + bloco, localizacao_ideal)  # Use int for numero
            Vaga.vagas.append(vaga_ideal)

        # Step 3: Allocate moradores
        moradores = self.morador_factory.gerar_alocacao(vagas)

        # Verify complete workflow
        assert len(vagas) > 0
        assert len(moradores) == (7 * 14) + (10 * 16)  # Total expected moradores
        assert all(isinstance(m, Morador) for m in moradores)

    def test_vaga_generation_and_allocation_consistency(self):
        """Test that generated vagas are properly allocated to moradores."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(3000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)
        allocated_vaga_numbers = {m.vaga_alocada.numero for m in moradores}
        original_vaga_numbers = {v.numero for v in vagas}

        # All allocated vaga numbers should be from the original set
        assert allocated_vaga_numbers.issubset(original_vaga_numbers)

    def test_morador_ideal_vaga_lookup(self):
        """Test that moradores can find their ideal vagas correctly."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas with real numbers
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(4000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)

        # Test that each morador's ideal vaga can be found
        for morador in moradores[:5]:  # Test first 5 for efficiency
            ideal_location = Morador.MAPA_VAGAS_IDEAL[morador.bloco - 1][0]
            ideal_vaga_result = Vaga.obter_vaga_pela_localizacao(ideal_location)

            assert ideal_vaga_result["ok"] is True
            assert ideal_vaga_result["data"]["vaga"].localizacao == ideal_location

    def test_distance_calculation_integration(self):
        """Test distance calculation between allocated and ideal vagas."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas with real numbers
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(5000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)

        # Calculate distances for a sample of moradores
        for morador in moradores[:5]:  # Test first 5 for efficiency
            ideal_location = Morador.MAPA_VAGAS_IDEAL[morador.bloco - 1][0]
            ideal_vaga_result = Vaga.obter_vaga_pela_localizacao(ideal_location)

            if ideal_vaga_result["ok"]:
                ideal_vaga = ideal_vaga_result["data"]["vaga"]
                distance_result = Vaga.calcular_distancia(
                    morador.vaga_alocada, ideal_vaga
                )

                assert distance_result["ok"] is True
                assert distance_result["data"]["distancia"] >= 0

    def test_bloco_distribution_in_allocation(self):
        """Test that moradores are properly distributed across blocos."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(6000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)

        # Count moradores per bloco
        bloco_counts = {}
        for morador in moradores:
            bloco_counts[morador.bloco] = bloco_counts.get(morador.bloco, 0) + 1

        # Verify expected distribution
        for bloco in range(1, 8):
            assert bloco_counts[bloco] == 14, f"Bloco {bloco} should have 14 moradores"

        for bloco in range(8, 18):
            assert bloco_counts[bloco] == 16, f"Bloco {bloco} should have 16 moradores"

    def test_vaga_number_uniqueness_across_system(self):
        """Test that all vaga numbers remain unique across the system."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas with unique numbers
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(7000 + bloco, localizacao_ideal)  # High unique numbers
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)

        # Collect all vaga numbers in the system
        all_vaga_numbers = set()
        all_vaga_numbers.update(v.numero for v in vagas)
        all_vaga_numbers.update(v.numero for v in Vaga.vagas)
        all_vaga_numbers.update(m.vaga_alocada.numero for m in moradores)

        # Verify uniqueness
        expected_total = (
            len(vagas) + len(Vaga.vagas) - len(vagas)
        )  # vagas are in Vaga.vagas too
        assert len(all_vaga_numbers) == expected_total

    def test_system_with_minimum_vagas(self):
        """Test system behavior with minimum required vagas."""
        needed_vagas = (7 * 14) + (10 * 16)

        # Create exactly enough vagas
        vagas = [Vaga(i, (i % 20, i // 20)) for i in range(needed_vagas)]
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(8000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.morador_factory.gerar_alocacao(vagas)

        # System should work with exact number of vagas
        assert len(moradores) == needed_vagas
        assert len(vagas) == 0  # All vagas used

    def test_error_handling_integration(self):
        """Test error handling across the integrated system."""
        # Test with insufficient vagas
        vagas = [Vaga(i, (i, i)) for i in range(50)]  # Too few vagas
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(9000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        # Should handle error gracefully
        with pytest.raises(IndexError):
            self.morador_factory.gerar_alocacao(vagas)

    def test_vaga_location_patterns(self):
        """Test that vaga locations follow expected patterns."""
        vagas = self.vaga_factory.gerar_todas_vagas()

        # Analyze location patterns
        locations = [v.localizacao for v in vagas]
        colunas = {loc[0] for loc in locations}
        linhas = {loc[1] for loc in locations}

        # Should have expected column patterns
        assert 0 in colunas  # First column
        assert any(c > 0 for c in colunas)  # Positive columns
        # Note: negative values are in lines (second coordinate), not columns

        # Should have both positive and negative line values
        assert any(l >= 0 for l in linhas)  # Positive lines
        assert any(l < 0 for l in linhas)  # Negative lines

    def test_morador_creation_with_real_vaga_data(self):
        """Test morador creation using real vaga data from factory."""
        vagas = self.vaga_factory.gerar_todas_vagas()
        Vaga.vagas.extend(vagas)

        # Setup ideal vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(10000 + bloco, localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        # Create moradores using real vaga data
        test_vaga = vagas[0]
        morador = Morador.criar_morador(101, 1, test_vaga)

        assert morador.bloco == 1
        assert morador.apt == 101
        assert morador.vaga_alocada == test_vaga
