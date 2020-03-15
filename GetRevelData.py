import io
import json
import os
import re
import warnings

import pandas as pd
import requests

from get_cet_report import get_cet_report_from_excel

warnings.simplefilter(action='ignore', category=FutureWarning)
API_KEY = os.environ["API_KEY"]


class GetRevelData:
    def __init__(self, start, end, cet_filename):
        self.start = start
        self.end = end
        self.filename = cet_filename
        self.devices_df = get_devices()
        self.cet_df = self.get_cet_report_df()
        self.revel_df = self.get_revel_data()
        print(self.cet_df.to_string())
        print(self.revel_df.to_string())

    def get_cet_report_df(self):
        return get_cet_report_from_excel(self.filename)

    def get_revel_data(self):
        affidavit_url = f"https://api.reveldigital.com/api/report/export/" \
                        f"Affidavit?api_key={API_KEY}"
        for device in self.devices_df["id"].unique():
            affidavit_url += f'&device_id={device}'
        start, end = re.sub('/', '%2F', self.start), re.sub('/', '%2F', self.end)
        affidavit_url += f'&start={start}&end={end}&format=1'
        print(f'Requesting: {affidavit_url}')
        download = requests.get(url=affidavit_url)
        print(f'Response : {download.status_code}')
        decoded_content = download.content.decode('utf-8')
        df_affidavit = pd.read_csv(io.StringIO(decoded_content), header=2)
        df_affidavit = df_affidavit.dropna(axis=1, how='all')
        df_affidavit = df_affidavit.drop(columns=['Textbox18', 'DailySummary', 'TotalSummary'])
        df_affidavit = df_affidavit.dropna()
        print('Affidavit Report from Revel:')
        print(df_affidavit.head().to_string())
        return df_affidavit


def get_devices():
    device_url = f"https://api.reveldigital.com/api/devices?api_key={API_KEY}"
    download = requests.get(url=device_url)
    print(f'Response : {download.status_code}')
    decoded_content = download.content.decode('utf-8')
    decoded_content = json.loads(decoded_content)
    devices_df = pd.DataFrame(decoded_content)
    groups = devices_df["group_name"].unique()
    print(f'Found devices for groups:')
    for (i, g) in enumerate(groups):
        print(i, g, sep=': ')
    group = groups[int(input("\nWhat group do you want? (Usually CET Partner Trailers)\n"))]
    print(f'Getting data for group: {group}.')
    return devices_df.loc[devices_df["group_name"] == group]
