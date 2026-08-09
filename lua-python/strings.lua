string = ""
filler = "."

function set_filler(s)
    filler = s
end

function gen_string()
    string = string .. filler
    return string
end
