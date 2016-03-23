#include <iostream>
#include <algorithm>
#include <math.h>
int main() {
  std::string input;
  getline(std::cin, input, '\n');
  int L = input.length();
  double LsquareRoot = sqrt(L);
  int lower = LsquareRoot;
  int upper;
  if(lower == LsquareRoot) {
    upper = lower;
  }
  else
    upper = lower + 1;
  int rows;
  int columns = upper;
  int counter = 0;
  if(L > (upper*lower))
    rows = upper;
  else
    rows = lower;
  int last_element_column = L - ((rows-1)*columns);
  char output[rows][columns];
  int k = 0;
  for(int i = 0; i < rows; i++)
    for(int j = 0; j < columns; j++) {
      if(k == L)
	goto result;
      output[i][j] = input[k];
      k++;
    }
 result:
  for(int j = 0; j < columns; j++) {
    for(int i = 0; i < rows; i++) {
      if(!((i == (rows-1)) && (j >= last_element_column)))
	std::cout << output[i][j];
    }
    std::cout << " ";
  }
}
