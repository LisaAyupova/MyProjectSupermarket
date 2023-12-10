import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Exploratory Data Analysis", layout="centered")

# Title and Sub-Title
st.markdown(
    "<h1 style='text-align:center; color:green;'>Exploratory Data Analysis</h1></div>",
    unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:black;'>Supermarket Sales Analysis</h3>", unsafe_allow_html=True)
st.image("super-market.jpg", use_column_width=True)
df1 = pd.read_csv("super-market.csv")


df2 = df1.drop("Invoice ID", axis=1)

# Problem
st.header("Problem Statement")
st.write(
    "- By analyzing sales data, we can learn about customer preferences, product features, and general patterns in the operation of supermarkets..")


# Resources
st.header("Links to the Resources")
st.markdown("- [Link to the Dataset](https://github.com/LisaAyupova/MyProjectSupermarket/blob/main/super-market.csv)")
st.markdown("- [Link to my GitHub](https://github.com/LisaAyupova/MyProjectSupermarket)")


params = st.selectbox(label="Select any Parameter", options=["Shape", "Columns", "Description"])

if params == None:
    st.write("Please select an Option...")
elif params == "Shape":
    st.write("Shape of the Dataset :", df2.shape)
elif params == "Columns":
    st.write("Columns in the Dataset :", df2.columns)
else:
    st.write("Description of the Dataset :", df1.describe())


# Null Values
st.header("Null Values and DataType of Columns")
col_dtype_nulls = st.selectbox(label="Select any Column", options=df2.columns)
if col_dtype_nulls == None:
    st.write("Please select a Column...")
elif col_dtype_nulls == "Invoice ID":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Branch":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "City":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Customer type":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Gender":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Product line":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Unit price":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Quantity":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Tax 5%":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Total":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Date":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Time":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "Payment":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "cogs":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "gross margin percentage":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
elif col_dtype_nulls == "gross income":
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())
else:
    st.write(f"DataType of **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].dtype)
    st.write(f"Null Values in **{col_dtype_nulls}** Column is", df2[col_dtype_nulls].isna().sum())


st.header("Examine Categorical Columns")
cat_col = st.selectbox(label="Select any Categorical Column",
                       options=["Branch", "City", "Customer type", "Gender", "Payment", "Product line", "Quantity"])
if cat_col == None:
    st.write("Please select a Column...")
elif cat_col == "Branch":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
elif cat_col == "City":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
elif cat_col == "Customer type":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
elif cat_col == "Gender":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
elif cat_col == "Payment":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
elif cat_col == "Product line":
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())
else:
    st.write(f"Count of every unique value in **{cat_col}** column")
    st.dataframe(df2[cat_col].value_counts())



# Data Visualization
st.header("Data Visualization")
data_col = st.selectbox(label="Select any Chart Type",
                        options=["Distribution Plot", "Bar Chart", "Line Plot", "Count Plot"])
if data_col == None:
    st.write("Please select any Chart Type...")

elif data_col == "Bar Chart":
    select_bar_one = st.checkbox(label="Gross Income from Different Product Lines in Different Cities")
    if select_bar_one:
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df2['Product line'], y=df2['gross income'], data=df2, hue=df2['City'])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.xlabel('Product Line')
        plt.title('Gross Income from Different Product Lines in Different Cities')
        plt.legend(title='Cities', loc='upper right')
        st.pyplot(fig)
    select_bar_two = st.checkbox(label="Taxes on Different Product Lines")
    if select_bar_two:
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df2['Product line'], data=df2, y=df2['Tax 5%'])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title('Taxes on Different Product Lines')
        st.pyplot(fig)
    select_bar_three = st.checkbox(label="Total Gross Income from Different Branches by Different Genders")
    if select_bar_three:
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df2['Branch'], y=df2['gross income'], data=df2, hue=df2['Gender'])
        plt.title('Total Gross Income from Different Branches by Different Genders')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)


