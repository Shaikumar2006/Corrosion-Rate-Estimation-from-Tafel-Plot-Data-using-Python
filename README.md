# Corrosion-Rate-Estimation-from-Tafel-Plot-Data-using-Python
This project helps materials and metallurgical engineers estimate how quickly a metal will corrode in a given environment — using electrochemical test data (called Tafel data) and Python programming.

##🧪 Scientific Context:
When materials like steel, aluminum, or titanium are exposed to corrosive environments (like saltwater), they degrade over time. Engineers study this behavior using Tafel plots, which come from experiments that apply voltage to a material and measure how much current flows (i.e., corrosion activity).

The Tafel curve is a plot of:
 ***Potential (V) vs. log(Current Density in µA/cm²)***
From this curve, we extract the corrosion current (i_corr) and use it to estimate the corrosion rate using a scientific formula.

##🧩 What My Code Does:
*Loads corrosion test data (Tafel data) from a CSV file

*Filters data for a specific material (e.g., SS 316 steel)

*Calculates log(current density) to prepare for Tafel plotting

*Plots a Tafel curve (a key visualization in corrosion science)

*Performs linear regression to estimate corrosion current (i_corr)

*Applies the corrosion rate formula:

  Corrosion Rate (mm/year) = 3272⋅𝑖corr⋅𝐸𝑊/𝜌
     
  Where:
         𝑖corr = corrosion current (µA/cm²)
         𝐸𝑊 = Equivalent weight of the material (g)
         ρ = Density of the material (g/cm³)

*Prints out the corrosion rate and current for the selected material

*Saves a Tafel plot image to an images/ folder

##🧾 Final Output :
Material: SS 316
Estimated i_corr: 7.9433 µA/cm²
Estimated corrosion rate: 87.13 mm/year

## 🛠️ Technologies Used
- Python
- Pandas, NumPy, Matplotlib
- SciPy (for regression)


##🎯 Why This Is Useful:
Helps engineers understand how fast a material degrades in real-world environments

Saves cost and time by avoiding premature material failure

Used in aerospace, marine, defense, automotive industries

Shows your ability to apply programming to real engineering problems


