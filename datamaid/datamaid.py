import pandas as pd

class DataMaidReport:
    
    def __init__(self, df: pd.DataFrame):
        pass


class TypeReport:

    def __init__(self, df: pd.DataFrame):
        self._df = df

    def get_shape(self):
        return self._df.shape
    
    def get_column_mins(self):
        return self._df.min().rename('min')
    
    def get_column_maxs(self):
        return self._df.max().rename('max')

    def get_column_ranges(self):
        result = pd.merge(
            left=self.get_column_mins(),
            right=self.get_column_maxs(),
            left_index=True,
            right_index=True
        )
        return result
