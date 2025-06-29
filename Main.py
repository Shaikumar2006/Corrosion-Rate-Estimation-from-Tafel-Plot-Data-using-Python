import pandas as pd
from corrosion_analysis import analyze_material

# Load data
df = pd.read_csv("corrosion_data.csv")

# Show available materials
materials = df["Material"].unique()
print("📋 Available Materials:")
for idx, mat in enumerate(materials, 1):
    print(f"{idx}. {mat}")

# Ask user for input
choice = int(input("🔍 Enter the number of the material to analyze: "))
selected_material = materials[choice - 1]

# Call the analyzer function
analyze_material(df, selected_material)
