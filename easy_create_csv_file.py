# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:50:03 2020

@author: Saurav
"""
import pandas as pd

def input_name():

'''This is a function to ask the user to enter a name'''
    
    first_name = input("Please Enter Your First Name: \n")
    first_name = first_name.capitalize()
    print("--------------------------------------")    
    print(f"Hello, {first_name}")
    return first_name

def input_file_name(first_name): 
    
'''This function asks the user to input a file name.
    It takes output of input_name() as input'''
    
    file_name = input("What would you like to name the file?: \n")
    print("--------------------------------------") 
#The first name taken as input during function call is used here only.
    print(f"So, {first_name}, you would like to create a csv_file named '{file_name}' \n") 
#Confirming the user's action. Needs improvement on the invalid response part    
    confirm = input("Would you like to confirm? [y/n]: \n")
    if confirm == "n" or confirm == "N":
        print("--------------------------------------") 
        file_name = input_file_name(first_name)
    elif confirm == "y" or confirm == "Y":
        print("--------------------------------------") 
        print("Thank you")
        file_name = file_name + ".csv"
    else:
        print("--------------------------------------") 
        print("Invalid response!Try again!")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        file_name = input_file_name(first_name)
    return file_name
    
def create_file(file_name):

'''Creates a file with the file_name parameter during function call. 
    The parameter is the output of input_file_name() function'''
    
    file = open(file_name, 'x', newline='')
    file.close()

def column_name():
    
'''This function asks user for the column names and places them in the table in required order.
    Needs improvement on input flexibility and reusability'''
    
    column_no = input("How many columns would you like? \n")
    column_no = int(column_no)
    print("--------------------------------------")
    print("Please name the columns in their proper order.")
    column_names = []
    for i in range(1,column_no + 1):
        col_name = input("Enter column no. " + str(i) + " name. \n")
        column_names.append(col_name)
        print("--------------------------------------")
    print("These are the column names that you entered")
    print(column_names)
       
    return column_no, column_names

def insert_values(column_no, column_names):
    
'''This function takes parameters, column_no and column_names(output of column_name() function). 
   It asks the user to input values in proper order i.e 1st row 1st column, 1st row 2nd column and so on.
   Needs flexibility and better user understandable language'''    
   
    row_values = []
    rows_no = input("How many rows would you like to insert? \n")
    rows_no = int(rows_no)
    print("Please insert values of rows in their respective order. \n")
    print("--------------------------------------")
    for i in range(1, rows_no + 1):
        values = []
        print(f"Please enter the value of row no. {i}")
        print("--------------------------------------")
        for j in range(1, column_no + 1):
            row_element = input("Enter value of column no. " + str(j) + " (" + column_names[j-1] + ") \n")
            values.append(row_element)
        print("--------------------------------------")
        row_values.append(values)
    
    dataframe = pd.DataFrame(row_values, columns = column_names)
    return dataframe

    

def main():
    
    user_name = input_name()
    file_name = input_file_name(user_name)
    create_file(file_name)
    column_no, column_names = column_name()
    dataframe = insert_values(column_no, column_names)
    dataframe.to_csv(file_name)
