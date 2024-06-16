function fill_in_list{T0}(size::T0)::List
l = []
for i in 0:size - 1
push!(l, i + 1);
end
return l
end

