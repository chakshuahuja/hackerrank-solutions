#include <iostream>
#include <vector>
#include <list>
int cnt = 0;
long long nC2(long long n) {
  if(n < 2)
    return 0;
  else
    return (n * (n-1))/2; 
}
void dfs(std::vector< std::list<int> >& adjacencyList, int s, int *visited, int no_of_astronauts) {
  visited[s] = true;
  cnt++;
  std::list<int>::iterator it;
  for(it = adjacencyList[s].begin(); it != adjacencyList[s].end(); ++it) {
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
      cnt = 0;
      dfs(adjacencyList, i, visited, no_of_astronauts);
      count[no_of_components] = cnt;
      no_of_components++;
    }
  }
  long long answer = 0;
  long long total_pairs = nC2(no_of_astronauts);
  for(long long i = 0; i < no_of_components; i++) {
    if(count[i] > 1)
      answer += (nC2(count[i]));
  }
  std::cout << total_pairs - answer << std::endl;
}
