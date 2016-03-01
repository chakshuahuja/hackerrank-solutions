#include <iostream>
#include <queue>
#include <list>
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
    std::vector< std::list< std::pair<int, int> > > adjacencyList(N);
    
    for(int i = 0; i < N; i++) {
      dist[i] = 999999;
      visited[i] = false;
    }
    for(int i = 0; i < M; i++) {
      int x, y, r;
      std::cin >> x >> y >> r;
      int flag = 0;
      for(std::list< std::pair<int, int> >::iterator it = adjacencyList[x-1].begin(); it != adjacencyList[x-1].end(); ++it) {
        if(it->first == (y-1)) {  
          if(it->second > r)
            it->second = r;
          flag = 1;
	}
      }
      if(flag == 0)
        adjacencyList[x - 1].push_back(std::pair<int, int>(y - 1, r));
      flag = 0;
      for(std::list< std::pair<int, int> >::iterator it = adjacencyList[y-1].begin(); it != adjacencyList[y-1].end(); ++it) {
        if(it->first == (x-1)) {  
          if(it->second > r)
            it->second = r;
          flag = 1;
	}
      }
      if(flag == 0)
        adjacencyList[y - 1].push_back(std::pair<int, int>(x - 1, r));
    }
    int S;
    std::cin >> S;
    dist[S-1] = 0;
    for(int count = 0; count < N-1; count++) {
      int w = minimum_dist();
      if(w == -1)
          break;
      visited[w] = true;
      for(std::list< std::pair<int, int> >::iterator v = adjacencyList[w].begin(); v != adjacencyList[w].end(); ++v) {
	if(!visited[v->first] && dist[w] != 999999) {
	  if(dist[v->first] > (dist[w] + v->second))
	    dist[v->first] = dist[w] + v->second;
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
