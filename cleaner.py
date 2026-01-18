import pandas as pd

class DataCleaner:
    def __init__(self, filepath):
        """Phase 3.1: Load the dataset upon initialization"""
        self.df = pd.read_csv(filepath)
        print(f"--- DataCleaner initialized with {len(self.df)} rows ---")

    def format_dates(self, column_name):
        """Phase 3.2: Convert strings to actual datetime objects"""
        self.df[column_name] = pd.to_datetime(self.df[column_name])
        print(f"✅ Formatted {column_name} to datetime.")

    def handle_nulls(self):
        """Phase 3.3: Drop rows where critical data is missing"""
        initial_count = len(self.df)
        # Drop rows where we don't have a customer ID or revenue
        self.df.dropna(subset=['customer_unique_id', 'total_order_revenue'], inplace=True)
        print(f"✅ Dropped {initial_count - len(self.df)} null rows.")

    def remove_outliers(self, column):
        """Phase 3.4: Use IQR method to remove extreme price anomalies"""
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        initial_count = len(self.df)
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        print(f"✅ Removed {initial_count - len(self.df)} outliers in {column}.")

    def save_data(self, output_path):
        """Export the clean data"""
        self.df.to_csv(output_path, index=False)
        print(f"💾 Cleaned data saved to {output_path}")