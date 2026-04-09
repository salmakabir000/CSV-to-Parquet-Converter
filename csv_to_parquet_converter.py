import pandas as pd 
import os
import time

# load/read the csv file
csv_file = "data/Q3_Account Inactivity Alert.csv"
df = pd.read_csv(csv_file)
print("csv loaded successfully")
print("First 5 rows")
print(df.head())

# save/convert to parquet
parquet_file = "sample.parquet"
df.to_parquet(parquet_file, engine="pyarrow", index=False)
print("saved as parquet successfully")

# read back the parquet file to verify
df_parquet = pd.read_parquet(parquet_file, engine="pyarrow")
print("parquet read back successfully")
print("First 5 rows from our parquet file")
print(df_parquet.head())

# verify that the original CSV and the Parquet dataframes are identical
df_csv = df
df_parquet = pd.read_parquet(parquet_file, engine="pyarrow")
print("CSV and Parquet dataframes are identical:", df_csv.equals(df_parquet))

# compare file sizes
csv_size = os.path.getsize(csv_file) /(1024 * 1024)  # size in MB
parquet_size = os.path.getsize(parquet_file) / (1024 * 1024)  # size in MB
print(f"CSV file size: {csv_size:.2f} MB")
print(f"Parquet file size: {parquet_size:.2f} MB")

# compare read times
start = time.time()
pd.read_csv(csv_file)
print(f"Time taken to read CSV: {time.time() - start:.2f} seconds")

start = time.time()
pd.read_parquet(parquet_file, engine="pyarrow")
print(f"Time taken to read Parquet: {time.time() - start:.2f} seconds")