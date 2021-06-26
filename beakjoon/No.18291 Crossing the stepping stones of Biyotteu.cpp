/*
	징검다리가 n개 있을때, 
	1번째 징검다리와 n번째 징검다리는 무조건 건너야 하므로 경우의 수가 1.
	그 외 모든 징검다리는 건널 수도, 아닐 수도 있으므로 경우의 수는 2
	따라서, 징검다리를 건너는 경우의 수는, 2^(징검다리의 갯수 - 2)
*/

//21-06-26
//외부함수를 하나로 줄임(squared).
//2^n = 2^(n/2) * 2^(n/2) 이용

#include <iostream>
#define INF 1000000007 //10^9 + 7
using namespace std;
long long squared(long long top) //2^top % INF 반환
{
	if(top == 1)
		return 2;
	if(top == 0)
		return 1;
	if(top % 2 == 1)
		return (2 * (squared((top-1)/2) % INF) * (squared((top-1)/2) % INF)) % INF;
	return ((squared(top/2) % INF) * (squared(top/2) % INF)) % INF;

}

int main()
{	
	int Test_case, count;
	cin >> Test_case;
	for(int i = 0; i < Test_case; i++){
	    cin >> count;
		if(count == 1 || count == 2) //징검다리가 하나, 또는 두개 있으면 경우의 수는 무조건 1이므로, 예외처리.
			cout << "1"<< endl;
		else
		    cout << squared(count - 2) << endl;
	}
	return 0;
}