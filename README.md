## Classification of stigmatizing news of mental illness, with machine learning and natural language processing

Author: Alina Yanchuk, 89093

### Data Collection program

This program collects data from public repository Arquivo.pt and performs web scraping. The result is a CSV file (data.csv) with structured relevant data. 
To execute, run: 

    pip install -r requirements.txt

    python3 collect_from_api.py 

### 1. Preprocessing

The preprocessing stage is organized in a Jupyter Notebook, with the relevant steps described in the same. The data file used is the file returned in the Data Collection step. 
 
 Note: this data file is already manually labeled and also got some manual processing (after being returned in the Data Collection stage) to fully prepare it for the next steps.

### 2. Exploratory Data Analysis

The Exploratory Data Analysis stage is organidez in a Jupyter Notebook, with the relevant steps described in the same. The data file used is the file with the cleaned and prepared (for EDA) data returned in the Preprocessing step. This step is not important for the main process (Classification) but was done to obtain initial insights about the data.

### 3. Classification

The classification stage is organized in a Jupyter Notebook, with the relevant steps described in the same. The data file used is the file with the cleaned data returned in the Preprocessing step. For now, it has only 6 basic machine learning algorithms and 1 simple neural network, their hyper-parameters tuning (except CNN) and evaluation metrics.

   - Logistic Regression
   - Linear SVC
   - Multinomial Naive Bayes
   - K-Nearest Neighbors
   - Random Forest
   - XGBoost
   - Convolutional Neural Network (with Word2Vec PT 100D)