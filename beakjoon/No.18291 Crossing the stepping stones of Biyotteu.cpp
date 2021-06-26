//21-06-26
//외부함수를 하나로 줄임.
#include <iostream>
#define INF 1000000007
using namespace std;
int squared(int top)
{
	if(top == 1)
		return 2;
	if(top == 0)
		return 1;
	if(top % 2 == 1)
		return 2 * squared((top-1)/2) % INF * squared((top-1)/2) % INF;
	return squared(top/2) % INF * squared(top/2) % INF;

}

int main()
{	
	int Test_case, count;
	cin >> Test_case;
	for(int i = 0; i < Test_case; i++){
		if(count == 1 || count == 2)
			cout << "1"<< endl;
		cin >> count;
		cout << squared(count) << endl;
	}
	return 0;
}