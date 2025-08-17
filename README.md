# 📊 Skill Craft – Data Science Tasks

This repository contains three data science & machine learning tasks, each focusing on different datasets, analysis, and visualization methods.  

---

## 📂 Tasks Overview

### **Task 01 – India Population Distribution (2022)**
- **Dataset:** `India_Population_Distribution_2022.csv`  
- **Script:** `program1.py`  
- **Description:**  
  - Visualizes India’s population distribution across different age groups.  
  - Creates a bar chart with percentage labels.  
  - Highlights how population is distributed among **0–20 years**, **21–64 years**, and **65+ years**.  

#### 🔹 Output  
<img width="800" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/9c1372b5-4e04-4344-82ce-407e6908ea2f" />

---

### **Task 02 – Titanic Dataset Analysis (EDA)**
- **Dataset:** `train.csv` (Titanic dataset)  
- **Script:** `Program1.py`  
- **Description:**  
  - Performs **data cleaning**: fills missing values, encodes categorical variables, drops unused columns.  
  - Exploratory Data Analysis with **Seaborn & Matplotlib**.  
  - Visualizations include:  
    - Survival count by **Sex, Pclass, Embarked**  
    - **Correlation heatmap** of dataset features  
    - **Age & Fare distribution** with survival overlay  

#### 🔹 Outputs  

**1. Survival Counts by Sex, Pclass, and Embarked:**  
<img width="1280" height="612" alt="Figure_1" src="https://github.com/user-attachments/assets/be8a052b-cf46-4a4f-b7b5-99a07dcf7df7" />

**2. Correlation Heatmap:**  
<img width="1280" height="612" alt="Figure_2" src="https://github.com/user-attachments/assets/2bb49f63-e574-4104-a3d2-d278786c6091" />
 

**3. Age & Fare Distribution by Survival:**  
<img width="1280" height="612" alt="Figure_3" src="https://github.com/user-attachments/assets/93916947-8331-4653-b7ce-585bb6f9a548" />
  

---

### **Task 03 – Bank Marketing Decision Tree**
- **Dataset:** `bank-additional-full.csv`  
- **Script:** `program1.py`  
- **Description:**  
  - Preprocesses dataset by **label encoding** categorical features.  
  - Splits dataset into **training and testing sets**.  
  - Trains a **Decision Tree Classifier** using `entropy` criterion and `max_depth=5`.  
  - Evaluates the model with:  
    - Accuracy Score  
    - Classification Report  
    - Confusion Matrix  
  - Visualizes the **Decision Tree** structure.  

#### 🔹 Output  

**Decision Tree Visualization:**  
<img width="1280" height="612" alt="Figure_1" src="https://github.com/user-attachments/assets/1e082b66-d0d2-4293-aa25-32e5199dabf8" />


---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/skill-craft-tasks.git
   cd skill-craft-tasks



### 1️⃣ Install Dependencies
Make sure you have Python installed (>=3.8). Then install the required libraries:

pip install -r requirements.txt

### requirements.txt should include:
pandas
numpy
matplotlib
seaborn
scikit-learn

### 2️⃣ Run Any Task

### Task 01 – India Population Distribution
python program1.py  

### Task 02 – Titanic Dataset EDA
python Program1.py  

### Task 03 – Bank Marketing Decision Tree
python program1.py


### MIT License

Copyright (c) 2025 Akshay Maryala
