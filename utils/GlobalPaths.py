import os

g_analyzed_path = "analyzed/"  # ../analyzed/
g_data_path = "datas/"
g_log_path = "logs/"


def GlobalPathsCheck():
    if not os.path.exists(g_analyzed_path):
        os.makedirs(g_analyzed_path)

    if not os.path.exists(g_data_path):
        os.makedirs(g_data_path)

    if not os.path.exists(g_log_path):
        os.makedirs(g_log_path)
