"""
Unit tests for Vaga entity.
"""

import pytest
from entidades.vaga import Vaga


class TestVaga:
    """Test Vaga entity functionality."""

    def setup_method(self):
        """Setup test data before each test."""
        # Clear the class variable for clean testing
        Vaga.vagas.clear()

        # Add test vagas
        self.vaga1 = Vaga(1, (0, 0))
        self.vaga2 = Vaga(2, (1, 1))
        self.vaga3 = Vaga(3, (2, 2))

        Vaga.vagas.extend([self.vaga1, self.vaga2, self.vaga3])

    def test_vaga_creation(self):
        """Test Vaga object creation."""
        vaga = Vaga(10, (5, 5))
        assert vaga.numero == 10
        assert vaga.localizacao == (5, 5)

    def test_obter_vaga_pelo_numero_success(self):
        """Test successful vaga retrieval by number."""
        result = Vaga.obter_vaga_pelo_numero(1)

        assert result["ok"] is True
        assert result["message"] == "Vaga encontrada"
        assert result["data"]["vaga"] == self.vaga1

    def test_obter_vaga_pelo_numero_not_found(self):
        """Test vaga retrieval by number when not found."""
        result = Vaga.obter_vaga_pelo_numero(999)

        assert result["ok"] is False
        assert result["message"] == "Vaga não encontrada"
        assert "data" not in result

    def test_obter_vaga_pela_localizacao_success(self):
        """Test successful vaga retrieval by location."""
        result = Vaga.obter_vaga_pela_localizacao((1, 1))

        assert result["ok"] is True
        assert result["message"] == "Vaga encontrada"
        assert result["data"]["vaga"] == self.vaga2

    def test_obter_vaga_pela_localizacao_not_found(self):
        """Test vaga retrieval by location when not found."""
        result = Vaga.obter_vaga_pela_localizacao((99, 99))

        assert result["ok"] is False
        assert result["message"] == "Vaga não encontrada"
        assert "data" not in result

    def test_calcular_distancia(self):
        """Test distance calculation between two vagas."""
        result = Vaga.calcular_distancia(self.vaga1, self.vaga3)

        assert result["ok"] is True
        assert result["message"] == "Distância calculada"
        # Distance = |0-2| + |0-2| = 2 + 2 = 4
        assert result["data"]["distancia"] == 4

    def test_calcular_distancia_same_vaga(self):
        """Test distance calculation for the same vaga."""
        result = Vaga.calcular_distancia(self.vaga1, self.vaga1)

        assert result["ok"] is True
        assert result["data"]["distancia"] == 0

    def test_calcular_distancia_negative_coordinates(self):
        """Test distance calculation with negative coordinates."""
        vaga_neg = Vaga(4, (-1, -1))
        result = Vaga.calcular_distancia(self.vaga1, vaga_neg)

        assert result["ok"] is True
        # Distance = |0-(-1)| + |0-(-1)| = 1 + 1 = 2
        assert result["data"]["distancia"] == 2

    def test_vagas_class_variable_initially_empty(self):
        """Test that Vaga.vagas is initially empty."""
        Vaga.vagas.clear()
        assert len(Vaga.vagas) == 0

    def test_vagas_class_variable_persistence(self):
        """Test that Vaga.vagas persists across instances."""
        Vaga.vagas.clear()
        vaga_a = Vaga(100, (10, 10))
        vaga_b = Vaga(200, (20, 20))

        # Manually add to class list since class doesn't auto-populate
        Vaga.vagas.extend([vaga_a, vaga_b])

        assert len(Vaga.vagas) == 2
        assert vaga_a in Vaga.vagas
        assert vaga_b in Vaga.vagas
