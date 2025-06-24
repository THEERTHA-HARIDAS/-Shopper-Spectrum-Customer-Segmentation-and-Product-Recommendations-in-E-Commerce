# -Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce
This project, Shopper Spectrum, leverages transactional data from an online retail platform to segment customers based on their purchasing behavior and deliver personalized product recommendations.


Project Overview
In the dynamic and highly competitive e-commerce industry, understanding customer behavior is crucial for driving growth and enhancing customer experience. This project, Shopper Spectrum, leverages transactional data from an online retail platform to segment customers based on their purchasing behavior and deliver personalized product recommendations. Using unsupervised machine learning techniques and collaborative filtering, the project provides actionable insights to support targeted marketing, customer retention, and inventory management.


Objectives
--Customer Segmentation: Identify distinct customer groups based on Recency, Frequency, and Monetary (RFM) analysis to tailor marketing strategies and improve customer retention.
--Product Recommendations: Develop an item-based collaborative filtering system to recommend relevant products to users based on purchase history similarity.
--Business Impact: Enable data-driven decisions for targeted promotions, personalized shopping experiences, and optimized inventory management.

Dataset
The project uses a public e-commerce transaction dataset spanning 2022–2023, including key fields such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country. The data captures detailed customer purchases, allowing for deep behavioral analysis.

Data Preprocessing
--Removed entries with missing CustomerID to ensure accuracy.
--Excluded cancelled invoices to focus on completed transactions.
--Filtered out transactions with negative or zero quantities and prices to maintain data integrity.

Exploratory Data Analysis (EDA)
--Analyzed transaction volume and purchase trends across countries.
--Identified top-selling products and their popularity distribution.
--Visualized monetary values and RFM score distributions to understand customer behavior patterns.
--Used elbow method and silhouette scores to guide cluster number selection.

Customer Segmentation Methodology
--Engineered RFM features:
    Recency: Days since the last purchase.
    Frequency: Number of purchases.
    Monetary: Total spend.
--Scaled RFM features for uniformity.
--Applied clustering algorithms (KMeans, DBSCAN, Hierarchical) and evaluated performance to select the optimal model.
--Labeled clusters based on average RFM values:
    High-Value: Frequent, recent, and high spenders.
    Regular: Steady purchasers with medium spending.
    Occasional: Rare buyers with low spend.
    At-Risk: Customers who haven’t purchased recently.
--Visualized clusters through 2D/3D plots for interpretability.

Recommendation System Approach
--Built an item-based collaborative filtering model using customer purchase history.
--Calculated cosine similarity between products to identify relationships.
--Developed a recommendation function to return the top 5 similar products given any product input.

Streamlit Application Features
--Product Recommendation Module: User inputs a product name to receive top 5 similar product recommendations displayed in a user-friendly layout.
--Customer Segmentation Module: User inputs RFM values and receives a predicted customer segment label instantly.
Interactive UI elements enable seamless, real-time predictions to support marketing and sales decisions.

Skills and Techniques Applied
--Data exploration and cleaning with Pandas and NumPy
--Feature engineering and scaling using Scikit-learn’s StandardScaler
--Clustering and unsupervised machine learning with KMeans, DBSCAN, and hierarchical algorithms
--Collaborative filtering and similarity computations
--Model evaluation with silhouette scores and elbow method
--Data visualization (plots, heatmaps) to communicate findings
--Streamlit for building interactive, real-time web applications

Business Use Cases
--Targeted marketing campaigns tailored to customer segments
--Personalized product recommendations enhancing shopping experience
--Identifying at-risk customers for retention efforts
--Dynamic pricing and stock management based on customer demand patterns

This project offers a comprehensive data science pipeline from raw data preprocessing to deployment of a real-time web app, showcasing a practical solution for customer insight and recommendation challenges in e-commerce.
