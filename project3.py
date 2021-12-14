import numpy as np
import matplotlib.pyplot as plt

class HousePrices:
    def __init__(self):
        self.data = []
        self.weights = np.ones(26)
        self.gradientArray = []
        self.priceList = []
        self.predPriceList = []
        self.totalRecords = 0
        self.minPrice = 0
        self.maxPrice = 0
        self.mean = 0
        self.standardDeviation = 0
        self.lossValue = 0

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


        plt.hist(self.priceList, bins='auto', range = (self.minPrice, self.maxPrice), )
        plt.gca().set(title='Number of Houses per Price', ylabel='Number of Houses', xlabel='Price');

        fig, ax = plt.subplots(4, 3, sharex='col', sharey='row')

        ax[0,0].scatter(GrLivArea, BedroomAbvGr)
        ax[0,0].set_xlabel('GrLivArea')
        ax[0, 0].set_ylabel('BedroomAbvGr')

        ax[0, 1].scatter(GrLivArea, TotalBsmtSf)
        ax[0, 1].set_xlabel('GrLivArea')
        ax[0, 1].set_ylabel('TotalBsmtSf')

        ax[0, 2].scatter(GrLivArea, FullBath)
        ax[0, 2].set_xlabel('GrLivArea')
        ax[0, 2].set_ylabel('FullBath')


        ax[1, 0].scatter(BedroomAbvGr, GrLivArea)
        ax[1, 0].set_xlabel('BedroomAbvGr')
        ax[1, 0].set_ylabel('GrLivArea')

        ax[1, 1].scatter(BedroomAbvGr, TotalBsmtSf)
        ax[1, 1].set_xlabel('BedroomAbvGr')
        ax[1, 1].set_ylabel('TotalBsmtSf')

        ax[1, 2].scatter(BedroomAbvGr, FullBath)
        ax[1, 2].set_xlabel('BedroomAbvGr')
        ax[1, 2].set_ylabel('FullBath')


        ax[2, 0].scatter(FullBath, BedroomAbvGr)
        ax[2, 0].set_xlabel('FullBath')
        ax[2, 0].set_ylabel('BedroomAbvGr')

        ax[2, 1].scatter(FullBath, TotalBsmtSf)
        ax[2, 1].set_xlabel('FullBath')
        ax[2, 1].set_ylabel('TotalBsmtSf')

        ax[2, 2].scatter(FullBath,  GrLivArea)
        ax[2, 2].set_xlabel('FullBath')
        ax[2, 2].set_ylabel('GrLivArea')


        ax[3, 0].scatter(TotalBsmtSf, BedroomAbvGr)
        ax[3, 0].set_xlabel('TotalBsmtSf')
        ax[3, 0].set_ylabel('BedroomAbvGr')

        ax[3, 1].scatter(TotalBsmtSf,  FullBath)
        ax[3, 1].set_xlabel('TotalBsmtSf')
        ax[3, 1].set_ylabel('FullBath')

        ax[3, 2].scatter(TotalBsmtSf,  GrLivArea)
        ax[3, 2].set_xlabel('TotalBsmtSf')
        ax[3, 2].set_ylabel('GrLivArea')








        plt.show()

        # plt.show()

    def pred(self):
        predPriceList = []
        for i in self.data:
            price = 0
            features = i.split(',')
            for j in range(1,len(features)-1):
                featureWeight = float(features[j]) * self.weights[j]
                price += featureWeight
            predPriceList.append(price)
        self.predPriceList = predPriceList

    def loss(self):
        loss = 0
        for i in range(0, len(self.priceList)):
            loss += (self.priceList[i] - self.predPriceList[i])**2
        self.lossValue = loss / self.totalRecords

    def gradient(self):
        gradient = np.zeros(26)
        for i in range(0, len(gradient)):
            gradient[i] = 2/self.totalRecords * np.tranpose(self.data)*(self.predPriceList[i]-self.priceList[i])

        print(gradient)
    def update(self):
        for i in range(1, len(self.weights)):
            self.weights[i] = self.weights[i] - 0.2* self.gradient[i]

if __name__ == '__main__':
    house = HousePrices()
    house.loadData('train.csv')
    house.plotData()
    house.pred()
    print(house.predPriceList)
    house.loss()
    print(house.lossValue)
    house.gradient()
    house.update()
    print(house.weights)