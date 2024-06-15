#include <cppitertools/range.hpp> // NOLINT(build/include_order)
#include <iostream>               // NOLINT(build/include_order)
inline int A(int m, int n) {
  if (m == 0) {
    return n + 1;
  }
  if (n == 0) {
    return A(m - 1, 1);
  }
  return A(m - 1, A(m, n - 1));
}

inline auto check_a() {
  for (auto m : iter::range(4)) {
    for (auto n : iter::range(5)) {
      std::cout << m;
      std::cout << " ";
      std::cout << n;
      std::cout << " ";
      std::cout << A(m, n);
      std::cout << std::endl;
    }
  }
}
