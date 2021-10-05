"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2021
question4.py - position of partial sorted list

"""

"""
A shelf contains some products sorted according to their width,
e.g.     |||10, 20|||

we place more already sorted products with lesser width than
the one that are already present.
e.g.     |||10,20||1,2,4,7|||

Find the position of a given product (no sorting allowed and find it in O(log n))

e.g.     |||10, 20||1, 2, 4, 7|||
         position of product with width 10 is 0
         position of product with width 7 is 5
"""


class Shelf:

    def search_product(self, shelf_contents, lower_l, upper_l, product):

        mid = (lower_l + upper_l) // 2  # get the middle index of the list
        if product == shelf_contents[mid]: # if our product is equal to the middle of the list, return the value
            return mid
        if lower_l >= upper_l: # if lower bound has become greater than or equal to upper bound, we know the product is
                                # not in the list.
            return -1
        if shelf_contents[lower_l] < shelf_contents[mid]:  # check to see if lower half is sorted
            if shelf_contents[lower_l] <= product <= shelf_contents[mid]: # check to see if product is in lower half
                return self.search_product(shelf_contents, lower_l, mid - 1, product)
            else:
                return self.search_product(shelf_contents, mid + 1, upper_l, product) # else it must be in upper half

        if shelf_contents[mid] < shelf_contents[upper_l]: # check to see if upper half is sorted
            if shelf_contents[mid] <= product <= shelf_contents[upper_l]: # check to see if product is in upper half
                return self.search_product(shelf_contents, mid + 1, upper_l, product)
            else:
                return self.search_product(shelf_contents, lower_l, mid - 1, product) # else it must be in lower half

    def locate_product(self, pos, shelf_contents):
        '''
        (Don't Modify this function) Notifies the position of the product under consideration
        '''
        if pos < -1:
            print("\nFill in the search function and remove 'return -2'")
            return

        if pos != -1:
            print("\n########### Found product on the Shelf ###########")

            print("Found product with width:{} at position:{} ".format(shelf_contents[pos], pos))

            print("\n##################################################")
        else:
            print("\nNo such product!!")


def main():
    shelf_contents = [10, 20, 1, 2, 3, 6, 7]
    shelf_obj = Shelf()
    product_to_be_found = 1
    pos = shelf_obj.search_product(shelf_contents, 0, len(shelf_contents) - 1, product_to_be_found)
    print("pos:{}".format(pos))
    shelf_obj.locate_product(pos, shelf_contents)


if __name__ == '__main__':
    main()
