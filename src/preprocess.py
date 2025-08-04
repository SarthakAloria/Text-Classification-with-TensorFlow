import tensorflow_datasets as tfds

def load_and_prepare():
    # Load IMDB reviews dataset
    (train, test), info = tfds.load(
        'imdb_reviews',
        split=['train', 'test'],
        as_supervised=True,
        with_info=True
    )
    # You can add tokenization/padding here if needed
    return train, test

if __name__ == '__main__':
    train_ds, test_ds = load_and_prepare()
    print("Loaded train and test datasets:", train_ds, test_ds)
