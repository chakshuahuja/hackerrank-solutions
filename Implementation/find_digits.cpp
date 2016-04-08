#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
  int test_cases;
  std::cin >> test_cases;
  int N;
  int orignal_number;
  for(int i = 0; i < test_cases; i++) {
    std::cin >> N;
    int digit;
    int count = 0;
    orignal_number = N;
    while(N) {
      digit = N % 10;
      N = N / 10;
      if(!((digit == 0) || (orignal_number % digit)))
	count++;
      else 
	continue;
    }
    std::cout << count << std::endl;
  }
  return 0;
}
