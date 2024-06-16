template <typename T0> int factorial(T0 n) {
  if (n < 0) {
    return NULL;
  }
  if (n == 0) {
    return 1;
  }
  int result = n * (factorial(n - 1));
  return result;
}
