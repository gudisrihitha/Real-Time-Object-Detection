import streamlit as st
import pandas as pd
import mysql.connector

# Page configuration
st.set_page_config(
    page_title="Object Detection Dashboard",
    page_icon="📷",
    layout="wide"
)

# Dashboard title
st.title("📷 Real-Time Object Detection Dashboard")
st.write("Monitor objects detected by the YOLO model.")

# Refresh button
if st.button("🔄 Refresh Detection Data"):
    st.rerun()

st.divider()

try:
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sravanthi123",
        database="object_detection"
    )

    # Retrieve detection records
    query = """
        SELECT id, object_name, confidence, detected_at
        FROM detections
        ORDER BY detected_at DESC
    """

    df = pd.read_sql(query, connection)
    connection.close()

    # Summary section
    st.subheader("Detection Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Detections", len(df))

    with col2:
        if not df.empty:
            unique_objects = df["object_name"].nunique()
        else:
            unique_objects = 0

        st.metric("Unique Object Types", unique_objects)

    with col3:
        if not df.empty:
            average_confidence = df["confidence"].mean() * 100
        else:
            average_confidence = 0.0

        st.metric("Average Confidence", f"{average_confidence:.2f}%")

    st.divider()

    # Detection records
    st.subheader("Detection Records")

    if not df.empty:

        # Object filter
        object_types = [
            "All"
        ] + sorted(df["object_name"].dropna().unique().tolist())

        selected_object = st.selectbox(
            "Filter by object",
            object_types
        )

        if selected_object == "All":
            filtered_df = df.copy()
        else:
            filtered_df = df[
                df["object_name"] == selected_object
            ]

        # Display table
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

        # Object count chart
        st.subheader("Objects Detected")

        object_counts = filtered_df["object_name"].value_counts()
        st.bar_chart(object_counts)

        # Confidence chart
        st.subheader("Detection Confidence")

        confidence_chart = filtered_df[
            ["object_name", "confidence"]
        ].copy()

        confidence_chart["confidence"] = (
            confidence_chart["confidence"] * 100
        )

        st.bar_chart(
            confidence_chart.set_index("object_name")
        )

    else:
        st.info(
            "No detections found. Run the webcam detection "
            "program to save records to MySQL."
        )

except mysql.connector.Error as error:
    st.error(f"MySQL database connection failed: {error}")

except Exception as error:
    st.error(f"An unexpected error occurred: {error}")