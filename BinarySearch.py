def bi_search(l, r, arr, x):
    if r >= l:
        if arr[l] == x:
            return 'True'

        elif arr[l] < x:
            return bi_search(l+1,r,arr,x)
        else:
            return 'False'
    else:
        return 'False'
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
# print(sorted(arr))
print(bi_search(0, len(arr) - 1, sorted(arr), k))