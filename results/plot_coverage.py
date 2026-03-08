import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
random = pd.read_csv("random.csv")
zigzag = pd.read_csv("zigzag.csv")
frontier = pd.read_csv("frontier.csv")

# Convert coverage from fraction to percentage
random["coverage"] = random["coverage"] * 100
zigzag["coverage"] = zigzag["coverage"] * 100
frontier["coverage"] = frontier["coverage"] * 100


# =========================
# Coverage vs Time Plot
# =========================

plt.figure(figsize=(8,5))

plt.plot(random["time"], random["coverage"], label="Random Exploration", linewidth=2)
plt.plot(zigzag["time"], zigzag["coverage"], label="Zig-Zag Coverage", linewidth=2)
plt.plot(frontier["time"], frontier["coverage"], label="Frontier Exploration", linewidth=2)

plt.xlabel("Time (seconds)")
plt.ylabel("Coverage (%)")
plt.title("Coverage vs Time for Exploration Strategies")

plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure for LaTeX
plt.savefig("coverage_plot.png", dpi=300)

plt.show()



# =========================
# Final Coverage Values
# =========================

random_final = random["coverage"].iloc[-1]
zigzag_final = zigzag["coverage"].iloc[-1]
frontier_final = frontier["coverage"].iloc[-1]

print("\nFinal Coverage Comparison:")
print("Random Exploration:", random_final)
print("Zig-Zag Coverage:", zigzag_final)
print("Frontier Exploration:", frontier_final)



# =========================
# Coverage Growth Rate
# =========================

random_rate = random_final / random["time"].iloc[-1]
zigzag_rate = zigzag_final / zigzag["time"].iloc[-1]
frontier_rate = frontier_final / frontier["time"].iloc[-1]

print("\nCoverage Growth Rate (% per second):")
print("Random Exploration:", random_rate)
print("Zig-Zag Coverage:", zigzag_rate)
print("Frontier Exploration:", frontier_rate)



# =========================
# Final Coverage Bar Chart
# =========================

strategies = ["Random", "Zig-Zag", "Frontier"]
final_coverage = [random_final, zigzag_final, frontier_final]

plt.figure(figsize=(6,4))

plt.bar(strategies, final_coverage)

plt.ylabel("Coverage (%)")
plt.title("Final Coverage Comparison")

plt.grid(axis='y')
plt.tight_layout()

# Save bar chart
plt.savefig("coverage_bar.png", dpi=300)

plt.show()