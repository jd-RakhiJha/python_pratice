def find_dublicate(arr):
    dublicate = []
    n= len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                if arr[i] is not dublicate:
                    dublicate.append(arr[i])

    return dublicate  

arr = [1, 2, 3, 5, 2, 3, 4]
result = find_dublicate(arr)
print("Duplicate elements:",result)              