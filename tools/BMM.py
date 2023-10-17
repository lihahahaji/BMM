# 逆向最大匹配法 BMM

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


def BMM(text,word_dict):
    res = ""
    # 令 length 的初始值等于词典中最大的词的长度
    max_length = max(len(word) for word in word_dict)
    length = max_length

    while(text!=""):
        # 从字符串的末尾取 长度为 len 的子串 w
        w = text[-length:]

        if(w in word_dict):
            text = text[:-length]
            res = w+" "+res
            length = max_length
        else:
            if length ==1 :
                text = text[:-length]
                res = w+" "+res
                length = max_length

            else:
                length-=1
    return res


if __name__ == '__main__':
    # 替换成你的字典文件路径
    dictionary_file = "corpuswordlist.dict.yaml"

    # 从 text.txt 文件中读取待分词的文本
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    word_dict = load_dictionary(dictionary_file)
    segmented_text = BMM(text, word_dict)

    # 将分词结果输出到 output.txt 文件
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("分词结果:\n " + segmented_text)



    