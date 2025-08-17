# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/marya/OneDrive/Desktop/Skill Craft/Task 02/train.csv")  # replace with your file name if different

# -----------------------
# Step 1: Data Cleaning
# -----------------------

# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin, Ticket, PassengerId, and Name
df.drop(columns=['Cabin', 'Ticket', 'PassengerId', 'Name'], inplace=True)

# Convert 'Sex' to numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encode 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# -----------------------
# Step 2: EDA Visualizations
# -----------------------

# Plot survival count by Sex
plt.figure(figsize=(14, 4))

plt.subplot(1, 3, 1)
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Sex")
plt.xticks([0, 1], ['Male', 'Female'])

# Plot survival count by Pclass
plt.subplot(1, 3, 2)
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival Count by Pclass")

# Plot survival count by Embarked
plt.subplot(1, 3, 3)
df_plot = df.copy()
df_plot['Embarked'] = 'C'
df_plot.loc[df_plot['Embarked_Q'] == 1, 'Embarked'] = 'Q'
df_plot.loc[df_plot['Embarked_S'] == 1, 'Embarked'] = 'S'
sns.countplot(x='Embarked', hue='Survived', data=df_plot)
plt.title("Survival Count by Embarked")

plt.tight_layout()
plt.show()

# -----------------------
# Step 3: Correlation Heatmap
# -----------------------

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------
# Step 4: Age & Fare Distribution
# -----------------------

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True)
plt.title("Age Distribution by Survival")

plt.subplot(1, 2, 2)
sns.histplot(data=df, x='Fare', hue='Survived', bins=30, kde=True)
plt.title("Fare Distribution by Survival")

plt.tight_layout()
plt.show()
