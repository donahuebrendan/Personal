// you can use includes, for example:
// include <algorithm>
#include <iostream>
#include <stack>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++11 (g++ 4.8.2)
    int temp;
    stack<int> add;
    stack<int> sub;
    int returnvalue = -1;
    int size = A.size();
    int frontadd [size];
    int backadd [size];
    for (int i = 0; i < size; i++)
        {

            if(!add.empty())
                {
                    int poptemp = add.top();
                    temp = poptemp + A[i];
                    frontadd[i] = temp;
                    
                }
            else
                {
                    temp = A[0];
                    frontadd[0] = A[0];
                }
            add.push(temp);
            cout << temp << "\n";
            
        }
    cout << "end of calculating front addition\n";
    int b = 1;
    for (int j = size; j > 0; j--)
        {
            int temp2;
            
            if(!sub.empty())
                {
                    int subtemp = sub.top();
                    temp2 = subtemp + A[j-1];
                    backadd[b] = temp2;
                    b++;
                }
            else
                {
                    temp2 = A[j-1];
                    backadd[0] = temp2;
                }
        sub.push(temp2);
        cout << temp2 << "\n";
       
        }
    for(int a = 0; a<size; a++)
    {
        for(int b = 0; b<size; b++)
        {
         if (frontadd[a] == backadd[b])
            {
            cout << "\n";
            cout << "front match found at " << a << " : " <<frontadd[a];
            cout << "back match found at " << b << " : " <<backadd[b];
            cout << "\n";
            
            if(a+b+2 == size-1)
                {
                cout<<"True match found at"<< a << " : "<<b<<"\n";
                returnvalue = a+1;
                }
            }
        }
    }
    
    
    

    return returnvalue;
}
