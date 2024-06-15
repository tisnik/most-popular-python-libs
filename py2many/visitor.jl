struct Visitor
nest_level::Int64
end

function __init__(self::Visitor)
self.nest_level = 0
end

function on_visit{T0}(self::Visitor, text::T0)
indent = " "*self.nest_level*2
println(join([indent, text], " "));
self.nest_level += 1
end

function on_leave{T0}(self::Visitor, node::T0)
self.nest_level -= 1
end

