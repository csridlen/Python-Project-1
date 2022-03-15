import pandas as pd

def recombine(file_1, file_2):
    recombined_file = pd.concat([file_1, file_2], ignore_index=True)
