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

    
    def heapSort(self, lista): #O(n log n)
        n = len(lista)
        self.buildMaxHeap(lista, n)

        for i in range(n-1, 0, -1):

            lista[0], lista[i] = lista[i], lista[0]

            j, index = 0, 0
            while True:
                index = 2 * j + 1

                if index < i-1 and lista[index] < lista[index + 1]:
                    index += 1
                
                if index < i and lista[j] < lista[index]:
                    lista[j], lista[index] = lista[index], lista[j]

                j = index
                if index >= i:
                    break

        return lista

    def buildMaxHeap(self, lista, n): #O(n)
        for i in range(1, n):
            self.maxHeapify(lista, i)

    def maxHeapify(self, lista, i): #(log n)
        # if child is bigger than parent
        j = (i-1)//2
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]            
            # swap child and parent until parent is smaller
            while lista[j] > lista[(j - 1) // 2] and j != 0:
                lista[j], lista[(j - 1) // 2] = lista[(j - 1) // 2], lista[j]
                j = (j - 1) // 2


    def mergeSort(self, lista): #O(n log n)
        width = 1
        n = len(lista)
        while width < n:
            l = 0
            while l < n:
                r = min(l+(2*width-1), n-1)
                m = min(l+width-1, n-1)

                self.merge(lista, l, m, r)
                l += 2*width
            width *= 2
        return lista

    def merge(self, lista, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = lista[l + i]
        for i in range(0, n2):
            R[i] = lista[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            lista[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            lista[k] = R[j]
            j += 1
            k += 1

    
    def quickSort(self, lista):
        n = len(lista)
        l = 0
        h = n-1

        stack = [l, h] + [0] * (n-2)
        top = 1
        
        while top >= 0:
            h = stack[top]
            l = stack[top-1]
            top -= 2

            p = self.partition(lista, l, h)
            if p-1 > l:
                top += 2
                stack[top-1] = l
                stack[top] = p-1

            if p + 1 < h:
                top += 2
                stack[top-1] = p+1
                stack[top] = h

        return lista

    def partition(self, lista, l, h):
        i = l-1
        element = lista[h]
        for j in range(l, h):
            if lista[j] <= element:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        
        i += 1
        lista[i], lista[h] = lista[h], lista[i]
        return i


    def insertionSort(self, lista): #O(n^2)
        for i in range(1, len(lista)):
            currentValue = lista[i]
            currentIndex = i
            while currentIndex > 0 and lista[currentIndex-1] > currentValue:
                lista[currentIndex] = lista[currentIndex-1]
                currentIndex = currentIndex-1
            lista[currentIndex] = currentValue
        return lista


    def selectionSort(self, lista): #O(n^2)
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


    def bubbleSort(self, lista): #O(n^2)
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
