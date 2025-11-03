import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# Set Streamlit theme for a more colorful appearance
st.set_page_config(page_title="Medical Dashboard", layout="wide")
st.markdown("""
    <style>
        .main {background-color: #f5f9ff;}
        .block-container {padding-top: 2rem;}
        .css-18e3th9 {background-color: #ffffff; border-radius: 10px; padding: 1rem;}
        h1, h2, h3, h4, h5, h6 {color: #003366;}
    </style>
""", unsafe_allow_html=True)

# Load cleaned data
df = pd.read_csv("cleaned_medical_data.csv")

# Ensure 'Result' is numeric
if df['Result'].dtype == 'object':
    df['Result'] = df['Result'].map({'Normal': 0, 'Abnormal': 1})

# ----- Sidebar Filters (Cascading Filters) -----
st.sidebar.title("Filter Age and Gender")
st.sidebar.markdown("Use the options below to customize the dashboard view.")
age_range = st.sidebar.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (30, 70))
gender_filter = st.sidebar.selectbox("Select Gender", options=['All', 'Male', 'Female'])

# Filter dataset
filtered_df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
if gender_filter != 'All':
    gender_code = 1 if gender_filter == 'Male' else 0
    filtered_df = filtered_df[filtered_df['Gender'] == gender_code]

# ----- Title -----
st.title("\U0001F3E5 Medical Diagnostic Dashboard")

# ----- Summary Metrics -----
st.subheader(" Summary Metrics")
col1, col2 = st.columns(2)
col1.metric("Average Troponin", f"{filtered_df['Troponin'].mean():.2f}")
abnormal_pct = (filtered_df['Result'].sum() / len(filtered_df)) * 100 if len(filtered_df) > 0 else 0
col2.metric("Abnormal Diagnoses", f"{abnormal_pct:.1f}%")

# ----- Connected Visualisations -----
st.markdown("### Connected Visualisations: Age vs Cardiac Markers")
x_feature = st.selectbox("Select Marker", ['CK-MB', 'Troponin'])
fig3 = px.scatter(filtered_df, x='Age', y=x_feature, color='Result',
                  title=f"Age vs {x_feature}", color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig3, use_container_width=True)

# ----- Dynamic Configuration Section -----
st.markdown("### Dynamic Configuration: Heart Rate Trend")
trend_metric = st.selectbox("Select Metric to Plot", ['Heart rate', 'CK-MB', 'Troponin'])
age_bins = pd.cut(filtered_df['Age'], bins=10)
trend_data = filtered_df.groupby(age_bins)[trend_metric].mean().reset_index()
trend_data['Age Bin'] = trend_data['Age'].astype(str)
fig5 = px.line(trend_data, x='Age Bin', y=trend_metric, title=f"{trend_metric} Trend by Age",
               markers=True, color_discrete_sequence=['#e76f51'])
st.plotly_chart(fig5, use_container_width=True)

# ----- Additional Visualisation -----
st.markdown("### Average Heart Rate by Age Group")
filtered_df['AgeGroup'] = pd.cut(filtered_df['Age'], bins=[20, 30, 40, 50, 60, 70, 80], right=False)
filtered_df['AgeGroup'] = filtered_df['AgeGroup'].astype(str)  # Convert for Plotly
heart_rate_grouped = filtered_df.groupby('AgeGroup', observed=True)['Heart rate'].mean().reset_index()

fig4 = px.bar(heart_rate_grouped, x='AgeGroup', y='Heart rate', title="Mean Heart Rate by Age Group")
fig4.update_traces(marker_color='#3b82f6')  # Solid blue color

st.plotly_chart(fig4, use_container_width=True)


# ----- Heatmap Visualisation -----
st.markdown("### Correlation Heatmap")
numeric_cols = ['Age', 'Heart rate', 'CK-MB', 'Troponin']
corr_matrix = filtered_df[numeric_cols].corr()

fig8 = px.imshow(
    corr_matrix,
    text_auto=True,
    color_continuous_scale='RdBu',  # Red to Blue gradient
    title="Correlation Heatmap of Vital Metrics",
    width=900,
    height=700
)

st.plotly_chart(fig8, use_container_width=True)


# ----- Interactive Data Table -----
st.markdown("### Interactive Data Table")
st.dataframe(filtered_df.sort_values(by='Age'), use_container_width=True)
