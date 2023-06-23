# The Snowpark package is required for Python Worksheets.
# You can add more packages by selecting them using the Packages control and then importing them.

from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters={
    "account":"",
    "user":"",
    "password":"",
    "role":"dba",
    "warehouse":"generic",
    "schema":"dbdemo.raw"
}

def main(session: Session):
    # Your code goes here, inside the "main" handler.
    # tableName = 'information_schema.packages'
    # dataframe = session.table(tableName).filter(col("language") == 'python')
    # Print a sample of the dataframe to standard output.
    # dataframe.show()
    session = session.builder.configs(connection_parameters).create()

    # Return value will appear in the Results tab.
    stagename = "dbdemo.raw.dbstage"
    filename = "parquetexample.parquet"

    # read the staged file
    dfRaw = session.read.parquet(f"@{stagename}/{filename}")

    # coDBDEMO.RAW.SNOWPARK_TEMP1DBDEMO.RAW.SNOWPARK_TEMP1py the data into a table
    session.sql("drop table if exists dbdemo.raw.SNOWPARK_TEMP1;")
    rawtable = "Snowpark_Temp2"
    dfRaw.count()
    dfRaw.write.mode('append').save_as_table(rawtable)
    return "success"

a = main(Session)
print(a)