#!/usr/bin/env python
# coding: utf-8

# ### Set of input files with benchmark results to be processed

# In[2]:


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
    "numba4.times")


# In[3]:


import pandas as pd


# ### Helper functions to read benchmark results

# In[4]:


def read_benchmark_result(filename):
    return pd.read_csv(filename, sep=" ", header=0, names=("size", "time", "memory"))

def filename2description(filename):
    return filename.split(".")[0].replace("_", " ")

def read_all_results(input_files):
    return {filename2description(input_file): read_benchmark_result(input_file)
            for input_file in input_files}


# ### Combine all results into one DataFrame

# In[5]:


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

# In[6]:


import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150
xticks=df.index


# ### Plot results

# In[12]:


results[0:5].plot(kind='bar', stacked=False, width=0.9, title="Startup time",
                  color=["#a00000", "#a0a000",
                         "#00a000", "#00b030", "#00c060", "#00d090", "#00e0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff"])


# In[9]:


results[5:10].plot(kind='bar', stacked=False, width=0.9,
                   title="Computation with startup time influence", color=["#a00000", "#a0a000",
                         "#00a000", "#00b030", "#00c060", "#00d090", "#00e0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff"])
plt.savefig("Startup time and computation.png")
plt.show()


# In[10]:


results[10:].plot(kind='bar', stacked=False, width=0.9, title="Extensive computation", color=["#a00000", "#a0a000",
                         "#00a000", "#00b030", "#00c060", "#00d090", "#00e0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff"])
plt.savefig("Extensive computation.png")
plt.show()


# In[43]:


results.plot(title="Approximation, incl. startup time",
            color=["#a00000", "#a0a000",
                         "#00c000", "#00c030", "#00c060", "#00c090", "#00c0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff"])
plt.savefig("Approximation computation.png")
plt.show()


# In[11]:


results[8:12].plot(title="Numba/CPython thresholds", color=["#a00000", "#a0a000",
                         "#00a000", "#00b030", "#00c060", "#00d090", "#00e0a0",
                         "#ff0000", "#ff8000",
                         "#0000ff", "#0060ff", "#00c0ff"])
plt.savefig("Numba CPython thresholds.png")
plt.show()


# In[15]:


results[:][["python 3 8", "python 3 9" , "python 3 10", "python 3 11", "python 3 12"]].plot(title="Python interpreters only")


# In[ ]:




