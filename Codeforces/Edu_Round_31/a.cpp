#include < bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	vector < int > v;
	int b;
	for( int  i=0 ; i < n ; i++)
	{
		cin>>b;
		if(i==0)
		{
			if(b==3)
			{
				cout<<"NO";
				return 0;
			}
		}
		v.push_back(b);
	}
	if(n==1)
	{
		cout<<"YES";
		return 0;
	}
	if(n==2)
	{
		if(((v[0]==1)&&(v[1]==2))||((v[0]==2)&&(v[1]==1)))
			{
				cout<<"NO";
				return 0;
			}
		else
		{
			cout<<"YES";
			return 0;
		}

	}
	for ( int i = 1 ; i < n-1 ; i++)
	{
		if(v[i-1]==v[i+1] && v[i]!=v[i-1])
		{
			print("NO");
			return 0;
		}
	}
cout<<"YES";