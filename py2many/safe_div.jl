function safe_div(x::Int64, y::Int64)::Int64
try
return x / y
catch exn
if exn isa Exception
return 0
end
end
end

