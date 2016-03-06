#include <iostream>
int graph[3000][3000];
int mstSet[3000];
int N, M;
int dist[3000];
#define INF 99999;
int minimum_dist() {
  int minimum = INF;
  int min_index = -1;
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
  dist[0] = 0;
  
  for(int count = 0; count < N-1; count++) {
    int u = minimum_dist();
    mstSet[u] = true;
    for(int v = 0; v < N; v++) {
      if(graph[u][v] != -1 && !mstSet[v] && dist[v] > graph[u][v]) {
	dist[v] = graph[u][v];
      }
    }
  }
  int sum = 0;
  for(int i = 0; i < N; i++) {
    sum += dist[i];
  }
  std::cout << sum << std::endl;
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
    graph[x-1][y-1] = r;
    graph[y-1][x-1] = r;
  }
  int src;
  std::cin >> src;
  prims();
}
