#include<bits/stdc++.h>
using namespace std;
int main(){
    string c;
    cin>>c;
    int hash[256]={0};
    for(int i=0;i<c.size();i++){
        hash[c[i]]++;
    }
    int q;
    cin>>q;
    while(q--){
        char k;
        cin>>k;
        cout<<hash[k]<<endl;
    }
    return 0;
}