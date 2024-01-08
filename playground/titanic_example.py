import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "D'Cap, Master Leon",
        ],
        "Age": [22, 35, 58, 17],
        "Sex": ["male", "male", "female", "male"],
    }
        
)

print(df)

