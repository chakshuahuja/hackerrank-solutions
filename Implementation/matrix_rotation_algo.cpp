#include <iostream>
int main() {
  int R, C, no_of_rotations;
  std::cin >> R >> C >> no_of_rotations;
  long int input[300][300];
  long int output[300][300];
  for(int i = 1; i <= R; i++)
    for(int j = 1; j <= C; j++)
      std::cin >> input[i][j];
  int no_of_rectangles = std::min(R, C)/2;
  for(int rect = 1; rect <= no_of_rectangles; rect++) {
    int effective_rotations = no_of_rotations % (2 * (R + C - (4 * (rect - 1)) - 2));
  
    for(int rot = 0; rot < effective_rotations; rot++) {
      int var = input[rect][rect];
      //Upper row
      for(int j = rect; j < (C-rect+1); j++) {
	input[rect][j] = input[rect][j+1];
      }
      //Right Column
      for(int i = rect; i < (R-rect+1); i++) {
	input[i][C-rect+1] = input[i+1][C-rect+1];
      }
      //Lower row
      for(int j = (C-rect+1); j > rect; j--) {
	input[R-rect+1][j] = input[R-rect+1][j-1];
      }
      //Left Column
      for(int i = (R-rect+1); i > rect; i--) {
	input[i][rect] = input[i-1][rect];
      }      
      input[rect+1][rect] = var;
    }
  }
  for(int i = 1; i <= R; i++) {
    for(int j = 1; j <= C; j++) {
      std::cout << input[i][j] << " ";
    }
    std::cout << std::endl;
  }
}
