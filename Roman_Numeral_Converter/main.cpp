#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

//Convert a character to decimal, and ensure it is a proper roman numeral
int convertValue(char romanSymbol) {
    if (romanSymbol == 'I') {
        return 1;
    } else if (romanSymbol == 'V') {
        return 5;
    } else if (romanSymbol == 'X') {
        return 10;
    } else if (romanSymbol == 'L') {
        return 50;
    } else if (romanSymbol == 'C') {
        return 100;
    } else if (romanSymbol == 'D') {
        return 500;
    } else if (romanSymbol == 'M') {
        return 1000;
    } else {
        return -1;
    }
}

int convertRomantoInt(string numeral) {
    int converted = 0;
    for (int i = 0; i < numeral.length(); i++) { //walk through the character array
        int a = convertValue(numeral[i]); //convert current roman index to decimal
        if (a == -1) //if not a roman numeral
            return a; //the whole char array is wrong

        if (i + 1 < numeral.length()) { //check for roman subtraction
            int b = convertValue(numeral[i + 1]); //convert the next roman index to decimal
            if (b == -1) //if not a roman numeral
                return b; //the whole char array is wrong
            if (a >= b) { //if current is greater than the next index
                converted += a; //current is good
            } else { //else, current is smaller than the next
                converted += (b - a); //subtract current from next
                i++;
            }
        } else { //we are at the end of the array
            converted += a; //return the last index
        }
    }
    //conversion is finished
    return converted;
}


int main() {
    printf("Please enter a number in Roman Numeral form: ");
    string numeral;
    cin >> numeral;
    int value = convertRomantoInt(numeral);
    if (value != -1) {
        printf("\nInteger form: %i\n", value);
    } else {
        printf("\nInvalid format, please use the following roman numeral notation:\n");
        printf("[I-1, V-5, X-10, L-50, C-100, D-500, M-1000]\n");
    }
    return 0;
}
