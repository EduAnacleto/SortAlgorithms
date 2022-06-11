import sys
sys.path.insert(0, '../')

import sort
import random    
import pytest


class TestaSortInt:
    @pytest.fixture
    def o(self):
        return sort.Sort()

    @pytest.fixture
    def lista_aleatoria(self):
        return [random.randrange(-100,100) for x in range(100)]

    #Testes
    @pytest.mark.parametrize("esperado", [(1) for x in range(1000)])
    def test_heapSort(self, esperado, o, lista_aleatoria):
        assert o.ordenada(o.heapSort(lista_aleatoria)) == esperado

    @pytest.mark.parametrize("esperado", [(1) for x in range(1000)])
    def test_mergeSort(self, esperado, o, lista_aleatoria):
        assert o.ordenada(o.mergeSort(lista_aleatoria)) == esperado

    @pytest.mark.parametrize("esperado", [(1) for x in range(1000)])
    def test_insertionSort(self, esperado, o, lista_aleatoria):
        assert o.ordenada(o.insertionSort(lista_aleatoria)) == esperado

    @pytest.mark.parametrize("esperado", [(1) for x in range(1000)])
    def test_selectionSort(self, esperado, o, lista_aleatoria):
        assert o.ordenada(o.selectionSort(lista_aleatoria)) == esperado

    @pytest.mark.parametrize("esperado", [(1) for x in range(1000)])
    def test_bubbleSort(self, esperado, o, lista_aleatoria):
        assert o.ordenada(o.bubbleSort(lista_aleatoria)) == esperado


