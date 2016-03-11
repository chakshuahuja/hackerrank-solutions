#include <iostream>
#define INF 999999
struct AdjListNode {
  int dest;
  int weight;
  AdjListNode* next;
};
struct AdjList {
  AdjListNode* head;
};
class Graph {
public:
  int V;
  AdjList* array;
  Graph(int V) {
    this->V = V;
    array = new AdjList[V];
    for(int i = 0; i < V; i++) {
      array[i].head = NULL;
    }
  }
  AdjListNode* newAdjListNode(int dest, int weight) {
    AdjListNode* node = new AdjListNode;
    node->dest = dest;
    node->weight = weight;
    return node;
  }
  void addEdge(int src, int dest, int weight) {
    AdjListNode* node = newAdjListNode(dest, weight);
    node->next = array[src].head;
    array[src].head = node;
    node = newAdjListNode(src, weight);
    node->next = array[dest].head;
    array[dest].head = node;
  }
  void printGraph() {
    for(int i = 0; i < V; i++) {
      AdjListNode* p = array[i].head;
      std::cout << i << "->";
      while(p) {
	std::cout << p->dest << "(" << p->weight << ")" << "->";
	p = p->next;
      }
      std::cout << "NULL" << std::endl;
    }
  }
  int minimum_dist(bool* visited, int* dist) {
    int minimum = INF;
    int min_index = -1;
    for(int i = 0; i < V; i++) {
      if(!visited[i] && minimum > dist[i]) {
	minimum = dist[i];
	min_index = i;
      }
    }
    return min_index;
  } 
  void dijkstra(bool* visited, int* dist) {
    for(int i = 0; i < V; i++) {
      visited[i] = false;
      dist[i] = INF;
    } 
    dist[0] = 0;
    for(int count = 0; count < V; count++) {
      int u = minimum_dist(visited, dist);
      if(u == -1)
	break;
      visited[u] = true;
      AdjListNode* v = array[u].head;
      while(v) {
	if(!visited[v->dest]) {
	  int initial_weight = dist[v->dest];
	  if(dist[v->dest] == INF)
	    dist[v->dest] = v->weight;
	  if(v->weight > dist[u])
	    dist[v->dest] = v->weight;
	  else
	    dist[v->dest] = dist[u];
	  if(dist[v->dest] > initial_weight)
	    dist[v->dest] = initial_weight;
	}
	v = v->next;
      }
    }
    if(dist[V-1] == INF)
      std::cout << "NO PATH EXISTS";
    else
      std::cout << dist[V-1];
    std::cout << std::endl;
  }
  ~Graph() {
    delete []array;
  }
};
int main() {
  int N, E;
  std::cin >> N >> E;
  Graph g(N);
  for(int i = 0; i < E; i++) {
    int x, y, w;
    std::cin >> x >> y >> w;
    g.addEdge(x-1, y-1, w);
  }
  //  g.printGraph();
  bool* visited = new bool[N];
  int* dist = new int[N];
  g.dijkstra(visited, dist);
  g.~Graph();
}
