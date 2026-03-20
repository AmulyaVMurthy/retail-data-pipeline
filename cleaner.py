import pandas as pd
import logging
import os

# Set up professional logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataCleaner:
    """
    A professional data cleaning pipeline for E-commerce retail data.
    Handles datetime conversion, null values, and statistical outlier removal.
    """
    def __init__(self, filepath):
        if not os.path.exists(filepath):
            logging.error(f"File not found: {filepath}")
            raise FileNotFoundError(f"Check your data folder for {filepath}")
            
        self.df = pd.read_csv(filepath)
        logging.info(f"--- DataCleaner initialized: {len(self.df)} rows loaded ---")

    def format_dates(self, column_name):
        """Converts strings to datetime objects with error handling."""
        try:
            self.df[column_name] = pd.to_datetime(self.df[column_name])
            logging.info(f"✅ Formatted {column_name} to datetime.")
        except Exception as e:
            logging.warning(f"❌ Failed to format {column_name}: {e}")

    def handle_nulls(self, columns_to_check):
        """Drops rows where critical business data is missing."""
        initial_count = len(self.df)
        self.df.dropna(subset=columns_to_check, inplace=True)
        logging.info(f"✅ Dropped {initial_count - len(self.df)} null rows based on {columns_to_check}.")

    def remove_outliers(self, column, factor=3):
        """
        Uses the IQR method to remove anomalies. 
        Professional Tip: Use a factor of 3 (Extreme Outliers) for revenue 
        to avoid deleting your best customers!
        """
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        upper_bound = Q3 + (factor * IQR)
        lower_bound = Q1 - (factor * IQR)
        
        initial_count = len(self.df)
        # We usually only care about the upper bound for 'revenue' 
        # unless there are negative values (returns)
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        
        logging.info(f"✅ Removed {initial_count - len(self.df)} outliers in {column} (Factor: {factor}).")

    def save_data(self, output_path):
        """Exports the clean data for Tableau visualization."""
        try:
            self.df.to_csv(output_path, index=False)
            logging.info(f"💾 Cleaned data saved to: {output_path}")
        except Exception as e:
            logging.error(f"❌ Error saving file: {e}")
