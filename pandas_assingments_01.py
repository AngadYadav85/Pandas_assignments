# """
# # Pandas Assignment — Class 1

# ## Level: Basic

# ### Topics Covered
# - What is Pandas
# - Importing Pandas
# - Series
# - DataFrame
# - Creating Series from List
# - Creating Series from Dictionary
# - Creating DataFrame from Dictionary
# - Creating DataFrame from NumPy Array

# ### Instructions
# - Use Pandas in every question.
# - Write code in the blank code cell below each question.
# - Print the required output.
# """


# """
# # Q1. Import Pandas

# ## Problem Statement
# Import the Pandas library and display its version.

# ## Sample Output
# ```python
# 2.x.x
# """

import pandas as pd
print(pd.__version__)


# """
# # Q2. Create a Series from a List

# ## Problem Statement
# Create a Pandas Series using the following list:

# ```python
# [10, 20, 30, 40, 50]
# ```

# ## Sample Output
# ```python
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
# """

import pandas as pd
marks=[10,20,30,40,50]
series=pd.Series(marks)
print(series)

# """
# # Q3. Create a Series of Student Names

# ## Problem Statement
# Create a Series using the following names:

# ```python
# ["Aman", "Rahul", "Neha", "Priya"]
# ```

# ## Sample Output
# ```python
# 0     Aman
# 1    Rahul
# 2     Neha
# 3    Priya
# dtype: object
# """

import pandas as pd
names=pd.Series(["Aman","Rahul","Neha","Priya"])
print(names)


# """

# # Q4. Create a Series from Dictionary

# ## Problem Statement
# Create a Series from the following dictionary:

# ```python
# {
#     "Maths": 80,
#     "Science": 75,
#     "English": 90
# }
# ```
# ## Sample Output
# ```python
# Maths      80
# Science    75
# English    90
# dtype: int64
# """

import pandas as pd
marks=pd.Series({"Maths":80,"Science":75,"English":90}) # dict.. accept the keys and values
print(marks)

# """

# # Q5. Create a Student DataFrame

# ## Problem Statement
# Create a DataFrame with the following data:

# ```python
# Name = ["Aman", "Rahul", "Neha"]
# Age = [21, 22, 20]
# ```

# ## Sample Output
# ```python
#     Name  Age
# 0   Aman   21
# 1  Rahul   22
# 2   Neha   20
# """

import pandas as pd
name=["Aman","Rahul","Neha"]
age=[21,22,20]
dataframe=pd.DataFrame({"Name":name,"Age":age})
print(dataframe)


# """
# # Q6. Employee DataFrame

# ## Problem Statement
# Create a DataFrame containing:

# ```python
# Employee = ["John", "Sara", "Mike"]
# Salary = [50000, 60000, 55000]
# ```

# ## Sample Output
# ```python
#   Employee  Salary
# 0     John   50000
# 1     Sara   60000
# 2     Mike   55000
# """

import pandas as pd 
detail=pd.DataFrame({"Employee":["John","Sara","Mike"],"Salary":["50000","60000","55000"]})
print(detail)


# """
# # Q7. DataFrame from NumPy Array

# ## Problem Statement
# Create the following NumPy array:

# ```python
# [[1,2],
#  [3,4],
#  [5,6]]
# ```

# Convert it into a Pandas DataFrame.

# ## Sample Output
# ```python
#    0  1
# 0  1  2
# 1  3  4
# 2  5  6
# """


import pandas as pd 
import numpy as np
arr=np.array([[1,2],
              [3,4],
              [5,6]])
pd_df=pd.DataFrame(arr)
print(pd_df)


# """
# # Q8. Create a Product DataFrame

# ## Problem Statement
# Create a DataFrame containing:

# ```python
# Product = ["Laptop", "Mouse", "Keyboard"]
# Price = [50000, 500, 1200]
# ```

# ## Sample Output
# ```python
#     Product  Price
# 0    Laptop  50000
# 1     Mouse    500
# 2  Keyboard   1200

# """


import pandas as pd 
detail=pd.DataFrame({"Product":["Laptop","Mouse","Keyboard"],"Price":["50000","500","1200"]})
print(detail)



# """
# # Q9. Display DataFrame Information

# ## Problem Statement
# Create a DataFrame with any 3 rows and 2 columns.

# Use:

# ```python
# df.info()
# ```

# to display information about the DataFrame.

# ## Sample Output
# ```python
# <class 'pandas.core.frame.DataFrame'>
# """

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Angad","Pawan"],"Age":[20,22,20]})
df.info()


# """
# # Q10. Create Marks DataFrame

# ## Problem Statement
# Create a DataFrame using:

# ```python
# Name = ["A", "B", "C"]
# Marks = [80, 75, 90]
# ```

# Print the DataFrame.

# ## Sample Output
# ```python
#   Name  Marks
# 0    A     80
# 1    B     75
# 2    C     90

# """


import pandas as pd 
name=["A","B","C"]
marks=[80,75,90]
detail=pd.DataFrame({"Name":name,"Marks":marks})
print(detail)


