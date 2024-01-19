#include <sstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string cinLine()
{
    cin.ignore();
    string tempVar {};
    getline(cin, tempVar);
    return tempVar;
}

long long int stringToInt(string num)
{
    long long int convertedVal = 0;
    stringstream strConverterOBJ;
    strConverterOBJ << num;
    strConverterOBJ >> convertedVal;
    return convertedVal;
}

int printIntVector(vector<long long int> lst)
{
    cout << "[";
    for(int i=0; i<lst.size(); i++){
        if(i!=lst.size()-1) {
            cout << lst.at(i) << ", ";
        }else{
            cout << lst.at(i);
        }
    }
    cout << "]" << endl;
    return 0;
}

string printStrVector(vector<string> lst)
{
    for(int i=0; i<lst.size(); i++){
        if(i!=lst.size()-1) {
            cout << lst.at(i) << endl;
        }else{
            cout << lst.at(i);
        }
    }
    return "";
}

vector<long long int> splitStringOutInt(char divider, string str)
{
    vector<long long int> intList;
    for(long long int j=0; j<=str.length(); j++){
        long long int answer {};
        if(str[j] == divider || j == str.length()){
            answer = stringToInt(str.substr(0, j+1));
            str.erase(0,j+1);
            intList.insert(intList.end(), answer);
            j=0;
        }
    }
    return intList;
}


int main()
{
    long long int inputs;
    return 0;
}