#include <iostream> // NOLINT(build/include_order)
class Visitor {
public:
  int nest_level;

  inline void __init__() { int this->nest_level = 0; }

  template <typename T0> void on_visit(T0 text) {
    std::string indent = (std::string{" "} * (this->nest_level)) * 2;
    std::cout << indent;
    std::cout << " ";
    std::cout << text;
    std::cout << std::endl;
    this->nest_level += 1;
  }

  template <typename T0> void on_leave(T0 node) { this->nest_level -= 1; }
};
