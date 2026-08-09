counter = 0

function reset_counter()
    counter = 0
end

function gen_int()
    counter = counter + 1
    return counter
end

function gen_double()
    counter = counter + 1
    return 1.0/counter
end
