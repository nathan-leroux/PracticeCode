"""assignment 2, hopefully this wont be as ass"""
import numpy
import csv
import matplotlib.pyplot as plt
import pandas as pd

def return_row_metrics(row):
    # given a row, returns a list of the needed metrics.
    row_metrics = []
    for i in [0,1,7,8,9,10,11,12,13]:
        row_metrics.append(row[i])
    return row_metrics

def load_metrics(filename):
    #iterates through a csv file and returns metrics
    result = []
    with open(filename, 'r') as input_file:
        csv_reader = csv.reader(input_file, quotechar='"', delimiter=',')
        for row in csv_reader:
            metrics = return_row_metrics(row)
            result.append(metrics)

    return numpy.array(result)


def unstructured_to_structured(data, indexes):
    """from data, removes header row and sets data types for metrics"""
    struct_values = {}
    structured_data = []
    headers = []

    # collecting headers
    for head in data[0]:
        headers.append(head)

    # removing heading
    unstructured_data = numpy.copy(data[1:])

    for x in list(range(0, 9)):
        if x in indexes:
            struct_values.setdefault(headers[x], "U30")
        else:
            struct_values.setdefault(headers[x], float)

    # setting data types
    dtypes = []
    for coloumn, dtype in struct_values.items():
        dtypes.append((coloumn, dtype))

    # setting rows as tuples
    for row in unstructured_data:
        structured_data.append(tuple(row.copy()))

    # putting it together
    result = numpy.array(structured_data, dtype=dtypes)
    return result

def converting_timestamps(array):
    #input data
    converted_array = []

    for row in array:
        #chop suey
        date_string = row
        month_switch = {'Jan' : '01',
                       'Feb' : '02',
                       'Mar' : '03',
                       'Apr' : '04',
                       'May' : '05',
                       'Jun' : '06',
                       'Jul' : '07',
                       'Aug' : '08',
                       'Sep' : '09',
                       'Oct' : '10',
                       'Nov' : '11',
                       'Dec' : '12'}
        year = date_string[26:]
        month = date_string[4:7]
        day = date_string[8:10]
        hour = date_string[11:19]
        #minute = date_string[14:16]
        #second = date_string[17:19]

        month = month_switch[month]

        finished_date_string = f'{year}-{month}-{day} {hour}'
        converted_array.append(finished_date_string)

    #output data
    return converted_array

def replace_nan(data):
    updated_data = numpy.copy(data)
    columns = ['valence_intensity', 'anger_intensity', 'fear_intensity',
                 'sadness_intensity', 'joy_intensity']

    for val in columns:
        average = numpy.nanmean(data[:][val])
        updated_val = []
        for metric in data[:][val]:
            if numpy.isnan(metric):
                updated_val.append(average)
            else:
                updated_val.append(metric)
        updated_data[:][val] = updated_val

    return updated_data

def boxplot_data(data):
    #collect data
    graph_data = []
    columns = ['valence_intensity', 'anger_intensity', 'fear_intensity',
               'sadness_intensity', 'joy_intensity']
    for val in columns:
        graph_data.append(data[:][val])

    #set figure size
    plt.figure(figsize=(10,7))

    #set box colors
    colors = ['green', 'red', 'purple', 'blue', 'yellow']

    #set linestyle
    boxprops = {'linestyle' : '-', 'linewidth' : 1, 'color' : 'black', 'facecolor' : 'yellow'}
    medianprops = {'color' : 'black'}

    #set xticks values
    labels = ['Valence', 'Anger', 'Fear', 'Sadness', 'Joy']

    #patch_artist=True & fill colors
    plot = plt.boxplot(graph_data, patch_artist=True, boxprops=boxprops, medianprops=medianprops )
    for box, color in zip(plot['boxes'], colors):
        box.set_facecolor(color)

    #adding axis labels
    plt.title('Distribution of Sentiment')
    plt.ylabel('Values')
    plt.xlabel('Sentiment')
    plt.xticks(range(1,len(graph_data)+1), labels)
    plt.grid(axis='y')

    #saving boxplot
    plt.savefig('output.png')

def number_of_outliers(sentiment, lower, upper):
    #finding outlier boundries
    bounds = numpy.percentile(sentiment, [lower, upper])
    #counting outliers
    count = 0
    for metric in sentiment:
        if (metric <= bounds[0] or metric >= bounds[1]):
            count +=1
    return count

def convert_to_df(data):
    dictionary = {}

    #storing numpy array in dict
    for data_type in data.dtype.names:
        dictionary.setdefault(data_type, [])
        for point in data[:][data_type]:
            dictionary[data_type].append(point)

    #initialising pandas dataframe
    return pd.DataFrame(dictionary)

def load_tweets(filename):
    df = pd.read_csv(filename, sep='\t')
    return df

def merge_dataframes(df_metrics, df_tweets):
    df_tweets = df_tweets.rename(columns={'id' : 'tweet_ID'})
    df_metrics['tweet_ID'] = pd.to_numeric(df_metrics['tweet_ID'])
    result = df_tweets.join(df_metrics.set_index('tweet_ID'), how='inner', on='tweet_ID')
    result = result.dropna()
    return result.astype({'tweet_ID' : 'int64'})

def plot_timeperiod(df_merged, from_date, to_date, output_name):
    pass