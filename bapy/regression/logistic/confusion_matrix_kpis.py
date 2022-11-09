from dataclasses import dataclass

@dataclass
class ConfusionMatrixKPIs:
    true_positives: int = 0 
    true_negatives: int = 0
    false_positives: int = 0
    false_negatives: int = 0
    round_by: int = 1 
    percent_returned: bool = True 

    @staticmethod 
    def check_if_balanced(mean_of_dataset, threshold = 0.35):
        """Checks if the dataset is balanced. If the mean of the dataset is 
        less than 0.35 of or greater than 1 - 0.35, then the dataset is imbalanced. 

        Args:
            mean_of_dataset (float): mean of the dataset
            threshold (float, optional): threshold to determine if dataset is balanced. Defaults to 0.35.

        Returns:
            bool: True if balanced, False if imbalanced
        """
        
        if mean_of_dataset < threshold or mean_of_dataset > 1 - threshold:
            return False
        else:
            return True


    def accuracy_score(self):
        """Calculates the accuracy score of the model. Use this if dataset is balanced (proportionate).

        Args:
            true_negatives (int): true negatives
            false_positives (int): false positives
            false_negatives (int): false negatives
            true_positives (int): true positives
            round_by (int, optional): number of decimal places to round to. Defaults to 1.
            percent (bool, optional): True if you want the score to be in percent. Defaults to True.

        Returns:
            float: accuracy score percentage
        """
        
        accuracy = round((self.true_positives + self.true_negatives) / (self.true_positives + self.true_negatives + self.false_positives + self.false_negatives), self.round_by)
        
        if self.percent_returned:
            accuracy *= 100 # convert to percent (*= is shorthand for accuracy = accuracy * 100)
        
        return accuracy


    def f1_score (self):
        """Calculates the f1 score of the model. Use this if dataset is not balanced (proportionate).

        Args:
            true_negatives (int): true negatives
            false_positives (int): false positives
            false_negatives (int): false negatives
            true_positives (int): true positives
            round_by (int, optional): number of decimal places to round to. Defaults to 1.
            percent (bool, optional): True if you want the score to be in percent. Defaults to True.

        Returns:
            float: f1 score percentage
        """
        
        f1 = round((2 * self.true_positives) / (2 * self.true_positives + self.false_positives + self.false_negatives), self.round_by)
        
        if self.percent_returned:
            f1 *= 100 # convert to percent (*= is shorthand for accuracy = accuracy * 100)
        
        return f1

    def specificity(self):
        """Calculates the specificity of the model. Use when model is focused on predicting negative (false).

        Args:
            true_negatives (int): true negatives
            false_positives (int): false positives
            round_by (int, optional): number of decimal places to round to. Defaults to 1.
            percent (bool, optional): True if you want the score to be in percent. Defaults to True.

        Returns:
            float: specificity percentage
        """
        
        specificity = round(self.true_negatives / (self.true_negatives + self.false_positives), self.round_by)
        
        if self.percent_returned:
            specificity *= 100 # convert to percent (*= is shorthand for accuracy = accuracy * 100)
        
        return specificity
    
        
    def sensitivity(self):
        """Calculates the sensitivity of the model. Use when model is focused on predicting positive (true).

        Args:
            true_positives (int): true positives
            false_negatives (int): false negatives
            round_by (int, optional): number of decimal places to round to. Defaults to 1.
            percent (bool, optional): True if you want the score to be in percent. Defaults to True.

        Returns:
            float: sensitivity percentage
        """
        
        sensitivity = round(self.true_positives / (self.true_positives + self.false_negatives), self.round_by)
        
        if self.percent_returned:
            sensitivity *= 100 # convert to percent (*= is shorthand for accuracy = accuracy * 100)
        
        return sensitivity