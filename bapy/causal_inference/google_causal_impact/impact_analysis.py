from dataclasses import dataclass
from causalimpact import CausalImpact 
from bapy.causal_inference.google_causal_impact.stationarity import StationarityHelper

import pandas as pd

@dataclass
class CausalImpactHelper:
    df: pd.DataFrame
    pre_period: list
    post_period: list
    make_data_stationary = True 
    differencing_with = 'percent_change' # method to use for differencing. Options are 'percent_change' and 'diff'


    def get_impact_object(self):
        """Returns the CausalImpact object.

            Args:
                df (pd.DataFrame): DataFrame with y col = timeseries to check for stationarity 
                make_data_stationary (bool): whether to make the data stationary or not
                differencing_with (str): method to use for differencing. Options are 'percent_change' and 'diff'

            Returns:
                CausalImpact object
        """
        
        df = self.df.copy()
        
        # get the differenced timeseries
        if self.make_data_stationary:
            df = StationarityHelper.make_data_stationary(self.df, differencing_with=self.differencing_with)
            
        # get the pre and post period
        pre_period = self.pre_period
        post_period = self.post_period

        # get the causal impact object
        impact = CausalImpact(df, pre_period, post_period)

        return impact


    def get_summary_metrics(self):
        """Returns the summary metrics of the CausalImpact object.

            Args:
                df (pd.DataFrame): DataFrame with y col = timeseries to check for stationarity 
                make_data_stationary (bool): whether to make the data stationary or not
                differencing_with (str): method to use for differencing. Options are 'percent_change' and 'diff'

            Returns:
                pd.DataFrame - summary metrics of the CausalImpact object
        """
        
        impact = self.get_impact_object()
        
        return impact.summary()


    def get_summary_written_report(self):
        """Returns the summary written report of the CausalImpact findings.

            Args:
                df (pd.DataFrame): DataFrame with y col = timeseries to check for stationarity 
                make_data_stationary (bool): whether to make the data stationary or not
                differencing_with (str): method to use for differencing. Options are 'percent_change' and 'diff'

            Returns:
                str - summary written report of the CausalImpact findings
        """
            
        return self.get_impact_object().summary('report')
    
    
    def get_plots(self):
        """Returns the plots of the CausalImpact findings.

            Args:
                df (pd.DataFrame): DataFrame with y col = timeseries to check for stationarity 
                make_data_stationary (bool): whether to make the data stationary or not
                differencing_with (str): method to use for differencing. Options are 'percent_change' and 'diff'

            Returns:
                df.plot() - plots of the CausalImpact findings
        """
                
        return self.get_impact_object().plot()