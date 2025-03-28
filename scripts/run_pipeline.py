import os #legato a quello sotto
import sys #sistem serve per muoversi nelle cartelle in python
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
#torna indietro e considera il path dalla cartella indietro cosi vedrà la cartella src


import logging
from src import config 
from src.load_data import load_data #sta chiamando delle funzioni in un altro file così è più comodo e logico
from src.preprocess import preprocess_data
from src.make_model import train_model
# from src.evaluation import evaluate_model
# from src.save_results import save_predictions

# log serve perche così vediamo dove si è fermato e dove è fallito con data e ora
# Set up logging
logging.basicConfig(filename='../logs/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Sentiment Analysis Pipeline...")

    # Step 1: Load data from Excel and store it in SQLite
    logging.info("Loading raw data...")
    load_data()

    # Step 2: Preprocess text data
    logging.info("Preprocessing data...")
    preprocess_data()

    # Step 3: Train sentiment analysis model
    logging.info("Training the model...")
    train_model()

    # # Step 4: Evaluate model performance
    # logging.info("Evaluating the model...")
    # evaluate_model(model, vectorizer, config.DATABASE_PATH)

    # # Step 5: Predict sentiment on new/processed data
    # logging.info("Making predictions...")
    # predictions = predict_sentiment(model, vectorizer, config.DATABASE_PATH)

    # # Step 6: Save results to the database
    # logging.info("Saving predictions to database...")
    # save_predictions(predictions, config.DATABASE_PATH)

    # logging.info("Sentiment Analysis Pipeline completed successfully!")

if __name__ == "__main__": #fa una condizione per cui se realizzata lancia la funzione definita sopra
    main()

#se lancio il file da qui mi fa partire la funzione main se invece importo questo file e lo faccio parrtire da un altro file non fa nulla