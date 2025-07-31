import torch
from torch import nn, Tensor, LongTensor
from torch.optim import Adam

from transformers import PreTrainedTokenizer

from typing import Literal


class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method
        self.weight.weight.data = self.embeddings.weight.data.clone()

    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        
        self.train()
        print(f"Starting training with {len(corpus)} documents...")
        
        for epoch in range(num_epochs):
            total_loss = 0
            num_batches = 0
            print(f"Epoch {epoch+1}/{num_epochs} starting...")
            
            for doc_idx, sentence in enumerate(corpus):
                if doc_idx % 10 == 0:  # 10개마다 진행상황 출력
                    print(f"  Processing document {doc_idx+1}/{len(corpus)}")
                
                # 문장을 토큰화
                tokens = tokenizer.encode(sentence, add_special_tokens=False)
                
                # padding token 제외 (보통 0번이 padding token)
                tokens = [token for token in tokens if token != tokenizer.pad_token_id]
                
                if len(tokens) < 2 * self.window_size + 1:
                    if doc_idx % 10 == 0:  # 10개마다만 출력
                        print(f"    Skipping document {doc_idx+1} (too short: {len(tokens)} tokens)")
                    continue
                
                if self.method == "cbow":
                    self._train_cbow(tokens, criterion, optimizer)
                elif self.method == "skipgram":
                    self._train_skipgram(tokens, criterion, optimizer)
                
                num_batches += 1
            
            if num_batches > 0:
                print(f"Epoch {epoch+1}/{num_epochs} completed. Processed {num_batches} documents.")
            else:
                print(f"Epoch {epoch+1}/{num_epochs} completed. No documents were processed (all too short).")
        
        print("Training completed!")

    def _train_cbow(
        self,
        tokens: list[int],
        criterion: nn.CrossEntropyLoss,
        optimizer: Adam
    ) -> None:
        for i in range(self.window_size, len(tokens) - self.window_size):
            # context words (주변 단어들)
            context_words = []
            for j in range(-self.window_size, self.window_size + 1):
                if j != 0:  # target word 제외
                    context_words.append(tokens[i + j])
            
            target_word = tokens[i]
            
            # context words를 텐서로 변환
            context_tensor = torch.tensor(context_words, dtype=torch.long)
            target_tensor = torch.tensor([target_word], dtype=torch.long)
            
            # forward pass
            context_embeddings = self.embeddings(context_tensor)  # (2*window_size, d_model)
            context_avg = context_embeddings.mean(dim=0, keepdim=True)  # (1, d_model)
            output = self.weight(context_avg)  # (1, vocab_size)
            
            # loss 계산 및 역전파
            loss = criterion(output, target_tensor)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    def _train_skipgram(
        self,
        tokens: list[int],
        criterion: nn.CrossEntropyLoss,
        optimizer: Adam
    ) -> None:
        for i in range(len(tokens)):
            target_word = tokens[i]
            
            # window 내의 context words 찾기
            for j in range(max(0, i - self.window_size), min(len(tokens), i + self.window_size + 1)):
                if i != j:  # 자기 자신 제외
                    context_word = tokens[j]
                    
                    # target과 context를 텐서로 변환
                    target_tensor = torch.tensor([target_word], dtype=torch.long)
                    context_tensor = torch.tensor([context_word], dtype=torch.long)
                    
                    # forward pass
                    target_embedding = self.embeddings(target_tensor)  # (1, d_model)
                    output = self.weight(target_embedding)  # (1, vocab_size)
                    
                    # loss 계산 및 역전파
                    loss = criterion(output, context_tensor)
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

    def forward(self, x: LongTensor) -> Tensor:
        embeddings = self.embeddings(x)
        output = self.weight(embeddings)
        return output