#!/usr/bin/env python
# coding: utf-8

# <h1>Classes</h1>
# <ul>
#   <li>
#   Object-orientated programming approach popular and efficient
#   </li>
#   <li>
#    Define classes of real-world things or situations (can be thought of as creating your own data type)
#     <ul>
#       <li>Attributes of various data types</li>
#       <li>Functions inside of a class are the same except called methods</li>
#       <li>Methods may be accessed using the dot operator</li>
#     </ul>
#   </li>
#   <li>Instanciate objects of your classes</li>
#   <li>__init()__ method used to prefill attributes</li>
#   <li>Capitalize class names</li>
# </ul>

# In[1]:


#Create a Payment class and assign it 3 attributes: payer, payee, amount

class Payment():  
    def __init__(self, payer, payee, amount):
        self.payer = payers
        self.payee = payees
        self.amount = amounts
    


# In[5]:


pay1 = Payment("Daniel", "Toppan", 100)


# In[7]:


print(pay1.amount)


# In[8]:


print(pay1.payee)


# ## Pandas 
# 
# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language. 
# 
# It will seamlessly bridge the gap between Python and Excel.
# 
# 
# Built Around 2 Main Classes:
#  - DataFrames
#  - Series

# ## Jupyter Notebook 
# 
# This is a web-based application (runs in the browser) that is used to interpret Python code. 
# 
# - To add more code cells (or blocks) click on the **'+'** button in the top left corner
# - There are 3 cell types in Jupyter:
#     - Code: Used to write Python code
#     - Markdown: Used to write texts (can be used to write explanations and other key information)
#     - NBConvert: Used convert Jupyter (.ipynb) files to other formats (HTML, LaTex, etc.) 
#     
# 
# - To run Python code in a specific cell, you can click on the **'Run'** button at the top or press **Shift + Enter**
# - The number sign (#) is used to insert comments when coding to leave messages for yourself or others. These comments will not be interpreted as code and are overlooked by the program
# 

# In[9]:


#Import pandas and assign it to a shorthand name pd 
import pandas as pd


# <h1>Reading CSV Files</h1>
# 
# <ul>
#     <li>Function to use in Pandas: read_csv()</li>
#     <li>Value passed to read_csv() must be string and the <b>exact</b> name of the file</li>
#     <li>CSV Files must be in the same directory as the python file/notebook</li>
# </ul>

# In[11]:


#Read our data into a DataFrame names features_df
#read_excel does the same but for spreadsheet files

features_df = pd.read_csv('features.csv')

#print(df)


# <h1>Basic DataFrame Functions</h1>
# 
# <ul>
#     <li>head() will display the first 5 values of the DataFrame</li>
#     <li>tail() will display the last 5 values of the DataFrame </li>
#     <li>shape will display the dimensions of the DataFrame</li>
#     <li>columns() will return the columns of the DataFrame as a list</li>
#     <li>dtypes will display the types of each column of the DataFrame</li>
#     <li>drop() will remove a column from the DataFrame</li>
# </ul>

# In[13]:


#Display top 5 rows

features_df.head()

#nan values are essentially empty entries


# In[15]:


#Display bottom 5 rows




# In[17]:


#Print dimensions of DataFrame as tuple

features_df.shape


# In[18]:


#Print list of column values

features_df.columns


# In[19]:


#To only rename specific columns

features_df.rename(columns = {"Temperature" : "Temp", "MarkDown1" : "MD1"}, inplace = True)


# In[21]:


#Print Pandas-specific data types of all columns

features_df.dtypes


# <h1>Indexing and Series Functions</h1>
# 
# <ul>
#     <li>Columns of a DataFrame can be accessed through the following format: df_name["name_of_column"] </li>
#     <li>Columns will be returned as a Series, which have different methods than DataFrames </li>
#     <li>A couple useful Series functions: max(), median(), min(), value_counts(), sort_values()</li>
# </ul>

# In[23]:


#Extract CPI column of features_df

features_df['CPI'].head()

# -- features_df.CPI -- is another way that this code can be run


# In[25]:


#Display the dimensions with 'shape'
#Display the total number of entries with 'size'
# Example with our DataFrame

print(features_df.shape)
print(features_df.size)


# In[26]:


#Maximum value in Series

features_df["CPI"].max()


# In[27]:


#Median value in Series

features_df['CPI'].median()


# In[28]:


#Minimum value in Series

features_df['CPI'].min()


# In[29]:


#Basic Statistical Summary of a column

features_df['Temp'].describe()


# In[30]:


#Print list of unique values

features_df['Store'].unique()


# In[31]:


#Print unique values and frequency

features_df['Store'].value_counts()


# In[35]:


#Return a sorted DataFrame acording to specified column

features_df.sort_values(by = "Store", ascending = True)

features_df.head()


# In[ ]:





# In[40]:


