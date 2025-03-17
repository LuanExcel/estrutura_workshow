import pandas as pd
from pathlib import Path
import os
import glob
from typing import List

'''
Função para ler arquivos de uma pasta
e retornar uma lista de dataframes

args: input_path (str): caminho da pasta com as arquivos

return: lista de dataframes
glob é para listar todos os arquivosde um pasta
'''

path = "data/input"

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path,"*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    return data_frame_list




if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)

    # Linha de teste
    # sabendo q se mesmo ao colocar esse if 
    # ao chamar qualquer função desse módulo o hello word será desconsiderado
    print('hello word')