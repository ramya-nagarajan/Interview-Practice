using namespace std;
#include<iostream>
#include<stack>
#include<string>

class myQueue
{
    public:
    stack<int> s;

    void push_stk(int x)
    {
        pushHelper(x);
    }
    void pushHelper(int x)
    {
        //cout<<x<<endl;
        if(s.size() == 0)
        {
            s.push(x);
            return;
        }
        int top = s.top();
        s.pop();
        pushHelper(x);
        s.push(top);
        return;
    }
    void display()
    {
        cout<<"Queue is "<<endl;
        while(!s.empty())
        {
            int elem = s.top();
            cout<<elem<<std::endl;
            s.pop();
        }
    }
    void stack_to_queue(stack<int> stk)
    {
        //stack<int> stk2;

       //using 2 stacks
       /* while(!stk.empty())
        {
            int elem = stk.top();
            //cout<<elem<<endl;
            stk.pop();
            stk2.push(elem);
        }
        //print the queue
        while(!stk2.empty())
        {
            int elem = stk2.top();
            cout<<elem<<std::endl;
            stk2.pop();
        }*/
    }
};
int main()
{
    //call constructor
    myQueue s;
    s.push_stk(1);
    s.push_stk(2);
    s.push_stk(3);
    s.display();
    //cout<<"stack contents "<<s.size()<<endl;
    /*while(!s.empty())
    {
        int elem = s.top();
        cout<<elem<<std::endl;
        s.pop();
    }*/

    //stack_to_queue(s);
    return 0;
}
