# CSV to Parquet Converter

## Overview
This project demonstrates how to convert CSV data into Parquet format using Python, evaluating the efficiency of Parquet in terms of file size and performance.

## Tools Used
- Python  
- Pandas  

## Process
1. Load CSV data into a DataFrame  
2. Convert the data to Parquet format  
3. Compare file sizes  
4. Measure read performance  
5. Validate data integrity  

## Results

### Data Integrity Check
The data was verified after conversion to ensure no loss or modification.
CSV and Parquet dataframes are identical: True

### File Size Comparison
| Format   | Size (MB) |
|----------|----------|
| CSV      | 0.50     |
| Parquet  | 0.27     |

Parquet file is smaller due to built-in compression.

### Performance Comparison
| Operation        | Time (seconds) |
|------------------|---------------|
| Read CSV         | 0.01          |
| Read Parquet     | 0.00          |

Parquet demonstrates faster read performance (especially at scale).

##  Rsults Screenshot
<img width="1296" height="393" alt="image" src="https://github.com/user-attachments/assets/90118f95-8dfe-46af-a7a6-225e3372eac4" />


## Key Insights
- Parquet preserves the same data as CSV  
- It uses columnar storage for efficiency  
- It significantly reduces file size  
- It improves performance for analytical workloads  


## Conclusion
Although CSV and Parquet store the same data, Parquet is more efficient for large-scale data processing due to its compression and optimized structure making it a better choice for analytics and data engineering workflows.

