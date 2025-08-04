import pandas as pd
from src.preprocess import load_and_prepare
from src.model import build_model

def train(epochs=5, batch_size=32, model_path='../models/sentiment_model.h5'):
    train_ds, test_ds = load_and_prepare()
    model = build_model()

    history = model.fit(
        train_ds.batch(batch_size),
        epochs=epochs,
        validation_data=test_ds.batch(batch_size)
    )
    model.save(model_path)

    # Save training metrics
    pd.DataFrame(history.history).to_csv('../metrics/training_metrics.csv', index=False)

if __name__ == '__main__':
    train()
