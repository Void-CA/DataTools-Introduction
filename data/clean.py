import pandas as pd

df = pd.read_csv("GaltonFamilies.csv")

df = df.drop(columns=["rownames", "midparentHeight", "childNum"])
df.to_csv("Families.csv", index=False)
