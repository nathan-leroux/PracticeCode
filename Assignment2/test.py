import unittest
from main import *

class Tests(unittest.TestCase):
    def test_load_metrics(self):
        self.assertListEqual(['created_at',
              'tweet_ID',
              'valence_intensity',
              'anger_intensity',
              'fear_intensity',
              'sadness_intensity',
              'joy_intensity',
              'sentiment_category',
              'emotion_category'], list(load_metrics('input.txt')[0]))

    def test_un_to_st(self):
        data = load_metrics('input.txt')
        new_data = unstructured_to_structured(data, [0,1,7,8])
        self.assertTupleEqual(tuple(new_data[0]), ('Tue Feb 04 17:04:01 +0000 2020', '1.22474E+18', 0.359, 0.477, 0.606, 0.49, 0.218, 'negative', 'fear'))

    def test_converting_timestamps(self):
        data = load_metrics('input.txt')
        new_data = unstructured_to_structured(data, [0, 1, 7, 8])
        new_data[:]['created_at'] = converting_timestamps(new_data[:]['created_at'])
        self.assertEqual(new_data[0]['created_at'], '2020-02-04 17:04:01')
        self.assertEqual((new_data[:]['created_at'][0].dtype), '<U19')

    def test_remove_val(self):
        data = load_metrics('input.txt')
        updated_data = unstructured_to_structured(data, [0, 1, 7, 8])
        updated_data[:]['created_at'] = converting_timestamps(updated_data[:]['created_at'])
        nan_data = numpy.copy(updated_data)
        dropout = 0.5
        intensity = ['valence_intensity', 'anger_intensity', 'fear_intensity',
                     'sadness_intensity', 'joy_intensity']
        for val in intensity:
            nan_data[:][val][numpy.random.choice(nan_data[:][val].size, int(dropout * nan_data[:][val].size),replace=False)] = numpy.nan
        nan_data = replace_nan(nan_data)
        #self.assertTrue(numpy.array_equal(nan_data, updated_data))

    def test_num_outliers(self):
        val = numpy.linspace(0, 100, 200)
        self.assertEqual(number_of_outliers(val, 10, 95), 30)