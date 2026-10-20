"""Codigo de implementacion (main): ordenamiento burbuja."""


class BubbleSorter:

    def bubble_sort(self, vet):
        n = len(vet)                                   # Nodo 1
        for i in range(n, 1, -1):                      # Nodo 2: i = n ... 2
            for j in range(i - 1):                     # Nodo 3: j = 0 ... i-2
                if vet[j] > vet[j + 1]:                # Nodo 4
                    aux = vet[j]                       # Nodo 5 (intercambio)
                    vet[j] = vet[j + 1]
                    vet[j + 1] = aux
        return vet                                     # Nodo 8
