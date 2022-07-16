

def insertion_sort(array):
    steps = 0
    key = None
    outer_loop = 0
    inner_loop = 0
    
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        outer_loop += 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
            inner_loop += 1
        array[j+1] = key
    print('Outer Loop Steps : ', outer_loop)
    print('Inner Loop Steps : ', inner_loop)
    steps = inner_loop + outer_loop
    return array, steps

array = [10,9,8,7,6,5,4,3,2,1]
size = len(array)
print("Input : ", array)
output, steps = insertion_sort(array)
print("Size of Array : ", size)
print("Steps Taken : ", steps)
print("Result : ", output)
