import sqlite3
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

import logging
# Set up logging
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data():
    logging.info('Opening Excel Files...')
    e1 = pd.read_excel(os.path.join(config.RAW_DATA_PATH,
                    'earth_day_tweets_sentiment_50k_(1).xlsx'))
    #e1.drop_duplicates(inplace=True)

    e2 = pd.read_excel(os.path.join(config.RAW_DATA_PATH,
                    'earth_day_tweets_sentiment_50k_(2).xlsx'))
    #e2.drop_duplicates(inplace=True)

    fifa = pd.read_excel(os.path.join(config.RAW_DATA_PATH,
                        'fifa_world_cup_2022_tweets_sentiment_22k.xlsx'))
    #fifa.drop_duplicates(inplace=True)
    
    generic = pd.read_excel(os.path.join(config.RAW_DATA_PATH, 'generic_27k.xlsx'))
    #generic.drop_duplicates(inplace=True)

    e1 = e1[['text', 'sentiment']]
    e2 = e2[['text', 'sentiment']]
    fifa = fifa[['Tweet', 'Sentiment']]
    fifa.columns = ['text', 'sentiment']
    generic = generic[['text', 'sentiment']]
    df = pd.concat([e1, e2, fifa, generic])
    df.reset_index(drop=True, inplace=True)
    

    # Create a connection to the SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Write the DataFrame to a table (replace 'my_table' with your desired table name)
    # scrivi la tabella su SQL
    df.to_sql(config.RAW_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    logging.info(f"Data successfully written to {config.RAW_TABLE} table.")
