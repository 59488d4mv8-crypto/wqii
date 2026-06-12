import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def classify_persona(row):
    hour = row['active_hour']
    if 9 <= hour <= 17:
        return '白天学习者'
    elif hour >= 22 or hour <= 5:
        return '夜猫子'
    else:
        return '周末集中学习者'


def personas_summary(df):
    df = df.copy()
    df['persona'] = df.apply(classify_persona, axis=1)
    return df['persona'].value_counts().to_dict()


def solve(path):
    df = load_data(path)
    return personas_summary(df)


if __name__ == "__main__":
    print(solve('../../datasets/user_profile.csv'))
