# Name: Eric Smith
# Date: 12/17/21
# Description: Return two numbers from an array that add up to the target value.

def twoNumberSum_v1(array, targetSum):

    for num in range(len(array)-1):
        first_num = array[num]

        for num in range(len(array)-1):
            second_num = array[num]

            if first_num + second_num == targetSum and first_num != second_num:
                answer = [first_num, second_num]
                return answer

    return []

def twoNumberSum_v2(array, targetSum):

    for num in range(0, len(array)):
        first_num = array[num]
        print(first_num)
        for num in range(0, len(array)):
            print(array[num])
            print(targetSum - first_num)
            if targetSum - first_num == array[num] and first_num != array[num]:
                return [first_num, array[num]]

    return []

array = [3,5,-4,8,11,1,-1,6]

targetSum = 0

print(twoNumberSum_v1(array, targetSum))

print(twoNumberSum_v2(array, targetSum))
