#include <iostream>
#include <vector>
#include <list>

void dfs(std::vector< std::list<int> >& adjacencyList, int s, int *visited, int no_of_astronauts) {
  visited[s] = true;
  for(std::list<int>::iterator it = adjacencyList[s].begin(); it != adjacencyList[s].end(); ++it) {
    if(!visited[*it]) {
      dfs(adjacencyList, *it, visited, no_of_astronauts);
    }
  }
}
int main() {
  int no_of_astronauts;
  int l;
  std::cin >> no_of_astronauts >> l;
  std::vector< std::list<int> > adjacencyList(no_of_astronauts + 1);
  for(int i = 0; i < l; i++) {
    int A, B;
    std::cin >> A >> B;
    adjacencyList[A].push_back(B);
    adjacencyList[B].push_back(A);
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
      dfs(adjacencyList, i, visited, no_of_astronauts);
      int visited_after = 0;
      for(int j = 0; j < no_of_astronauts; j++) {
	if(visited[j])
	  visited_after++;
      }
      count[no_of_components] = visited_after - visited_before;
      no_of_components++;
    }
  }
  long long answer = 0;
  long long sum = 0;
  for(int i = 0; i < no_of_components; i++) {
    sum = sum + count[i];
  }
  for(int i = 0; i < no_of_components; i++) {
    answer += ((sum - count[i]) * count[i]);
  }
  std::cout << answer / 2 << std::endl;
}
