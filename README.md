# SortAlgorithms
A python module that contains iterative (non-recursive) sort algorithms.<br />

All algorithms were extensively tested before post. The test procedure <br />
is automatic and can be performed inside the 'Test' folder using the <br />
command line 'pytest test_sort.py'.

Usage example:

import sort

operator = sort.Sort()<br />
unsorted_list = [1,4,2,1,5,7,8,2,1,3]

print('heapSort     :', operator.heapSort(unsorted_list[:]))<br />
print('mergeSort    :', operator.mergeSort(unsorted_list[:]))<br />
print('insertionSort:', operator.insertionSort(unsorted_list[:]))<br />
print('selectionSort:', operator.selectionSort(unsorted_list[:]))<br />
print('bubbleSort   :', operator.bubbleSort(unsorted_list[:]))
