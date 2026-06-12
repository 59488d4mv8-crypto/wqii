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


def strategy_matrix():
    return {
        '白天学习者': ['工作日推送学习任务', '组织社群打卡活动', '推荐系统化长期课程'],
        '夜猫子': ['开设晚间直播课', '推送夜读内容', '推荐轻量碎片化课程'],
        '周末集中学习者': ['周末打包课程', '短期训练营项目', '周末专属优惠活动']
    }


def solve(path):
    df = load_data(path)
    df = df.copy()
    df['persona'] = df.apply(classify_persona, axis=1)
    counts = df['persona'].value_counts().to_dict()
    strategies = strategy_matrix()
    return {'counts': counts, 'strategies': strategies}


if __name__ == "__main__":
    print(solve('../../datasets/user_profile.csv'))
