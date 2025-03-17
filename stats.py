
def count_words_in_book(book: str) -> str:
    return "Found " +  str(len(book.split())) +  " total words"

def count_char_from_string(book: str) -> dict:
    stat = {}
    for char in book:
        char = char.lower()
        if stat.get(char):
            stat[char] += 1
        else:
            stat[char] = 1
    return gen_list_from_dict(stat)
def sort_on(tup):

    return tup["count"]

def get_sorted_list(char_dict: list) -> list:
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict
    

def gen_list_from_dict(char_count_list: dict):
    count_list = list()
    for i in char_count_list.items():
        count_list.append({"char": i[0], "count": i[1] })
    return get_sorted_list(count_list)
