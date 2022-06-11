class Sort:
    def __init__(self):
        pass

    def ordenada(self, lista):
        order = 0
        for i in range(1,len(lista)):
            if lista[i-1] < lista[i]:
                if order == 1 or order == 0:
                    order = 1
                else:
                    return -1
            elif lista[i-1] > lista[i]:
                if order == 2 or order == 0:
                    order = 2
                else:
                    return -1

        return order

    # Sort in O(nlog(n))


    # Sort in O(n^2)
    def insertion_sort(self, lista):
        for i in range(1, len(lista)):
            currentValue = lista[i]
            currentIndex = i
            while currentIndex > 0 and lista[currentIndex-1] > currentValue:
                lista[currentIndex] = lista[currentIndex-1]
                currentIndex = currentIndex-1
            lista[currentIndex] = currentValue
        return lista

    def selection_sort(self, lista):
        print(lista)
        range_lista = range(len(lista))
        for i in range_lista[:-1]:
            aux_i = i
            for j in range_lista[i+1:]:
                #aux_i ^= (aux_i ^j) & -(lista[aux_i] > lista[j])
                if lista[aux_i] > lista[j]:
                    aux_i = j
            lista[aux_i], lista[i] = lista[i], lista[aux_i]
        print(lista)
        return lista

    def bubble_sort(self, lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                break
        return lista
