#!/usr/bin/env python
# coding: utf-8

# ### Set of input files with benchmark results to be processed

# In[25]:


input_files = (
    "native.times",
    "native_optim.times",
    "python_3_8.times",
    "python_3_9.times",
    "python_3_10.times",
    "python_3_11.times",
    "python_3_12.times",
    "mypyc_no_type_hints.times",
    "mypyc_with_type_hints.times",
    "numba2.times",
    "numba3.times",
    "numba4.times",
    "numba5.times",
    "numba6.times",
    "numba7.times")


# In[14]:


import pandas as pd

# ### Helper functions to read benchmark results

# In[39]:


def read_benchmark_result(filename):
    return pd.read_csv(filename, sep=" ", header=0, names=("size", "time", "memory"))

def filename2description(filename):
    return filename.split(".")[0].replace("_", " ")

def read_all_results(input_files):
    return {filename2description(input_file): read_benchmark_result(input_file)
            for input_file in input_files}


# ### Combine all results into one DataFrame

# In[53]:


r = read_all_results(input_files)

results = pd.DataFrame()

# column to be transformed into index
results["size"] = (r["native"]["size"])

for description, df in r.items():
    results[description] = df["time"]

# create meaningful index
results.set_index("size", inplace=True)
results


# ### Set plot size

# In[77]:


import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["figure.dpi"] = 150


# ### Plot results

# In[97]:


results[0:3].plot(kind="bar", stacked=False, width=0.9, title="Startup time",
            color=["#a00000", "#a0a000",
                         "#00c000", "#00c030", "#00c060", "#00c090", "#00c0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff",
                         "#a08000", "#c0a000", "#f0c000"])
plt.savefig("Startup time.png")
plt.show()


# In[95]:


results[-2:].plot(kind="bar", stacked=False, width=0.9,
                   title="Computation w/o startup time influence",
                   color=["#a00000", "#a0a000",
                         "#00a000", "#00b030", "#00c060", "#00d090", "#00e0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff",
                         "#a08000", "#c0a000", "#f0c000"])
plt.savefig("Extensive computation.png")
plt.show()


# In[101]:

results.plot(title="Approximation, incl. startup time",
            color=["#a00000", "#a0a000",
                         "#00c000", "#00c030", "#00c060", "#00c090", "#00c0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff",
                         "#a08000", "#c0a000", "#f0c000"],
            style=[":", ":", "--", "--", "--", "--", "--"])
plt.savefig("Approximation computation.png")
plt.show()


# In[102]:


# In[104]:


results[:][["python 3 8", "python 3 9" , "python 3 10", "python 3 11", "python 3 12"]].plot(
        kind="bar", title="Python interpreters only")
plt.savefig("Python interpreters only.png")
plt.show()

results[:][["numba5", "numba6" , "numba7"]].plot(
        kind="bar", title="Numba: serial/parallel")
plt.savefig("Numba_serial_parallel.png")
plt.show()

results[:][["native", "native optim", "numba7"]].plot(
        kind="line", title="Parallel Numba vs native")
plt.savefig("Parallel Numba vs native.png")
plt.show()

