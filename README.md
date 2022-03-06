##Classification of stigmatizing news of mental illness, with machine learning and natural language processing

Author: Alina Yanchuk, 89093

## Data Collection program

This program collects data from public repository Arquivo.pt and performs web scraping. The result is a CSV file (data.csv) with structured relevant data. 
To execute, run: 

    pip install -r requirements.txt

    python3 collect_from_api.py 

## Preprocessing

The preprocessing stage is organized in a Jupyter Notebook, with the relevant steps described in the same. The data file used is a sample from the original file that will be retrieved in the Data Collection step.
