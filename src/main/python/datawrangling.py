# 1)Load the data
# 2)Make sure your data set is cleaned enough, so we for example don't include in results with
# empty/null "titles" and/or "number of pages" is greater than 20 and "publishing year" is
# after 1950. State your filters clearly.
# 3)Run the following queries with the preprocessed/cleaned dataset:
# 1. Select all "Harry Potter" books
# 2. Get the book with the most pages
# 3. Find the Top 5 authors with most written books (assuming author in first position in the array,
# "key" field and each
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
            #print(df.columns)
            #print(df.dtypes)
            #print(df.head(5))
            #print(df.count)

            dfcleantitle=df[df['title'].notnull()]
            dfcleantitle=dfcleantitle[dfcleantitle['title'] !='No Title Exists.']
            dfgenre = dfcleantitle[dfcleantitle['genres'].notnull()]
            dfgenre.dropna(subset=['genres'],inplace=True)
            dfgenre = dfgenre[dfgenre['genres'].str.len()>0]

            dfnop=dfgenre[dfgenre['number_of_pages'].notnull()]
            dfnop['number_of_pages'] = dfnop['number_of_pages'].apply(str).str.strip()
            dfnop = dfnop[dfnop['number_of_pages'].str.len()>0]
            dfnop = dfnop[dfnop['number_of_pages'] != 'nan']
            dfnop['number_of_pages'] = dfnop['number_of_pages'].apply(float)
            dfnop['number_of_pages'] = dfnop['number_of_pages'].apply(int)

            dfnop = dfnop[dfnop['number_of_pages']>20]
            logger.info('going to clean publish date')
            # dfpub = dfnop[dfnop['publish_date'].fillna(0).notnull()]
            # dfpub = dfpub[dfpub['publish_date'] !='NaN']
            dfpub=dfnop.copy()
            dfpub['publish_date'] = dfpub['publish_date'].str[-4:]
            dfpub['publish_date'] = pd.to_numeric(dfpub['publish_date'],errors='coerce')
            dfpub = dfpub[dfpub['publish_date'].notnull()]
            logger.info('publish date cleaning')
            dfpub = dfpub[dfpub['publish_date'] != 'nan']

            dfpub['publish_date']= dfpub['publish_date'].astype(int)

            dfpub = dfpub[dfpub['publish_date'].apply(int) > 1950]
            dfpub['publish_date'].value_counts().reset_index().to_csv('../../../resources/pub.csv')
            logger.info('going to check the records for Harry Potter')
            dfharrypotter=dfpub.copy()
            dfharrypotter=dfharrypotter[dfharrypotter['title'].str.contains('Harry',case=False)]
            dfharrypotter = dfharrypotter[dfharrypotter['title'].str.contains('Potter', case=False)]

            dfharrypotter.to_csv('../../../resources/harry.csv')
            #findig max number of pages
            logger.info('going to check the maximum number of pages')
            dfmaxpg=dfpub[dfpub['number_of_pages']==dfpub['number_of_pages'].max()]
            dfmaxpg.to_csv('../../../resources/maxpage.csv')
    # Authors with most written books (assuming author in first position in the array, "key" field and each
    # row is a different book)

            logger.info('writing distinct authors')
            dfauthlist=dfpub[['authors','title']]
            dfauthlist['authors']=dfauthlist['authors'].str[0].astype(str).str.slice(18, 100)\
                .map(lambda x: str(x)[:-2])
            dfauthlist[['title','authors']].groupby(['authors']).size().nlargest(5).\
                to_csv('../../../resources/top5authors.csv')

# *******
            logger.info('writing genres')
            dfgenres = dfpub[['genres']]
            dfgenres['genres'] = dfgenres['genres'].str[0].astype(str)
            dfgenres[['genres']].groupby(['genres']).size().nlargest(5).to_csv('../../../resources/genres.csv')
#           dfauthlist[['genres']].groupby(['genres']).\
#                   to_csv('../../../resources/genres.csv')
# ************
    # 4.Find the top 5 genres with most books
            logger.info('going to average number of pages')
            dfavepgsum = dfpub.copy()
            # dfavepgsum = dfpub['number_of_pages']
            dfave=str(round(dfavepgsum['number_of_pages'].sum()/dfavepgsum['number_of_pages'].count()))
            file2 = open('../../../resources/averagepage.csv', 'w')
            file2.write(dfave)
            file2.close()


            # dfavepgsum['number_of_pages'] = dfavepgsum['number_of_pages'].astype(int)
            # logger.info('going to sum number of pages')
            # dfavepgsum['number_of_pages'] = dfavepgsum[['number_of_pages']].groupby(['number_of_pages']).sum(['number_of_pages'])
            # logger.info('sum of pages is ***',dfavepgsum)
            # dfavepgsum[-1].to_csv('../../../resources/sumnumberofpages.csv')


            # dfavepgsum['number_of_pages'].groupby(['number_of_pages']).sum()
            # logger.info('sum of number of pages is ',dfavepgsum)
            # dfavepgcount = dfpub[['number_of_pages']]
            # dfavepgcount['number_of_pages'].groupby(['number_of_pages']).count()
            # logger.info('count of books is',dfavepgcount)
         #   dfavepg=dfavepgsum/dfavepgcount
         #   dfavepg.to_csv('../../../resources/avepage.csv')
   # 5. Get the avg. number of pages

    # 6. Per publish year, get the number of authors that published at least one book

    # "number of pages" is greater than and "publishing year" is after 1950. State your filters clearly.
    except Exception as e:
        # dfHarryPotter.to_csv(fileOutDirectory + "/" + "HarryPotter.csv")
        logger.error(e)

output=dataprocessing()
