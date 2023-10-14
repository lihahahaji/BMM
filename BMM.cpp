#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>

// 读取词典文件并存储为一个unordered_set
std::unordered_set<std::string> loadDictionary(const std::string& dictionaryFile) {
    std::unordered_set<std::string> wordDict;
    std::ifstream file(dictionaryFile);
    if (file.is_open()) {
        std::string word;
        while (std::getline(file, word)) {
            wordDict.insert(word);
        }
        file.close();
    } else {
        std::cerr << "Error: Unable to open dictionary file." << std::endl;
    }
    return wordDict;
}

// 使用双向最大匹配法进行分词
std::vector<std::string> bmmSegment(const std::string& text, const std::unordered_set<std::string>& wordDict) {
    std::vector<std::string> result;
    int maxWordLength = 0;
    for (const std::string& word : wordDict) {
        if (word.length() > maxWordLength) {
            maxWordLength = word.length();
        }
    }

    int textLength = text.length();
    int i = 0;

    while (i < textLength) {
        int length = std::min(maxWordLength, textLength - i);
        while (length > 0) {
            std::string sub = text.substr(i, length);
            if (wordDict.find(sub) != wordDict.end()) {
                result.push_back(sub);
                i += length;
                break;
            }
            length--;
        }

        if (length == 0) {
            length = 1;
            result.push_back(text.substr(i, length));
            i++;
        }
    }

    return result;
}

int main() {
    // 替换成你的词典文件路径
    std::string dictionaryFile = "dictionary.txt";
    std::string text = "我喜欢编程和学习";

    std::unordered_set<std::string> wordDict = loadDictionary(dictionaryFile);
    std::vector<std::string> result = bmmSegment(text, wordDict);

    for (const std::string& word : result) {
        std::cout << word << " ";
    }

    return 0;
}
