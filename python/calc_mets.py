import pandas as pd
import json

def main(weight,major,consume):
  with open('json/consume.json', 'w') as f:
    f.write('[')
    df = pd.read_csv('python/mets.csv')

    # # 60kgの人
    # weight = 60
    # # 大分類(major-heading)
    # major = '家での活動'
    # # 消費したいカロリー kcal
    # consume = 100

    df = df[df['major_heading']==major]
    df = df.sort_values('mets', ascending=False)

    i=0
    for index, row in df.iterrows():
      minutes = int(60 * consume / (row['mets'] * weight * 1.05) )
      d = {'Activity':row['specific_activities'], 'minutes':minutes}
      json.dump(d, f, indent = 4, ensure_ascii=False)
      if i < len(df)-1:
          f.write(',')
      i=i+1
    f.write(']')
    f.close()

if __name__ == "__main__":
    main(60,'自転車',100)