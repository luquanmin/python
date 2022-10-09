import pandas as pd
import io

csv = '''
breed,type,longevity,size,weight
German Shepherd,herding,9.73,large,
Beagle,hound,12.3,small,
Yorkshire Terrier,toy,12.6,small,5.5
Golden Retriever,sporting,12.04,medium,60.0
Bulldog,non-sporting,6.29,medium,45.0
Labrador Retriever,sporting,12.04,medium,67.5
Boxer,working,8.81,medium,
Poodle,non-sporting,11.95,medium,
Dachshund,hound,12.63,small,24.0
Rottweiler,working,9.11,large,
Boston Terrier,non-sporting,10.92,medium,
Shih Tzu,toy,13.2,small,12.5
Miniature Schnauzer,terrier,11.81,small,15.5
Doberman Pinscher,working,10.33,large,
Chihuahua,toy,16.5,small,5.5
Siberian Husky,working,12.58,medium,47.5
Pomeranian,toy,9.67,small,5.0
French Bulldog,non-sporting,9.0,medium,27.0
Great Dane,working,6.96,large,
Shetland Sheepdog,herding,12.53,small,22.0
Cavalier King Charles Spaniel,toy,11.29,small,15.5
German Shorthaired Pointer,sporting,11.46,large,62.5
Maltese,toy,12.25,small,5.0
'''

dogs = pd.read_csv(io.StringIO(csv))

dogs1=dogs['longevity']

dogs2=dogs.groupby('size').mean()

dogs3=dogs.sort_values('size').groupby('size')['weight'].agg(['sum','mean','std'])

dogs4=dogs.groupby('size')['weight'].agg(['sum','mean','std'])

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 10, 'b': 20, 'c': 30, 'd': 40},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000},
          {'a': 10000, 'b': 20000, 'c': 30000, 'd': 40000},
          ]

df = pd.DataFrame(mydict, index=['one', 'two', 'three', 'four', 'five'])

df1=df.loc[:, df.loc['two'] <= 20]

csv1 = '''
breed,group,longevity,size
Labrador,sporting,12.04,medium
German,herding,9.73,large
Beagle,hound,12.3,small
Golden,sporting,12.04,medium
Yorkshire,toy,12.6,small
Bulldog,non-sporting,6.29,medium
Boxer,working,8.81,medium
Poodle,non-sporting,11.95,medium
'''

dogs4 = pd.read_csv(io.StringIO(csv1))
dogs4 = dogs[['breed', 'size', 'longevity']]

print(dogs4)


