import pandas as pd

online = pd.read_csv(
    "s3://udacity-ab-test/udacity_ab_test_cleaned.csv", parse_dates=["Datetime"]
)
online["group_bin"] = (online["group"] == "treatment").astype(int)

permutation_df = pd.read_csv(
    "s3://udacity-ab-test/permutation_test.csv", names=["diffs"]
)
