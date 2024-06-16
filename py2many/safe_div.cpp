#include <iostream> // NOLINT(build/include_order)
inline int safe_div(int x, int y) {
  try {
    return x / y;
  } catch (const std::exception &e) {
    ExceptHandler /*unimplemented()*/
  } catch (const std::overflow_error &e) {
    std::cout << "OVERFLOW ERROR" << std::endl;
  } catch (const std::runtime_error &e) {
    std::cout << "RUNTIME ERROR" << std::endl;
  } catch (...) {
    std::cout << "UNKNOWN ERROR" << std::endl;
    0
  }
}
