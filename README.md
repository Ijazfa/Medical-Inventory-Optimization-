# Medical-Inventory-Optimization-

Project Overview
Dataset: The dataset, loaded from "Medical Inventory Optimization Dataset.csv", likely contains information related to medical inventory management, potentially including details such as drug formulations, quantities, costs, and sales types.
Analysis Steps and Visualizations
Data Loading and Initial Exploration:

You used pandas to load the dataset and checked its structure using df.head(), df.shape, df.info(), and df.describe() to understand its dimensions, column types, and summary statistics.
Identified missing values (df.isnull().sum()) and filled them using forward filling (df.fillna(method='ffill')) to ensure data completeness.
Data Visualization:

Histograms (df.hist()): Used to visualize the distribution of numerical variables like quantities, costs, etc., across the dataset.
Boxplots (sns.boxplot()): Plotted to identify outliers and the distribution of data points across different variables.
Pairplot (sns.pairplot()): Provided a matrix of scatterplots for numerical variables, offering a quick overview of potential relationships and distributions.
Correlation Heatmap (sns.heatmap()): Visualized correlations between numerical variables, which helps in understanding which variables might be influencing each other.
Further Insights:

Distribution Plots (sns.histplot()): Specifically visualized the distribution of Final_Cost, likely indicating how costs are distributed across the dataset.
Categorical Analysis (sns.boxplot(), sns.countplot()): Analyzed categorical variables like Formulation and Typeofsales to understand their distributions and potential impacts on inventory management.
Project Goals and Next Steps
From the visualizations and analysis conducted, potential project goals or next steps could include:

Inventory Optimization: Identify trends in costs, quantities, and formulations to optimize inventory management strategies.
Sales Analysis: Understand which types of sales (Typeofsales) are most frequent or profitable.
Formulation Impact: Investigate how different drug formulations (Formulation) affect quantities sold or costs incurred.
Outlier Detection and Handling: Develop strategies to handle outliers identified in the data.
Predictive Modeling: Potentially build predictive models to forecast demand, costs, or optimal inventory levels based on historical data patterns.
