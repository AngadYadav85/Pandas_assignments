"""
# Q1. Select Single Column

## Problem Statement
Create a DataFrame and display only the Name column.

## Sample Input
```python
Name, Age
```

## Sample Output
```python
Only Name column
"""

import pandas as pd

text=pd.DataFrame({"Name":["Angad","Aman","Pawan"],"Age":[20,22,30]})
print("Original data is:")
print(text)
print('The data after print the  single column:')
print(text["Name"])


"""
# Q2. Select Multiple Columns

## Problem Statement
Display Name and Marks columns from a DataFrame.

## Sample Input
```python
Name, Marks
```

## Sample Output
```python
Selected columns
"""

import pandas as pd
text=pd.DataFrame({"Name":["Angad","Pawan","Harsh"],
                   "Marks":[80,90,78],
                   "Age":[20,21,22]})
print("The original data is :")
print(text)
print("The data after printing only two column: ")
print(text[["Name","Marks"]])


"""
# Q3. Filter Students

## Problem Statement
Display students with Marks greater than 80.

## Sample Input
```python
Marks > 80
```

## Sample Output
```python
Filtered rows
"""

import pandas as pd
text=pd.DataFrame({"Name":["Angad","Pawan","Harsh"],
                    "Marks":[80,90,78],
                    "Age":[20,21,22]})
print("The original data is: ")
print(text)
print("THe students who got marks>80:")
print(text[text["Marks"]>80])


"""
# Q4. Filter by City

## Problem Statement
Display students belonging to Bhopal.

## Sample Input
```python
City = Bhopal
```

## Sample Output
```python
Matching rows
"""

import pandas as pd
text=pd.DataFrame({"Students":["Angad","Pawan","Harshit","Abhi"],
                   "City":["Bhopal","Delhi","Bombay","Bhopal"]})
print("The original datais:")
print(text)
print("Students who lives in Bhopal: ")
print(text[text["City"]=="Bhopal"])


"""
# Q5. Find Maximum Marks

## Problem Statement
Find the highest marks from a DataFrame.

## Sample Input
```python
Marks column
```

## Sample Output
```python
Highest value
"""

import pandas as pd
text=pd.DataFrame({"Name":["Angad","Pawan","Harsh"],
                    "Marks":[80,90,78],
                    "Age":[20,21,22]})
print("The original data is:")
print(text)
print("The row with maximum marks of a student:")
print(text[text["Marks"]==text["Marks"].max()])

"""
# Q6. Find Minimum Age

## Problem Statement
Find the minimum age.

## Sample Input
```python
Age column
```

## Sample Output
```python
Minimum age
"""

import pandas as pd
text=pd.DataFrame({"Name":["Angad","Pawan","Harsh"],
                    "Marks":[80,90,78],
                    "Age":[20,21,22]})
print("The original data is :")
print(text)
print("The student who has maximum age:")
print(text[text["Age"]==text["Age"].max()])


"""
# Q7. Sort Data

## Problem Statement
Sort students by Marks.

## Sample Input
```python
Marks column
```

## Sample Output
```python
Sorted DataFrame
"""

import pandas as pd
text=pd.DataFrame({"Name":["Angad","Pawan","Harsh"],
                    "Marks":[80,90,78],
                    "Age":[20,21,22]})
print("The original data is :")
print(text)
print("The data after sort students by marks : ")
sorted_text=text.sort_values(by="Marks")
print(sorted_text)

"""
# Q8. Value Counts

## Problem Statement
Count occurrences of each city.

## Sample Input
```python
City column
```

## Sample Output
```python
Frequency count
"""

import pandas as pd
text=pd.DataFrame({"Students":["Angad","Pawan","Harshit","Abhi"],
                   "City":["Bhopal","Delhi","Bombay","Bhopal"]})
print("The original datais:")
print(text)
print("The frequency of the city: ")
print(text["City"].value_counts())

"""

# Q9. Group By City

## Problem Statement
Find average marks city-wise.

## Sample Input
```python
City and Marks
```

## Sample Output
```python
Grouped result
"""

import pandas as pd
text=pd.DataFrame({"Students":["Angad","Pawan","Harshit","Abhi"],
                   "City":["Bhopal","Delhi","Bombay","Bhopal"],
                   "Marks":[80,90,45,56]})
print("The original datais:")
print(text)
print("THe average marks of the student as city wise:")
print(text.groupby("City")["Marks"].mean())

"""

# Q10. Multiple Conditions

## Problem Statement
Display students with Marks > 70 and Age > 20.

## Sample Input
```python
Marks and Age
```

## Sample Output
```python
Filtered rows
"""


import pandas as pd
text=pd.DataFrame({"Students":["Angad","Pawan","Harshit","Abhi"],
                   "Age":[21,22,19,18],
                   "Marks":[80,90,89,56]})
print("The original datais:")
print(text)
print("The students who got marks>80 and age>20:")
filtured_text=text[(text["Marks"]>80) & (text["Age"]>20)]
print(filtured_text)








