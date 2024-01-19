#include <iostream>
using namespace std;
int main()
{
	string tempVar {};
	getline(cin, tempVar);
	int sq = stoi(tempVar.substr(0, tempVar.find(" ")));
	int cr = stoi(tempVar.substr(tempVar.find(" "), tempVar.length()));
	sq *= sq;
	cr *= 3.14 * cr;
	if(sq > cr){
		cout << "SQUARE";
	}else{
		cout << "CIRCLE";
	}
	return 0;
}