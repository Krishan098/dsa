#include<iostream>
using namespace std;
int factorial(int n){
	if(n==0){
		return 1;
	}
	else{
		return n*(factorial(n-1));
	}
};
int sumofNnumbers(int N){
	if(N==0){
		return 0;
	}
	else{
		return N+sumofNnumbers(N-1);
	}
};
void f(int i,int arr[],int n){
	if(i>=n/2)return;
	swap(arr[i],arr[n-i-1]);
	f(i+1,arr,n);
};
bool isPalindrome(int k,string &s){
	if(k>=s.size()/2) return true;
	if(s[k]!=s[s.size()-k-1]) return false;
	return isPalindrome(k+1, s);
}
int fibonacci(int x){
	if(x==0){
		return 0;
	}
	else if (x==1)
	{
		return 1;
	}
	else{
		return fibonacci(x-1)+fibonacci(x-2);
	}
}
int main() {
	// int n;
	// cin>>n;
	// int cnt=0;
	// for(int i=1;i*i<=n;i++){
	// 	if(n%i==0){
	// 		cnt++;
	// 		if((n/i)!=i)cnt++;
	// 	}
	// }
	// if(cnt==2)cout<<"True";
	// else cout<<"False";

	cout<<factorial(5)<<endl;
	cout<<sumofNnumbers(10)<<endl;
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)cin>>arr[i];
	f(0,arr,n);
	for(int i=0;i<n;i++)cout<<arr[i]<<' ';
	string s="madam";
	// cout<<boolalpha<<isPalindrome(0,s)<<endl;
	cout<<fibonacci(5)<<endl;
}


