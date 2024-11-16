  import re
  import collections
  import json
  import os
  import random

  # clean and process lines of the novel
  def resubstitutions(line):
      # remove unnecessary characters
      line = line.strip()

      # skip if the line is empty
      if len(line) < 1:
          return None

      # replace "Mr.", "Mrs.", and "St." to avoid sentence break signals
      line = re.sub(r"Mr\.", "Mr", line)
      line = re.sub(r"Mrs\.", "Mrs", line)
      line = re.sub(r"St\.", "St", line)

      # remove underscores
      line = re.sub(r"[_]", "", line)

      # replace punctuation with a space preceding them
      punctuation = r'\.\,\:\;\!\?\"\”'
      line = re.sub(r'([' + punctuation + r'])', r' \1', line)

      # replace opening quotes with space after them
      line = re.sub(r'[“]', r' ', line)

      return line

  # main code execution
  novel_file = 'tale_of_2_cities.txt'  # change for different novels (see all text files, there are 6 options)

  # check if the file exists
  if not os.path.isfile(novel_file):
      print(f"File '{novel_file}' not found.")
      exit()

  print(f"Processing file: {novel_file}")

  # create trigram model
  trigrams = collections.defaultdict(lambda: collections.defaultdict(list))

  # process file line by line
  with open(novel_file, 'r', encoding='utf-8') as file:
      for line_number, line in enumerate(file, 1):
          line = resubstitutions(line)

          # skip if the line is empty after processing
          if not line:
              continue

          # split line by spaces into words
          words = line.split()

          # iterate through words to build trigram dictionary
          # need to start at index 2 because a trigram only happens when there are two words before it
          for i in range(2, len(words)):
              w1 = words[i - 2]
              w2 = words[i - 1]
              w3 = words[i]

              # only include words that start with alphabetic characters
              if w1.isalpha() and w2.isalpha() and w3.isalpha():
                  trigrams[w1][w2].append(w3)

          # print progress for every 100 lines
          if line_number % 100 == 0:
              print(f"Processed {line_number} lines")

  # used to check when to break loop
  end_sent_punc = {'.', '!', '?'}

  # only continue if there are words in the trigram dictionary

  if trigrams:
      print("\nGenerated Text:\n")

      # randomly select initial words
      while True:
          word1 = random.choice(list(trigrams.keys()))
          word2 = random.choice(list(trigrams[word1].keys()))
          word3 = random.choice(trigrams[word1][word2])
          if word3 not in end_sent_punc:
              break

      print(word1, word2, word3, end=' ')

      word1 = word2
      word2 = word3

      # generating text
      while True:
          # getting word3
          possible_words = trigrams[word1][word2]
          if possible_words:
              word3 = random.choice(possible_words)
          else:
              # backtrack to different trigram
              if trigrams[word2]:
                   word3 = random.choice(list(trigrams[word2].keys()))
              else:
                  break

          # stop if the next word is an end-of-sentence punctuation
          if word3 in end_sent_punc:
              break

          # print the next word
          print(word3, end=' ')

          # move to the next trigram
          word1 = word2
          word2 = word3

      print()
