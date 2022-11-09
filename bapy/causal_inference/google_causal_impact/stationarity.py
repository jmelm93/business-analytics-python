from statsmodels.tsa.stattools import adfuller # Augmented Dickey-Fuller test - to check for stationarity

class StationarityHelper:

    @staticmethod
    def check_p_value(timeseries):
        """Checks if the timeseries is stationary using the Augmented Dickey-Fuller test.

            Args:
                timeseries (pd.Series): timeseries to check for stationarity
            
            Returns:
                p-value(float), message(str) - p-value of the test and message to indicate if the timeseries is stationary or not
        """
        result = adfuller(timeseries)
        
        message = None 
        
        if result[1] > 0.05:
            message = "The timeseries is not stationary."
        else:
            message = "The timeseries is stationary."
        
        return result[1], message

    @staticmethod
    def make_data_stationary(df, differencing_with='percent_change'):
        """Differencing the timeseries to make it stationary.
                
                Args:
                    df (pd.DataFrame): DataFrame with y col = timeseries to check for stationarity
                    differencing_with (str): method to use for differencing. Options are 'percent_change' and 'diff'
                
                Returns:
                    pd.DataFrame - DataFrame with stationary timeseries data in y col
            """
        
        # check if data is stationary. 
        p_value, message = StationarityHelper.check_p_value(df.y)

        if p_value > 0.05:
            # if not, make it stationary and return 
            if differencing_with == 'percent_change':
                return df.pct_change().dropna()
            elif differencing_with == 'diff':
                return df.diff().dropna()
            else:
                raise ValueError("Invalid differencing method. Please use 'percent_change' or 'diff'.")
        else:
            # If so, return the df. 
            return df