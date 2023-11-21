#!/usr/bin/env python
# coding: utf-8

# ### Set of input files with benchmark results to be processed

# In[25]:


input_files = (
    "numba7_normal.times",
    "numba7_no_output.times",
    "numba7_nocalc.times",
    "numba7_double_output.times")


# In[14]:


import pandas as pd


# ### Helper functions to read benchmark results

# In[39]:


def read_benchmark_result(filename):
    return pd.read_csv(filename, sep=" ", header=0, names=("size", "time", "memory"))

def filename2description(filename):
    return filename.split(".")[0].replace("_", " ")[7:]

def read_all_results(input_files):
    return {filename2description(input_file): read_benchmark_result(input_file)
            for input_file in input_files}


# ### Combine all results into one DataFrame

# In[53]:


r = read_all_results(input_files)

results = pd.DataFrame()

# column to be transformed into index
results["size"] = (r["normal"]["size"])

for description, df in r.items():
    results[description] = df["time"]

# create meaningful index
results.set_index("size", inplace=True)
results


# ### Set plot size

# In[77]:


import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150


# ### Plot results

# In[97]:


results[0:3].plot(kind='bar', stacked=False, width=0.9, title="Startup time")
plt.savefig("Startup time.png")
plt.show()


# In[95]:

results[-3:].plot(kind='bar', stacked=False, width=0.9, title="Extensive computation")
plt.savefig("Extensive computation.png")
plt.show()



# In[101]:

results.plot(title="Approximation, incl. startup time")
plt.savefig("Approximation computation.png")
plt.show()

