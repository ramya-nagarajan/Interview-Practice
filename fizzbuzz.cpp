using namespace std;
#include<iostream>
#include<string>

bool checkDigit(int i,int p, int q)
{
    bool flag = false;

    while(i>0){
        int r = i%10;
        if(r==p||r==q){
            flag = true;
            return flag;
        }
        i= i/10;
    }
    return false;
}

int main(void){

    int N, p, q;
    cout<<"\nEnter N, p and q"<<endl;
    cin>>N>>p>>q;
    for(int i=N;i>=1;i--){
       // ((i%3==0) && (i%5==0) ? cout<<"\nFizzBuzz"<<endl : ((i%3==0) ? cout<<"\nFizz"<<endl; : (i%5==0)) ? cout<<"\nBuzz"<<endl; : cout<<i<<endl;);
        /*if((i%3==0) && (i%5==0))
            cout<<"\nFizBuzz"<<endl;
        else if(i%3 ==0)
            cout<<"\nFizz"<<endl;
        else if(i%5 ==0)
            cout<<"\nBuzz"<<endl;
        else
            cout<<i<<endl;*/
        bool condition1 =  ((i%p == 0) || (i%q == 0));
        bool condition2 = checkDigit(i,p,q);
        if((condition1 && condition2)){
            cout<<"OUTTHINK,";
        }
        else if(condition1){
            cout<<"OUT,";
        }

        else if(condition2){
            cout<<"THINK,";
        }
        else{
            cout<<i<<",";
        }
    }
    return 0;
}

