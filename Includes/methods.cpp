//methods.cpp
#include "methods.h"
#include "colors.h"
#include <iostream>
#include <windows.h>
#include <sstream>
#include <Lmcons.h>
#include <time.h>
#include <stdio.h>
#include <stdarg.h>

using namespace std;

int randomInt(int min, int max) {
	return rand() % (max - min) + min;
}