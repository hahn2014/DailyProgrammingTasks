/****************************************************
 * 													*
 * 			Day 1 Programming Task					*
 *   -  Given a list of numbers and a number 'k',  	*
 * 	 -	 return whether any two numbers from	   	*
 *	 -	 the list add up to 'k.'				   	*
 * 													*
*****************************************************/

//INCLUDES
#include <stdio.h>
#include <iostream>
#include "../includes/colors.h"
#include "../includes/methods.h"

//NAMESPACE
using namespace std;

//FUNCTION DECLARATIONS
void printMain();
void generateNumbers();
void printResults();

int main() {
	//SetConsoleTitle("Test");

	printMain();
	generateNumbers();
	printResults();

	printf("%s", White);
	return 0;
}

void printMain() {
	printf("%sWelcome to %sDay 1%s Programming Task.\n",Blue, Red, Blue);
	printf("The goal of this programming task is as follows:\n");
	printf("Given a list of numbers and a number, k, ");
	printf("return whether any two numbers from the list add up to k.\n\n");
}

void generateNumbers() {
	printf("%sGenerating Numbers:%s\n", Red, Blue);
	//First generate the list of numbers between 1 and 10
	int listLength = randomInt(1, 10);

	for (int i = 0; i < listLength; i++) {
		//printf("[%i] - %i", i, (randomInt(1, 20)));
	}
	//next generate k

	//next test for sum of two numbers = k

}

void printResults() {

}