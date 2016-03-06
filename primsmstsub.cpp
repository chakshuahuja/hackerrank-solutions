#include <iostream>
int graph[3000][3000];
int mstSet[3000];
int N, M;
int dist[3000];
int minimum_dist() {
  int minimum = INF, min_index = -1;
  for(int i = 0; i < N; i++) {
    if(!mstSet[i] && dist[i] < minimum) {
      minimum = dist[i];
      min_index = i;
    }
  }
  return min_index;
}
void prims() {
  for(int i = 0; i < N; i++) {
    mstSet[i] = false;
    dist[i] = INF;
  }
  mstSet[0] = true;
  dist[0] = 0;
  int u = minimum_dist();
  while(u != -1) {
    
  }
}
int main() {
  std::cin >> N >> M;
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      graph[i][j] = -1;
    }
  }
  for(int i = 0; i < M; i++) {
    int x, y, r;
    std::cin >> x >> y >> r;
    graph[x][y] = r;
    graph[y][x] = r;
  }
  prims();
}
