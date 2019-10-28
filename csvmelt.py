''' Created by Jeremy Reynolds for UALR COSMOS Team
    Merges multiple columns into two, with the header being repeated
    for as many rows as is below each respective header.
            before              after
        FRUIT	COLOR       FRUIT   mango
        mango	red         FRUIT   apple
        apple	green       FRUIT   papaya
        papaya	blue        COLOR   red
                            COLOR   green
                            COLOR   blue
'''

import csv, pandas as pd

inputFile = 'test.csv'
headers = 'FRUIT', 'COLOR'

with open(inputFile, 'r') as file:   # Determins file delimiter from first 512bytes
    dialect = csv.Sniffer().sniff(file.read(512))

df = pd.read_csv(inputFile, delimiter=dialect.delimiter)
df = pd.melt(df)                    # 'Unpivots' DateFrame from wide to long format
df = df.dropna(how='any')           # Drops rows with missing values (NAN)
df.columns = headers                # Renames column headers
df.to_csv('output_'+inputFile, index=False, encoding='utf-8')