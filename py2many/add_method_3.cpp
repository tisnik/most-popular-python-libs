class Foo {
public:
  int _value;

  inline void __init__(int value) { int this->_value = value; }

  inline Foo __add__(Foo other) { return Foo((this->_value) + (other._value)); }

  inline std::string __str__() { return std::string{"*"} * (this->_value); }
};
