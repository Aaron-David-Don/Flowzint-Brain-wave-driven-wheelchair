import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("InActive30April2.csv")

# Get 2nd column (index 1)
y = df.iloc[:, 1]

# Plot
plt.figure(figsize=(10, 4))
plt.plot(y, color='blue')

# Optional styling (to match your image style)
plt.grid(False)
plt.tight_layout()

plt.show()