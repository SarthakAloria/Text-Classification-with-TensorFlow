from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

def build_model(vocab_size=10000, embedding_dim=16):
    model = Sequential([
        Embedding(vocab_size, embedding_dim),
        GlobalAveragePooling1D(),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

if __name__ == '__main__':
    m = build_model()
    m.summary()
