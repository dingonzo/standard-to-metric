######################################################################
# Script Name: Assignment5.py
# Title: Assignment 5 Code File
# Description: Code file for SCP220 Week 5 Assignment. Re-write into
#              IDE of your choice.
# Author: Edgar Gonzalez
# Date: September 29, 2022
#####################################################################

# Initializing global data lists
standard1 = [12.25, 18.0, 27.125]
standard2 = [22.4, 60.0, 98.5]
metric1 = [0.0, 0.0, 0.0]
metric2 = [0.0, 0.0, 0.0]

# Global aliases used for the scope exercises
st1 = standard2
mc1 = metric2
st = standard1
mc = metric1

# =====================================================================
# TODO 1.1: Using function parameters. Delete 'pass' and modify the function to
# convert the values in the standard1 list (inch) and store in the metric1 list (mm).
# Do not print the data within the function, this will be done in TODO 2.1.
# DO NOT USE THE GLOBAL KEYWORD OR FUNCTION IN THIS STEP!
# =====================================================================
def standard_to_metric(st_param, mc_param):
    for x in range(len(st_param)):
        mc_param[x] = st_param[x] * 25.4

# TODO 1.2: Run the above function, passing in standard1 and metric1 as the parameter arguments.
standard_to_metric(standard1, metric1)


# =====================================================================
# TODO 2.1: Write a function that uses a loop to print the original and converted values in parallel with each other,
# each element and its converted value on each line with appropriate headings. Round to 2 decimal places.
# Only print the standard1 and metric1 functions.
# =====================================================================
def print_data(st_param, mc_param):
    print(f'{"Standard"}\t\t{"Metric"}')
    for x in range(len(mc_param)):
        print(f'{st_param[x]}\t\t\t{mc_param[x]:.2f}')

# TODO 2.2: Run the above function.
print_data(standard1, metric1)
print()


# =====================================================================
# TODO 3.1: Using global variables and the 'globals()' function or 'global' keyword, modify the function
# below to convert the standard values in the standard2 list and store in the metric2 list.
# DO NOT USE THE PARAMETERS IN THIS STEP. Do not print the data within this function, this will
# done in TODO 3.3.
# =====================================================================
def standard2_to_metric2():
    global st1, mc1
    for x in range(len(st1)):
        mc1[x] = st1[x] * 25.4

# TODO 3.2: Run the above function.
standard2_to_metric2()

# TODO 3.3: Using the function you defined in 2.1, print the results of your second conversion function.
# NOTE: DO NOT re-create the print_data() function! Depending on how you originally set up the
# print_data() function, you may need to go back and modify the print_data(). Only print standard2 and metric2.
print_data(st1, mc1)
print()


# =====================================================================
# TODO 4: Using the function 'main' below, repeat the above process from within the scope of main.
# Perform the conversions by calling the functions you wrote earlier, print the results using the
# function you defined earlier. BEST PRACTICE: Be sure to use the 'global' keyword or the 'globals()'
# functions, try not to access the global variables.
# =====================================================================
def main():
    # Explicitly referencing global scope as per instructions
    global standard1, metric1, standard2, metric2
    
    # Resetting the metric output vectors for the main execution run
    metric1 = [0.0, 0.0, 0.0]
    metric2 = [0.0, 0.0, 0.0]
    
    # Performing local parameter conversion & printing
    standard_to_metric(standard1, metric1)
    print("--- Main Function: Dataset 1 ---")
    print_data(standard1, metric1)
    print()
    
    # Performing global scope conversion & printing
    standard2_to_metric2()
    print("--- Main Function: Dataset 2 ---")
    print_data(standard2, metric2)

# Executing the main wrapper program
main()
