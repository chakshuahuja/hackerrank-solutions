#include <iostream>
int graph[3001][3001];
int dist[3001];
int visited[3001];
int N, M;
int minimum_dist() {
    int minimum = 99999, min_index = -1;
    for(int i = 0; i < N; i++) {
        if(!visited[i] && dist[i] < minimum) {
            minimum = dist[i];
            min_index = i;
        }
    }
    return min_index;
}

int main() {
  int T;
  std::cin >> T;
  for(int t = 0; t < T; t++) {
    std::cin >> N >> M;
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
	graph[i][j] = -1;
      }
    }
    for(int i = 0; i < N; i++) {
      dist[i] = 999999;
      visited[i] = false;
    }
    for(int i = 0; i < M; i++) {
      int x, y, r;
      std::cin >> x >> y >> r;
      if(graph[x-1][y-1] == -1 || graph[x-1][y-1] > r)
	graph[x-1][y-1] = r; 
      if(graph[y-1][x-1] == -1 || graph[y-1][x-1] > r)
	graph[y-1][x-1] = r;
    }
    int S;
    std::cin >> S;
    dist[S-1] = 0;
    for(int count = 0; count < N-1; count++) {
      int w = minimum_dist();
      visited[w] = true;
      for(int v = 0; v < N; v++) {
	if(graph[w][v] != -1 && !visited[v] && dist[w] != 999999) {
	  if(dist[v] > (dist[w] + graph[w][v]))
	    dist[v] = dist[w] + graph[w][v];
	
      }
    }
    }
    for(int i = 0; i < N; i++) {
        if(dist[i] == 999999)
            std::cout << "-1" << " ";
      if(i != (S-1) && dist[i] != 999999)
	 std::cout << dist[i] << " ";
    }
    std::cout << std::endl;
  }
}
