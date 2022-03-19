# put the paths of the two split files into file_1 and file_2
# then, this function returns a complete dataframe.
import pandas as pd
def recombine(file_1, file_2):
    d1 = pd.read_csv(file_1)
    d2 = pd.read_csv(file_2)
    recombined_file = pd.concat([d1, d2], ignore_index=True)
    return recombined_file