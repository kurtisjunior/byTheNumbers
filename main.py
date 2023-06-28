import pandas as pd

import athlete_data
import test_data
from extract import get_athletes_links, get_name, get_fight_data


def extract():
    athletes_links = get_athletes_links()

    athlete_data = {}

    for athlete_link in athletes_links:
        athlete_name = get_name(athlete_link)
        athlete_fight_data = get_fight_data(athlete_link)
        athlete_data[athlete_name] = athlete_fight_data

    return athlete_data


def transform():
    dfs = []
    columns = ['name', 'finish', 'year', 'opponent', 'weight', 'competition']

    for key, sub_values in test_data.data.items():
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
    print(result_df.head(5))


transform()
