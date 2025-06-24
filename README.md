# -Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce
This project, Shopper Spectrum, leverages transactional data from an online retail platform to segment customers based on their purchasing behavior and deliver personalized product recommendations.


Project Overview
In the dynamic and highly competitive e-commerce industry, understanding customer behavior is crucial for driving growth and enhancing customer experience. This project, Shopper Spectrum, leverages transactional data from an online retail platform to segment customers based on their purchasing behavior and deliver personalized product recommendations. Using unsupervised machine learning techniques and collaborative filtering, the project provides actionable insights to support targeted marketing, customer retention, and inventory management.


Features
1. Customer Segmentation
Segments customers into meaningful groups (High-Value, Regular, Occasional, At-Risk) using clustering algorithms like KMeans.
Uses RFM metrics as input features to identify purchasing behavior.
Enables targeted marketing strategies and customer retention programs.

2. Product Recommendation
Provides top 5 similar product recommendations based on item-item collaborative filtering.
Calculates product similarity using cosine similarity on purchase history data.
Enhances user shopping experience by offering relevant product suggestions.

3. Streamlit Web Application
User-friendly interface for inputting customer RFM values or product names.
Interactive buttons to toggle between segmentation and recommendation modules.
Real-time prediction and recommendation display.

Dataset
The project uses a public e-commerce transactional dataset containing:
InvoiceNo: Transaction number,
StockCode: Unique product/item code,
Description: Product name,
Quantity: Number of items purchased,
InvoiceDate: Date and time of purchase,
UnitPrice: Price per item,
CustomerID: Unique customer identifier,
Country: Customer location

Usage
Customer Segmentation Module
Input Recency (days since last purchase), Frequency (number of purchases), and Monetary (total spend).

Click Predict Cluster to get the customer segment label.

Product Recommendation Module
Enter a product name in the text box.

Click Get Recommendations to view the top 5 similar products based on purchase history.

Methodology
Data Preprocessing
--Clean data by removing missing CustomerIDs and cancelled orders.
--Filter out negative or zero quantities and prices.

RFM Feature Engineering
--Calculate Recency, Frequency, and Monetary values per customer.

Scale features before clustering.

Clustering
--Apply KMeans clustering for customer segmentation.
--Evaluate cluster quality using silhouette scores and elbow method.
--Label clusters for business interpretation.

Recommendation System
--Create CustomerID-Product purchase matrix.
--Compute cosine similarity between products.
--Recommend top 5 similar products for a given product input.

Technologies Used
Python (Pandas, NumPy, Scikit-learn)

Collaborative Filtering, KMeans Clustering

Streamlit for web app interface

Data Visualization (Matplotlib, Seaborn,Plotly)



