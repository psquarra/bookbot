def main():
    frankenstein_path = "books/frankenstein.txt"
    book_content = read_book_content(frankenstein_path)
    #print(book_content)
    #print(word_count(book_content))
    #print(count_letters(book_content))
    print_report(frankenstein_path, count_letters(book_content))
        
def read_book_content(path):
    with open(path) as book:
        return book.read()

def word_count(text):
    return len(text.split())

def count_letters(text):
    lowercase_text = text.lower()
    letters = {}
    for letter in lowercase_text:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    return letters

def print_report(path, occurence_dict):
    print(f'--- Begin report of {path} ---')
    print(f'{word_count(read_book_content(path))} words found in the document')
    print("")
    occurence_list = list( occurence_dict.items())
    only_letters_occurrence_list = [dict for dict in occurence_list if next(iter(dict)).isalpha() == True]
    only_letters_occurrence_list.sort(key= lambda x:x[1], reverse=True)
    for letter in only_letters_occurrence_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")
    
      
main()