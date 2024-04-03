""" yf_example3.py

本模块用于下载指定年份的昆塔斯航空公司股票价格数据，并将其保存为 CSV 文件。
"""

import os
import toolkit_config as cfg
import yf_example_2

def qan_prc_to_csv(year):
    """
    下载指定年份的昆塔斯航空公司股票价格，并将其保存为 CSV 文件。

    参数
    ----
    year : int
        需要下载股票价格数据的年份。
    """
    # 构建 CSV 文件路径
    filename = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')

    # 下载股票数据
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    yf_example_2.yf_prc_to_csv('QAN.AX', filename, start=start_date, end=end_date)

if __name__ == "__main__":
    # 示例用法：下载2020年昆塔斯航空公司的股票价格数据
    qan_prc_to_csv(2020)