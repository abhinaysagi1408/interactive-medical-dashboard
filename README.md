# 🏥 Interactive Medical Dashboard

An **interactive data visualization dashboard** built with **Streamlit**, **Pandas**, and **Plotly** to analyze and visualize medical diagnostic data, including heart rate, cardiac markers, and patient demographics.

---

## 👨‍⚕️ Author
**Name:** Abhinay Sagi  
**GitHub:** [abhinaysagi1408](https://github.com/abhinaysagi1408)

---

## 🚀 Project Overview

This dashboard enables healthcare professionals and data analysts to:
- Explore patient data through interactive filters (Age & Gender)
- Visualize cardiac health indicators such as **CK-MB** and **Troponin**
- Examine **trends**, **correlations**, and **summary metrics**
- Interactively view and sort patient data

---

## 🧰 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Python** | Main programming language |
| **Streamlit** | Web-based dashboard framework |
| **Plotly** | Interactive and dynamic data visualizations |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib / Seaborn** | (Used in preprocessing for static plots) |

---

## 📊 Datasets

1. **originaldataset.csv**  
   - Raw medical dataset before cleaning.

2. **cleaned_medical_data.csv**  
   - Cleaned dataset generated after filling missing values and performing basic preprocessing.  
   - Used by the Streamlit dashboard.

---

## 🧹 Data Cleaning (Preprocessing)

Data cleaning was performed using Python (`pandas`).  
Missing values in **Result**, **Blood sugar**, and **Diastolic blood pressure** were filled using **forward and backward fill**.

### Key Steps:
- Removed or filled missing values
- Verified data types
- Saved cleaned dataset as `cleaned_medical_data.csv`
- Generated plots:
  - Age distribution histogram
  - Gender count plot
  - Correlation heatmap

---

## 📈 Dashboard Features

- **Sidebar Filters:** Filter by Age range and Gender  
- **Summary Metrics:**  
  - Average Troponin  
  - Abnormal Diagnosis %  
- **Interactive Visualizations:**  
  - Age vs CK-MB / Troponin  
  - Heart rate trends by age group  
  - Correlation heatmap of vital signs  
- **Interactive Table:** Sorted and filtered patient data view  

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/interactive-medical-dashboard.git
cd interactive-medical-dashboard
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the app
streamlit run app.py
Then open your browser and go to:
http://localhost:8501
