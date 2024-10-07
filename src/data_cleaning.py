import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns
import os

def filter_columns(df):
    columns = [
        'SEQN', # 'RIDAGEYR', 'RIDRETH3', 'DMDBORN4', 'DMDEDUC2', 'DMDMARTZ', 'DMDHHSIZ', 'INDFMPIR',    # DEMO_L.XPT
        'LBDTCSI',  # TCHOL_L.XPT
        'DIQ010', 'DID040', 'DIQ160',  # DIQ_L.XPT
        'DBQ930', 'DBQ940', 'DBQ945',  # DBQ_L.XPT
        'BPQ020', 'BPQ080', 'BPQ101D', 'BPQ150',  # BPQ_L.XPT
        'PAD680', 'PAD810U', 'PAD790U',  # PAQ_L.XPT
        'ALQ130', 'ALQ142', 'ALQ280',  # ALQ_L.XPT
        'INDFMMPC',  # INQ_L.XPT
        'DPQ010', 'DPQ020', 'DPQ030', 'DPQ040', 'DPQ050', 'DPQ060', 'DPQ070', 'DPQ080', 'DPQ090', 'DPQ100',  # DPQ_L.XPT
        'SMQ040', 'SMD641'  # SMQ_L.XPT
    ]

    # Filter the merged dataframe to keep only the desired columns
    filtered_df = df[columns]

    return filtered_df