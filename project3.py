import numpy as np
import matplotlib.pyplot as plt

class HousePrices:
    def __init__(self):
        self.data = np.array(0)
        self.weights = np.ones(26)
        self.gradientArray = np.zeros([1,26])
        self.MSEArray = np.zeros([1,818])
        self.priceList = []
        self.predPriceList = []
        self.totalRecords = 0
        self.minPrice = 0
        self.maxPrice = 0
        self.mean = 0
        self.standardDeviation = 0
        self.MSE = 0


    def plotData(self):
        GrLivArea = []
        BedroomAbvGr = []
        TotalBsmtSf= []
        FullBath = []
        for i in self.data: # assign spreadsheet attributes to lists
            tempList = np.array(i)
            GrLivArea.append(float(tempList[11]))
            BedroomAbvGr.append(float(tempList[15]))
            TotalBsmtSf.append(float(tempList[7]))
            FullBath.append(float(tempList[13]))


        plt.hist(self.priceList, bins='auto', range = (self.minPrice, self.maxPrice)) # price vs house histogram
        plt.gca().set(title='Number of Houses per Price', ylabel='Number of Houses', xlabel='Price');

        fig, ax = plt.subplots(4, 4, sharex= 'col')

        ax[0, 0].hist(GrLivArea, bins='auto')
        ax[0, 0].set_xlabel('Number of Houses')
        ax[0, 0].set_ylabel('GrLivArea')

        ax[0, 1].scatter(GrLivArea, BedroomAbvGr)
        ax[0, 1].set_xlabel('GrLivArea')
        ax[0, 1].set_ylabel('BedroomAbvGr')

        ax[0, 2].scatter(GrLivArea, TotalBsmtSf)
        ax[0, 2].set_xlabel('GrLivArea')
        ax[0, 2].set_ylabel('TotalBsmtSf')

        ax[0, 3].scatter(GrLivArea, FullBath)
        ax[0, 3].set_xlabel('GrLivArea')
        ax[0, 3].set_ylabel('FullBath')


        ax[1, 0].scatter(BedroomAbvGr, GrLivArea)
        ax[1, 0].set_xlabel('BedroomAbvGr')
        ax[1, 0].set_ylabel('GrLivArea')

        ax[1, 1].hist(BedroomAbvGr, bins='auto')
        ax[1, 1].set_xlabel('Number of Houses')
        ax[1, 1].set_ylabel('BedroomAbvGr')

        ax[1, 2].scatter(BedroomAbvGr, TotalBsmtSf)
        ax[1, 2].set_xlabel('BedroomAbvGr')
        ax[1, 2].set_ylabel('TotalBsmtSf')

        ax[1, 3].scatter(BedroomAbvGr, FullBath)
        ax[1, 3].set_xlabel('BedroomAbvGr')
        ax[1, 3].set_ylabel('FullBath')


        ax[2, 0].scatter(FullBath, BedroomAbvGr)
        ax[2, 0].set_xlabel('FullBath')
        ax[2, 0].set_ylabel('BedroomAbvGr')

        ax[2, 1].scatter(FullBath, TotalBsmtSf)
        ax[2, 1].set_xlabel('FullBath')
        ax[2, 1].set_ylabel('TotalBsmtSf')

        ax[2, 2].hist(FullBath, bins='auto')
        ax[2, 2].set_xlabel('Number of Houses')
        ax[2, 2].set_ylabel('FullBath')

        ax[2, 3].scatter(FullBath,  GrLivArea)
        ax[2, 3].set_xlabel('FullBath')
        ax[2, 3].set_ylabel('GrLivArea')


        ax[3, 0].scatter(TotalBsmtSf, BedroomAbvGr)
        ax[3, 0].set_xlabel('TotalBsmtSf')
        ax[3, 0].set_ylabel('BedroomAbvGr')

        ax[3, 1].scatter(TotalBsmtSf,  FullBath)
        ax[3, 1].set_xlabel('TotalBsmtSf')
        ax[3, 1].set_ylabel('FullBath')

        ax[3, 2].scatter(TotalBsmtSf,  GrLivArea)
        ax[3, 2].set_xlabel('TotalBsmtSf')
        ax[3, 2].set_ylabel('GrLivArea')

        ax[3, 3].hist(TotalBsmtSf, bins='auto')
        ax[3, 3].set_xlabel('Number of Houses')
        ax[3, 3].set_ylabel('TotalBsmtSf')

        plt.show()


    def plotMSES(self, MSE11, MSE12):

        x = np.linspace(0, 500, 500)
        plt.plot(x, MSE12)
        plt.plot(x, MSE11) # plot two MSEs on the same plot
        plt.xlabel('iterations')
        plt.ylabel('MSE')
        plt.legend(['MSE w/ a = 10^-12', 'MSE w/ a = 10^-11'], loc='upper right')
        plt.autoscale()
        plt.show()


    def loadData(self, filename: str):
        file = open(filename, 'r')
        infoList = file.readlines()[1:]  # grab everything after the first line of data
        mean = 0
        totalRecords = 0
        minPrice = 10000
        maxPrice = 0
        priceList = []
        dataList = []
        for i in infoList:
            totalRecords += 1
            tempList = i.split(',')  # break list a part based on | operator
            tempList = tempList[1:27]  # remove 'id' attribute from list
            dataList.append(tempList)
            price = float(tempList[25])
            priceList.append(price)
            mean += price
            if price < minPrice: # grab min price
                minPrice = price
            if price > maxPrice: # grab max price
                maxPrice = price

        standardDev = np.std(priceList)
        mean = mean / totalRecords
        self.priceList = priceList
        self.data = np.array(dataList)
        self.mean = mean
        self.maxPrice = maxPrice  # assign class variables
        self.minPrice = minPrice
        self.standardDeviation = standardDev
        self.totalRecords = totalRecords

        print('max price ' + str(maxPrice))
        print('min price ' + str(minPrice))
        print('mean price ' + str(mean))
        print('total records ' + str(totalRecords))
        print('standard deviation ' + str(standardDev))

    def pred(self):
        self.predPriceList = []
        for row in self.data: # iterate through every row in data set
            valueRow = []
            totalPrice = 0
            rowArray = np.asfarray(row, dtype = float) # convert row of string to row of floats

            for value in rowArray:
                valueRow.append(value) # append to list for manipulation

            for i in range(0, len(valueRow)):
                totalPrice += valueRow[i] * self.weights[i]
            self.predPriceList.append(totalPrice) # add total predicted price for that house to a list

    def loss(self):
        totalLoss = 0
        predPriceArray  = np.array(self.predPriceList) # convert to np array for manipulation
        priceArray = np.array(self.priceList) # convert to np array for manipulation
        lossArray = np.square(predPriceArray- priceArray) # create an array of loss values
        self.MSEArray = lossArray
        for loss in lossArray:
            totalLoss += loss # calculate summation

        self.MSE= totalLoss / self.totalRecords

    def gradient(self):
        dataArray = np.asfarray(self.data,  dtype = float) # convert to np array of floats
        MSEArray = self.MSEArray
        self.gradientArray = 2/self.totalRecords * dataArray.transpose().dot(MSEArray) # calculate gradient

    def update11(self):
        self.weights = self.weights - 10 ** -11 * self.gradientArray # for alpha of 10^-11

    def update12(self):
        self.weights = self.weights - 10 ** -12 * self.gradientArray # for alpha of 10^-12

if __name__ == '__main__':
    mse11 = []
    mse12 = []

    house = HousePrices()
    house.loadData('train.csv')
    house.plotData()

    for i in range(0, 500):
        house.pred()
        house.loss()
        house.gradient()
        house.update11()
        mse11.append(house.MSE)
        i+=1

    print(house.MSE)

    house = HousePrices()
    house.loadData('train.csv')
    for i in range(0, 500):
        house.pred()
        house.loss()
        house.gradient()
        house.update12()
        mse12.append(house.MSE)
        i += 1

    print(house.MSE)
    house.plotMSES(mse11, mse12)

