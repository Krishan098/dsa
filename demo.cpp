// #include<bits/stdc++.h>

// using namespace std;

// // void print(){
// //     cout<<"Raj";
// // }
// // int sum(int a, int b){
// //     return a+b;
// // }
// // void explainPair(){
// //     pair<int,int>p={1,4};
// //     cout<<p.first<<' '<<p.second;
// //     pair<int,pair<int, int>>p={1,{3,4}};
// //     cout<<p.first<<" "<<p.second.second<<" "<< p.second.first;
// //     pair<int,int> arr={{1,2},{3,4},(5,6)};
// //     cout<<arr[1].second;
// // }

// // void explainVector(){
// //     vector<int> v;
// //     v.push_back(1);
// //     v.emplace_back(2);
// //     vector<pair<int,int>>vec;
// //     v.push_back({1,2});
// //     v.emplace_back(1,2);
// //     vector<int>v(5,100);
// //     vector<int>v(5);
// //     vector<int>v1(5,10);
// //     vector<int>v2(v1);
// //     vector<int>::iterator it =v.begin();
// //     it++;
// //     cout<<*(it)<<" ";

// //      it=it+2;
// //     cout<<*(it)<<" ";
// //     vector<int>::iterator it=v.end();
// //     vector<int>::iterator it=v.rend();
// //     vector<int>::iterator it=v.rbegin();
// //     cout<<v[0]<<" "<<v.at(0);
// //     cout<< v.back()<< " ";
// //     for(vector<int>::iterator it=v.begin(); it!=v.end();it++){
// //         cout<<*(it)<<" ";
// //     }
// //     for(auto it= v.begin(); it!=v.end();it++){
// //         cout<<*(it)<<" ";
// //     }
// //     for(auto it:v){
// //         cout<<it<<" ";
// //     }
// //     v.erase(v.begin()+1);
// //     v.erase(v.begin()+2,v.begin()+4);
// //     vector<int>v(2,100);
// //     v.insert(v.begin(),300);
// //     v.insert(v.begin()+1,2,10);
// //     vector<int> copy(2,50);
// //     v.insert(v.begin(),copy.begin(),copy.end());
// //     cout<<v.size();
// //     v.pop_back();
// //     v1.swap(v2);
// //     v.clear();
// //     cout<<v.empty();
// // }   

// // void explainList(){
// //     list<int>ls;
// //     ls.push_back(2);
// //     ls.emplace_back(2);
// //     dq.push
// // }
// // void printName(string name){
// //     cout<<"hey "<<name<<endl;
// // }
// // int add(int x,int y){
// //     int sum= x+y;
// //     return sum;
// // }

// int digitCount(int x){
//     while (x>0){
//         int lastDigit=x%10;
//         x=x/10;
//         cout<<lastDigit<<' ';
//     };
// };
// int main(){
//     // int x;
//     // cin >> x;
//     // cout<<"Value of x: "<<x;
//     // long x=15;
//     // long long x=15000000000;
//     //float, double
//     digitCount(444002);
//     // float x =5.6;
//     // float y=5;
//     // cout<<"VAlue of y:"<<y;

//     //string
//     // string S1;
//     // string S2;
//     // getline(cin,S1);
//     // cout<<str;
//     // int age;
//     // cin >> age;
//     // if(age>=18){
//     //     cout<<"You are an adult.";
//     // }
//     // else{
//     //     cout<<"You are a child";
//     // }

//     // int marks;
//     // cin>> marks;
//     // if(marks<25){
//     //     cout<<"F";
//     // }
//     // else if (marks<=44){
//     //     cout<<"E";
//     // }
//     // else if(marks<=49){
//     //     cout<<"D";
//     // }
//     // else if(marks<=59){
//     //     cout<<"C";
//     // } 
//     // else if(marks<=79){
//     //     cout<<"B";
//     // }
//     // else if(marks<=100){
//     //     cout<<"A";
//     // }
//     // return 0;


