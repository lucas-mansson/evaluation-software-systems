import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import glob
# Lab 5

coll_path_jit = "data/collections/jit/*.csv"
coll_path_jit_data2 = "data/collections/jit/*_data2.csv"
coll_path_no_jit = "data/collections/*.csv"
coll_path_no_jit_data2 = "data/collections/*_data2.csv"

own_path_jit = "data/own/jit/*.csv"
own_path_jit_data2 = "data/own/jit/*_data2.csv"
own_path_no_jit = "data/own/*.csv"
own_path_no_jit_data2 = "data/own/*_data2.csv"

# coll jit
file_list = glob.glob(coll_path_jit)
coll_dfs_jit = [pd.read_csv(file) for file in file_list]
coll_jit = pd.concat(coll_dfs_jit, ignore_index=True)

print(coll_path_jit)
print(coll_jit)

#coll jit data 2

# coll not jit
file_list = glob.glob(coll_path_no_jit)
coll_dfs_no_jit = [pd.read_csv(file) for file in file_list]
coll_no_jit = pd.concat(coll_dfs_no_jit, ignore_index=True)

print(coll_path_no_jit)
print(coll_no_jit)

# Own jit
file_list = glob.glob(own_path_jit)
own_jits = [pd.read_csv(file) for file in file_list]
own_jit = pd.concat(own_jits, ignore_index=True)

print(own_path_jit)
print(own_jit)

# own no jit
file_list = glob.glob(own_path_no_jit)
own_no_jits = [pd.read_csv(file) for file in file_list]
own_no_jit = pd.concat(own_no_jits, ignore_index=True)

print(own_path_no_jit)
print(own_no_jit)

t_jit, p_val_jit = st.ttest_ind(coll_jit["0"], own_jit["0"])
t_no_jit, p_val_no_jit = st.ttest_ind(coll_no_jit["0"], own_no_jit["0"])

print(f"T test jit: {t_jit}, {p_val_jit}")
print(f"T test no jit: {t_no_jit}, {p_val_no_jit}")
