# 12. Из двух отсортированных массивов сделать третий отсортированный, не сортируя его.
def sortTwoArraysInOne(arrayA, arrayB):
    sizeA = len(arrayA)
    sizeB = len(arrayB)
    if sizeA == 0 & sizeB == 0:
        return arrayA
    else:
        arrayA.sort()
        arrayB.sort()
        arrayC = [None] * (sizeA + sizeB)
        i, j, k = 0, 0, 0
        while i < sizeA and j < sizeB:
            if arrayA[i] < arrayB[j]:
                arrayC[k] = arrayA[i]
                k = k + 1
                i = i + 1
            else:
                arrayC[k] = arrayB[j]
                k = k + 1
                j = j + 1 

        while i < sizeA:
            arrayC[k] = arrayA[i]
            k += 1
            i += 1
        while j < sizeB:
            arrayC[k] = arrayB[j]
            k += 1
            j += 1
    return arrayC