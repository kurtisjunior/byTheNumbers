import pandas as pd


def clean_data(athlete_data):
    dfs = []
    columns = ['name', 'finish', 'year', 'opponent', 'weight', 'competition']

    for key, sub_values in athlete_data.items():
        rows = []
        for sub in sub_values:
            rows.append({
                'name': key,
                'finish': sub['finish'],
                'year': sub['year'],
                'opponent': sub['opponent'],
                'weight': sub['weight'],
                'competition': sub['competition']
            })
        df = pd.DataFrame(rows, columns=columns)
        dfs.append(df)

    result_df = pd.concat(dfs, ignore_index=True)
    result_df