elif data_col == "Distribution Plot":
    select_dist_one = st.checkbox(label="Subplots of Distribution of Unit Price, Ratings and Gross Income")
    if select_dist_one:
        fig, ax = plt.subplots(1, 3, figsize=(12, 5))
        sns.histplot(data=df2['Rating'], kde=True, ax=ax[0])
        ax[0].set_title('Distribution of Rating of Products')
        sns.histplot(data=df2['Unit price'], kde=True, ax=ax[1])
        ax[1].set_title('Distribution of Unit Price of Products')
        sns.histplot(data=df2['gross income'], kde=True, ax=ax[2])
        ax[2].set_title('Distribution of Gross Income from Sales')
        fig.tight_layout()
        st.pyplot(fig)


elif data_col == "Line Plot":
    select_line_one = st.checkbox(label="Per Unit Price of Each Product Lines")
    if select_line_one:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Unit price'], data=df2)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.xlabel('Product Line')
        plt.title('Per Unit Price of Each Product Lines')
        st.pyplot(fig)
    select_line_two = st.checkbox(label="Quantity of Products Sold from Each Product Line")
    if select_line_two:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Quantity'], data=df2)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title('Quantity of Products Sold from Each Product Line')
        st.pyplot(fig)
    select_line_three = st.checkbox(label="Total Amount Spend on Different Product Lines by Different Genders")
    if select_line_three:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Total'], data=df2, hue=df2['Gender'], err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title('Total Amount Spend on Different Product Lines by Different Genders')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_line_four = st.checkbox(label="Rating of Different Product Lines by Different Genders")
    if select_line_four:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Rating'], data=df2, hue=df2['Gender'], err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.xlabel('Product Line')
        plt.title('Rating of Different Product Lines by Different Genders')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_line_five = st.checkbox(label="Total Sale on Each Day for All Months")
    if select_line_five:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Day'], y=df2['Total'], hue=df2['Month'], err_style=None, palette='crest')
        plt.legend(title='Month', loc='upper right')
        plt.title('Total Sale on Each Day for All Months')
        st.pyplot(fig)
    select_line_six = st.checkbox(label="Number of Products bought by Different Genders from Different Product Lines")
    if select_line_six:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Quantity'], data=df2, hue=df2['Gender'], err_style=None)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title('Number of Products bought by Different Genders from Different Product Lines')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)

else:
    select_count_one = st.checkbox(label="Count of Different Types of Customers from Different Cities")
    if select_count_one:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Customer type'], data=df2, hue=df2['City'])
        plt.xlabel('Customer Type')
        plt.title('Count of Different Types of Customers from Different Cities')
        plt.legend(title='City', loc='upper right')
        st.pyplot(fig)
    select_count_two = st.checkbox(label="Count of Different Types of Products in Super Market")
    if select_count_two:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Product line'], data=df2, order=df2['Product line'].value_counts().index)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.xlabel('Product Line')
        plt.title('Count of Different Types of Products in Super Market')
        st.pyplot(fig)
    select_count_three = st.checkbox(label="Count of Different Gender Visitors at Different Branches")
    if select_count_three:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Gender'], data=df2, hue=df2['Branch'])
        plt.xlabel('Gender')
        plt.title('Count of Different Gender Visitors at Different Branches')
        plt.legend(title='Branch', loc='upper right')
        st.pyplot(fig)
    select_count_four = st.checkbox(label="Count of Different Types of Payment Methods used by Different Genders")
    if select_count_four:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Payment'], data=df2, hue=df2['Gender'])
        plt.xlabel('Payment')
        plt.title('Count of Different Types of Payment Methods used by Different Genders')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_count_five = st.checkbox(label="Count of Different Gender Visitors from Different Cities")
    if select_count_five:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'], data=df2, order=df2['City'].value_counts().index, hue=df2['Gender'])
        plt.xlabel('City')
        plt.title('Count of Different Gender Visitors from Different Cities')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_count_six = st.checkbox(label="Different Payment Methods Used by Different Cities")
    if select_count_six:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'], data=df2, hue=df2['Payment'])
        plt.legend(title='Payment Method', loc='upper right')
        plt.title('Different Payment Methods Used by Different Cities')
        st.pyplot(fig)


st.markdown("<h3 style='text-align:center; color:green;'>Thanks for Visiting!;)</h3>", unsafe_allow_html=True)