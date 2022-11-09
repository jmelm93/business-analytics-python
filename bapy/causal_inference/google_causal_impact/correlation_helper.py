from dataclasses import dataclass
import pandas as pd

@dataclass
class CorrelationMatrixHelper:
    df: pd.DataFrame
    
    def build_correlation_matrix(self):
        """Uses DataFrame.corr() to build a correlation matrix.
        
            Args:
                df (pd.DataFrame): DataFrame with numeric columns
                
            Returns:
                pd.DataFrame - correlation matrix
        """
        
        df = self.df.copy()
        
        return df.corr()


    def remove_correlation_metrix_outside_of_target_range(self, target_range):
        """Removes the correlation matrix values outside of the target range.
        
            Args:
                df (pd.DataFrame): DataFrame with numeric columns
                target_range (list): list of 2 values. The first value is the lower bound and the second value is the upper bound
                
            Returns:
                pd.DataFrame - correlation matrix with values outside of the target range removed
        """        
        corr_matrix = self.build_correlation_matrix()
        
        # remove the values outside of the target range
        corr_matrix = corr_matrix[(corr_matrix > target_range[0]) & (corr_matrix < target_range[1])]
        
        return corr_matrix