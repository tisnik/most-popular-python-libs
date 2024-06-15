#include <cppitertools/range.hpp> // NOLINT(build/include_order)
#include <iostream>               // NOLINT(build/include_order)
template <typename T0, typename T1> int A(T0 m, T1 n) {
  if (m == 0) {
    return n + 1;
  }
  if (n == 0) {
    return A(m - 1, 1);
  }
  return A(m - 1, A(m, n - 1));
}

inline void check_a() {
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
