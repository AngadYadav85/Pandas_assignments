"""
# Pandas Class 5 Assignment

## Topics
- sort_values()
- mean()
- median()
- mode()
- value_counts()
- corr()
- cov()

Difficulty: Easy to Moderate
"""

"""
## Q1. Sort Age in Ascending Order

Input:
Age = [25, 18, 30, 22]

Output:
18
22
25
30
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],"Age":[25,18,30,22]})
print(df)
df=df.sort_values(by="Age",ascending=True)
print("After sort the vlaues in ascending order is:")
print(df)

"""
## Q2. Sort Marks in Descending Order

Input:
Marks = [70, 95, 80, 60]

Output:
95
80
70
60
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[25,18,30,22],
                 "Marks":[70,95,80,60]})
print(df)
print("After sort the values in descending order is:")
df=df.sort_values(by="Marks",ascending=False)
print("After sort the vlaues in ascending order is:")
print(df)

"""
## Q3. Find Mean Age

Input:
Age = [20, 25, 30, 25]

Output:
25.
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[20,25,30,25],
                  "Marks":[70,95,80,60]})
print("The original data is :")
print(df)
print("After find the mean of age values is: ")
age_mean=df["Age"].mean()
print(age_mean)

"""
## Q4. Find Median Marks

Input:
Marks = [50, 60, 70, 80, 90]

Output:
70
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello","Anju"],
                "Age":[20,25,30,25,45],
                "Marks":[50,60,70,80,90]})
print("The original data is : ")
print(df)
print("After finding the median of Marks data is :")
Age_median=df["Marks"].median()
print(Age_median)


"""
## Q5. Find Mode

Input:
Age = [20, 25, 25, 30, 25]

Output:
25
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello","Anju"],
                "Age":[20,25,25,30,25],
                "Marks":[50,60,70,80,90]})
print("The original data is : ")
print(df)
print("After finding the mode of age is : ")
mode_Age=df["Age"].mode()
print(mode_Age)

"""
## Q6. Find Maximum Score

Input:
Score = [78, 90, 67, 88]

Output:
90
"""
import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello","Anju"],
                "Age":[20,25,25,30,25],
                "Score":[50,60,70,80,90]})
print("The original data is : ")
print(df)
print("After finding the maximum score is:")
s_max=df["Score"].max()
print(s_max)

"""
## Q7. Find Minimum Score

Input:
Score = [78, 90, 67, 88]

Output:
67
"""
import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                "Age":[20,25,25,30],
                "Score":[78,90,67,88]})
print("The original data is : ")
print(df)
print("After finding the minimum score is: ")
s_min=df["Score"].min()
print(s_min)


"""
## Q8. Count City Frequency

Input:
City = ['Bhopal','Indore','Bhopal','Jabalpur']

Output:
Bhopal      2
Indore      1
Jabalpur    1
"""
import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                "Age":[20,25,25,30],
                "City":["Bhopal","Indore","Bhopal","Jabalpur"]})
print("The original data is : ")
print(df)
count_city=df["City"].value_counts()
print(count_city)

"""
## Q9. Find Percentage Frequency

Input:
City = ['A','A','B','C']

Output:
A = 50%
B = 25%
C = 25%
"""
import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                "Age":[20,25,25,30],
                "City":["Bhopal","Indore","Bhopal","Jabalpur"]})
print("The original data is : ")
print(df)
print("The data after finding the percent city: ")
count_city_percent=df["City"].value_counts(normalize=True)*100
print(count_city_percent)


"""
## Q10. Sort DataFrame by Salary

Input:
Name   Salary
Aman   30000
Raj    50000
Riya   40000

Output:
Raj
Riya
Aman
"""

import pandas as pd
df=pd.DataFrame({"Name":["Aman","Raj","Riya"],
                 "Salary":[30000,50000,40000]})
print("The original data is : ")
print(df)
print("After sorting the dataframe by salary is: ")
sorted_df=df.sort_values(by="Salary",ascending=False)
print(sorted_df)

"""
## Q11. Find Correlation

Input:
Math = [10,20,30,40]
Science = [15,25,35,45]

Output:
1.0
"""

import pandas as pd
df=pd.DataFrame({"Math":[10,20,30,40],
                 "Science":[15,25,35,45]})
print("The original data is : ")
print(df)
print("After finding the correlation between math and science is:")
correlaction=df["Math"].corr(df["Science"])
print(correlaction)


"""
## Q12. Find Covariance

Input:
Math = [10,20,30,40]
Science = [15,25,35,45]

Output:
166.67 (approx)
"""

import pandas as pd
df=pd.DataFrame({"Math":[10,20,30,40],
                 "Science":[15,25,35,45]})
print("The original data is: ")
print(df)
covariance=df["Math"].cov(df["Science"])
print("The covariance between Math and Science is: ")
print(covariance,"approx 166.67")

"""
## Q13. Sort by Two Columns

Input:
Sort by City and then Age

Output:
Sorted DataFrame
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Age":[25,18,30,22],
                 "City":["Bhopal","Indore","Bhopal","Jabalpur"]})

print("The original data is: ")
print(df)
print("After sorting by City and then Age: ")
sorted_df=df.sort_values(by=["City","Age"])
print(sorted_df)

"""
## Q14. Student Statistics

Input:
Marks = [60,70,80,90]

Output:
Mean = 75
Median = 75
Max = 90
Min = 60
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello"],
                 "Marks":[60,70,80,90]})
print("The original data is: ")
print(df)   
print("After finding the statistics of Marks: ")
mean_marks=df["Marks"].mean()
median_marks=df["Marks"].median()
max_marks=df["Marks"].max()
min_marks=df["Marks"].min() 
print("Mean = ", mean_marks)    
print("Median = ", median_marks)
print("Max = ", max_marks)
print("Min = ", min_marks)

"""
## Q15. Mini Practice

Create a DataFrame with:
Name, Age, Score, Height

Tasks:
1. Sort by Score (Descending)
2. Find Mean Age
3. Find Median Height
4. Show Score Frequency
"""

import pandas as pd
df=pd.DataFrame({"Name":["Angad","Pawan","Abhi","Hello","Anju"],
                    "Age":[20,25,30,25,45],
                    "Score":[50,60,70,80,90],
                    "Height":[5.5,6.0,5.8,5.9,6.1]})
print("The original data is: ")
print(df)
sorted_df=df.sort_values(by="Score",ascending=False)
print("After sorting by Score (Descending): ")
print(sorted_df)
mean_age=df["Age"].mean()
print("Mean Age = ", mean_age)
median_height=df["Height"].median()
print("Median Height = ", median_height)
score_freq=df["Score"].value_counts()
print("Score Frequency: ")
print(score_freq)

