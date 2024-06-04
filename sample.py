print('hello world')
print('hey im from github')
print('hey im changed!')
print('hey its neww message')
arr=[1,4,5,3,2]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)