"""assignment 2, hopefully this wont be as ass"""
import numpy
import csv
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
    unstructured_data = numpy.copy(data[1:]) #removing heading
    for row in unstructured_data:
        structured_row = row.copy()
        for x in list(range(0, 9)):
            if x in indexes:
                #make <U30
            else:
                #make float
        structured_data.append(tuple(structured_row))
    return numpy.array(structured_data)





