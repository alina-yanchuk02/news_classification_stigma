## Classification of stigmatizing news of mental illness, with machine learning and natural language processing

Author: Alina Yanchuk, 89093

### Data Collection program

This program collects data from public repository Arquivo.pt and performs web scraping. The result is a CSV file (data.csv) with structured relevant data. 
To execute, run: 

    pip install -r requirements.txt

    python3 collect_from_api.py 

### Preprocessing

The preprocessing stage is organized in a Jupyter Notebook, with the relevant steps described in the same. The data file used is the labeled data returned in the Data Collection step.

### Classification

The classification stage is organized in a Jupyter Notebook, with the relevant steps described in the same. The data file used is the cleaned data returnned in the Preprocessing step. For now, it has only 6 basic machine learning algorithms, their hyper-parameters tuning and evaluation metrics.

   - Logistic Regression
   - Linear SVC
   - Multinomial Naive Bayes
   - K-Nearest Neighbors
   - Random Forest
   - XGBoost