"""
## Q1. Find Missing Values

Input:
df = pd.DataFrame({
    "Name":["Aman","Riya",None],
    "Age":[21,np.nan,25]
})

Output:
    Name    Age
0  False  False
1  False   True
2   True  False
"""

import pandas as pd
import numpy as np
df=pd.DataFrame({"Name":["Aman","Riya",None],"Age":[21,np.nan,25]})
print(df)
# after finding the null elements, we use the .isnull() methods
print(df.isnull())

"""
## Q2. Count Total Missing Values

Input:
df = pd.DataFrame({
    "Name":["Aman",None,"Raj"],
    "Age":[20,None,25]
})

Output:
Name    1
Age     1
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman",None,"Raj"],"Age":[20,None,25]})
# it counts the missing values in the sepcific column
print(df.isnull().sum())

"""
## Q3. Fill Missing Age with 0

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj"],
    "Age":[20,None]
})

Output:
   Name   Age
0  Aman  20.0
1   Raj   0.0
"""
import pandas as pd

df=pd.DataFrame({"Name":["Aman","Raj"],"Age":[20,None]})
print("the original data is: ")
print(df)

print("Data after adding the number 0")
print(df.fillna({"Age":0}))


"""
## Q4. Fill Missing City with 'Unknown'

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj"],
    "City":["Bhopal",None]
})

Output:
   Name     City
0  Aman   Bhopal
1   Raj  Unknown
"""

import pandas as pd 
df=pd.DataFrame({"Name":["Aman","Raj"],"City":["Bhopal",None]})
# by using the the fillna() method to put the Unknown  in place of None
df["City"]=df["City"].fillna("Unknown")
print(df)

"""
## Q5. Remove Rows Having Null Values

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj",None],
    "Age":[20,25,30]
})

Output:
   Name  Age
0  Aman   20
1   Raj   25
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Raj",None],"Age":[20,25,30]})
# the data with the None in the key Name
print(df)
# by using the dropna() inbuilt function to remove the missing data
df=df.dropna(subset=["Name"])
print("the data after removing thr unknown or null data  is ")
print(df)


"""
## Q6. Convert Age Column into Float

Input:
df = pd.DataFrame({"Age":[20,25,30]})

Output:
20.0, 25.0, 30.0
"""

import pandas as pd 

df=pd.DataFrame({"Age":[20,25,30]})
# we use the astype() to convert the int into float
df["Age"]=df["Age"].astype(float)

print("After changing into float is :",df)


"""
## Q7. Replace Delhi with New Delhi

Input:
df = pd.DataFrame({
    "City":["Delhi","Mumbai","Delhi"]
})

Output:
New Delhi, Mumbai, New Delhi
"""

import pandas as pd
df=pd.DataFrame({"City":["Delhi","Mumbai","Delhi"]})
print("Original data is :",df)

# by using the replace() inbuilt function  to change the string data
df["City"]=df["City"].replace("Delhi","New Delhi")
print("After changing the data is :",df)

"""
## Q8. Replace Score 88 with 100

Input:
df = pd.DataFrame({
    "Score":[88,90,88,75]
})

Output:
100,90,100,75
"""

import pandas as pd
df=pd.DataFrame({"Score":[88,90,88,75]})
print("The data before changing is :")
print(df)
# we can replace any data by using the .replace()
df["Score"]=df["Score"].replace(88,100)
print("the data after changing is: ")
print(df)

"""
## Q9. Drop City Column

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj"],
    "City":["Bhopal","Indore"]
})

Output:
   Name
0  Aman
1   Raj
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Raj"],"City":["Bhopal","Indore"]})
print("original data is :")
print(df)

df=df.drop("City",axis=1) # axis is used for column column
print("the data after removing the 2 column is:")
print(df)

"""
## Q10. Drop Row at Index 1

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj","Riya"]
})

Output:
   Name
0  Aman
2  Riya 
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Raj","Riya"]})
print("The original data is :")
print(df)
df=df.drop(1) # simple for reving the first index
print("Data after deleting is :")
print(df)

"""
## Q11. Check Duplicate Rows

Input:
df = pd.DataFrame({
    "Name":["Aman","Raj","Aman"]
})

Output:
False, False, True
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Raj","Aman"]})
print("The data before editing is :")
print(df)
# for checking the duplicate elements
df["Name"]=df["Name"].duplicated()
print(df)

"""
## Q12. Mini Data Cleaning Task

Input:
data = {
    "Name":["Aman","Raj","Aman",None],
    "Age":[20,None,20,25],
    "City":["Bhopal","Delhi","Bhopal","Indore"]
}

Task:
1. Fill missing Age with mean.
2. Remove duplicate rows.
3. Display final DataFrame.
"""
import pandas as pd
data=pd.DataFrame({"Name":["Aman","RAj","Aman",None],
                   "Age":[20,None,20,25],
                   "City":["Bhopal","Delhi","Bhopal","Indore"]})
print("The original data is:")
print(data)
# 1. filling the missing Age with mean
data["Age"]=data["Age"].fillna("mean")
print("the data after missing the values in the age :")
print(data)
# revove the duplicates rows

data=data.drop_duplicates()
print("Data after revoming duplicates is :")
print(data)
print("Final dataframe:")
print(data)

