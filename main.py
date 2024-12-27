def counts_words(text):    
    words = text.split()
    return len(words)

#Now redundant lines of code
#        print()
#        word_count = counts_words(file_contents)
#        if word_count == 1:
#            print("This book contains one word!") 
#        elif word_count > 1:
#            print(f"This book contains {word_count} words!")
#        else:
#            print("This is empty")
#        print()
#        count_fin = character_count(file_contents)
#        print(count_fin)


def character_count(text):
    count = {}
    for c in text:
        if c.isalpha():  
            truecount = c.lower()
            if truecount in count:
                count[truecount] += 1
            else:
                count[truecount] = 1
    return count

def sort_on(dict):
    return dict["count"]

def report(text):
    char_count = character_count(text)
    word_count = counts_words(text)

    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count":count})
    
    char_list.sort(reverse=True, key=sort_on)
    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    print()    
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print()
        report(file_contents)
main()