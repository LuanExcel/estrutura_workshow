import pandas as pd
from typing import List


'''
Função para trasformas uma lista de dataframe em um unico df
'''

def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)