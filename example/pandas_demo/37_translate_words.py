import re

import requests
from bs4 import BeautifulSoup

from pandas_demo import log, pd

if __name__ == '__main__':
    # 对批量的英语文本, 生成英语-汉语翻译的单词本, 提供exceL下载
    # 1. 提供一个英文文章URL, 自动下载网页
    # 2. 实现网站中所有英语单词的翻译
    # 3. 下载翻译结果的excel
    # 材料: https://github.com/skywind3000/ECDICT , 下载master分支后, 里边有一个 stardict.csv 的文件
    file_path = "C:/WorkSpace/python3-example/material/stardict.csv"
    # 要么指定每一列的类型: dtype={'column_11': str}, 要么设置low_memory=False, 目的是一次性读取文件进行类型推断
    df = pd.read_csv(file_path, low_memory=False)
    log.info("df: \n{}".format(df.sample(10).head()))
    log.info("df shape: {}".format(df.shape))
    df = df[["word", "translation"]]
    log.info("df: \n{}".format(df.head()))

    url = "https://pandas.pydata.org/docs/user_guide/index.html"
    html_content = requests.get(url).text
    # log.info("html_content: \n{}".format(html_content[:100]))
    # 提取 html 正文内容
    # 1. 去除 html 标签, 获取正文
    soup = BeautifulSoup(html_content, features="html.parser")
    html_text = soup.get_text()
    # log.info("html_text: \n{}".format(html_text[:100]))

    # 2. 英文分词和数据清洗
    word_list = re.split(r"""[ ,.\(\)/\n|\-:=\$\["']""", html_text)
    log.info("word_list: \n{}".format(word_list[:100]))
    # 读取停用词表
    with open("C:/WorkSpace/python3-example/material/stop_words.txt") as fin:
        stop_words = set(fin.read().split("\n"))
    log.info("stop_words: \n{}".format(list(stop_words)[:100]))
    # 数据清洗
    word_list_clean = []
    for word in word_list:
        word = str(word).lower().strip()
        # 过滤掉空词, 数字, 单个字符, 停用词
        if not word or word.isnumeric() or len(word) <= 1 or word in stop_words:
            continue
        word_list_clean.append(word)
    log.info("word_list_clean: \n{}".format(list(word_list_clean)[:100]))
    # 分词结果构造成一个 DataFrame
    df_words = pd.DataFrame({"word": word_list_clean})
    log.info("df_words shape: ".format(df_words.shape))
    # 统计词频
    df_words = df_words.groupby("word")["word"].aggregate(count="size").reset_index().sort_values(by="count",
                                                                                                  ascending=False)
    log.info("df_words: ".format(df_words.head()))
    # 和单词词典实现 merge
    df_merge = pd.merge(left=df, right=df_words, left_on="word", right_on="word")
    log.info("df_merge: ".format(df_merge.head()))
    # df.to_excel("C:/WorkSpace/python3-example/material/translate_words.xlsx",index=False)
