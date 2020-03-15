import math

import pandas as pd


# This file is just used to read the excel file. You don't need to
# use it or understand anything that happens in here. Just call this
# one time in GetRevelData.py


def get_cet_report_from_excel(filename):
    df = pd.read_excel(filename)

    truck_routes = []
    truck_rows = df.index[df.eq('TRUCK').any(1)].to_list()
    truck_rows.append(df.shape[0])
    cols = ['Date', 'Route', 'Destination', 'Departure', 'Return', 'Hours', 'Miles', 'Green Light']

    for i in range(len(truck_rows) - 1):
        truck_row = df.iloc[truck_rows[i]]
        truck_col = get_column_index_by_label(df, 'TRUCK')
        truck_id = truck_row.iloc[truck_col + 1]

        for row in range(truck_rows[i] + 2, truck_rows[i + 1]):
            entry = df.iloc[row]
            route_json = {"truck": truck_id}

            for col in cols:
                col_index = get_column_index_by_label(df, col)
                route_json[camel_case(col)] = entry.iloc[col_index]
            if not any(type(v) == float and math.isnan(v) for v in route_json.values()):
                truck_routes.append(route_json)

    week, report_start_date, report_end_date = get_report_info(df)
    cet_df = pd.DataFrame(truck_routes)
    cet_df['week'] = week
    cet_df['ReportStartDate'] = report_start_date
    cet_df['ReportEndDate'] = report_end_date
    return cet_df

def get_column_index_by_label(df, label):
    row = df[df.eq(label).any(1)]
    return [row.columns.get_loc(c) for c in row if row.iloc[0][c] == label][0]


def camel_case(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


def get_report_info(df):
    w = get_value_in_cell_next_to_label(df, 'Week:')
    start = get_value_in_cell_next_to_label(df, 'From:')
    end = get_value_in_cell_next_to_label(df, 'To:')
    return w, start, end


def get_value_in_cell_next_to_label(df, label):
    row = df[df.eq(label).any(1)]
    column = [row.columns.get_loc(c) for c in row if row.iloc[0][c] == label][0]
    return row.iloc[0][column + 1]
