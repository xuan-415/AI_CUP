# Model
- 其中在進行Retrieval時，用到了兩個模型，一個是BM25一個是gpt-4o-mini
- BM25使用到的是預訓練好的檢索模型，透過Library
- 我們先是透過了BM25來檢索出與問題最相關的3個文檔內容
- 接著再透過gpt-4o-mini從3個之中挑出最相關的作為答案
