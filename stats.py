def count_words(text):
    return len(text.split())

def count_characters(text):
    wc = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            wc[char] = wc.get(char, 0) + 1
    # print(wc)
    return wc
    
def sort_characters(characters):
    chars_list = []
    for char, count in characters.items():
        if not char.isalpha():
            continue
        chars_list.append({"char": char, "num": count})
    # Sort by count in descending order
    chars_list.sort(key=lambda x: x["num"], reverse=True)
    for item in chars_list:
        print(f"{item['char']}: {item['num']}")
    # print(chars_list)
        