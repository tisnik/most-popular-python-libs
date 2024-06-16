#include <cppitertools/range.hpp> // NOLINT(build/include_order)
#include <vector>                 // NOLINT(build/include_order)
template <typename T0> List fill_in_list(T0 size) {
  std::vector<
      decltype(std::declval<typename decltype(range(size))::value_type>() + 1)>
      l = {};
  for (auto i : iter::range(size)) {
    l.push_back(i + 1);
  }
  return l;
}
