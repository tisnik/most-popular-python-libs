struct Foo
    _value::Int64
end

function __init__(self::Foo, value::Int64)
    self._value = value
end

function __add__(self::Foo, other::Foo)::Foo
    return Foo(self._value + other._value)
end

function __str__(self::Foo)::String
    return "*"*self._value
end