//     // int age;
//     // cin>>age;
//     // if(age<18){
//     //     cout<<"not eligible for job";
//     // }
//     // else if(age>=18 && age<=54){
//     //     cout<<"eligible for job";
//     // }
//     // else if(age>=55 && age<=57){
//     //     cout<<"eligible for job , but retirement soon.";
//     // }
//     // else if(age>57){
//     //     cout<<"retirement time";
//     // }


//     // int day;
//     // cin>>day;
//     // switch(day){
//     //     case 1:
//     //             cout<<"Monday";
//     //             break;
//     //     case 2:
//     //             cout<<"Tuesday";
//     //             break;
//     //     case 3:
//     //             cout<<"Wednesday";
//     //             break;
//     //     default:
//     //             cout<<"Invalid";
//     //             break;
//     // }
//     // cout<<"Check";
//     // return 0;



//     // int arr[5];
//     // cin>>arr[0]>>arr[1]>>arr[2]>>arr[3]>>arr[4];
//     // cout<<arr[3];


//     // for(int i=1;i<=5;i++){
//     //     cout<<"Striver"<<endl;
//     // }
//     // return 0;


//     // int i=0;
//     // while(i<=5){
//     //     cout<<"Striver"<<i<<endl;
//     //     i=i+1;
//     // }

//     // do{
//     //     cout<<"Striver"<<i<<endl;
//     //     i+=1;
//     // }
//     // while(i<=1);
//     // cout<<i<<endl;
//     // return 0;

//     // string name;
//     // cin>>name;
//     // printName(name);
//     // return 0;


//     // int x,y;
//     // cin>>x>>y;
//     // int sum=add(x,y);
//     // cout<<sum;
//     // return 0;

// //     for(int i=0; i<=4;i++){
// //         for(int j=1;j<=i;j++){
// //             cout<<j<<" ";
// //         };
// //         cout<<endl;
// //     };
    
// //     for(int i=0; i<=5;i++){
// //         for (int j=1;j<=i;j++){
// //             cout<<i<<" ";
// //         };
// //         cout<<endl;
// //     };

// //     for(int i=4;i>=0;i--){
// //         for(int j=0;j<=i;j++){
// //             cout<<'*'<<' ';
// //         };
// //         cout<<endl;
// //     };

// //     for(int i=0;i<5;i++){
// //         for(int j=0;j<4-i+1;j++){
// //             cout<<"*"<<' ';
// //         };
// //         cout<<endl;
// //     };

// //     for(int i=0;i<5;i++){
// //         for(int j=1;j<5-i+1;j++){
// //             cout<<j<<' ';
// //         };
// //         cout<<endl;
// //     };

// //     for(int i=5; i>=0; i--){
// //         for(int j=1;j<=i;j++){
// //             cout<<j<<' ';
// //         };
// //         cout<<endl;
// //     };

// //     for(int i=0;i<5;i++){
// //        for(int j=0;j<5-i-1;j++){
// //             cout<<" ";
// //        };
// //        for(int j=0;j<2*i+1;j++){
// //            cout<<'*';
// //        };
// //        for(int j=0;j<5-i-1;j++){
// //            cout<<" ";
// //        };
// //         cout<<endl;
// //     };

    
// // for(int i=0;i<5;i++){
// //     for(int j=0;j<i;j++){
// //         cout<<' ';
// //     };
// //     for(int j=0;j<((2*5)-((2*i)+1));j++){
// //         cout<<"*";
// //     };
// //     for(int j=0;j<i;j++){
// //         cout<<" ";
// //     };
// //     cout<<endl;
// // }

// // for(int i=0;i<=2*5-1;i++){
// //     int stars=i;
// //     if(i>5) stars=2*5-i;
// //     for(int j=0;j<stars;j++){
// //         cout<<'*';
// //     };
// //     cout<<endl;
// // };

// //  for(int i=0;i<=5;i++){
// //     int s=1;
// //     if(i%2==0) s=1;
// //     else s=0;
// //     for(int j=0;j<=i;j++){
// //         cout<<s;
// //         s=1-s;
// //     };
// //     cout<<endl;
// //  };

