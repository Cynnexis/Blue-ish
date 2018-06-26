# -*- coding: utf-8 -*-
import random
from time import time
import argparse

vowels: tuple = ('a', 'e', 'i', 'o', 'u', 'y')
consonants: tuple = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

greek: tuple = ("alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu",
                "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "psi", "omega")

random.seed(time())

parser = argparse.ArgumentParser(description="Blue-ish is a name generator for project.")
parser.add_argument("length", metavar='L', type=int, help="the length of the word to generate")
parser.add_argument("--number", dest="number", metavar='N', nargs='?', default=1, type=int, help="the number word(s) to generate (default: 1)")

args = parser.parse_args()

for iter_word in range(0, args.number):
	word: str = ""
	
	# 'vowelPart' tell if the program must add a vowel or a consonant character
	vowelPart: bool = bool(random.getrandbits(1))
	
	# There is a chance to add a greek word at the beginning
	greek_word = ""
	tried_words = []
	if random.randint(1, 100) >= 80:
		# Search a greek word such that len(greek_word) + 4 < args.length
		while len(tried_words) < len(greek):
			# Construct list of available greek word
			available_words = [x for x in greek if x not in tried_words]
			
			# Take randomly a word
			g = available_words[random.randint(0, len(available_words) - 1)]
			if len(g) + 4 < args.length:
				greek_word = g
				break
			
			# If it does not fit, add it to the 'tried_words'
			tried_words.append(g)
		
		# If no greek word has been found, continue anyway. Otherwise, add it to the word with '-'
		if greek_word != "":
			word = greek_word + '-'
	
	i = len(word)
	while i < args.length:
		# half vowel, half consonant
		word += vowels[random.randint(0, len(vowels) - 1)] if vowelPart else consonants[random.randint(0, len(vowels) - 1)]
		
		# Adding letter according to grammar
		
		# If the last character of 'word' is 'q' OR if the last character of 'word' is 'g' and there is luck, then add a 'u'
		if (word[-1:] == 'q' or word[-1:] == 'g' and random.randint(1, 100) >= 60) and i + 1 < args.length:
			word += 'u'
			i += 1
		# If the last character of 'word' is either 'aeiou' and there is luck, then add an n
		elif word[-1:] in vowels[:-1] and random.randint(1, 100) >= 60 and i + 1 < args.length:
			word += 'n'
			i += 1
		
		# Switching
		vowelPart = not vowelPart
		
		i += 1
	
	# Now that the word is generated, check the grammar rules
	i = 1
	while i < len(word):
		# If found 'm', 'b' or 'p', and the previous letter was 'n', then replace this character by 'm' (grammar rule:
		# always put 'm' forward another 'm', 'b' or 'p').
		if (word[i] == 'm' or word[i] == 'b' or word[i] == 'p') and i > 1:
			if word[i - 1] == 'n':
				w = list(word)
				w[i - 1] = 'm'
				word = "".join(w)
		
		i += 1
	
	print(word)
