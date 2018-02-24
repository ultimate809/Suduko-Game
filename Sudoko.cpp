#include<bits/stdc++.h>
using namespace std;
bool check(int mat[9][9],int row,int col,int val)
{
    for(int i=0;i<9;i++)
    {
        if(mat[row][i]==val||mat[i][col]==val)
        {
            return false;
        }
    }
    int bi,bj;
    bi=(row/3)*3;
    bj=(col/3)*3;
    for(int i=bi;i<bi+3;i++)
    {
        for(int j=bj;j<bj+3;j++)
        {
            if(mat[i][j]==val)
            {
                return false;
            }
        }
    }
    return true;
}
void input(int mat[9][9])
{
    int val;
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            cin>>val;
            mat[i][j]=val;
        }
    }
}
void find_zero(int mat[9][9],int &row,int &col)
{
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            if(mat[i][j]==0)
            {
                row=i;
                col=j;
                
                return ;
            }
        }
    }
}
int sudoko(int mat[9][9])
{
    int row=-1,col=-1,flag=0;
    find_zero(mat,row,col);
    
    if(row==-1)
    {
        //cout<<row<<col;
        return 1;
        
    }//
    for(int i=1;i<10;i++)
    {
        //cout<<i;
        if(check(mat,row,col,i))
        {
            //cout<<row<<col<<i;
            mat[row][col]=i;
            if(sudoko(mat)==1)
            {
                return 1;
            }
            else
            {
                mat[row][col]=0;
            }
        }
    }
    return 0;
    
}
void output(int mat[9][9])
{
    cout<<endl;
    cout<<"******************\n";
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<"******************\n";
    cout<<endl;
}
int main()
 {
	int t;
	cout<<"Enter the number of Sudoko to solve : ";
        cin>>t;
        while(t--)
        {
        	cout<<"Enter the Sudoko to solve and 0 ( zero ) for blank spaces : \n"; 
          int mat[9][9];
          input(mat);
          sudoko(mat);
          output(mat);
        }

	return 0;
}
