import pandas as pd

def main():
    df = pd.read_csv('mets.csv')

    # 60kgの人
    weight = 60
    # 大分類(major-heading)
    major = '家での活動'
    # 消費したいカロリー kcal
    consume = 100

    df = df[df['major_heading']==major]
    df = df.sort_values('mets', ascending=False)

    for index, row in df.iterrows():
      minutes = int(60 * consume / (row['mets'] * weight * 1.05) )
      print(minutes,'分 ',row['specific_activities'])





if __name__ == "__main__":
    main()