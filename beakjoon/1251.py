#link: https://www.acmicpc.net/problem/1251
#level: sliver 5
#problem
'''
알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.

먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다. 즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다. 각각은 적어도 길이가 1 이상인 단어여야 한다. 이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

예를 들어,

단어 : arrested
세 단어로 나누기 : ar / rest / ed
각각 뒤집기 : ra / tser / de
합치기 : ratserde
단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다
'''

'''
arrested
01234567
0 2
2 6
6 8

[0, a] 1 <= a <= 6
[a, b] 
a = 1 : 2 <= b <= 7
a = 2 : 3 <= b <= 7

a+1 <= b <= 7

'''
#1.만들 수 있는 모든 문자열을 리스트에 몰아 넣는다.
#2.sort함수를 이용해 사전순으로 정렬한다.

usr_string = input()
string_length = len(usr_string)
reverse_string = ""
dictionary_list = []
for a in range(1, string_length - 1): #ex) string_length = 8, 0<= a <= 6) 
	for b in range(a+1, string_length): #ex) string_length = 8, 1<= b <= 7-a

		first_char = usr_string[0:a] #set range
		second_char = usr_string[a:b]
		third_char = usr_string[b:string_length]

		reverse_string += first_char[::-1] #using silce(string reverse) 
		reverse_string += second_char[::-1]
		reverse_string += third_char[::-1]
		dictionary_list.append(reverse_string) # append maked_string
		reverse_string = "" #reset
 
dictionary_list.sort() # sort 
print(dictionary_list[0])


