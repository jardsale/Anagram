def char_dict(word):
    ref_chars = {}
    for char in word:
        if char.isalpha():
            ref_chars[char.lower()] = ref_chars.get(char.lower(), 0) + 1
    return ref_chars


def sub_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        result[key] = dict1.get(key,0) - dict2.get(key,0)
    return result


def read_file(filename):
    words = []
    with open(filename) as file:
        for line in file:
            words.append(line.strip().lower())
    return words


def format_string(input_str):
    output_str = ""
    for char in input_str:
        if char.isalpha():
            output_str += char.lower()
    return output_str


def valid_words(chars, curr_words):

    new_words = []
    for word2 in curr_words:
        chars_copy = chars.copy()
        valid = True
        for char in word2:
            chars_copy[char] = chars_copy.get(char, 0) - 1
            if chars_copy[char] < 0:
                valid = False
                break

        if valid:
            new_words.append(word2)
    return new_words
    

def get_anagrams(original, curr, words):
    original_dict = char_dict(original)
    curr_dict = char_dict(curr)
    if len(words)==0:
        return curr
    else:
        r = sub_dicts(original_dict, curr_dict)
        valid = valid_words(r, words)
        return [curr + " " + word for word in get_anagrams(original, valid)]
    


def get_anagrams(input_str):
    clean_str = format_string(input_str)
    original = char_dict(clean_str)

    words_master = read_file("words_alpha.txt")
    words_master = valid_words(char_dict(input_str), words_master)
    original = sub_dicts(original, char_dict("maker"))
    print(original)
    words_rem = valid_words(original, words_master)

    return words_rem

print(get_anagrams("Maker Space"))