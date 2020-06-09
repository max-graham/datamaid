import pandas as pd

class DataMaidReport:
    
    def __init__(self, df: pd.DataFrame):
        pass


class TypeReport:

    def __init__(self, df: pd.DataFrame):
        self._df = df

    def get_shape(self):
        return self._df.shape
        