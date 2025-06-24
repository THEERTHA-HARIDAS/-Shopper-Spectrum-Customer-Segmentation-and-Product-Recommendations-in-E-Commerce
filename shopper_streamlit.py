import pickle 
import numpy as np
import streamlit as st

# Load the scaler
with open(r"C:\Users\PC1\DATA SCIENCE\PROJECTS\SHOPPER SPECTRUM PROJECT\scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load the KMeans model
with open(r"C:\Users\PC1\DATA SCIENCE\PROJECTS\SHOPPER SPECTRUM PROJECT\kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open(r"C:\Users\PC1\DATA SCIENCE\PROJECTS\SHOPPER SPECTRUM PROJECT\similarity_matrix.pkl", 'rb') as f:
    similarity_matrix = pickle.load(f)

def recommend_products(product_name, top_n=5):
    if product_name not in similarity_matrix.columns:
        return f" Product '{product_name}' not found in dataset."

    similar_scores = similarity_matrix[product_name].drop(product_name)
    top_similar = similar_scores.sort_values(ascending=False).head(top_n)

    return top_similar


# Define cluster labels 
cluster_labels = {
    0: "High-Value",
    1: "At-Risk",
    2: "Regular",
    3: "Occasional"
}

st.title("🛍️ Shopper Spectrum - Customer Segmentation &  Product Recommendations")

# Sidebar buttons
clustering_btn = st.sidebar.button("Customer Segmentation")
recommendation_btn = st.sidebar.button("Product Recommendation")

if "show_section" not in st.session_state:
    st.session_state.show_section = None

if clustering_btn:
    st.session_state.show_section = "clustering"
if recommendation_btn:
    st.session_state.show_section = "recommendation"

if st.session_state.show_section == "clustering":
    st.header("Customer Segmentation Input")

    recency = st.number_input("Recency (days)", min_value=0)
    frequency = st.number_input("Frequency (purchases)", min_value=0)
    monetary_input = st.text_input("Monetary (total spend)", value="0")
    try:
        monetary = float(monetary_input)
        if monetary < 0:
            st.error("Please enter a non-negative value for Monetary.")
            monetary = None
    except ValueError:
        st.error("Please enter a valid number for Monetary.")
        monetary = None

    if st.button("Predict Cluster"):
        try:
            input_data = np.array([[recency, frequency, monetary]])
            scaled_input = scaler.transform(input_data)
            cluster = kmeans.predict(scaled_input)[0]
            segment = cluster_labels.get(cluster, "Unknown")
            st.success(f"🎯 Segment: **{segment}** (Cluster {cluster})")
        except Exception as e:
            st.error(f"⚠️ Prediction failed: {e}")

#  Product Recommendation 
elif st.session_state.show_section == "recommendation":
    st.header("🎯 Product Recommendation")

    product_name = st.text_input("Enter a product name (e.g., 'WHITE HANGING HEART T-LIGHT HOLDER')")

    if st.button("🔎 Get Recommendations"):
        # You need to have similarity_matrix defined somewhere above this line!
        if product_name in similarity_matrix.columns:
            similar_items = (
                similarity_matrix[product_name]
                .drop(product_name)
                .sort_values(ascending=False)
                .head(5)
            )
            st.success("Top 5 similar products:")
            for i, (desc, score) in enumerate(similar_items.items(), start=1):
                st.markdown(f"**{i}. {desc}**  — Similarity Score: `{score:.2f}`")
        else:
            st.error("❌ Product not found. Please try a different name.")

else:
    st.write("Please select a module from the sidebar.")

