import torch

from transformers import AutoTokenizer

from word2vec import Word2Vec
from load_corpus import load_corpus
from config import *


if __name__ == "__main__":
    print("Starting Word2Vec training...")
    
    # load pretrained tokenizer
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    vocab_size = tokenizer.vocab_size
    print(f"Tokenizer loaded. Vocab size: {vocab_size}")

    # load corpus
    print("Loading corpus...")
    corpus = load_corpus()
    print(f"Corpus loaded. Number of documents: {len(corpus)}")
    
    # 앞의 10개 문장만 사용
    corpus = corpus[:10]
    print(f"Using only first {len(corpus)} documents for ultra-fast training.")
    
    if len(corpus) == 0:
        print("ERROR: No documents loaded! Check if the dataset is available.")
        exit(1)
    
    # Print first few characters of first document
    if corpus:
        print(f"First document preview: {corpus[0][:200]}...")

    # declare word2vec
    print(f"Creating Word2Vec model with method: {method}")
    word2vec = Word2Vec(vocab_size, d_model, window_size, method).to(device)
    print(f"Model created on device: {device}")

    # train word2vec
    print(f"Starting training with {num_epochs_word2vec} epochs...")
    word2vec.fit(corpus, tokenizer, lr_word2vec, num_epochs_word2vec)
    print("Training completed!")

    # save word2vec checkpoint
    print("Saving model...")
    torch.save(word2vec.cpu().state_dict(), "word2vec.pt")
    print("Model saved to word2vec.pt")