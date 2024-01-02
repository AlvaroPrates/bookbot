file_path = "books/frankenstein.txt"

with open(file_path) as f:
  file_contents = f.read()
  letters = {}

  for char in file_contents:
    if char.isalpha():
      letters[char.lower()] = letters.get(char, 0) + 1
  
  print(f"--- Begin report of {file_path} ---")
  print("")

  letters_list = list(letters.items())

  for letter in letters_list:
    print(f"The '{letter[0]}' was found {letter[1]} times")

  print("")
  print("--- End report ---")