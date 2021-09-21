"""
UMass ECE 241 - Advanced Programming
Homework #3     Fall 2021
question3.py - Manipulating weather data

"""
# provides system specifics
import sys

# needed to make web requests
import requests

# store the data we get as a dataframe
import pandas as pd

# convert the response as a strcuctured json
import json

# mathematical operations on lists
import numpy as np

# parse the datetimes we get from NOAA
from datetime import datetime

# add the access token you got from NOAA
Token = 'QbUfrFiAhMCQJpobnyrIDvnbDycnanjZ'

# Long Beach Airport station
station_id = 'GHCND:USW00023129'

# Amherst Station
# station_id = 'GHCND:USC00190120'


# initialize lists to store data
dates_temp = []
dates_prcp = []


class QuestionThree(object):
    def highest_temp(self, alist):
        """
        This function receives an array of max. temperature data from a specified period
        and returns the highest temperature (highest T) in that period and the index on the array
        when that highest temperature occurred.
        :param alist: list with max. temp. data
        :return: highest temp and the index
        """
        maxVal = 0  # max value to be returned at the end of list iteration
        index = 0  # store the index of the max value
        for i in range(len(alist)):
            if alist[i] > maxVal:
                maxVal = alist[i]
                index = i
        return maxVal, index
        pass

    def lowest_temp(self, alist):
        """
        Similar to the previous method, this function receives an array with min. temp. data
        from a specific period and returns the lowest temp. (lowest T) and the index
        when this lowest temp. occurred.
        :param alist: list with min. temp. data
        :return: lowest temp. and the index
        """
        minVal = 0  # min value to be returned at the end of the list iteration
        index = 0  # store the index of the min value
        for i in range(len(alist)):
            if alist[i] < minVal:
                minVal = alist[i]
                index = i
        return minVal, index
        pass

    def average_high(self, alist):
        """
        This function receives an array with max. temp. data from a specific period and
        returns the average temp.
        :param alist: list with max. temp. data
        :return: average max. temp.
        """
        sum = 0  # will contain the sum of all the values in the list
        for i in range(len(alist)):
            sum += alist[i]

        averageMax = sum / len(alist)  # divide the total sum by the length of the list
        return averageMax
        pass

    def average_low(self, alist):
        """
        This function receives an array with min. temp. data from a specific period and
        returns the average temp.
        :param alist: list with min. temp. data
        :return: average min. temp.
        """
        sum = 0  # will contain the sum of all the values in the list
        for i in range(len(alist)):
            sum += alist[i]

        averageMin = sum / len(alist)  # divide the total sum by the length of the list
        return averageMin
        pass


# DO NOT MODIFY  THE CODE BELOW!!!!!!
def GetTemps(startyear, endyear, type):
    dates_temp = []
    tempsmax = []
    tempsmin = []
    for year in range(startyear, endyear):
        year = str(year)
        print('working on year ' + year)
        for type in type:
            print('working on Type:' + type)
            # make the api call
            r = requests.get(
                'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=' + type + '&limit=1000&stationid=GHCND:USC00190120&startdate=' + year + '-01-01&enddate=' + year + '-12-31',
                # 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=COOP:010008&units=metric&startdate=2010-05-01&enddate=2010-05-31',
                headers={'token': Token})
            # load the api response as a json
            d = json.loads(r.text)
            print(d)
            if type == 'TMAX':
                # get all items in the response which are average temperature readings
                max_temps = [item for item in d['results'] if item['datatype'] == 'TMAX']
                # get the date field from all average temperature readings
                dates_temp += [item['date'] for item in max_temps]
                # get the actual average temperature from all average temperature readings
                tempsmax += [item['value'] for item in max_temps]
                print(tempsmax)
            elif type == 'TMIN':
                # get all items in the response which are average temperature readings
                min_temps = [item for item in d['results'] if item['datatype'] == 'TMIN']
                # get the date field from all average temperature readings
                dates_temp += [item['date'] for item in min_temps]
                # get the actual average temperature from all average temperature readings
                tempsmin += [item['value'] for item in min_temps]
                print(tempsmin)
            else:
                print('Datatype not supported!!!')
    return tempsmax, tempsmin, dates_temp


maxTemps, minTemps, datesTemp = GetTemps(2010, 2011, ['TMAX', 'TMIN'])

statistics = QuestionThree()
max, maxindex = statistics.highest_temp(maxTemps)
min, minindex = statistics.lowest_temp(minTemps)
print('Max:', max, maxindex, ' Min:', min, minindex)
avg_max = statistics.average_high(maxTemps)
avg_min = statistics.average_low(minTemps)
print("Average high:", avg_max, " Average low:", avg_min)

# initialize dataframe
df_temp = pd.DataFrame()

# populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['avgTemp'] = [float(v) / 10.0 * 1.8 + 32 for v in maxTemps]
