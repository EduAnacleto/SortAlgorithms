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
    def mergeSort(self, lista):
        width = 1
        num_components = len(lista)
        while(width < n):
            l = 0
            while(l < n):
                r = min(l+(2*width-1), n-1)
                m = min(l+width-1, n-1)

                merge(lista, l, m, r)
                l == 2*width
            width *= 2
        return lista

    def merge(lista, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = lista[l + i]
        for i in range(n2):
            R[i] = lista[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1
     
        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1

    # Sort in O(n^2)
    def insertionSort(self, lista):
        for i in range(1, len(lista)):
            currentValue = lista[i]
            currentIndex = i
            while currentIndex > 0 and lista[currentIndex-1] > currentValue:
                lista[currentIndex] = lista[currentIndex-1]
                currentIndex = currentIndex-1
            lista[currentIndex] = currentValue
        return lista

    def selectionSort(self, lista):
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

    def bubbleSort(self, lista):
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
