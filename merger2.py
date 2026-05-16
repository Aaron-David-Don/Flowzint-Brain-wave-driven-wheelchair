import pandas as pd

files = ["InActive24April1.csv", "InActive24April2.csv", "InActive24April3.csv", "InActive24April4.csv"]

dfs = [pd.read_csv(f, header=None).iloc[:, :2] for f in files]
final_df = pd.concat(dfs, ignore_index=True)

final_df.to_csv("mergedInActive24April.csv", index=False, header=False)

print("Done. Data is now stacked into only 2 columns.")