// //    for(int i=1;i<=4;i++){
// //     for(int j=1;j<=i;j++){
// //         cout<<j;
// //     };
// //     for(int j=0;j<=2*4-(2*i)-1;j++){
// //         cout<<' ';
// //     };
// //     for(int j=i;j>=1;j--){
// //         cout<<j;
// //     };
// //     cout<<endl;
// //    };
// //     int num=1;
// //    for(int i=0;i<=5;i++){
// //     for(int j=0;j<=i;j++){
// //         cout<<num<<' ';
// //         num+=1;
// //     };
// //     cout<<endl;
// //    };

// //    for(int i=0;i<=5;i++){
// //     for(char c='A';c<='A'+i;c++){
// //         cout<<c<<" ";
// //     };
// //     cout<<endl;
// //    };

// //    for(int i=5; i>0;i--){
// //     for(char c='A';c<'A'+i;c++){
// //         cout<<c<<" ";
// //     };
// //     cout<<endl;
// //    };

// //    for(int i=0;i<5;i++){
// //     char ch='A'+i;
// //     for(int j=0;j<=i;j++){
// //         cout<<ch<<" ";
// //     };
// //     cout<<endl;
// //    };

// //     for(int i=0;i<=5;i++){
// //         for(int j=0;j<5-i-1;j++){
// //             cout<<' ';
// //         };
// //         char ch='A';
// //         int breakpoint=(2*i+1)/2;
// //         for(int j=1;j<=2*i+1;j++){
// //             cout<<ch;
// //             if(j<=breakpoint)ch++;
// //             else ch--;
// //         };
// //         for(int j=0;j<5-i-1;j++){
// //             cout<<" ";
// //         };
// //         cout<<endl;
// //     }

// //     for(int i=0;i<5;i++){
// //         char ch='A'+5-1;
// //         for(int j=0;j<i;j++){
// //             cout<<ch<<' ';
// //             ch--;
// //         };
// //         cout<<endl;
// //     };
// //     int iniS=0;
// //     for(int i=0;i<5;i++){
// //         for(int j=0;j<5-i;j++){
// //             cout<<'*';
// //         };
// //         for(int j=0;j<iniS;j++){
// //             cout<<" ";
// //         };
// //         for(int j=0;j<5-i;j++){
// //             cout<<'*';
// //         };
// //         iniS+=2;
// //         cout<<endl;
// //     };

// //     for(int i=0;i<5;i++){
// //         for(int j=0;j<i;j++){
// //             cout<<'*';
// //         };
// //         for(int j=0;j<iniS;j++){
// //             cout<<" ";
// //         };
// //         for(int j=0;j<i;j++){
// //             cout<<'*';
// //         };
// //         iniS-=2;
// //         cout<<endl;
// //     };
// //     int spaces=2*n-2;
// // for(int i=1;i<=2*n-1;i++){
// //     int stars=i;
// //     if(i>n) stars=2*n-i;
// //     for(int j=1;j<=stars;j++){
// //         cout<<'*';
// //     };
// //     for(int j=1;j<=spaces;j++){
// //         cout<<' ';
// //     };
// //     for(int j=1;j<=stars;j++){
// //         cout<<'*';
// //     };
// //     cout<<endl;
// //     if(i<n) spaces-=2;
// //     else spaces+=2;
// // };
// // for(int i=0;i<n;i++){
// //     for(int j=0;j<n;j++){
// //         if(i==0||j==0||i==n-1||j==n-1){
// //             cout<<'*';
// //         }
// //         else cout<<' ';
// //     };
// //     cout<<endl;
// // };

// // for(int i=0;i<2*n-1;i++){
// //     for(int j=0;j<2*n-1;j++){
// //         int top=i;
// //         int left=j;
// //         int right=(2*n-2)-j;
// //         int down=(2*n-2)-i;
// //         cout<< (n-min(min(top,down),min(left,right)));
// //     }
// //     cout<<endl;
// // };
// }