import random 

def shuffleWord(wrd):
  pw = random.sample(wrd, k=len(wrd))
  return "".join(pw)

def PuzzleWord(word,score):
  problemWord = shuffleWord(word)
  print('Arrange The letters to form a valid word:')
  print(problemWord)
  user = input()
  if user.upper() == word:
    print('Correct\n')
    score+=1
  else:
    print('Wrong')
    score-=1

  return score

def main():
  score = 0
  wordsss = ['FATHER','UMBRELLA','COUNTRY']
  words = random.sample(wordsss,k=len(wordsss))
  for word in words:
    score=PuzzleWord(word,score)
  print('Your Score is:',score)
  print()

main()
  