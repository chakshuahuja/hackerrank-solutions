#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
int main() {
  int test_cases;
  std::cin >> test_cases;
  for(int t = 0; t < test_cases; t++) {
    std::string str;
    std::cin >> str;
    int N = str.length();
    int count = 0;
    std::map<std::string, int> pairs;
    for(int len = 1; len < N; len++) {
      for(int i = 0; i < N-len+1; i++) {
	std::string s = str.substr(i, len);
	std::sort(s.begin(), s.end());
	pairs[s]++;
      }
    }
    for(std::map<std::string, int>::iterator it = pairs.begin(); it != pairs.end(); it++) {
      count += ((it->second)*(it->second-1))/2;
    }
    std::cout << count << std::endl;
  }
}
