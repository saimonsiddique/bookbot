def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words, words = get_num_words(text)
    num_characters = get_num_charecters(words)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n \n")
    print_num_characters(num_characters)
    print(f"--- End report ---")


def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
   words = text.split()
   return len(words), words

def get_num_charecters(words):
  char_dict = {}
  for word in words:
    word = word.lower()
    for char in word:
       if ord(char) >= 97 and ord(char) <= 122:
          if char not in char_dict:
             char_dict[char] = 1
          else:
             char_dict[char] += 1
       else:
          continue 
  
  return char_dict

def print_num_characters(characters_dict):
   sorted_char_dict = dict(sorted(characters_dict.items(), key=lambda item: item[1], reverse=True))
   for char in sorted_char_dict:
      print(f"The {char} character was found {characters_dict[char]} times")

main()
