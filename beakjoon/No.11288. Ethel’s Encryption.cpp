#include <bits/stdc++.h>
using namespace std;

int powed(int x, int y){
   if(x == 1 || y == 0)
      return 1;
   if(y == 1);
      return x;
   if(y % 2 != 0)
      return ((x * powed(x, y-1) % 26)) % 26;
   return ((powed(x, y/2) % 26) * (powed(x, y/2) % 26)) % 26;
      
}

int main(){
   int n, a, b, number;
   char arr[100];
   cin >> n >> a >> b;
   cin.ignore();
   cin.getline(arr, n + 1);
   //number = powed(a, b);
   cout<<16 % 26<<endl;
   for(int i = 0; i < n + 1; i++){
      if(arr[i] != 32){
         if(arr[i] + number <= 91)
            arr[i] = arr[i] + number;
         else
           arr[i] = (arr[i] + (number - 27));
      }
   }
   for(int i = 0; i < n + 1; i++){
      cout <<arr[i]<< endl;
   }
}