import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the correct path
df = pd.read_csv("C:/Users/marya/OneDrive/Desktop/Skill Craft/Task 01/India_Population_Distribution_2022.csv")

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Age Group"], df["Population (Millions)"], color=["gold", "dodgerblue", "deeppink"])
plt.title("India's Population Distribution by Age in 2022")
plt.xlabel("Age Group")
plt.ylabel("Population (in Millions)")

# Add percentage labels on top of each bar
for i, value in enumerate(df["Population (Millions)"]):
    plt.text(i, value + 1, f"{df['Percentage'][i]}%", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
