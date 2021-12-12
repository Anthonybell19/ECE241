import numpy as np
import matplotlib.pyplot as plt

class HousePrices:
    def __init__(self):
        self.data = []
        self.weights = []
        self.priceList = []
        self.predPriceList = []
        self.totalRecords = 0
        self.minPrice = 0
        self.maxPrice = 0
        self.mean = 0
        self.standardDeviation = 0
        self.loss = 0

    def loadData(self, filename: str):
        file = open(filename, 'r')
        infoList = file.readlines()[1:]  # grab everything after the first line of data
        mean = 0
        totalRecords = 0
        minPrice = 10000
        maxPrice = 0
        priceList = []
        for i in infoList:
            totalRecords += 1
            tempList = i.split(',')  # break list a part based on | operator
            priceString = tempList[26].split('\n')
            price = float(priceString[0])
            priceList.append(price)
            mean += price
            if price < minPrice:
                minPrice = price
            if price > maxPrice:
                maxPrice = price

        standardDev = np.std(priceList)
        mean = mean / totalRecords
        self.priceList = priceList
        self.data = infoList
        self.mean = mean
        self.maxPrice = maxPrice
        self.minPrice = minPrice
        self.standardDeviation  = standardDev
        self.totalRecords = totalRecords

        print('max price ' + str(maxPrice))
        print('min price ' + str(minPrice))
        print('mean price ' + str(mean))
        print('total records ' + str(totalRecords))
        print('standard deviation ' + str(standardDev))

    def plotData(self):
        GrLivArea = []
        BedroomAbvGr = []
        TotalBsmtSf= []
        FullBath = []
        for i in self.data:
            tempList = i.split(',')
            GrLivArea.append(float(tempList[12]))
            BedroomAbvGr.append(float(tempList[16]))
            TotalBsmtSf.append(float(tempList[8]))
            FullBath.append(float(tempList[14]))

        plt.scatter(GrLivArea,BedroomAbvGr,TotalBsmtSf, FullBath, )
        # plt.hist(self.priceList, bins='auto', range = (self.minPrice, self.maxPrice))
        plt.gca().set(title='Price Histogram', ylabel='Price');
        plt.show()

    def pred(self, weights):
        predPriceList = []
        for i in self.data:
            price = 0
            features = i.split(',')
            for j in features:
                featureWeight = features[j] * weights[j]
                price += featureWeight
            predPriceList.append(price)
        self.predPriceList = predPriceList
    def loss(self):
        loss = 0
        for i in range(0, len(self.priceList)):
            loss += (self.priceList[i] - self.predPriceList[i])**2
        self.loss = loss / self.totalRecords

if __name__ == '__main__':
    house = HousePrices()
    house.loadData('train.csv')
    house.plotData()
