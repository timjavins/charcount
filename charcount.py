with open("input1.txt", "r") as input_file:
  # debug attempt
  # print input_file
  def wordCount(input_file):
    words = []
    for i in input_file:
      words.append(i)
    wordcount = len(words)
    return wordcount
  # debug attempt
  # print words
  def uniqueCount(input_file):
    dup_words = []
    for i in input_file:
      if i not in dup_words:
        dup_words.append(i)
    uniquecount = len(dup_words)
    return uniquecount
    # debug attempt
    # print dup_words
  def sentenceCount(input_file):
    x = 0
    import copy
    stringinput = copy.deepcopy(input_file)
    chars = str(stringinput)
    for i in chars:
      if i == "." or i == "!" or i == "?":
        x += 1
      else:
        x
    return x
    
  print "Total words:", wordCount(input_file)
  print "Unique words:", uniqueCount(input_file)
  print "Total sentences:", sentenceCount(input_file)
  
  input_file.close();

print ' '
print "Now running code from StackOverflow.com."
print ' '

# Everything below this comment came from stackoverflow.
# I only modified it with my input file name for testing purposes.
# My code won't input the file properly and I'm trying to figure out why.

import string

#
# Per-line counting functions
#
def countLines(ln):      return 1
def countBlankLines(ln): return 0 if ln.strip() else 1
def countWords(ln):      return len(ln.split())

def charCounter(validChars):
    vc = set(validChars)
    def counter(ln):
        return sum(1 for ch in ln if ch in vc)
    return counter
countSentences = charCounter('.!?')
countLetters   = charCounter(string.letters)
countPunct     = charCounter(string.punctuation)

#
# do counting
#
class FileStats(object):
    def __init__(self, countFns, labels=None):
        super(FileStats,self).__init__()
        self.fns    = countFns
        self.labels = labels if labels else [fn.__name__ for fn in countFns]
        self.reset()

    def reset(self):
        self.counts = [0]*len(self.fns)

    def doFile(self, fname):
        try:
            with open(fname) as inf:
                for line in inf:
                    for i,fn in enumerate(self.fns):
                        self.counts[i] += fn(line)
        except IOError:
            print('Could not open file {0} for reading'.format(fname))

    def __str__(self):
        return '\n'.join('{0:20} {1:>6}'.format(label, count) for label,count in zip(self.labels, self.counts))

fs = FileStats(
    (countLines, countBlankLines, countSentences, countWords, countLetters, countPunct),
    ("Lines",    "Blank Lines",   "Sentences",    "Words",    "Letters",    "Punctuation")
)
fs.doFile('input1.txt')
print(fs)
