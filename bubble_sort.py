

def bubble_sort(array):
    steps = 0
    swapped = False
    for i in range(len(array)):
        for j in range(0,(len(array))-i-1):
            steps+=1
            if array[j]>array[j+1]:
                swapped = True
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        if not swapped:
            break
    return array, steps

array = [10,9,8,7,6,5,4,3,2,1]
size = len(array)
print("Input : ", array)
output, steps = bubble_sort(array)
print("Size of Array : ", size)
print("Steps Taken : ", steps)
print("Result : ", output)
