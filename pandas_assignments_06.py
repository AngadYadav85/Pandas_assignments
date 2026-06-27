"""
# Q1. Display Unique Values

## Problem Statement
Create a DataFrame with a City column and display all unique cities.

## Sample Input
```python
City = ["Bhopal", "Indore", "Bhopal", "Delhi"]
```

## Sample Output
```python
['Bhopal' 'Indore' 'Delhi']
"""


import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                "Age":[20,25,25,30],
                "City":["Bhopal","Indore","Bhopal","Delhi"]})
print("The original data is:")
print(df)
print("After finding the unique cities is:")
print(df['City'].unique())

## (02) Count City Frequency

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[20,25,25,30],
                "City":["Bhopal","Indore","Bhopal","Delhi"]})
print("The original data is: ")
print(df)
print("After counting the frequency of cities is:")
print(df['City'].value_counts())

"""

# Q3. Count Unique Values

## Problem Statement
Find the number of unique cities in a DataFrame.

## Sample Input
```python
City = ["Bhopal", "Indore", "Bhopal", "Delhi"]
```

## Sample Output
```python
3
`
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[20,25,25,30],
                "City":["Bhopal","Indore","Bhopal","Delhi"]})
print("The original data is: ")
print(df)
print("after counting the number of cities is:")
print(df['City'].nunique())

"""
# Q4. Group By City

## Problem Statement
Find average marks city-wise using groupby().

## Sample Input
```python
City   Marks
Bhopal 80
Bhopal 90
Delhi  70
```

## Sample Output
```python
Bhopal 85
Delhi  70
"""

import pandas as pd
df=pd.DataFrame({"City":["Bhopal","Bhopal","Delhi"],
                 "Marks":[80,90,70]})

print("The original data is: ")
print(df)
print("After grouping by city and calculating average marks is:")
print(df.groupby('City')['Marks'].mean())


"""
# Q5. Sort Values

## Problem Statement
Sort students by Marks in ascending order.

## Sample Output
```python
Sorted DataFrame
"""
import pandas as pd
df=pd.DataFrame({"Student_Name":["Angad","Pawan","Abhi","Hello"],
                 "Marks":[80,90,70,85]})
print("The original data is: ")
print(df)
print("After sorting the students by marks in ascending order is:")
print(df.sort_values(by="Marks",ascending=True))



"""

# Q6. Sort Values Descending

## Problem Statement
Sort students by Marks in descending order.

## Sample Output
```python
Sorted DataFrame
"""

import pandas as pd
df=pd.DataFrame({"Student_Name":["Angad","Pawan","Abhi","Hello"],
                 "Marks":[80,90,70,85]})
print("the original data is: ")
print(df)
print("After sorting the students by marks in descending order is:")
print(df.sort_values(by="Marks",ascending=False))

"""
# Q7. Filter Records

## Problem Statement
Display students having marks greater than 75.

## Sample Output
```python
Filtered rows
"""

import pandas as pd
df=pd.DataFrame({"Student_Name":["Angad","Pawan","Abhi","Hello"],
                 "Marks":[80,90,70,85]})
print("The original data is: ")
print(df)
print("Filtered rows (marks > 75):")
print(df[df["Marks"]>75])


"""
# Q8. Multiple Conditions

## Problem Statement
Display students whose marks are greater than 70 and age is greater than 20.

## Sample Output
```python
Filtered rows
"""

import pandas as pd
df=pd.DataFrame({"Student_Name":["Angad","Pawan","Abhi","Hello"],
                 "Marks":[80,90,70,85],
                 "Age":[25,30,20,25]})
print("The original data is: ")
print(df)
print("Filtered rows (marks > 70 and age > 20):")   
filtered_df=df[(df["Marks"]>70) & (df["Age"]>20)]
print(filtered_df)

"""

# Q9. Group By Department

## Problem Statement
Create Employee and Department data and find total salary department-wise.

## Sample Output
```python
HR       50000
IT      120000
"""

import pandas as pd
df=pd.DataFrame({"Employee_Name":["Angad","Pawan","Abhi","Hello"],
                 "Department":["HR","IT","HR","IT"],      
                 "Salary":[25000,60000,25000,60000]})
print("The original data is: ")
print(df)
print("After grouping by department and calculating total salary is:")
print(df.groupby('Department')['Salary'].sum())

"""
# Q10. Complete Practice Question

## Problem Statement
Create a DataFrame containing:
- Name
- Age
- City
- Marks

Perform:
1. Show unique cities
2. Count city frequency
3. Filter marks > 80
4. Sort by marks

## Sample Output
```python
Required Results
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[20,25,25,30],   
                 "City":["Bhopal","Indore","Bhopal","Delhi"],
                 "Marks":[80,90,70,85]})
print("The original data is: ")
print(df)
print("Unique cities:")
print(df["City"].unique())
print("City frequency:")
print(df["City"].value_counts())
print("Filtered rows (marks > 80):")
filtered_df=df[df["Marks"]>80]
print(filtered_df)