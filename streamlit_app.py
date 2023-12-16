import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Exploratory Data Analysis", layout="centered")

# Title
st.markdown("<h1 style='text-align:center; color:green;'>Supermarket Sales Analysis</h1>", unsafe_allow_html=True)
st.image("super-market.jpg", use_column_width=True)
df2 = pd.read_csv("super-market.csv")

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
    st.write("Description of the Dataset :", df2.describe())

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
                        options=["Pie Plot", "Bar Chart", "Line Plot", "Count Plot"])
if data_col == None:
    st.write("Please select any Chart Type...")
if data_col == "Pie Plot":
    select_bar_one = st.checkbox(label="The percentage of different types of products in Supermarket")
    if select_bar_one:
        fig, ax = plt.subplots()
        labels = df2['Product line'].value_counts().index
        colors = sns.color_palette(palette='Accent')
        ax = plt.pie(x=df2['Product line'].value_counts().values, labels=labels, colors=colors, autopct="%1.1f%%")
        plt.title('The percentage of different types of products in Supermarket')
        st.pyplot(fig)


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


elif data_col == "Line Plot":
    select_line_one = st.checkbox(label="The price per item of each product line")
    if select_line_one:
        fig, ax = plt.subplots()
        ax = sns.lineplot(x=df2['Product line'], y=df2['Unit price'], data=df2)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title('The price per item of each product line')
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

else:
    select_count_one = st.checkbox(label="Count of Different Types of Payment Methods used by Different Genders")
    if select_count_one:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['Payment'], data=df2, hue=df2['Gender'])
        plt.xlabel('Payment')
        plt.title('Count of Different Types of Payment Methods used by Different Genders')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_count_two = st.checkbox(label="Count of Different Gender Visitors from Different Cities")
    if select_count_two:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'], data=df2, order=df2['City'].value_counts().index, hue=df2['Gender'])
        plt.xlabel('City')
        plt.title('Count of Different Gender Visitors from Different Cities')
        plt.legend(title='Gender', loc='upper right')
        st.pyplot(fig)
    select_count_three = st.checkbox(label="Different Payment Methods Used by Different Cities")
    if select_count_three:
        fig, ax = plt.subplots()
        ax = sns.countplot(x=df2['City'], data=df2, hue=df2['Payment'])
        plt.legend(title='Payment Method', loc='upper right')
        plt.title('Different Payment Methods Used by Different Cities')
        st.pyplot(fig)

st.markdown("<h3 style='text-align:center; color:green;'>Thanks for Visiting!;)</h3>", unsafe_allow_html=True)
