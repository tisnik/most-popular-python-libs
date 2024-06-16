function factorial{T0}(n::T0)::Int64
if n < 0
return nothing
end
if n == 0
return 1
end
result = n*factorial(convert(, n - 1))
return result
end

