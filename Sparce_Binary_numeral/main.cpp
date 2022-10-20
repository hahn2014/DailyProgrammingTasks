#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int* convertToBinary(unsigned int decimal) {
    int binary[32];
    unsigned int mask = 1 << (sizeof(int) * 8 - 1);

    for(int i = 0; i < sizeof(int) * 8; i++) {
        if((decimal & mask) == 0 ) {
            cout << '0' ;
            binary[i] = 0;
        } else {
            binary[i] = 1;
            cout << '1' ;
        }
        mask  >>= 1;
    }
  // // cout << endl ;
  //   int i = 0;
  //
  //   while (i > 0) {
  //       binary[i] = decimal % 2;
  //       decimal = decimal / 2;
  //       i++;
  //   }
    return binary;
}

void printBinary(int* binary) {
    for (int i = 0; i < sizeof(binary); i++) {
        printf("%i", binary[i]);
    }
}

int nextSparceInt(int n) {

    return 0;
}

int main() {
    printf("Give me an integer: ");
    int numeral;
    cin >> numeral;

    int* binary = convertToBinary(numeral);
    printf("\n%i in binary - ", numeral);
    printBinary(binary);
    int nextSparce = nextSparceInt(numeral);
    printf("\nThe next sparce integer is %i", nextSparce);
    return 0;
}
