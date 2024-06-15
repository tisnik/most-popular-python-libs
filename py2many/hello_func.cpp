#include <iostream> // NOLINT(build/include_order)
inline void hello() {
  std::cout << std::string{"Hello, world!"};
  std::cout << std::endl;
}

hello();
