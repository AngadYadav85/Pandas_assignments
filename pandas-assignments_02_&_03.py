"""
# Pandas Final Assignment (Class 2 + Class 3)

### Topics Covered
- head()
- tail()
- info()
- shape
- dtypes
- loc
- iloc
- rename()
- set_index()
- reset_index()
- isnull()
- fillna()
- astype()
- replace()
- drop()
- duplicated()
- drop_duplicates()

### Instructions
- Use Pandas in every question.
- Write code in the blank code cell below each question.
- Print the required output.
"""


"""
# Q1. Display First Rows

## Problem Statement
Create the following DataFrame:

| Name | Age |
|------|-----|
| Aman | 21 |
| Rahul | 22 |
| Neha | 20 |
| Priya | 23 |
| Ravi | 24 |

Display the first 3 rows using `head()`.

## Sample Output
```python
First 3 rows of DataFrame
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Aman","Rahul","Neha","Priya","Ravi"],"Age":[21,22,20,23,24]})
print(detail)
print(detail.head(3))



"""
# Q2. Display Last Rows

## Problem Statement
Create a DataFrame containing 6 student records.

Display the last 2 rows using `tail()`.

## Sample Output
```python
Last 2 rows of DataFrame
"""

import pandas as pd
detail=pd.DataFrame({"Students name":["Prince","Angad","Pawan","Abhishek","Karan"],"Marks":[60,75,80,90,50]})
print(detail)
print(detail.tail(2))


"""
# Q3. Check DataFrame Information

## Problem Statement
Create a DataFrame containing:

```python
Name = ["Aman","Rahul","Neha"]
Marks = [80,75,90]
```

Display DataFrame information using `info()`.

## Sample Output
```python
<class 'pandas.core.frame.DataFrame'>
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Aman","Rahul","Neha"],"Marks":[80,75,90]})
print(detail)
print(detail.info())


"""

# Q4. Shape and Data Types

## Problem Statement
Create a DataFrame with:

```python
Name
Age
City
```

Print:
- Shape
- Data Types

## Sample Output
```python
(3,3)
object
int64
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Pawan","Angad","Aman"],"Age":[20,24,26],"City":["Bhopal","Delhi","Mumbai"]})
print(detail)
print(detail.shape)
print(detail.dtypes)



"""
# Q5. Select Data using loc

## Problem Statement
Create a DataFrame with Name, Age and City.

Using `loc`, display the Name and City of the first row.

## Sample Output
```python
Name    Aman
City    Bhopal
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Pawan","Angad","Aman"],"Age":[20,24,26],"City":["Bhopal","Delhi","Mumbai"]})
print(detail)
print(detail.loc[2,["Name","City"]])



"""
# Q6. Select Data using iloc

## Problem Statement
Create a DataFrame with at least 4 rows.

Using `iloc`, print:
- Second row
- First two columns

## Sample Output
```python
Selected row values
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Pawan","Angad","Aman"],"Age":[20,24,26],"City":["Bhopal","Delhi","Mumbai"]})
print(detail)
print(detail.iloc[1:2,0:2])


"""

# Q7. Rename a Column

## Problem Statement
Create a DataFrame:

```python
Name
Marks
```

Rename column `Marks` to `Score`.

## Sample Output
```python
Name  Score
"""

import pandas as pd
detail=pd.DataFrame({"Name":["Aman","Rahul","Neha"],"Marks":[80,75,90]})
print(detail)
print(detail.rename(columns={"Marks":"Score"},inplace=True))
print(detail)


"""
# Q8. Handle Missing Values

## Problem Statement
Create a DataFrame:

```python
Name = ["Aman", None, "Neha"]
Marks = [80, 75, None]
```

Fill missing values using `fillna()`.

## Sample Output
```python
Missing values replaced
"""


import pandas as pd
name=["Aman",None,"Neha"]
marks=[80,75,None]
detail=pd.DataFrame({"Name":name,"Marks":marks})
print(f"the original data is {detail}")
# After replacing the None place

detail["Name"]=detail["Name"].fillna("unknown")
detail["Marks"]=detail["Marks"].fillna(0)
print(f"Data after missing values replaced is{detail} ")


"""
# Q9. Replace Values

## Problem Statement
Create a DataFrame:

```python
City = ["BPL", "IND", "BPL"]
```

Replace:
- BPL → Bhopal
- IND → Indore

## Sample Output
```python
Bhopal
Indore
Bhopal
"""
import pandas as pd
city=["BPL","IND","BPL"]
detail=pd.DataFrame({"City":city})
print(detail)

detail["City"]=detail["City"].replace({"BPL":"BHOPAL","IND":"INDORE"})
print("The detail after updating : ")
print(detail)


"""
# Q10. Remove Duplicate Records

## Problem Statement
Create a DataFrame:

```python
Name = ["Aman","Rahul","Aman","Neha"]
```

Check duplicate rows using `duplicated()` and remove them using `drop_duplicates()`.

## Sample Output
```python
Aman
Rahul
Neha
"""

import pandas as pd

detail=pd.DataFrame({"Name":["Aman","Rahul","Aman","Neha"]})
print("The original data is ")
print(detail)

# check the duplicates elements in the detail 
print(detail.duplicated(detail))

# print after removing the duplicates
print("After removing the duplicates")
print(detail.drop_duplicates(detail))











