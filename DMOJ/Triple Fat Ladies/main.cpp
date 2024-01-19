#include <iostream>
#include <math.h>
using namespace std;


int main()
{
	string tempVarConverter {};
	getline(cin, tempVarConverter);
	int testCases = stoi(tempVarConverter);
	for(int i=0; i<testCases; i++)
	{
		getline(cin, tempVarConverter);
		long long int num = stoi(tempVarConverter)+1;
		if(num < 192){
			num = 192;
		}
		unsigned long long int powe {pow(num, 3)};

 		while (to_string(powe).substr(to_string(powe).length()-3,3) != "888")
		{
			num=num+1;
			powe=pow(num,3);
		}
		cout << num << endl;
	}
	return 0;
}