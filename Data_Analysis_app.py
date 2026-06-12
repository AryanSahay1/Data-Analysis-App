import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
sns.set_theme(style = 'whitegrid')
st.sidebar.title("navigation")
page =st.sidebar.radio(
    "pages:",
    ["Home","univariate analysis","bivariate analysis","multivariate analysis"]
)

if page == "Home":
    st.title("Welcome to the Data Analysis Application 🎉")
    st.write("""
        This application is designed for dynamic data visualization and analysis using your uploaded dataset. It supports:

        - **Univariate Analysis:** Single-variable exploration.
        - **Bivariate Analysis:** Explore relationships between two variables.
        - **Multivariate Analysis:** Advanced insights involving multiple variables.

        ### Features include:
        - Interactive visualizations.
        - Seamless data upload and processing.
        - Advanced plots with custom options.

        Navigate through the sidebar options to begin your journey! 📊
             """)
    
if page != "Home":
        st.title("Upload your dataset to get started")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv", key = "navigation")
        if uploaded_file:
            data =pd.read_csv(uploaded_file)
            st.sidebar.success("File uploaded successfully!")
            numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()
            categorical_columns = data.select_dtypes(include=["object", "category"]).columns.tolist()
            def display_plot(fig):
                 st.pyplot(fig)
        else:
            st.sidebar.info("Please upload a CSV file to start.")
            st.stop()
    
     
if page == "univariate analysis":
    st.title("Univariate Analysis")
    st.header("Explore Single-Variable Trends")
    st.write("Explore univariate plots with dynamic column selection.")
    fig, ax = plt.subplots(2,2, figsize=(22,13))

    #histogram
    hist_col = st.selectbox("Select a numeric column for histogram",numeric_columns, key = "histogram")
    sns.histplot(data[hist_col], kde=True, ax=ax[0,0])
    ax[0,0].set_title(f"Histogram of {hist_col}")
    ax[0, 0].tick_params(axis='x', labelsize=15, rotation=90)

    #countplot
    count_col = st.selectbox("Select a categorical column for countplot", categorical_columns, key = "countplot")
    sns.countplot(data=data, x=count_col, ax=ax[0, 1])
    ax[0, 1].set_title(f"Countplot of {count_col}", fontsize=30, color="red", weight="bold")
    ax[0, 1].tick_params(axis='x', labelsize=15, rotation=90)

    #pie chart
    pie_col = st.selectbox("Select a categorical column for pie chart", categorical_columns, key = "pie_chart")
    pie_col = st.selectbox("Select column for Pie Chart:", categorical_columns, key="pie", index=0)
    top_categories = data[pie_col].value_counts().sort_values(ascending=False).head(5)
    top_categories.plot.pie(autopct='%1.1f%%', ax=ax[1, 0], textprops={'fontsize': 30})
    ax[1, 0].set_title(f"Pie Chart of Top 5 Categories in {pie_col}", fontsize=30, color="red", weight="bold")

    #boxplot
    box_col = st.selectbox("Select a numeric column for boxplot", numeric_columns, key = "boxplot")
    sns.boxplot(data=data, y=box_col, ax=ax[1, 1])
    ax[1, 1].set_title(f"Boxplot of {box_col}", fontsize=30, color="red", weight="bold")
    ax[1, 1].tick_params(axis='x', labelsize=15, rotation=90)
    plt.tight_layout()
    display_plot(fig)

#bivariate analysis
elif page == "bivariate analysis":
     st.title("Bivariate Analysis", anchor=False)
     st.header("Explore Relationships Between Two Variables")
     st.write("Explore bivariate relationships with dynamic column selection.")
#line plot 1
     fig, axes = plt.subplots(2, 2, figsize=(22, 13))
     line_x1 = st.selectbox("X for Line Plot 1:", numeric_columns, key="line_x1", index=0)
     line_y1 = st.selectbox("Y for Line Plot 1:", numeric_columns, key="line_y1", index=0)
     sns.lineplot(data=data, x=line_x1, y=line_y1, ax=axes[0, 0])
     axes[0, 0].set_title(f"Line Plot of {line_x1} vs {line_y1}", fontsize=30, color="red", weight="bold")
     axes[0, 0].tick_params(axis='x', labelsize=15, rotation=90)
#scatter plot
     scatter_x = st.selectbox("X for Scatter Plot:", numeric_columns, key="scatter_x", index=0)
     scatter_y = st.selectbox("Y for Scatter Plot:", numeric_columns, key="scatter_y", index=0)
     sns.scatterplot(data=data, x=scatter_x, y=scatter_y, ax=axes[0, 1])
     axes[0, 1].set_title(f"Scatter Plot of {scatter_x} vs {scatter_y}", fontsize=30, color="red", weight="bold")
     axes[0, 1].tick_params(axis='x', labelsize=15, rotation=90)
#bar chart
     bar_x = st.selectbox("X for Bar Chart:", categorical_columns, key="bar_x", index=0)
     bar_y = st.selectbox("Y for Bar Chart:", numeric_columns, key="bar_y", index=0)
     sns.barplot(data=data, x=bar_x, y=bar_y, ax=axes[1, 0])
     axes[1, 0].set_title(f"Bar Chart of {bar_y} by {bar_x}", fontsize=30, color="red", weight="bold")
     axes[1, 0].tick_params(axis='x', labelsize=15, rotation=90)
#boxplot
     box_x = st.selectbox("X for Boxplot:", categorical_columns, key="box_x", index=0)
     box_y = st.selectbox("Y for Boxplot:", numeric_columns, key="box_y", index=0)
     sns.boxplot(data=data, x=box_x, y=box_y, ax=axes[1, 1])
     axes[1, 1].set_title(f"Boxplot of {box_y} by {box_x}", fontsize=30, color="red", weight="bold")
     axes[1, 1].tick_params(axis='x', labelsize=15, rotation=90)
     plt.tight_layout()
     display_plot(fig)

#multivariate analysis
elif page == "multivariate analysis":
     st.title("Multivariate Analysis", anchor=False)
     st.header("Explore Relationships Involving Multiple Variables")
     st.write("Explore multivariate relationships with dynamic column selection.")
     #pairplot
     st.subheader("Pairplot")
     if numeric_columns:
         pairplot_cols = st.multiselect("Select columns for Pairplot:", numeric_columns, default=numeric_columns[:min(3, len(numeric_columns))])
         if pairplot_cols:
            pairplot_fig = sns.pairplot(data[pairplot_cols])
            st.pyplot(pairplot_fig)
         else:
            st.warning("Please select at least one column for the Pairplot.")
     else:
        st.error("No numeric columns available for Pairplot.")
#heatmap
     st.subheader("Heatmap")
     if numeric_columns:
      fig, ax = plt.subplots(figsize=(40, 30))
      sns.heatmap(data[numeric_columns].corr(), annot=True, cmap="coolwarm", ax=ax, annot_kws={"size": 30})
      ax.set_title("Correlation Heatmap", fontsize=40, color="red", weight="bold")
      ax.tick_params(axis='x', labelsize=40)
      ax.tick_params(axis='y', labelsize=40)
      display_plot(fig)
     else :
         st.error("No numeric columns available for Heatmap.")











