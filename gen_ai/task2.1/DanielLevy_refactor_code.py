# ChatGPT Code Refactoring
import os
import pandas as pd

def extractMetaDataFromCSV(self):
    csv_file = next((f for f in os.listdir(self.dirName) if f.endswith('.csv')), None)

    if csv_file:
        self.metaData = pd.read_csv(os.path.join(self.dirName, csv_file))
    else:
        print("No .csv file containing student metadata was found.")
        exit(1)
