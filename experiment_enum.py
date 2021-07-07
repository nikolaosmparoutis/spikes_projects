import pandas as pd

ls = [ ('jack', 34, 'Sydeny') ,
             ('jack', 30, 'Delhi' ) ,
             ('Aadi', 16, 'New York') ]


df = pd.DataFrame(ls, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])

# print(df)
#
print(df.groupby(['Name']))

