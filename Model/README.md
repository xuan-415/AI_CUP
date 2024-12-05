# Model
## gpt-4o-mini
## BM25

## 使用情況
- 其中在進行Retrieval時，用到了兩個模型，一個是BM25一個是gpt-4o-mini
- BM25使用到的是預訓練好的檢索模型，透過Library rank_bm25 import BM25Okapi，透過其來建立模型檢索相關的文檔內容
- gpt-4o-mini是透過現有的LLM，並沒有特別pre-train新的模型，而是透過API的方式直接使用外部提供的大語言模型來做更精確地檢索


# 程式說明
- 我們先是透過了BM25來檢索出與問題最相關的3個文檔內容
- 接著再透過gpt-4o-mini從3個之中挑出最相關的作為答案
