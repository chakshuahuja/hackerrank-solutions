#include <iostream>
#include <algorithm>
int child[5001][5001];
int main() {
  std::string s1, s2;
  std::cin >> s1 >> s2;
  int l1 = s1.length();
  int l2 = s2.length();

  for(int i = 0; i <= l1; i++) {
    for(int j = 0; j <= l2; j++) {
      if(i == 0 || j == 0)
	child[i][j] = 0;
      else if(s1[i-1] == s2[j-1]) {
	child[i][j] = child[i-1][j-1] + 1;
      }
      else {
	child[i][j] = std::max(child[i-1][j], child[i][j-1]);
      }
    }
  }
  std::cout << child[l1][l2];
}
