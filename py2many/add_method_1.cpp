class Foo {
public:
  auto _value;

  template <typename T0> void __init__(T0 value) { auto this->_value = value; }

  template <typename T0> Foo __add__(T0 other) {
    return Foo((this->_value) + (other._value));
  }

  inline std::string __str__() { return std::string{"*"} * (this->_value); }
};
