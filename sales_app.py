import streamlit as st
import pandas as pd

# Title and subheader
st.title("📊 Sales Summary Dashboard")
st.subheader("A simple interactive app to view product sales by category")

# Hardcoded dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [1200, 800, 600, 150, 400]
}
df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filters")
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select Category", options=categories)

# Filtered DataFrame
filtered_df = df[df["Category"] == selected_category]

# Main content area
st.dataframe(filtered_df)

# Line chart of Sales values for the selected category
st.line_chart(filtered_df.set_index("Product")["Sales"])