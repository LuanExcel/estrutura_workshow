import pandas as pd
from typing import List




def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:

    '''
    Função para trasformas uma lista de dataframe em um unico df
    '''

    return pd.concat(data_frame_list, ignore_index=True)