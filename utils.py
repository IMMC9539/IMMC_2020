'''
IMMC 2020

This program contains the basic formulas
used in calculating the damage score.
'''

###########
# IMPORTS #
###########
import numpy as np

def people_per_product_metric(pop_density, prod_density, max_ratio):
    return pop_density / (prod_density * max_ratio)

def population_density(num_people, pop_perc, area_of_department):
    return (num_people * pop_perc) / area_of_department

def product_density(num_products, display_area):
    return num_products / display_area

def visibility(cashier_pos, dep_pos, pop_per, max_dist = (2*(48**2))**0.5):
    '''
    A Gaussian function with average change in decrease as a function of the popularity percentage.
    '''
    dist = ((max_dist - cashier_pos.distance(dep_pos))/(max_dist))

    return np.e ** (-1 * (1 - pop_per) * (dist ** 2))

#########
# POINT #
#########
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point2):
        return ((self.y - point2.y) ** 2 + (self.x - point2.x) ** 2) ** 0.5