# delete one column

features_df.drop(columns = "MD1").head()

features_df.head()


# In[42]:


# Check for missing values and how many

features_df.isnull().sum()


# In[44]:


# delete multiple columns

features_df.drop(columns = "MD1", inplace = True)


# In[46]:



features_df.head()


# In[48]:


#Define a function to convert float values to our custom categorical ranges

def temp_categorical(temp):

#Function Name : temp_categorical -> temp

#The first condition is: IF VALUE IS LESS THAN 50
    if temp < 50: 
        return "Pretty Mild"


#The second condition is: IN BETWEEN 50 (INCLUSIVE) AND 80 (EXCLUSIVE)
    elif temp >= 50 and temp < 80 : 
        return "Somewhat Warm"


#FALLBACK OPTION
    else:
        return "Very Hot"


# In[49]:


#With the apply() function we can apply our custom function to each value of the Series

features_df["Temp"] = features_df["Temp"].apply(temp_categorical)


# In[50]:



features_df["Temp"].tail()


# In[58]:


#More efficient way method
#Uses matrix manipulation instead of row by row increments

features_df["Unemployment"] += 1

#The function above can be the same as this: ------- features_df["Unemployment"] = features_df["Unemployment"] + 1 --------


# In[59]:



features_df.head()


# In[61]:


#Say a colleague of yours asks for a new metric called "customerCost"
#Add a column that is equal to Fuel_Price * CPI 

features_df["customerCost"] = features_df["Fuel_Prices"] * features_df["CPI"]

features_df.head()


# <h1>Indexing</h1>
# 
# <ul>
#     <li>Because Pandas will select entries based on column values by default, selecting data based on row values requires the use of the iloc method. 
#     </li>
#     <li>
#       Allowed inputs are:
#         <ul>
#             <li>An integer, e.g. 5.</li>
#             <li>A list or array of integers, e.g. [4, 3, 0].</li>
#             <li>A slice object with ints, e.g. 1:7.</li>
#         </ul>
#     </li>
# </ul>

# In[62]:


#Return Fuel_Price to IsHoliday columns of 0-10th rows
#Note how LOC can reference columns by their names

features_df.loc[0 : 10 , "Fuel_Price" : "IsHoliday"]


# In[63]:


features_df.loc[[100, 105]]


# In[65]:


#Retrieve the CPI and customerCost of rows 500 to 505

features_df.loc[500 : 505 , ['CPI', 'CustomerCost']]


# In[66]:


#Retrieve a couple rows from their ROW index values

features_df.iloc[0 , 1]


# In[67]:


#We may also provide specific row/column values to access specific values

features_df.iloc[[0, 2] , [1, 3]]


# In[ ]:


#Multiple rows and specific columns


# In[ ]:


#Access rows 1 to 3 for Store column to Fuel_Price


# <h1>Formatting Data</h1>
# 
# <ul>
#     <li>To access and format the string values of a DataFrame, we can access methods within the "str" module of the DataFrame </li>
#     <li>We may also format float values using options.display.float_format() in Pandas</li>
# </ul>

# In[68]:


#By accessing .str, we gain access to all the string methods we covered in Python 1!

features_df["Temp"] = features_df["Temp"].str.upper()


# In[69]:



features_df.head()


# In[70]:


#Format float 

features_df.round(2).head()


# In[71]:


features_df["customerCost"].round(1).head()


# <h1>Conditional Indexing</h1>
# 
# <ul>
#     <li>Conditional Operators (>, ==, >=) can be used to return rows based on their values </li>
#     <li>Bitwise Operators (|, &) can be used to combine conditonal statements</li>
# </ul>

# In[72]:



features_df.head()


# In[75]:


#Return rows with CPI lower than 130

CPI_filt = features_df["CPI"] < 130

low_CPI = features_df[CPI_filt]
low_CPI.head()


# In[78]:


#Return rows with customerCost larger than 320.2 AND unemployment larger than 8

filt1 = features_df["customerCost"] > 320.2
filt2 = features_df["Unemployment"] > 8.00

q1 = features_df[filt1 & filt2]
q1.head()


# In[79]:


#Return rows with temp larger than 40 OR Store number equal to 4

filt1 = features_df["Temp"] == "COLD"
filt2 = features_df["Store"] == 4

features_df[filt1 | filt2].head()


# In[ ]:


##CLASS EXERCISE 
# find the rows with Fuel_Price larger than 3.00 AND IsHoliday is True


# In[ ]:





# In[ ]:


# find the rows with CPI < 200  OR Unemployment < 5


# In[80]:



features_df.head()


# In[82]:


#Export the current version of our DataFrame to a .csv file

features_df.to_csv("features_final.csv", index = False)

#to_excel also an option to export to Excel Spreadsheet

features_df.to_excel("features_final.xlsx", index = False)


# In[ ]:




