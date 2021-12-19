# Author: Eric Smith
# Date: 12/18/21
# Description: Determine if the sequence is a valid subset of an array, where the sequence
# where the sequence numbers appear in the same order within the array

def isValidSubsequence(array, sequence):
    
    sequence_id = 0
    array_id = 0
    
    for num in range(array_id, len(array)):

        if array[array_id] in sequence[sequence_id:]:
            sequence_id += 1
        array_id += 1

    if sequence_id == len(sequence):
        return True
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 10, 10]

isValidSubsequence(array, sequence)
