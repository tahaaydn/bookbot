def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_letter_count(text)
    # print(f"{num_words} words found in the document")
    char_count_list = [{'character': key, 'count': value} for key, value in char_count.items()]
    char_count_list.sort(key=lambda x: x['count'], reverse=True)
    print_report(char_count, char_count_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    _temp = {}
    low_text = text.lower()
    for t in low_text:
        if t in _temp:
            _temp[t] += 1
        else:
            _temp[t] = 1
    return _temp

def print_report(char_count, char_count_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(char_count.values())} words found in the document")
    # print(char_count)
    # print(char_count_list)
    for i in char_count_list:
        if i['character'].isalpha():
            print(f"The '{i['character']}' character was found {i['count']} times")
    print("--- End report ---")

main()