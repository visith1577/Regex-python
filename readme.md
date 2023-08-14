# Regex Matcher

### SCS2201 | Assignment 1 - String Matching 

**Name: K.A.V.C Kumarapperuma**\
**Index no. : 21001057**

This project was made with reference to SE III assignment.\
The Knuth Morris Pratt algorithm has been used for matching patterns corresponding 
to the regex symbols '|', '$', and '^' . \
more info on [why KMP?](why_kmp.txt)\
matcher can be accessed via terminal or importing from file.

## Requirements

Python 3.7+ \
Pytest = For unit testing

```bash
pip install -r requirements.txt
```

## Use from terminal

after running main file follow the instructions

```bash
python main.py
```

## Usage
clone the repository and place the files in your project
```python
import pattern_matcher, readfile

text = 'text'
words = 'text word abc'
pattern = '^a|t$'

# input: single word (text)
# returns: true
pattern_matcher.matcher(text, pattern)

# input: string of words (words)
# returns [True, False, True]
pattern_matcher.matcher_iter(words, pattern)

# input: file containing string of words
# output: writes to .output file the boolean values of pattern match
readfile.write_output_to_file('in_path', 'out_path', pattern)
```

## Running test cases

**Pytest** is used to efficiently write test cases.\
```bash
python pattern_matcher_test.py
```
```bash
python matcher_iter_test.py
```
total of 18 test cases covers all possible scenarios

### _File structure_
[KMP algorithm](kmp_algorithm.py)\
[logic specific to regex](reg_cmds.py)\
[Functions to assist in regex](helper.py)\
[Matcher algorithm](pattern_matcher.py)\
[Matcher algorithm modified for files](readfile.py)