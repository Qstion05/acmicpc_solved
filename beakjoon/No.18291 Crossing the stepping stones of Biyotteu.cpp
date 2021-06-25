//21-06-25
//시간초과. 알고리즘을 좀 더 효율적으로 쓸 필요가 있음.
//외부함수 두개 쓰는건 진짜 아닌듯..


#include <iostream>
using namespace std;
int squared(int top)
{
	if(top == 1)
		return 2;
	if(top == 0)
		return 1;
	if(top % 2 == 1)
		return 2 * squared(top - 1);
	return squared(top/2) * squared(top/2);

}

int Crossing_Stone(int count)//
{

	if(count == 1 || count == 2)
		return 1;
	return squared(count-2);
}





int main()
{	
	int Test_case, Count;
	cin >> Test_case;
	for(int i = 0; i < Test_case; i++){
		cin >> Count;
		cout << Crossing_Stone(Count) << endl;
	}
	return 0;
}