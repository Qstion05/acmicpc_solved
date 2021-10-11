n, k = input().split()
n = int(n)
k = int(k)

arr = [[0]*2 for i in range(n)]
for i in range(n):
	w, v = input().split()
	arr[i].append(int(w))
	arr[i].append(int(v))
	arr[i].remove(0)
	arr[i].remove(0)
print(arr)
