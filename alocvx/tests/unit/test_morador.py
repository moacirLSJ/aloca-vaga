"""
Unit tests for Morador entity.
"""

import pytest
from entidades.morador import Morador
from entidades.vaga import Vaga


class TestMorador:
    """Test Morador entity functionality."""

    def setup_method(self):
        """Setup test data before each test."""
        # Clear Vaga.vagas for clean testing
        Vaga.vagas.clear()

        # Add test vagas
        self.vaga1 = Vaga(1, (0, 0))
        self.vaga2 = Vaga(2, (1, 1))
        Vaga.vagas.extend([self.vaga1, self.vaga2])

    def test_morador_creation(self):
        """Test Morador object creation."""
        morador = Morador(
            bloco=1, apt=101, vaga_ideal=self.vaga1, vaga_alocada=self.vaga2
        )

        assert morador.bloco == 1
        assert morador.apt == 101
        assert morador.vaga_ideal == self.vaga1
        assert morador.vaga_alocada == self.vaga2

    def test_mapa_vagas_ideal_structure(self):
        """Test MAPA_VAGAS_IDEAL structure."""
        mapa = Morador.MAPA_VAGAS_IDEAL

        assert len(mapa) == 17  # 17 blocos
        assert len(mapa[0]) == 1  # Bloco 1 has 1 tuple
        assert mapa[0][0] == (0, 19)  # Bloco 1 range

    def test_mapa_vagas_ideal_bloco_1(self):
        """Test MAPA_VAGAS_IDEAL for bloco 1."""
        mapa = Morador.MAPA_VAGAS_IDEAL
        assert mapa[0][0] == (0, 19)

    def test_mapa_vagas_ideal_bloco_2(self):
        """Test MAPA_VAGAS_IDEAL for bloco 2."""
        mapa = Morador.MAPA_VAGAS_IDEAL
        assert mapa[1][0] == (0, 30)

    def test_mapa_vagas_ideal_bloco_8(self):
        """Test MAPA_VAGAS_IDEAL for bloco 8 (different pattern)."""
        mapa = Morador.MAPA_VAGAS_IDEAL
        assert mapa[7][0] == (10, 48)

    def test_mapa_vagas_ideal_bloco_17(self):
        """Test MAPA_VAGAS_IDEAL for bloco 17 (last bloco)."""
        mapa = Morador.MAPA_VAGAS_IDEAL
        assert mapa[16][0] == (10, 34)

    def test_criar_morador_success(self):
        """Test successful morador creation."""
        # Setup vaga for the location
        vaga_ideal = Vaga(100, (0, 10))  # Within bloco 1 range
        Vaga.vagas.append(vaga_ideal)

        morador = Morador.criar_morador(
            apartamento=101, bloco=1, vaga_alocada=self.vaga1
        )

        assert morador.bloco == 1
        assert morador.apt == 101
        assert morador.vaga_alocada == self.vaga1

    def test_criar_morador_bloco_2(self):
        """Test morador creation for bloco 2."""
        # Setup vaga for the location
        vaga_ideal = Vaga(200, (0, 15))  # Within bloco 2 range
        Vaga.vagas.append(vaga_ideal)

        morador = Morador.criar_morador(
            apartamento=201, bloco=2, vaga_alocada=self.vaga2
        )

        assert morador.bloco == 2
        assert morador.apt == 201
        assert morador.vaga_alocada == self.vaga2

    def test_criar_morador_bloco_8(self):
        """Test morador creation for bloco 8 (different range)."""
        # Setup vaga for the location
        vaga_ideal = Vaga(300, (10, 25))  # Within bloco 8 range
        Vaga.vagas.append(vaga_ideal)

        morador = Morador.criar_morador(
            apartamento=801, bloco=8, vaga_alocada=self.vaga1
        )

        assert morador.bloco == 8
        assert morador.apt == 801

    def test_criar_morador_all_blocos_coverage(self):
        """Test morador creation for all blocos to ensure coverage."""
        for bloco in range(1, 18):
            # Create a vaga for each bloco's ideal location
            localizacao_ideal = Morador.MAPA_VAGAS_IDEAL[bloco - 1][0]
            vaga_ideal = Vaga(f"ideal_{bloco}", localizacao_ideal)
            Vaga.vagas.append(vaga_ideal)

            vaga_alocada = Vaga(f"aloc_{bloco}", (bloco, bloco))
            Vaga.vagas.append(vaga_alocada)

            morador = Morador.criar_morador(
                apartamento=bloco * 100 + 1, bloco=bloco, vaga_alocada=vaga_alocada
            )

            assert morador.bloco == bloco
            assert morador.apt == bloco * 100 + 1

    def test_criar_morador_invalid_bloco_high(self):
        """Test morador creation with invalid bloco number (too high)."""
        with pytest.raises(IndexError):
            Morador.criar_morador(101, 99, self.vaga1)

    def test_criar_morador_invalid_bloco_low(self):
        """Test morador creation with invalid bloco number (too low)."""
        with pytest.raises(IndexError):
            Morador.criar_morador(101, 0, self.vaga1)

    def test_criar_morador_bloco_17_boundary(self):
        """Test morador creation for bloco 17 (boundary case)."""
        # Setup vaga for the location
        vaga_ideal = Vaga(400, (10, 20))  # Within bloco 17 range
        Vaga.vagas.append(vaga_ideal)

        morador = Morador.criar_morador(
            apartamento=1701, bloco=17, vaga_alocada=self.vaga1
        )

        assert morador.bloco == 17
        assert morador.apt == 1701
