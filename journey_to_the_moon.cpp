#include <iostream>
void dfs(int *graph, int s, int *visited, int no_of_astronauts) {
  visited[s] = true;
  for(int i = 0; i < no_of_astronauts; i++) {
    if(*((graph + s*no_of_astronauts) + i)) {
      if(!visited[i]) {
	dfs(graph, i, visited, no_of_astronauts);
      }
    }
  }
}
int main() {
  int no_of_astronauts;
  int l;
  std::cin >> no_of_astronauts >> l;
  int graph[no_of_astronauts][no_of_astronauts];
  for(int i = 0; i < no_of_astronauts; i++) {
    for(int j = 0; j < no_of_astronauts; j++) {
      graph[i][j] = 0;
    }
  }
  for(int i = 0; i < l; i++) {
    int A, B;
    std::cin >> A >> B;
    graph[A][B] = 1;
    graph[B][A] = 1;
  }
  int visited[no_of_astronauts];
  for(int i = 0; i < no_of_astronauts; i++) {
    visited[i] = false;
  }
  int no_of_components = 0;
  int count[l];
  for(int i = 0; i < no_of_astronauts; i++) {
    if(!visited[i]) {
      int visited_before = 0;
      for(int j = 0; j < no_of_astronauts; j++) {
	if(visited[j])
	  visited_before++;
      }
      dfs((int*)graph, i, visited, no_of_astronauts);
      int visited_after = 0;
      for(int j = 0; j < no_of_astronauts; j++) {
	if(visited[j])
	  visited_after++;
      }
      count[no_of_components] = visited_after - visited_before;
      no_of_components++;
    }
  }
  int answer = 0;
  for(int i = 0; i < no_of_components; i++) {
    for(int j = i+1; j < no_of_components; j++) {
      answer += (count[i]*count[j]);
    }
  }
  std::cout << answer << std::endl;
}
