import collections
import section4_30 as sec30


def word_appearance_frequency(file_r: str):
    file_w = "output36"
    sentence_list = sec30.sentence_mapping_list(file_r)
    noun_list = []
    frequency_list = []
    with open(file_w, mode="w") as f_w:
        for line in sentence_list:
            for mapping in line:
                noun_list.append(mapping["surface"])
        noun_counter = collections.Counter(noun_list)
        noun_list_sorted = noun_counter.most_common()
        for noun in noun_list_sorted:
            output = "{0} : {1}".format(noun[0], noun[1])
            f_w.write(output + "\n")
            frequency_list.append(noun)
    return frequency_list


if __name__ == "__main__":
    file_r = "neko.txt.mecab"
    word_appearance_frequency(file_r)
