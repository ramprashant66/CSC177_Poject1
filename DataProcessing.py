'''
Names: Prashant Ram
Course: CSC 177
Assignment: 1 - Data Preprocessing
Professor: Chidella
Details: This project deals with preprocessing data from a .csv file to ready it for
        data mining.
'''

import pandas
import matplotlib.pyplot as matPlot

class DataPreprocessing:
    '''
    This class is used to preprocess the data
    '''
    #constructor
    def __init__(self):
        self.data = None

'''
This function reads the data from a .csv file and makes columns for the data
'''
def makeTables(self):
     #formatting to display steps
    print("\n")
    print("." * 40, '\n', "." * 40)
    print(" " * 5, "Making Tables From CSV", " " * 5)
    print("." * 40, '\n', "." * 40)

    try:
        # import the data from the .csv file. "data" = dataframe
        self.data = pandas.read_csv('LaqnData.csv')

        #print the data attribute columns
        print(self.data.columns)
        
        # print the number of rows and columns
        print(f'We have {self.data.shape[0]} rows')
        print(f'We have {self.data.shape[1]} columns')

        # print the first 5 rows of the data
        print('\n', self.data.head())
    except Exception as e:
        print("An error occured while trying to read from the CSV file", e)

'''
This function counts the number of missing values in each column
'''
def missingValuesCount(self):
    #formatting to display steps
    print("\n")
    print("." * 40, '\n', "." * 40)
    print(" " * 5, "Missing Values In Each Column", " " * 5)
    print("." * 40, '\n', "." * 40)

    #list to hold the columns with missing values
    missingColumns = []

    try:
        #loop through the columns and get the number of missing values
        for col in self.data.columns:
            #get the total of column of missing values
            total = self.data[col].isna().sum()
            #display the column and the missing values number
            print(f"{col}: {total}")

            #add missing value columns to the list
            if total > 0:
                missingColumns.append(col)

        #finally display which columns had missing values
        print(f"\nThese columns had missing data: {missingColumns}")
    
    #catch any reading errors
    except Exception as e:
        print("umm. An error occurred while trying to replace the missing values..", e)

'''
This function drops all rows with missing data
'''
def dropMissingData(self):
    # print the number of rows and columns
    print(f'We have {self.data.shape[0]} [original] rows')
    print(f'We have {self.data.shape[1]} [original] columns')
     # print the first 5 rows of the data
    print('\n', self.data.head())
    
    #drops all rows with no data
    self.data = self.data.dropna()

    print(f'We have {self.data.shape[0]} [original] rows')
    print(f'We have {self.data.shape[1]} [original] columns')
     # print the first 5 rows of the data
    print('\n', self.data.head())

'''
Plots the data from the current dataframe
'''
def PlotData(self):
    #choose figure size for the plot area
    self.data.boxplot(figsize=(20,8))
    #display the data
    matPlot.show()
    

'''
This function cleans the data by removing outliers
through Z-Score calculation (drops data > 3 or < -3)
'''
def cleanOutliers(self):
    #convert field to numeric so that they can be used in the zScore calculation
    #calculate the mean of "Value" column
    mean = self.data['Value'].mean()
    #calculate the standard deviation of "Value" column
    std = self.data['Value'].std()
    #calulate the zScore
    zScore = (self.data['Value'] - mean) / std

    #show original data WITH outliers
    print(f"\nNumer of rows WITH outliers: {zScore.shape[0]}")

    # Create a mask for the all values in 'Values' that are outliers
    #accounts for +- 3 using normal distribution
    mask = zScore.abs() <= 3

    # Keep only the rows that pass this condition
    cleanData = self.data[mask]

    # #remove outliers
    self.data = cleanData
    
    print(f"Numer of rows without outliers: {self.data.shape[0]}")
    print(f"We removed {zScore.shape[0] - self.data.shape[0]} number of outliers from the original data!\n")

 

if __name__ == "__main__":
    #make the class object to work with
    preprocessedData = DataPreprocessing()

    #import the data file for reading and make columns
    makeTables(preprocessedData)

    #check for missing values
    missingValuesCount(preprocessedData)
    
    #drop all rows with missing data
    dropMissingData(preprocessedData)

    #clean the data by removing outliers
    cleanOutliers(preprocessedData)

    #Plots the current data from the dataframe
    PlotData(preprocessedData)
   