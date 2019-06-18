# import module
import pandas as pd

############################ import data #################################
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')

# divide into train and test set
train = data[0:1460]
test = data[1460:]

# gradient descent for 
# MSE(a1) = 1/n*(sum(a1*x1 - y1)**2)
def derivative(a1, xi_list, yi_list):
    dev = 0
    for i in range(0, len(xi_list)):
        dev += xi_list[i]*(a1*xi_list[i] - yi_list[i])
    dev = 2*dev/len(xi_list)
    return dev

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial):
    a1_list = [a1_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        deriv = derivative(a1, xi_list, yi_list)
        a1_new = a1 - alpha*deriv
        a1_list.append(a1_new)
    return(a1_list)

param_iterations = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150)
final_param = param_iterations[-1]

# gradient descent for 
# MSE(a0, a1) = 1/n*(sum(a0 + a1*x1 - y1)**2)

def a1_derivative(a0, a1, xi_list, yi_list):
    dev = 0
    len_x = len(xi_list)
    for i in range(len_x):
        dev += xi_list*(a0 + a1*xi_list - yi_list)
    dev = 2*dev/len_x
    return dev

def a0_derivative(a0, a1, xi_list, yi_list):
    dev = 0
    len_x = len(xi_list)
    for i in range(len_x):
        dev += (a0 + a1*xi_list - yi_list)
    dev = 2*dev/len_x
    return dev

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial, a0_initial):
    a1_list = [a1_initial]
    a0_list = [a0_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        a0 = a0_list[i]
        
        a1_deriv = a1_derivative(a0, a1, xi_list, yi_list)
        a0_deriv = a0_derivative(a0, a1, xi_list, yi_list)
        
        a1_new = a1 - alpha*a1_deriv
        a0_new = a0 - alpha*a0_deriv
        
        a1_list.append(a1_new)
        a0_list.append(a0_new)
    return(a0_list, a1_list)

# Uncomment when ready.
a0_params, a1_params = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150, 1000)