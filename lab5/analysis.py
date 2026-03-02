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
dfs = [pd.read_csv(file) for file in file_list]
coll_jit = pd.concat(dfs, ignore_index=True)

#coll jit data 2
file_list = glob.glob(coll_path_jit_data2)
dfs = [pd.read_csv(file) for file in file_list]
coll_jit_data2 = pd.concat(dfs, ignore_index=True)

# coll not jit
file_list = glob.glob(coll_path_no_jit)
dfs = [pd.read_csv(file) for file in file_list]
coll_no_jit = pd.concat(dfs, ignore_index=True)

# coll not jit data2
file_list = glob.glob(coll_path_no_jit_data2)
dfs = [pd.read_csv(file) for file in file_list]
coll_no_jit_data2 = pd.concat(dfs, ignore_index=True)

# Own jit
file_list = glob.glob(own_path_jit)
pds = [pd.read_csv(file) for file in file_list]
own_jit = pd.concat(pds, ignore_index=True)

#own jit data2
file_list = glob.glob(own_path_jit_data2)
pds = [pd.read_csv(file) for file in file_list]
own_jit_data2 = pd.concat(pds, ignore_index=True)

# own no jit
file_list = glob.glob(own_path_no_jit)
pds = [pd.read_csv(file) for file in file_list]
own_no_jit = pd.concat(pds, ignore_index=True)

#own no jit data2
file_list = glob.glob(own_path_no_jit_data2)
pds = [pd.read_csv(file) for file in file_list]
own_no_jit_data2 = pd.concat(pds, ignore_index=True)


t_jit, p_val_jit = st.ttest_ind(coll_jit["0"], own_jit["0"])
t_jit_data2, p_val_jit_data2 = st.ttest_ind(coll_jit_data2["0"], own_jit_data2["0"])

t_no_jit, p_val_no_jit = st.ttest_ind(coll_no_jit["0"], own_no_jit["0"])
t_no_jit_data2, p_val_no_jit_data2 = st.ttest_ind(coll_no_jit_data2["0"], own_no_jit_data2["0"])

print(f"T test jit: {t_jit}, {p_val_jit}")
print(f"T test jit data2: {t_jit_data2}, {p_val_jit_data2}")
print(f"T test no jit: {t_no_jit}, {p_val_no_jit}")
print(f"T test no jit data2: {t_no_jit_data2}, {p_val_no_jit_data2}")
