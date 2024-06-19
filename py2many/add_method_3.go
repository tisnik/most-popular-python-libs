package main

type Foo struct {
	_value int
}

func __init__(self Foo, value int) {
	self._value = value
}

func __add__(self Foo, other Foo) Foo {
	return Foo{_value: (self._value + other._value)}
}

func __str__(self Foo) string {
	return ("*" * self._value)
}
