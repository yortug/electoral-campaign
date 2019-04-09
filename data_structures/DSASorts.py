#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

# import numpy as np


class DSASorts:
    def __init__(self):
        ...



    # nested loop O(N^2)
    # DESCRIPTION:
    # this approach takes a pairwise approach, pairs are looked at and the larger value is always moved up to the end, it
    # is then compared to the next value, if still larger it switches again (moving it up the ladder) until it gets to the
    # point where its either at the end (largest value and for-loop completes), or the value next is in fact larger than it
    # if the value next WAS larger than it then we use it as the 'vehicle' for our pairwise comparisions under the same
    # conditions; this process will continue until EACH pair does not require a swap (whole array is sorted)

    def bubbleSort(self, A):
        swap = False # set a 'swap flag' as being false, we assume our pairs AREN'T in correct swapped order
        while not swap: # while a pair ISN'T in correct swap order (swap = False)
            swap = True # we set the swap = True first, 'giving it the benifit of the doubt,' but if it fails the comparision
            # we of course know everything ISN'T in perfect order and the boolean is switched back to False as a result
            for i in range(1, len(A)): # we will itterate through all values in our array (besides the first because it has no previous)
                if A[i-1] > A[i]: # comparing our value in question to its previous value, and if it is indeed smaller...
                    swap = False # then the pair ISN'T in correct swapped order so we switch the boolean to reflect that
                    # temp = A[i]
                    # A[i] = A[i-1]
                    # A[i-1] = temp
                    (A[i], A[i-1]) = (A[i-1], A[i]) # and then we swap those two values so the smaller is on the left 
                    # and the larger is now on the right

            # this whole process will continue until the for-loop goes through each pair, and finds EACH PAIR to be in correct
            # order (NOT executing the if-statement), this in turn means the 'swap flag' will never be switched to False, keeping
            # it as True and therefore exiting the while-loop and completing the function call
        return A
        #print('Sorted ', A)





    # nested loop O(N^2)
    # DESCRIPTION:
    # starting at the second value in list, compare its value to value before it, if it is found to be smaller then
    # initiate a swap, and begin the comparison process to its new 'previous neighbour;' this process continues until
    # it is found that our value is either not first in array (j>0) or value before it IS NOT smaller than value in question
    # thus, when the process stops we know for sure that the current position is the overall rightful position for our
    # value in question; it's 'cemented' in place, and the for-loop continues to assess the next value to all previous

    def insertionSort(self, A):
        for i in range(1, len(A)):
            z = A[i] # unsorted value
            j = i # unsorted index
            while j > 0 and A[j-1] > z: # while unsorted index > 0 AND previous value IS GREATER than unsorted value - initiate swap
                A[j] = A[j-1] # unsorted value IN ARRAY becomes the previous value (which was found to be GREATER)
                j -= 1 # we then decrement our unsorted index so we can check if the previous values are GREATER than our 'z'

            A[j] = z # if the while loop requirements AREN'T met then it means the current 'j' is the rightful place for original 'z'

        return A
        #print('Sorted ', A)


    def edgeSort(self, A):
        """
        takes an array of len(2) arrays where the 0th element is the sort index, and the 1st element will be the object
        """
        for i in range(1, len(A)):
            z = A[i] # unsorted value
            x = A[i][0]
            y = A[i][1]
            j = i # unsorted index

            while j > 0 and A[j-1][0] > x: # while unsorted index > 0 AND previous value IS GREATER than unsorted value - initiate swap
                A[j] = A[j-1] # unsorted value IN ARRAY becomes the previous value (which was found to be GREATER)
                j -= 1 # we then decrement our unsorted index so we can check if the previous values are GREATER than our 'z'

            A[j] = z # if the while loop requirements AREN'T met then it means the current 'j' is the rightful place for original 'z'

        return A
        #print('Sorted ', A)


    # nested loop O(N^2)
    # DESCRIPTION:
    # looks at first element in array, if a value is smaller then switch places, continue comparing through
    # the array and switching when next element is found to be smaller than 'current smallest'
    # by the time you get to the end of the array (for-loop exits), you are guarenteed that the value
    # at the front (that was going through all the comparisons) will infact be your smallest overall value
    # thus, you itterate the 'sorted value counter' to look at only everything else (front value 'cemented')

    def selectionSort(self, A):
        z = 0 # keeping track of how many elements HAVE been sorted
        while z != len(A): # WHILE we HAVEN'T sorted ALL elements in the list
            for i in range(z, len(A)): # itterate through every CURRENTLY UNSORTED element left in list
                if A[i] < A[z]: # if itterated element IS LESS THAN the 'currently found to be smallest' element
                    # temp = A[i]
                    # A[i] = A[z]
                    # A[z] = temp
                    (A[z], A[i]) = (A[i], A[z]) # swap the position of this smaller value and the front (comparison) element
                    # once for-loop exits we can be sure that the value at the front is the overall smallest, so...
            z += 1 # we iterrate the sorted counter to ignote this already sorted value; looking at everything else
            # (process repeats until the 'sorted counter' is the length of our overall list - every value is sorted)
        return A
        #print('Sorted ', A)


    # O(N*log(N))
    # DESCRIPTION:
    # 

    def mergeSort(self, A):
        #print("Splitting ", A)
        
        if len(A)>1: # if it's not a single element array
            mid = len(A)//2 # find the middle point of the array to split on
            lefthalf = A[:mid].copy() # our left half becomes everything to the left of the middle point
            righthalf = A[mid:].copy() # our right half becomes everything on the right of the middle point

            mergeSort(lefthalf) # begin recursion with left side; keep splitting until single element array
            mergeSort(righthalf) # begin recursion with right side; keep splitting until single element array

            merge(A, lefthalf, righthalf) # once we have a sorted left and sorted right side (by definition a single
            # element array meets this criteria) we can begin the merging process, which just takes the smallest
            # of the leftmost index in each array until one side is empty, once one side is empty what's left is
            # just put onto the end of our final array
        return A
        #print("Merging ", A)
        

    def merge(self, A, lefthalf, righthalf):
        (i, j, k) = (0, 0, 0)
        while i < len(lefthalf) and j < len(righthalf): # as long as there's something left in the left list AND something left in the right list
            if lefthalf[i] < righthalf[j]: # if the entry for the left list is smaller than entry for right list
                A[k] = lefthalf[i] # this smaller value goes into our final list
                #print('1', i, j, A)
                i += 1 # we then increase the step (on the left) to compare our next smallest value
            else:
                A[k] = righthalf[j] # otherwise the right value must have been the smaller entry so we add THAT to our final list
                #print('2', i, j, A)
                j += 1 # we then increase the step (on the right) to compare our next smallest value
            k += 1 # as the entry we added MUST be the smallest, then we iterate through our final array, because next element will be the NEXT smallest

        # if we are up to this point it MUST mean one of the lists is empty (according to clause on the previous while loop)

        while i < len(lefthalf): # while the left half still has stuff in it
            A[k] = lefthalf[i] # add first part of stuff to list
            #print('3', i, j, A)
            i += 1 # add the next part of stuff
            k += 1 # to the next part of overall list

        while j < len(righthalf): # while the right half still has stuff in it
            A[k] = righthalf[j] # add first part of stuff to list
            #print('4', i, j, A)
            j += 1 # add the next part of stuff
            k += 1 # to the next part of overall list

        return A


        
        #mergeSortRecurse(A, 0, len(A)-1)

    # def mergeSortRecurse(A, leftIdx, rightIdx):
    #     if leftIdx < rightIdx: # if the list ISN'T just one element
    #         midIdx = (leftIdx + rightIdx) // 2 # integer division to find middle point of list (split point)
    #         mergeSortRecurse(A, leftIdx, midIdx) # call the function again with the left half
    #         mergeSortRecurse(A, midIdx+1, rightIdx) # call the function again with the right half
    #         merge(A, leftIdx, midIdx, rightIdx)


    # def merge(A, leftIdx, midIdx, rightIdx):
    #     result = np.zeros(rightIdx - leftIdx + 1)
    #     #print(len(result), leftIdx, midIdx, rightIdx)
    #     #print(result)
    #     #print(A)
    #     i = leftIdx
    #     j = midIdx+1
    #     z = 0

    #     while i <= midIdx and j <= rightIdx: # while either left or right array ISN'T empty
    #         if A[i] <= A[j]: # if first entry in left array is smaller
    #             result[z] = A[i] # then put it into our results
    #             i += 1 # and itterate its counter
    #         else:
    #             result[z] = A[j] # otherwise the first entry in the right array must be smaller, so add it to results
    #             j += 1 # and itterate its counter
    #         z += 1 # itterate the overall result's element counter

    #     for c in range(i, midIdx):
    #         result[z] = A[c] # left over bits in left array go into results
    #         z +=1 # itterate counter because we've added an entry
    #     for d in range(j, rightIdx): 
    #         result[z] = A[d] # left over bits in right array go into results
    #         z +=1 # itterate counter because we've added an entry
    #     for e in range(leftIdx, rightIdx): # copy sorted bits into original array
    #         A[e] = result[e-leftIdx]

    #     #print('Sorted ', A)

    # def mergeSortRecurse(A):
    #     if len(A) > 2:
    #         return A[:]
    #     else:
    #         middle = len(A) // 2
    #         left = mergeSortRecurse(A[:middle])
    #         right = mergeSortRecurse(A[middle:])
    #         return merge(left, right)

    # def merge(left, right):
    #     result = []
    #     i, j = 0, 0 
    #     while i < len(left) and j < len(right):
    #         if left[i] < right[i]:
    #             result.append(left[i])
    #             i += 1
    #         else:
    #             result.append(right[j])
    #             j += 1
    #     while (i < len(left)):
    #         result.append(left[i])
    #         i += 1
    #     while (j < len(right)):
    #         result.append(right[j])
    #         j += 1


    # 
    # DESCRIPTION:
    # find a pivot point (initial is middle number), everything smaller than our pivot point goes to
    # its left, our pivot then becomes the next value after this 'left half' list, leaving everything
    # on the right as known to be larger than the pivot; the process then repeats except this time we're
    # splitting the left and right half of the intial pivot into ANOTHER set of halves and repeating the
    # whole process indefinitely until the array attempting to be split is found to be single element
    # i.e sorted

    def quickSort(self, A):
        """ quickSort - front-end for kick-starting the recursive algorithm
        """
        quickSortRecurse(A, 0, len(A)-1)

    def quickSortRecurse(self, A, leftIdx, rightIdx):
        if rightIdx > leftIdx: # if array is NOT just a single element
            pivotIdx = (leftIdx+rightIdx) // 2 # the (first?) pivot index becomes the middle value (rounded down)
            newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx) # find what values are smaller than our pivot
            # edit array to put them to the left of our pivot (everything bigger goes to the right), return a new pivot
            # value

            quickSortRecurse(A, leftIdx, newPivotIdx-1) # start the whole process again with everything that was found to be SMALLER than pivot
            quickSortRecurse(A, newPivotIdx+1, rightIdx) # start the whole process again with everything that was found to be LARGER than pivot

        #print(A)
        return A

    def doPartitioning(self, A, leftIdx, rightIdx, pivotIdx):
        pivotVal = A[pivotIdx] # save the value of our pivot for future comparison
        (A[pivotIdx], A[rightIdx] ) = (A[rightIdx], A[pivotIdx]) # swap the pivot with the rightmost value in partition
        # (this leaves the rest of the partition as itterable through a for-loop)

        z = leftIdx # start a counter at the left most part of the partition
        for i in range(leftIdx, rightIdx): # for all values within the partition 
        # (besides our pivot on the very right, which is not included due to range() not being inclusive of final value)
            if A[i] < pivotVal: # if a value is SMALLER than our pivot value
                (A[i], A[z]) = (A[z], A[i]) # swap it with the first available slot in the partition (move it to the 'left of pivot area')
                z += 1 # itterate the 'left of pivot counter' to indicate that the next smallest value should go in next available left area slot

        (A[rightIdx], A[z]) = (A[z], pivotVal) # once the for-loop has completed it means all values in this 'left area' are smaller than the pivot
        # thus, we must place our pivot directly after this group (where the z-counter currently sits), as that is its rightful place in overall array

        return z # we then return the position where we just placed our pivot, because this whole process must now be
        # repeated with the 'left area' (smaller than pivot), and 'right area' (larger than pivot), until the process
        # as a whole FAILS the first if-statement, indicating that the partitions are now single-element i.e. sorted


