# 加载字典
def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        word_dict = {}
        for line in file:
            try:
                word, frequency = line.strip().split()
            except Exception as e:
                print(line)

            word_dict[word] = int(frequency)
        return word_dict

# 双向最大匹配法分词
def bidirectional_maximum_matching(text, word_dict):
    # 创建一个空的列表 result，该列表将用于存储分词结果
    result = []
    # 词典中词语的最大长度，将其存储在 max_word_length 变量中
    max_word_length = max(len(word) for word in word_dict)
    # 待分词文本的长度
    text_length = len(text)
    i = 0

    # 遍历整个文本
    while i < text_length:
        # 确定每次尝试匹配的子串的长度
        # 初始时，将 length 设置为最大词语长度和剩余文本长度中较小的那个值。
        length = min(max_word_length, text_length - i)
        while length > 0:
            # 从文本中截取长度为 length 的子串
            sub = text[i:i + length]
            # 检查该子串是否在词典 word_dict 中存在。
            # 如果存在，表示找到了一个匹配的词语，将该词语添加到结果列表 result
            if sub in word_dict:
                result.append(sub)
                i += length
                break
            # 如果没有找到匹配的词语，将 length 减小为 length - 1，然后继续尝试匹配更短的子串。
            length -= 1

        # 如果 length 减小到 0，表示在当前位置找不到匹配的词语，将当前位置 i 增加 1，并将一个字符添加到结果列表 result 中。
        if length == 0:
            length = 1
            result.append(text[i:i + length])
            i += length

    return result

if __name__ == '__main__':
    # 替换成你的字典文件路径
    dictionary_file = "corpuswordlist.dict.yaml"

    # 从 text.txt 文件中读取待分词的文本
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    word_dict = load_dictionary(dictionary_file)
    segmented_text = bidirectional_maximum_matching(text, word_dict)

    # 将分词结果输出到 output.txt 文件
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("分词结果:\n " + " ".join(segmented_text))
