#include <iostream>
#include <vector>
#include <algorithm>
int main() {
  int N, M;
  std::cin >> N >> M;
  char arr[501][501];
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      char val;
      std::cin >> val;
      arr[i][j] = val;
    }
  }
  //Constructing left array for easy computation
  int left[N][M];
  for(int i = 0; i < N; i++) {
    if(arr[i][0] == 'x')
        left[i][0] = -1;
    else
        left[i][0] = 0;
  }
  for(int i = 0; i < N; i++) {
    for(int j = 1; j < M; j++) {
      if(arr[i][j] == 'x')
	left[i][j] = -1;
      else
	left[i][j] = left[i][j-1] + 1;
    }
  }
//Constructing up array for easy computation
  int up[N][M];
  for(int i = 0; i < M; i++) {
    if(arr[0][i] == 'x')
        up[0][i] = -1;
    else
        up[0][i] = 0;
  }
  for(int i = 1; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(arr[i][j] == 'x')
	up[i][j] = -1;
      else
	up[i][j] = up[i-1][j] + 1;
    }
  }

  int maximum = 0;
  for(int r1 = 0; r1 < N; r1++) {
    for(int r2 = r1+1; r2 < N; r2++) {
      int rdiff = r2 - r1;
      std::vector<int> v;
      for(int i = 0; i < M; i++) {
	if(up[r2][i] >= rdiff)
	  v.push_back(i);
      }
      int l = 0, r;
      for(r = 0; r < v.size(); r++) {
	int min_left = v[r] - std::min(left[r1][v[r]], left[r2][v[r]]);
	while(v[l] < min_left)
	  l++;
	if(v[r] > v[l])
	  maximum = std::max(maximum, 2*(rdiff) + 2*(v[r] - v[l]));
      }
    }
  }
  if(maximum == 0)
      std::cout << "impossible" << std::endl;
  else
      std::cout <<  maximum << std::endl;
}
