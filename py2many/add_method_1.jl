struct Foo
_value::
end

function __init__{T0}(self::Foo, value::T0)
self._value = value
end

function __add__{T0}(self::Foo, other::T0)::Foo
return Foo(self._value + other._value)
end

function __str__(self::Foo)::String
return "*"*self._value
end

