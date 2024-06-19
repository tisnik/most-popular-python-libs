function bubble_sort{T0}(size::T0)
    a = [randrange(random, 0, 10000) for i in 0:size - 1]
    for i in 0 - 1:-1:size - 1
    for j in 0:i - 1
    if a[j] > a[j + 1]
    a[j], a[j + 1] = (a[j + 1], a[j])
    end
    end
    end
    println(join([a], " "));
end

