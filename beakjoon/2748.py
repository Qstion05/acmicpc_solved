#link: https://www.acmicpc.net/problem/2748
#level: bronze 1
#problem
'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

'''



dynimic_list = [0] * 90
def pibonachi(n):
	global dynimic_list
	if n == 1 or n == 2:
		return 1

	if dynimic_list[n] != 0: #memoization
		return	dynimic_list[n]

	dynimic_list[n] = pibonachi(n-1) + pibonachi(n-2)
	return dynimic_list[n]

n = int(input())
print(pibonachi(n))

#time_out