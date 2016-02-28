#include <iostream>
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
        left[0][i] = -1;
    else
        left[0][i] = 0;
  }
  for(int i = 1; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(arr[i][j] == 'x')
	up[i][j] = -1;
      else
	up[i][j] = up[i-1][j] + 1;
    }
  }
  int output[N][M];
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(left[i][j] == 0 || up[i][j] == 0 || left[i][j] == -1 || up[i][j] == -1)
	output[i][j] = 0;
      else {
	output[i][j] = 2*(left[i][j] + up[i][j]);
      }
    }
  }
  int max = 0;
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(max < output[i][j])
	max = output[i][j];
    }
  }
  if(max == 0)
      std::cout << "impossible" << std::endl;
  else
      std::cout <<  max << std::endl;
}
