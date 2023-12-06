//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution 
{
    public:
    //Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& M, int n) 
    {
        stack<int>st;
        
        
        //STEP 1 :Push all persons into stack
        for(int i =0; i<n; i++){
            st.push(i);
        }
        
        //STEP 2 : Run discard method , to get a MightbeCelebrity
        while(st.size() != 1){
            int a = st.top(); st.pop();
            int b = st.top(); st.pop();
            
            // Check if a knows b??
            if(M[a][b]){
                //a is not a celebrity pop a, and push b back, b might be
                st.push(b);
            }
            else{
                //a might be a celebrity
                st.push(a);
            }
        }
        //Step 3 : Check that single person left in stack is a celebrity or not?
        int mightBeCelebrity = st.top(); st.pop();
        
        //CONDITION: Celebrity should not know anyone
        //and that can be check by if the celebrity all rows is 0 or not 
        // if all rows are 0 that means it could be a celebrity(we have to check another
        //condition as well)
        for(int i = 0; i<n; i++){
            if( M[mightBeCelebrity][i] != 0){
                return -1;
            }
        }
        //2nd CONDITION all cols of celebrity should be 1 except the celebrity wala chodh ke
        // OR can be say all elemnts should be 1 except the diagonal element
        for(int i = 0; i<n; i++){
            if(M[i][mightBeCelebrity] == 0 && i!= mightBeCelebrity){
                return -1;
            }
        }
        //mightBeCelebrity is the celebrity
        return mightBeCelebrity;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int> > M( n , vector<int> (n, 0));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>M[i][j];
            }
        }
        Solution ob;
        cout<<ob.celebrity(M,n)<<endl;

    }
}

// } Driver Code Ends