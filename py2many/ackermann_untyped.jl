function A{T0, T1}(m::T0, n::T1)::Int64
if m == 0
return n + 1
end
if n == 0
return A(convert(, m - 1), convert(, 1))
end
return A(convert(, m - 1), convert(, A(m, convert(, n - 1))))
end

function check_a()
for m in 0:4 - 1
for n in 0:5 - 1
println(join([m, n, A(m, n)], " "));
end
end
end

