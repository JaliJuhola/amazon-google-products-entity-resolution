import pandas as pd

def read_google_products():
    productsGoogle = pd.read_csv("./Amazon-GoogleProducts/GoogleProducts.csv", encoding="ISO-8859-1")
    return productsGoogle

def read_amazon_products():
    productsAmazon = pd.read_csv("./Amazon-GoogleProducts/Amazon.csv", encoding="ISO-8859-1")
    return productsAmazon

def get_blocks_by_column(dataframe, column):
    groupedItem = dataframe.groupby(by=column).groups
    return groupedItem

def get_entity_indexes(mainDataframe, column):
    cleaned = {}
    grouped = get_blocks_by_column(mainDataframe, column)
    for item in grouped.values():
        # Duplicates cannot be found in groups of ones
        if(len(item) > 1):
            manufacturer = mainDataframe[column].iloc[item[0]]
            cleaned[manufacturer] = item
    return cleaned
def compare_dataframes(df1, df2, entity1, entity2):
    cleanedGoogleIndexes = get_entity_indexes(df1, entity1)
    cleanedAmazonIndexes = get_entity_indexes(df2, entity2)
    for groupName, groupItems in block1.items():
        if groupName in cleanedGoogleIndexes.keys():
            df1Group = df1.take(cleanedGoogleIndexes[groupName])
            df2Group = df2.take(cleanedAmazonIndexes[groupName])
            for index, row in df1Group.iterrows():
                nameToSearch = row['name']
                nameMatches=df2Group[df2Group['title']==nameToSearch]
                priceToSearch = row['price']
                priceMatches=df2Group[df2Group['price']==priceToSearch]
                descriptionToSearch = row['description']
                descriptionMatches=df2Group[df2Group['description']==descriptionToSearch]
                if len(priceMatches.index):
                    print(priceMatches)
                    print()
                    print(row)
                    print("*******")
                if len(nameMatches.index):
                    print(nameMatches)
                    print()
                    print(row)
                    print("*******")
                if len(descriptionMatches.index):
                    print(descriptionMatches)
                    print()
                    print(row)
                    print("*******")
googleProducts = read_google_products()
amazonProducts = read_amazon_products()

            
