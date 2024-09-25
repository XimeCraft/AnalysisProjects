import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class AnalysisToolbox():

    def __init__(self) -> None:
        pass
        
    def descripbe_num_features(self, df):
        
        df_num = df.select_dtypes(include=[int, float])

        df_num.describe().T\
            .join(pd.DataFrame(df_num.skew(), columns=['Skew']))\
            .join(pd.DataFrame(df_num.kurtosis(), columns=['Kurtosis']))\
            .join(pd.DataFrame(df_num.std()/df_num.mean(), columns=['Coefficient of Variation']))
        
    f