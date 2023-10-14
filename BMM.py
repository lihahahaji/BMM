import yaml

# 读取词典文件
def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        word_dict = yaml.load(file, Loader=yaml.FullLoader)
    return set(word_dict)

# 使用双向最大匹配法进行分词
def bmm_segment(text, word_dict):
    result = []
    max_word_length = max(len(word) for word in word_dict)

    text_length = len(text)
    i = 0

    while i < text_length:
        length = min(max_word_length, text_length - i)
        while length > 0:
            sub = text[i:i + length]
            if sub in word_dict:
                result.append(sub)
                i += length
                break
            length -= 1

        if length == 0:
            length = 1
            result.append(text[i:i + length])
            i += length

    return result

# 主程序
if __name__ == '__main__':
    # 替换成你的词典文件路径
    dictionary_file = "corpuswordlist.dict.yaml"

    # 替换成你的待分词文本文件路径
    text_file = "text.txt"

    word_dict = load_dictionary(dictionary_file)

    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    result = bmm_segment(text, word_dict)
    print("分词结果:", " ".join(result))
