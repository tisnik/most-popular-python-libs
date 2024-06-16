function fill_in_list(size::Int64)::
l = []
for i in 0:size - 1
push!(l, i + 1);
end
return l
end

