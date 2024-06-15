function A(m::Int64, n::Int64)::Int64
if m == 0
return n + 1
end
if n == 0
return A(m - 1, 1)
end
return A(m - 1, A(m, n - 1))
end

function check_a()::
for m in 0:4 - 1
for n in 0:5 - 1
println(join([m, n, A(m, n)], " "));
end
end
end

