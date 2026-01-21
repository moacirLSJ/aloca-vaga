"""
Unit tests for MoradorVagaFactory.
"""

import pytest
from unittest.mock import patch, MagicMock
from fabricas.morador_vaga import MoradorVagaFactory
from entidades.morador import Morador
from entidades.vaga import Vaga


class TestMoradorVagaFactory:
    """Test MoradorVagaFactory functionality."""

    def setup_method(self):
        """Setup test data before each test."""
        self.factory = MoradorVagaFactory()
        Vaga.vagas.clear()

    def test_factory_initialization(self):
        """Test factory initialization."""
        factory = MoradorVagaFactory()
        assert factory is not None

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_calls_shuffle(self, mock_shuffle):
        """Test that gerar_alocacao calls numpy.random.shuffle."""
        vagas = [Vaga(i, (i, i)) for i in range(300)]

        self.factory.gerar_alocacao(vagas)

        mock_shuffle.assert_called_once_with(vagas)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_returns_moradores_list(self, mock_shuffle):
        """Test that gerar_alocacao returns a list of Morador objects."""
        # Create enough vagas for all moradores
        vagas = [Vaga(i, (i, i)) for i in range(300)]

        # Setup Vaga.vagas for Morador.criar_morador
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        assert isinstance(moradores, list)
        assert len(moradores) > 0
        for morador in moradores:
            assert isinstance(morador, Morador)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_1_to_7_apartamentos(self, mock_shuffle):
        """Test allocation for blocos 1-7 with 14 apartamentos each."""
        vagas = [Vaga(i, (i, i)) for i in range(200)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        # Count moradores for blocos 1-7
        bloco_1_to_7_count = sum(1 for m in moradores if 1 <= m.bloco <= 7)
        expected_count = 7 * 14  # 7 blocos * 14 apartamentos

        assert bloco_1_to_7_count == expected_count

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_8_to_17_apartamentos(self, mock_shuffle):
        """Test allocation for blocos 8-17 with 16 apartamentos each."""
        vagas = [Vaga(i, (i, i)) for i in range(300)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        # Count moradores for blocos 8-17
        bloco_8_to_17_count = sum(1 for m in moradores if 8 <= m.bloco <= 17)
        expected_count = 10 * 16  # 10 blocos * 16 apartamentos

        assert bloco_8_to_17_count == expected_count

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_total_moradores(self, mock_shuffle):
        """Test total number of moradores created."""
        vagas = [Vaga(i, (i, i)) for i in range(300)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        expected_total = (7 * 14) + (10 * 16)  # blocos 1-7 + blocos 8-17
        assert len(moradores) == expected_total

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_1_range(self, mock_shuffle):
        """Test that bloco 1 moradores have correct apartamento range."""
        vagas = [Vaga(i, (i, i)) for i in range(200)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        bloco_1_moradores = [m for m in moradores if m.bloco == 1]
        apartamentos = [m.apt for m in bloco_1_moradores]

        assert len(apartamentos) == 14
        assert all(1 <= apt <= 14 for apt in apartamentos)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_7_range(self, mock_shuffle):
        """Test that bloco 7 moradores have correct apartamento range."""
        vagas = [Vaga(i, (i, i)) for i in range(200)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        bloco_7_moradores = [m for m in moradores if m.bloco == 7]
        apartamentos = [m.apt for m in bloco_7_moradores]

        assert len(apartamentos) == 14
        assert all(1 <= apt <= 14 for apt in apartamentos)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_8_range(self, mock_shuffle):
        """Test that bloco 8 moradores have correct apartamento range."""
        vagas = [Vaga(i, (i, i)) for i in range(200)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        bloco_8_moradores = [m for m in moradores if m.bloco == 8]
        apartamentos = [m.apt for m in bloco_8_moradores]

        assert len(apartamentos) == 16
        assert all(1 <= apt <= 16 for apt in apartamentos)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_bloco_17_range(self, mock_shuffle):
        """Test that bloco 17 moradores have correct apartamento range."""
        vagas = [Vaga(i, (i, i)) for i in range(200)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        bloco_17_moradores = [m for m in moradores if m.bloco == 17]
        apartamentos = [m.apt for m in bloco_17_moradores]

        assert len(apartamentos) == 16
        assert all(1 <= apt <= 16 for apt in apartamentos)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_uses_vagas_disponiveis(self, mock_shuffle):
        """Test that allocated vagas come from vagas_disponiveis list."""
        vagas = [Vaga(i, (i, i)) for i in range(300)]
        original_vaga_ids = [id(v) for v in vagas]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        allocated_vaga_ids = [id(m.vaga_alocada) for m in moradores]

        # All allocated vagas should be from the original list
        for allocated_id in allocated_vaga_ids:
            assert allocated_id in original_vaga_ids

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_insufficient_vagas(self, mock_shuffle):
        """Test behavior when insufficient vagas are provided."""
        vagas = [Vaga(i, (i, i)) for i in range(50)]  # Not enough vagas

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        # This should raise an IndexError when trying to pop from empty list
        with pytest.raises(IndexError):
            self.factory.gerar_alocacao(vagas)

    @patch("numpy.random.shuffle")
    def test_gerar_alocacao_exact_vagas_needed(self, mock_shuffle):
        """Test behavior with exact number of vagas needed."""
        needed_vagas = (7 * 14) + (10 * 16)  # Total moradores needed
        vagas = [Vaga(i, (i, i)) for i in range(needed_vagas)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        assert len(moradores) == needed_vagas
        assert len(vagas) == 0  # All vagas should be used

    def test_gerar_alocacao_without_mock(self):
        """Test gerar_alocacao without mocking numpy (integration test style)."""
        # Create enough vagas
        vagas = [Vaga(i, (i, i)) for i in range(300)]

        # Setup Vaga.vagas
        for bloco in range(1, 18):
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

        moradores = self.factory.gerar_alocacao(vagas)

        # Just verify it works and returns correct structure
        assert isinstance(moradores, list)
        assert len(moradores) == (7 * 14) + (10 * 16)
        assert all(isinstance(m, Morador) for m in moradores)
