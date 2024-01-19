#include <iostream>


using namespace std;

int main()
{
	cout << "Ready" << endl;
	while (true){
		string tempVar {};
		getline(cin, tempVar);
		if(tempVar == "  "){
			break;
		}else{
			if(tempVar[0] == 'd' && tempVar[1] == 'b'){
				cout << "Mirrored pair" << endl;
			}else if(tempVar[0] == 'b' && tempVar[1] == 'd'){
				cout << "Mirrored pair" << endl;
			}else if(tempVar[0] == 'q' && tempVar[1] == 'p'){
				cout << "Mirrored pair" << endl;
			}else if(tempVar[0] == 'p' && tempVar[1] == 'q'){
				cout << "Mirrored pair" << endl;
			}else{
				cout << "Ordinary pair" << endl;
			}
		}
	}
	return 0;
}