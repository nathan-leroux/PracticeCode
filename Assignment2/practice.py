import numpy
from main import *

data = load_metrics('dummy_data.txt')
updated_data = unstructured_to_structured(data,[0,1,7,8])
updated_data[:]['created_at'] = converting_timestamps(updated_data[:]['created_at'])

"""adding nan
dropout = 0.5
intensity = ['valence_intensity', 'anger_intensity', 'fear_intensity',
       'sadness_intensity', 'joy_intensity']

for val in intensity:
    print(f'val {val}')
    print(f'coloumn before : {updated_data[0:5][val]}')
    updated_data[:][val][numpy.random.choice(updated_data[:][val].size, int(dropout * updated_data[:][val].size), replace=False)] = numpy.nan
    print(f'coloumn after : {updated_data[0:5][val]}')
updated_data = replace_nan(updated_data)
print(f'column after nan removal : {updated_data[0:5][val]}')
"""
df = load_tweets('dummy_tweets.tsv')
df1 = convert_to_df(updated_data)

new_df = merge_dataframes(df1, df)
new_df.info()
