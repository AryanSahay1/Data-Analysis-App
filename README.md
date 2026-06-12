# Data-Analysis-App
# 📊 Data Analysis Application

An interactive **Exploratory Data Analysis (EDA)** dashboard built with **Streamlit**, enabling users to upload datasets and generate insightful visualizations without writing code.

---

## 🚀 Project Overview

The Data Analysis Application is a user-friendly web application designed to simplify data exploration and visualization. By uploading a CSV dataset, users can instantly perform univariate, bivariate, and multivariate analyses through interactive graphical representations.

The project is intended for students, researchers, data analysts, and anyone interested in understanding datasets quickly and efficiently.

---

## ✨ Key Features

### 📁 Dataset Upload

* Upload CSV datasets directly through the web interface.
* Automatic detection of numerical and categorical variables.
* Instant dataset processing for analysis.

### 📊 Univariate Analysis

Analyze individual variables to understand their distributions and characteristics.

Available visualizations:

* Histogram with KDE (Kernel Density Estimation)
* Count Plot
* Pie Chart (Top Categories)
* Box Plot

### 📈 Bivariate Analysis

Examine relationships between two variables.

Available visualizations:

* Line Plot
* Scatter Plot
* Bar Chart
* Comparative Box Plot

### 🔥 Multivariate Analysis

Explore relationships among multiple variables simultaneously.

Available visualizations:

* Pair Plot
* Correlation Heatmap

### 🎨 Interactive Interface

* Easy-to-use sidebar navigation
* Dynamic column selection
* Real-time visualization generation
* Clean and intuitive user experience

---

## 🛠️ Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core Programming Language      |
| Streamlit  | Web Application Framework      |
| Pandas     | Data Manipulation and Analysis |
| NumPy      | Numerical Computing            |
| Matplotlib | Data Visualization             |
| Seaborn    | Statistical Visualization      |
| Plotly     | Interactive Charts             |

---

## 📂 Project Structure

```text
.
├── youtube.py
├── README.md
└── requirements.txt
```

### File Description

#### youtube.py

Main Streamlit application containing:

* Dataset upload functionality
* Navigation system
* Univariate analysis module
* Bivariate analysis module
* Multivariate analysis module
* Visualization generation logic

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/data-analysis-application.git
cd data-analysis-application
```

### Install Required Dependencies

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly
```

Alternatively, install from requirements.txt:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit server using:

```bash
streamlit run youtube.py
```

After execution, open your browser and navigate to:

```text
http://localhost:8501
```

---

## 📊 How to Use

### Step 1: Launch the Application

Run the Streamlit script.

### Step 2: Upload a Dataset

Upload a CSV file through the file uploader.

### Step 3: Choose an Analysis Type

Available options:

* Home
* Univariate Analysis
* Bivariate Analysis
* Multivariate Analysis

### Step 4: Select Variables

Choose the desired columns from the dropdown menus.

### Step 5: Generate Insights

Visualizations are automatically generated based on the selected variables.

---

## 📈 Supported Visualizations

### Univariate Analysis

* Histogram
* Count Plot
* Pie Chart
* Box Plot

### Bivariate Analysis

* Line Plot
* Scatter Plot
* Bar Chart
* Box Plot

### Multivariate Analysis

* Pair Plot
* Correlation Heatmap

---

## 🎯 Applications

This project can be used for:

* Exploratory Data Analysis (EDA)
* Academic Research
* Business Analytics
* Data Science Learning
* Statistical Exploration
* Dataset Validation
* Data Visualization Projects

---

## 🔮 Future Improvements

Potential enhancements include:

* Interactive Plotly Dashboards
* Missing Value Analysis
* Data Cleaning Utilities
* Statistical Summary Reports
* Machine Learning Integration
* Automated Insight Generation
* Export Reports as PDF
* Time Series Analysis
* Feature Engineering Tools

---

## 👨‍💻 Author

### Aryan Sahay

Aspiring Quantitative Researcher, Data Science Enthusiast, and Finance Professional with interests in:

* Data Science
* Machine Learning
* Quantitative Finance
* Algorithmic Trading
* Financial Analytics
* Hedge Fund Research

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## ⭐ Support the Project

If you found this project useful:

* Give the repository a Star ⭐
* Share it with others
* Suggest new features
* Report issues

---

## 📄 License

This project is released under the MIT License.

Feel free to use, modify, and distribute it for educational and commercial purposes.

---

### 📊 Transforming Raw Data into Actionable Insights

Built with Python and Streamlit by **Aryan Sahay**.
