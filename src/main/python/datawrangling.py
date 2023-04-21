# 1)Load the data
# 2)Make sure your data set is cleaned enough, so we for example don't include in results with
# empty/null "titles" and/or "number of pages" is greater than 20 and "publishing year" is
# after 1950. State your filters clearly.
# 3)Run the following queries with the preprocessed/cleaned dataset:
# 1. Select all "Harry Potter" books
# 2. Get the book with the most pages
# 3. Find the Top 5 authors with most written books (assuming author in first position in the array, "key" field and each
# row is a different book)
# 4. Find the Top 5 genres with most books
# 5. Get the avg. number of pages
# 6. Per publish year, get the number of authors that published at least one book
import configparser as cp
import pandas as pd
import logging
import os
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
loggingFormat = '%(asctime)-15s %(message)s'
logging.basicConfig(format=loggingFormat)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

conf=cp.RawConfigParser()
conf.read('../../../resources/application.properties')
def readconfig(env,propkey):
    return conf.get(env,propkey)

def dataprocessing():
    try:
        env='dev'
        filedirectory=readconfig(env,'filedirectory')
        filename = readconfig(env, 'filename')
        filepath=filedirectory+filename
        logger.info('going to check the file')
        if os.path.isfile(filepath):
            logger.info('file found - going to read the file')
            df=pd.read_json(filepath,lines=True)
            print(df.columns)
            print(df.dtypes)
            print(df.head(5))
            print(df.count)

            dfcleantitle=df[df['title'].notnull()]
            dfcleantitle=dfcleantitle[dfcleantitle['title'] !='No Title Exists.']
            dfgenre = dfcleantitle[dfcleantitle['genres'].notnull()]
            dfgenre = dfgenre.dropna(subset=['genres'],inplace=True)
            dfgenre = dfgenre[dfgenre['genres'].str.len()>0]
            dfnop=dfgenre[dfgenre['number_of_pages'].notnull()]
            dfnop = dfnop[dfnop['number_of_pages'].int>20]
            dfpub = dfgenre[dfgenre['number_of_pages'].notnull()]
            dfnop = dfnop[dfnop['number_of_pages'].int > 20]
    # "number of pages" is greater
    # than
    # 20 and "publishing year" is
    # # after 1950. State your filters clearly.
    except Exception as e:
            #dfHarryPotter.to_csv(fileOutDirectory + "/" + "HarryPotter.csv")

        logger.error(e)

output=dataprocessing()
