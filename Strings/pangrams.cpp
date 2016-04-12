#include <iostream>
#include <set>
int main() {
  std::set<char> myset;
  for(char c = 'a'; c <= 'z'; c++)
    myset.insert(c);
  std::string str;
  getline(std::cin, str, '\n');
  std::set<char> strset;
  for(int i = 0; i < str.length(); i++)
    if(!(str[i] == ' '))
      strset.insert(tolower(str[i]));
  /* for(std::set<char>::iterator it = myset.begin(); it != myset.end(); ++it)
     std::cout << *it << " ";
     std::cout << std::endl;
  for(std::set<char>::iterator it = strset.begin(); it != strset.end(); ++it)
  std::cout << *it << " ";
  std::cout << std::endl;
  */
  if(strset == myset)
    std::cout << "pangram" << std::endl;
  else 
    std::cout << "not pangram" << std::endl;
}
