#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int speak(const vector<int> &data, int target) {
  unordered_map<int, pair<int, int>> pos;
  for (int i = 0; i < data.size(); ++i) {
    pos[data[i]] = {i + 1, 0};
  }

  int last = data.back();
  for (int cur = data.size() + 1; cur <= target; ++cur) {
    if (pos.find(last) != pos.end()) {
      auto x = pos[last];
      if (x.second == 0) {
        last = 0;
      } else {
        last = x.first - x.second;
      }
    } else {
      last = 0;
    }
    if (pos.find(last) != pos.end()) {
      pos[last] = {cur, pos[last].first};
    } else {
      pos[last] = {cur, 0};
    }
  }
  return last;
}

int main(int argc, char **argv) {
  int size = 30000000;
  if (argc > 1) {
    size = stoi(argv[1]);
  }
  cout << speak({6, 13, 1, 15, 2, 0}, size) << endl;
  return 0;
}
