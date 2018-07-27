import os
import pandas as pd

DATA_DIR = '/Users/apple/Downloads/data/'


def merge_all_data(data_dir):
    categories = [cat for cat in os.listdir(data_dir) if os.path.isdir(cat)]
    merged_df = []
    for category in categories:
        pages = []
        csv_files = [DATA_DIR + category + '/' + page for page in os.listdir(DATA_DIR + category + '/')]
        for f in csv_files:
            print(f)
            page = pd.read_csv(f, delimiter='\t', header=None, error_bad_lines=False, engine='python')
            pages.append(page)
        category_df = pd.concat(pages)
        category_df['category'] = category
        merged_df.append(category_df)

    full_df = pd.concat(merged_df)
    return full_df


df = merge_all_data(DATA_DIR)
print(df.head())
print(df.shape)


