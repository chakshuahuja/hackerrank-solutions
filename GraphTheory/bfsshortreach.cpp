#include <iostream>
#include <queue>
#include <list>
#define INF 999999
int main() {
  int T;
  std::cin >> T;
  for(int t = 0; t < T; t++) {
    int N, M;
    std::cin >> N >> M;
    std::vector< std::list<int> > adjacencyList(N);
    for(int i = 0; i < M; i++) {
      int A, B;
      std::cin >> A >> B;
      adjacencyList[A - 1].push_back(B - 1);
      adjacencyList[B - 1].push_back(A - 1);
    }
    int S;
    std::cin >> S;
    int visited[N];
    int dist[N];
    int prev[N];
    for(int i = 0; i < N; i++) {
      visited[i] = false;
      dist[i] = INF;
      prev[i] = -1;
    }
    dist[S-1] = 0;
    visited[S-1] = true;
    std::queue<int> Q;
    Q.push(S-1);
    while(!Q.empty()) {
      int v = Q.front();
      Q.pop();
      for(std::list<int>::iterator it = adjacencyList[v].begin(); it != adjacencyList[v].end(); ++it) {
	if(!visited[*it]) {
	  visited[*it] = true;
	  Q.push(*it);
	  prev[*it] = v;
	  if(dist[*it] > dist[v] + 6)
	    dist[*it] = dist[v] + 6;
	}
      }
    }
    for(int i = 0; i < N; i++) {
      if(i != (S - 1)) {
	if(dist[i] == INF)
	  std::cout << "-1" << " ";
	else
	  std::cout << dist[i] << " ";
      }
    }
    std::cout << std::endl;
  }
}
