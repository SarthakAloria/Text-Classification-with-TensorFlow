from tensorflow.keras.models import load_model
from src.preprocess import load_and_prepare

def evaluate(model_path='../models/sentiment_model.h5', batch_size=32):
    _, test_ds = load_and_prepare()
    model = load_model(model_path)
    loss, acc = model.evaluate(test_ds.batch(batch_size))
    print(f"Test Accuracy: {acc:.4f}")

if __name__ == '__main__':
    evaluate()
