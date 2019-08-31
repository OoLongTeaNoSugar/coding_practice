# =================================
# quicksort small-->big O(NlogN)
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def partition(arr, L, R):
    less = L - 1
    more = R
    while L < more:
        if arr[L] < arr[R]:
            less += 1
            swap(arr, less, L)
            L += 1
        elif arr[L] > arr[R]:
            more -= 1
            swap(arr, more, L)
        else:
            L += 1
    swap(arr, more, R)
    return [less+1, more]

def QuickSort(arr, L, R):
    if L < R:
        swap(arr, L + random.randint(0, R-L), R)
        p = partition(arr, L, R)
        QuickSort(arr, L, p[0] - 1)
        QuickSort(arr, p[1] + 1, R)
def quicksort(arr):
    if len(arr) < 2:
        return
    QuickSort(arr, 0, len(arr) - 1)

########################
# for test
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def compare(arr1, arr2):
    return arr1 == arr2

if __name__ == "__main__":
    import random
    for i in range(100):

        test = random_int_list(1, 100, 10)
        comp = sorted(test)
        quicksort(test)
        if compare(test, comp):
            print('nice!')


