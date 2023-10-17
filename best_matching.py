import yaml

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        word_dict = {}
        for line in file:
            word, frequency = line.strip().split()
            word_dict[word] = int(frequency)
        return word_dict

def best_matching(text, word_dict):
    n = len(text)
    dp = [0] * (n + 1)
    seg_points = [-1] * n

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        seg_points[i - 1] = i - 1
        for j in range(i - 1, -1, -1):
            word = text[j:i]
            if word in word_dict:
                cost = len(word)
                if j > 0:
                    cost += dp[j - 1]
                if cost < dp[i]:
                    dp[i] = cost
                    seg_points[i - 1] = j - 1

    segmented_text = []
    i = n - 1
    while i >= 0:
        j = seg_points[i]
        segmented_text.insert(0, text[j + 1:i + 1])
        i = j

    return segmented_text

if __name__ == '__main__':
    # 替换成你的字典文件路径
    dictionary_file = "corpuswordlist.dict.yaml"

    # 从 text.txt 文件中读取待分词的文本
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    word_dict = load_dictionary(dictionary_file)
    segmented_text = best_matching(text, word_dict)

    # 将分词结果输出到 output.txt 文件
    with open("output1.txt", "w", encoding="utf-8") as output_file:
        output_file.write("分词结果: " + " ".join(segmented_text))
