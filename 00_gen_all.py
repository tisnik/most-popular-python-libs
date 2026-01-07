import os

directories = "FM", "PyTorch", "assembly", "faiss"
directories = "pygame_zero",
directories = "PySimpleGUI", 
directories = "pydantic", 

for directory in directories:
    cwd = os.getcwd()
    os.chdir(directory)

    with open("00_index.py", "w") as indexfile:
        print("# Seznam zdrojových kódů v tomto podadresáři", file=indexfile)
        print("# ------------------------------------------", file=indexfile)
        print("#", file=indexfile)
        files = sorted(os.listdir())

        for file in files:
            if file.endswith(".py") and file != "00_index.py":
                print("# " + file + ":", file=indexfile)
                with open(file, "r") as fin:
                    for line in fin:
                        line = line.strip()
                        if line == "":
                            break
                        if line.startswith("# - ") or line.startswith("#  "):
                            print(line, file=indexfile)
                print("#", file=indexfile)
    os.chdir(cwd)
