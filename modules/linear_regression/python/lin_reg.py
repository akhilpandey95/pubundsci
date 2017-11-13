# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import math
import matplotlib
import numpy as np
import pandas as pd

def loess_linear_regression(dataframe, init_index, expected_index, variable_x, variable_y, degree_of_smoothness):
    result = []
    initial = np.array(dataframe[init_index])
    expected = np.array(dataframe[expected_index])

    # iterate over the columns of the given dataframe
    for values in initial:
        result.append(loess_point(values, degree_of_smoothness, initial, expected))

    # return both the initial array and the result
    result = np.array(result)
    return initial, result

def loess_point(values, smoothness, values_of_matrix_one, values_of_matrix_two):
    weight = math.exp(-0.5 * (((values - values_of_matrix_one) / smoothness) ** 2) / math.sqrt(2 * math.pi * smoothness ** 2))
    c = (sum(weight * values_of_matrix_two) - m * sum(weight * values_of_matrix_two)) / sum(weight)
    m = ((sum(weight * values_of_matrix_one) * sum(weight * values_of_matrix_two)) - (sum(weight) * sum(weight * values_of_matrix_one * values_of_matrix_two)))
    m /= sum(weight * values_of_matrix_two) - sum(weight) * sum(values * values_of_matrix_one ** 2)

    # return the loess point
    result = m*x + c
    return result

if __name__ == "__main__":
    print "Linear Regression Model"
    loess_linear_regression()
else:
    sys.exit(0)
