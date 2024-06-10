filenames = (
    "pipeline-basic",
    "pipeline-none-aware",
    "pipeline-backward-none-aware",
    "pipeline-backward-none-not-aware",
    "pipeline-backward",
    "pipeline-basic",
    "pipeline-basic-simplified",
    "pipeline-keyword-arguments",
    "pipeline-multiple-arguments-2",
    "pipeline-multiple-arguments",
    "pipeline-none-aware-2",
    "pipeline-none-aware",
    "pipeline-none-aware-simplified",
    "pipeline-none-not-aware",
)

functions = (
        "print",
        "abs",
        "hex",
        "sum",
        "ord",
        "reversed",
        "evens",
        "sub",
        "swap",
)

def simplify_funcion_calls(line):
    for function in functions:
        to_name = function
        from_name = f"({function})"
        line = line.replace(from_name, to_name)
    return line


def transformation(fin, fout):
    for line in fin:
        # remove regular comments created by Coconut
        if " #" in line:
            line = line[:line.find("#")]

        # replace the first comment
        if line.startswith("# Compiled Coconut"):
            line = "# Simplified version of Coconut transpiled into Python\n"

        # simplify function calls
        line = simplify_funcion_calls(line)

        # remove spaces and other whitespace characters at end of lines
        line = line.rstrip() + "\n"
        fout.write(line)


def main():
    for filename in filenames:
        source = filename + ".py"
        target = filename + "-simplified.py"
        with open(source, "r") as fin:
            with open(target, "w") as fout:
                transformation(fin, fout)


main()
