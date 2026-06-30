"""
# Pandas Class 7 Assignment


### Topics Covered
- Creating DataFrame
- Selecting Columns
- Filtering
- Sorting
- groupby()
- value_counts()
- Creating New Columns
- drop_duplicates()
- fillna()

### Instructions
- Create the DataFrame whenever required.
- Solve all questions using Pandas.
- Write your solution in the blank code cell after each question.
"""

"""
# Q1. Create a Student DataFrame

## Problem Statement
Create the following DataFrame using a Python dictionary.

| Name | Age | City | Marks |
|------|----:|------|------:|
| Aman | 21 | Bhopal | 85 |
| Rahul | 22 | Indore | 72 |
| Neha | 20 | Delhi | 91 |
| Priya | 23 | Bhopal | 68 |
| Ravi | 21 | Indore | 95 |

## Sample Input
```python
{
"Name":["Aman","Rahul","Neha","Priya","Ravi"],
"Age":[21,22,20,23,21],
"City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
"Marks":[85,72,91,68,95]
}
```

## Sample Output
```python
Display the complete DataFrame.
"""

import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)

"""
# Q2. Display Selected Columns

## Problem Statement
Using the DataFrame created in Question 1, display only the **Name** and **Marks** columns.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
Name and Marks columns only.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)

formated_df=df[["Name","Marks"]]
print(formated_df)


"""
# Q3. Filter Students

## Problem Statement
Display only those students whose **Marks are greater than 75**.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
Filtered rows.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
formated_df=df[df["Marks"]>75]
print(formated_df)

"""
# Q4. Sort by Marks

## Problem Statement
Sort the DataFrame by **Marks** in descending order.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
Sorted DataFrame.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
print("After sorting the marks values in ascending order: ")
print(df.sort_values(by="Marks",ascending=True))


"""
# Q5. Average Marks by City

## Problem Statement
Find the average Marks of each City using **groupby()**.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
Average marks city-wise.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
print("After finding the average mark in city wise: ")
print(df.groupby("City")["Marks"].mean())

"""
# Q6. Count Students by City

## Problem Statement
Count the number of students in each City using **value_counts()**.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
City frequency.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
print("After count the student city wise: ")
print(df.groupby("City")["Name"].value_counts())


"""
# Q7. Create Result Column

## Problem Statement
Create a new column named **Result**. If Marks are **40 or more**, store **Pass**, otherwise **Fail**.

## Sample Input
```python
Use the DataFrame from Q1
```

## Sample Output
```python
Updated DataFrame with Result column.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
print("After updating the DataFrame with result column is: ")
# Add the result column
df["Result"]=df["Marks"].apply(lambda x:"pass"if x>=40 else "fail")
print(df)

"""
# Q8. Remove Duplicate Rows

## Problem Statement
Create the following DataFrame:

| Name | Age | City | Marks |
|------|----:|------|------:|
| Aman | 21 | Bhopal | 85 |
| Rahul | 22 | Indore | 72 |
| Aman | 21 | Bhopal | 85 |
| Neha | 20 | Delhi | 91 |

Remove duplicate rows using **drop_duplicates()**.

## Sample Input
```python
Use the table above.
```

## Sample Output
```python
Duplicate rows removed.
"""
import pandas as pd
df=pd.DataFrame({
                "Name":["Aman","Rahul","Neha","Priya","Ravi"],
                "Age":[21,22,20,23,21],
                "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                "Marks":[85,72,91,68,95]
                })
print(df)
print("After remove the duplicates: ")
print(df.duplicated("City"))
print(df.drop_duplicates("City"))

"""
# Q9. Fill Missing Values

## Problem Statement
Create the following DataFrame:

| Name | Marks |
|------|------:|
| Aman | 85 |
| Rahul | NaN |
| Neha | 91 |
| Priya | NaN |

Fill missing values in the **Marks** column with **0** using **fillna()**.

## Sample Input
```python
Use the table above.
```

## Sample Output
```python
Missing values replaced with 0.
"""

import pandas as pd
import numpy as np
df=pd.DataFrame({"Name":["Aman","Rahul","Neha","Priya"],
                 "Marks":[85,np.nan,91,np.nan]})
print("The original data is:\n ")
print(df)
print("The null value is :\n")
print(df.isnull())
print("After filling the value 0 in place of null in the marks:\n ")
print(df.fillna(0))

"""
# Q10. Final Practice

## Problem Statement
Create a DataFrame with the following data:

| Name | City | Marks |
|------|------|------:|
| Aman | Bhopal | 85 |
| Rahul | Indore | 72 |
| Neha | Delhi | 91 |
| Priya | Bhopal | 68 |
| Ravi | Indore | 95 |

Perform all of the following:
1. Display students with Marks > 80.
2. Sort the DataFrame by Marks.
3. Find the average Marks of each City.

## Sample Input
```python
Use the table above.
```

## Sample Output
```python
Required outputs displayed.
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Rahul","Neha","Priya","Ravi"],
                 "City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
                 "Marks":[85,72,91,68,95]})
print("The original data is: ")
print(df)
print("The students with Marks > 90 :")
print(df[df["Marks"]>80])
print(("After sorting the Dataframe by marks : "))
print(df.sort_values(by="Marks"))
print("The average marks of each city: ")
print(df.groupby("City")["Marks"].mean())