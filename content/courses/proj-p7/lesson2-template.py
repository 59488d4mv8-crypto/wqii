import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df


def build_baskets(df):
    baskets = df.groupby('user_id')['course_id'].apply(set).tolist()
    return baskets


if __name__ == "__main__":
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    print("事务数:", len(baskets))
    print("前 3 个事务:", baskets[:3])
