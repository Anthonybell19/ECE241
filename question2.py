"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question2.py - DP planks with turtle
"""


class Fence_Builder:
    def __init__(self, planks):
        self.plank_list = planks

    def dpChoosePlanks(self, plankList, totalDistance, minPlanks, planksUsed):
        """
        EXAMPLE:
            plankList = [1,5,10,21,25] # list of possible planks
            distance = 63 # Actual amount
            minPlanks = [0,0...0] (64)
            planksUsed = [0,0...0] (64)
        """
        for plank in range(totalDistance+1):
            plankCount = plank
            newPlank = 1
            for j in [p for p in plankList if p <= plank]:
                if minPlanks[plank-j] + 1 < plankCount:
                    plankCount = minPlanks[plank-j]+1
                    newPlank = j
            minPlanks[plank]=plankCount
            planksUsed[plank] = newPlank
        return minPlanks[totalDistance]
        '''
        Fill your code here!
        '''


        return minPlanks[totalDistance]

    def printPlanks(self, planksUsed, totalDistance):
        dist = totalDistance
        plankOrder = []
        while dist > 0:
            thisDistance = planksUsed[dist]
            plankOrder.append(thisDistance)
            dist = dist - thisDistance
        return plankOrder[::-1]


    def select_planks(self, totalDist):
        planksUsed = [0] * (totalDist + 1)
        distCovered = [0] * (totalDist + 1)

        self.dpChoosePlanks(self.plank_list, totalDist, distCovered, planksUsed)
        A_list = self.printPlanks(planksUsed, totalDist)
        return A_list


if __name__ == "__main__":
    plankList = [1,5,10, 21, 25]
    fb = Fence_Builder(plankList)

    print(fb.select_planks(64))
    print(fb.select_planks(67))