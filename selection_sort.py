

def selection_sort(array):
    steps = 0
    minimum = 0
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            steps+=1
            if array[minimum]>array[j]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]

    return array, steps

array = [10,9,8,7,6,5,4,3,2,1]
size = len(array)
print("Input : ", array)
output, steps = selection_sort(array)
print("Size of Array : ", size)
print("Steps Taken : ", steps)
print("Result : ", output)
