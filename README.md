# Competitive Programming Solutions

## Overview

This repository showcases my solutions to various competitive programming problems, primarily from DMOJ (Don Mills Online Judge) and the University of Waterloo contests. It serves as a personal progress tracker and a resource for others interested in competitive programming.

## Repository Structure

- **DMOJ**: Contains solutions for problems from Don Mills Online Judge.
- **Waterloo**: Includes solutions for University of Waterloo contest problems.

Solutions are organized by contest or problem set within each folder. Each solution file is named after the problem code or title for easy reference.

## Technologies

- **Languages**: Mainly Python and C++.
- **Environment**: Developed in various IDEs compatible with the above languages.

## Problems and Solutions

Each problem is briefly described in its corresponding solution file, along with a detailed explanation of my approach.




## Contact

For any queries or feedback, feel free to reach out to me at [gdhesi2005@gmail.ca](mailto:gdhesi2005@gmail.ca).




## Example

```cpp
// START CP CODE
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

// END CP CODE



int main()
{
    long long int inputs;
    cin >> inputs;
    vector<string> answers {};
    for(int i=0; i<inputs; i++) {
        string inputVal;
        inputVal = cinLine();
        vector<long long int> inputValVec = splitStringOutInt(' ', inputVal);
        if(inputValVec.at(0) * inputValVec.at(1) == inputValVec.at(2)){
            answers.insert(answers.end(), "POSSIBLE DOUBLE SIGMA");
        }else{
            answers.insert(answers.end(), "16 BIT S/W ONLY");
        }
        inputValVec.clear();
    }
    printStrVector(answers);
    return 0;
}
