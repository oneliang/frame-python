import os

import pandas as pd


def write_excel(full_filename: str, data_list: [{}], sheet_name: str):
    """
    write excel
    :param full_filename:
    :param data_list:
    :param sheet_name:
    :return:
    """
    if os.path.exists(full_filename):
        writer = pd.ExcelWriter(full_filename, mode='a')
    else:
        writer = pd.ExcelWriter(full_filename, mode='w')
    data_frame = pd.DataFrame(data_list)
    data_frame.to_excel(writer, sheet_name=sheet_name)
    writer.close()
