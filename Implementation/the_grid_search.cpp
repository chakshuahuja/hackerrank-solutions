#include <iostream>
bool check_two_blocks(int r, int c, char a[1000][1000], char b[1000][1000], int x, int y) {
  int flag = 0;
  for(int i = 0; i < r; i++) {
    for(int j = 0; j < c; j++) {
      if(a[i][j] != b[i+x][j+y]) {
	flag = 1;
	goto result;
      }
      else continue;
    }
  }
  if(!flag) return true;
 result : return false;
}
int main() {
  int test_cases;
  std::cin >> test_cases;
  int R, C, r, c; 
  char grid[1000][1000];
  char search[1000][1000];
  for(int k = 0; k < test_cases; k++) {
    int flag = 0;
    std::cin >> R;
    std::cin >> C;
    char dummy;
    for(int i = 0; i < R; i++) {
      std::cin.get();
      for(int j = 0; j < C; j++) {
	std::cin.get(dummy);
	grid[i][j] = dummy;
      }
    }
    std::cin >> r >> c;
    for(int i = 0; i < r; i++) {
      std::cin.get();
      for(int j = 0; j < c; j++) {
	std::cin.get(dummy);
	search[i][j] = dummy;
      }
    }
    for(int i = 0; i < R; i++) {
      if((i+r) > R)
	break;
      for(int j = 0; j < C; j++) {
	if((j+c) > C)
	  break;
	if(check_two_blocks(r, c, search, grid, i, j)) {
	  std::cout << "YES" << std::endl; flag = 1;
	}
      }
    }
    if(flag == 0)
      std::cout << "NO" << std::endl;
  }
} 
