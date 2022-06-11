# SortAlgorithms
A python module that contains iterated (non-recursive) sort algorithms. 
All algorithms were extensively tested before post, the test procedure 
is automatic and can be performed inside the 'Test' folder using the 
command pytest test_sort.py.

Usage example:

import sort

operator = sort.Sort()
unsorted_list = [1,4,2,1,5,7,8,2,1,3]

print('heapSort     :', operator.heapSort(unsorted_list[:]))
print('mergeSort    :', operator.mergeSort(unsorted_list[:]))
print('insertionSort:', operator.insertionSort(unsorted_list[:]))
print('selectionSort:', operator.selectionSort(unsorted_list[:]))
print('bubbleSort   :', operator.bubbleSort(unsorted_list[:]))
