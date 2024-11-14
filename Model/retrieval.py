import time
import jieba
import openai
from rank_bm25 import BM25Okapi  # 使用BM25演算法進行文件檢索

def gpt4_retrieve(ans, qs, corpus_dict):
    """先是利用BM25挑出三個與問題最相關的文檔，再透過openai的gpt-4o-mini來選擇與問題最相關的文檔"""
    while len(ans) < 3:
        ans.append("")
    retries = 10
    prompt =f"""
            Document 0: {ans[0]}
            Document 1: {ans[1]}
            Document 2: {ans[2]}
            Question: {qs}

            Please choose the most relevant document by returning either 0, 1, 2 based on the question. Only return the number.
            """ 
    while retries > 0:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an assistant that helps retrieve the most relevant document based on a given question."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.0,
                n=1
            )
            retries = -1
        except openai.error.RateLimitError as e:
            print("Rate limit reached, waiting before retrying...")
            retries -= 1
            time.sleep(10)  # 等待 1000 毫秒（1 秒）後重試

    index = response['choices'][0]['message']['content'].strip()
    res = [key for key, value in corpus_dict.items() if value == ans[int(index)]]
    return res[0] 

def BM25_retrieve(qs, source, corpus_dict):
    """透過BM25來挑出三個與問題最相關的文檔"""
    filtered_corpus = [corpus_dict[int(file)] for file in source]
    tokenized_corpus = [list(jieba.cut_for_search(doc)) for doc in filtered_corpus]  # 將每篇文檔進行分詞
    bm25 = BM25Okapi(tokenized_corpus)  # 使用BM25演算法建立檢索模型
    tokenized_query = list(jieba.cut_for_search(qs))  # 將查詢語句進行分詞
    ans = bm25.get_top_n(tokenized_query, list(filtered_corpus), n=3)  # 根據查詢語句檢索，返回最相關的文檔，其中n為可調整項
    pid = gpt4_retrieve(ans, qs, corpus_dict)
    return pid