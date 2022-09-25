def prevPermutation(array):
    n = len(array) - 1
    i = n
    while (i > 0 and array[i - 1] <= array[i]):
        i -= 1
    if (i <= 0):
        return None
    j = i - 1
    while (j + 1 <= n and array[j + 1] < array[i - 1]):
        j += 1
    array[j],array[i-1]=array[i-1],array[j]
    array=array[:i] +array[i:][::-1]
    return array

print(prevPermutation([3,2,1]))
