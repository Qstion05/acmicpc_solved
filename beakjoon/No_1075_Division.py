N = int(input())
F = int(input())

N = (N // 100) *100


for i in range(0, F + 1):
	if(N % F == 0):
		break;
	N += 1
if( i < 10):
	print("0"+str(i))
else:
	print(i)