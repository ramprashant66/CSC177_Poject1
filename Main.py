'''
Names: Prashant Ram
Course: CSC 177
Assignment: 1 - Data Preprocessing
Professor: Chidella

Details: This project deals with preprocessing data from a .csv file to ready it for
        data mining.
'''

import pandas

'''
This functions reads the data from a .csv file and makes columns for the data
'''
def makeTables():
    try:
        # import the data from the .csv file. "data" = dataframe
        data = pandas.read_csv('LaqnData.csv')

        #print the data attribute columns
        print(data.columns)
        
        # print the number of rows and columns
        print(f'We have {data.shape[0]} rows')
        print(f'We have {data.shape[1]} columns')

        # print the first 5 rows of the data
        data.head()
    except Exception as e:
        print("An error occured while trying to read from the CSV file", e)


def main():
    #import the data file for reading and make columns
    makeTables()

    
    


main()





