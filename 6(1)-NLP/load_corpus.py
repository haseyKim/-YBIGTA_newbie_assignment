# 구현하세요!
import kagglehub  # type: ignore
import os
import glob
import re

# Download latest version
path = kagglehub.dataset_download("prashantkarwasra/books-dataset-text-generation")

def load_corpus() -> list[str]:
    corpus: list[str] = []
    
    # Get all .txt files in the dataset directory
    txt_files = glob.glob(os.path.join(path, "*.txt"))
    
    # Read each text file and add its content to corpus
    for file_path in txt_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # 긴 텍스트를 문장 단위로 분할
                sentences = re.split(r'[.!?]+', content)
                
                # 적절한 길이의 문장만 추가
                for sentence in sentences:
                    sentence = sentence.strip()
                    if sentence and len(sentence) > 10 and len(sentence) < 500:
                        corpus.append(sentence)
                
                print(f"Loaded: {os.path.basename(file_path)} - {len(sentences)} sentences")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    print(f"Total sentences loaded: {len(corpus)}")
    return corpus