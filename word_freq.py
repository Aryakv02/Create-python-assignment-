import string

def word_frequency(text):

  words = text.lower().split()
  words = [word.strip(string.punctuation) for word in words]

  word_counts = {}
  for word in words:
    if word:
      word_counts[word] = word_counts.get(word, 0) + 1

  return word_counts

if __name__ == "__main__":
  text = input("Enter a paragraph of text: ")

  word_freq = word_frequency(text)

  for word, count in word_freq.items():
    print(f"{word}: {count}")