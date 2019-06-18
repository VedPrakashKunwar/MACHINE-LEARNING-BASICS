# convert binary into decimal
print(int('100', 2))

def binary_add(b, c):
    return bin(int(b, 2) + int(c, 2))[2:]

# Start both at 0
a = 0
b = "0"

# Loop 10 times
for i in range(0, 10):
    # Add 1 to each
    a += 1
    b = binary_add(b, "1")

    # Check if they are equal
    print(int(b, 2) == a)
    
# comverting word into binary
asci_a = ord('a')
bin_a =  bin(asci_a)[2:]

binary_w = bin(ord('w'))
binary_bracket = bin(ord('}'))
    
'''
ASCII can't handle them, because it only supports 255 characters. The tech community realized it needed a new standard, and created Unicode.

Unicode assigns "code points" to characters. In Python, code points look like this:
    "\u3232"

We can use an encoding system to convert these code points to binary integers. The most common encoding system for Unicode is UTF-8. This encoding tells a computer which code points are associated with which integers.

UTF-8 can encode values that are longer that one byte, which enables it to store all Unicode characters. It encodes characters using a variable number of bytes, which means that it also supports regular ASCII characters (which are one byte each).
'''

code_point = "⟶"

# This particular code point maps to a right arrow character.
print(code_point)

# We can get the base 10 integer value of the code point with the ord function.
print(ord(code_point))

# As you can see, this takes up a lot more than 1 byte.
print(bin(ord(code_point)))

# unicode to binary
uni = '\u1019'
print(uni)
asci_uni = ord(uni)
print(asci_uni)
binary_1019 = bin(asci_uni)


s1 = "café"
# The \u prefix means "the next four digits are a Unicode code point"
# It doesn't change the value at all (the last character in the string below is \u00e9)
s2 = "caf\u00e9"

# These strings are the same, because code points are equal to their corresponding Unicode characters.
# \u00e9 and é are equivalent.
print(s1 == s2)

'''
Python includes a data type called "bytes." It's similar to a string, except that it contains encoded bytes values.

When we create an object with a bytes type from a string, we specify an encoding system (usually UTF-8).

Then, we can use the .encode() method to encode the string into bytes.
'''
# We can make a string with some Unicode values
superman = "Clark Kent␦"
print(superman)

# This tells Python to encode the string superman as Unicode using the UTF-8 encoding system
# We end up with a sequence of bytes instead of a string
superman_bytes = "Clark Kent␦".encode("utf-8")
print(superman_bytes)
#  Similar to the \u prefix for a Unicode code point, \x is the prefix for a hexadecimal character.
# The three sections of this result (which the \ character separates) represent three hexadecimal bytes. The \x prefix means "the next two digits are in hexadecimal."

# F is the highest single digit in hexadecimal (base 16)
# Its value is 15 in base 10
print(int("F", 16))

# A in base 16 has the value 10 in base 10
print(int("A", 16))

# Just like the earlier binary_add function, this adds two hexadecimal numbers
def hexadecimal_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

# When we add 1 to 9 in hexadecimal, it becomes "a"
value = "9"
value = hexadecimal_add(value, "1")
print(value)

hex_ea = hexadecimal_add('2', 'ea')
hex_ef = hexadecimal_add('e', 'f')


# One byte (eight bits) in hexadecimal (the value of the byte below is \xe2)
hex_byte = "â"

# Print the base 10 integer value for the hexadecimal byte
print(ord(hex_byte))

# This gives the exact same value. Remember that \x is just a prefix, and doesn't affect the value.
print(int("e2", 16))

# Convert the base 10 integer to binary
print(bin(ord("â")))





batman = "Bruce Wayne␦"
batman_bytes = batman.encode('utf-8')
print(batman_bytes)
binary_aa = bin(ord('\xaa'))
binary_ab = bin(ord('\xab'))

'''
There's no encoding system associated with the bytes data type. That means if we have an object with that data type, Python won't know how to display the (encoded) code points in it. For this reason, we can't mix bytes objects and strings together.
'''
hulk_bytes = "Bruce Banner␦".encode("utf-8")

# We can't mix strings and bytes
# For instance, if we try to replace the Unicode ␦ character as a string, it won't work, because that value has been encoded to bytes
try:
    hulk_bytes.replace("Banner", "")
except Exception:
    print("TypeError with replacement")

# We can create objects of the bytes data type by putting a b in front of the quotation marks in a string
hulk_bytes = b"Bruce Banner"
# Now, instead of mixing strings and bytes, we can use the replace method with bytes objects instead
hulk_bytes.replace(b"Banner", b"")
thor_bytes = b"Thor"


# Make a bytes object with aquaman's secret identity
aquaman_bytes = b"Who knows?"

# Now, we can use the decode method, along with the encoding system (UTF-8) to turn it into a string
aquaman = aquaman_bytes.decode("utf-8")

# We can print the value and type to verify that it's a string
print(aquaman)
print(type(aquaman))

morgan_freeman_bytes = b"Morgan Freeman"
morgan_freeman = morgan_freeman_bytes.decode("utf-8")
# =============================================================================
# 
# We can read our data in using csvreader
# =============================================================================
import csv
import pandas as pd
# trying to open with pandas
df_cia = pd.read_csv("D:/Study/Dataquest/Data sets/sentences_cia.csv", encoding='utf-8')
# When we open a file, we can specify the system used to encode it (in this case, UTF-8).
f = open("D:/Study/Dataquest/Data sets/sentences_cia.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
sentences_cia = list(csvreader)


# The data consists of two columns
# The first column contains the year, and the second contains a sentence from a CIA report written in that year
# Print the first column of the second row
print(sentences_cia[1][0])

# Print the second column of the second row
print(sentences_cia[1][1])
sentences_ten = sentences_cia[1:10][1]
sentences_cia = pd.DataFrame(sentences_cia[1:], columns=sentences_cia[0])


f = open("D:/Study/Dataquest/Data sets/legislators.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
legislators = list(csvreader)

# Now, we can import pandas and use the DataFrame class to convert the list of lists to a dataframe.
#import pandas as pd

legislators_df = pd.DataFrame(legislators)

# As you can see, the first row contains the headers, which we don't want (because they're not actually data)
print(legislators_df.iloc[0,:])

# To remove the headers, we'll subset the df and pass them in separately
# This code removes the headers from legislators, and instead passes them into the columns argument
# The columns argument specifies column names
legislators_df = pd.DataFrame(legislators[1:], columns=legislators[0])
# We now have the right data in the first row, as well as the proper headers
print(legislators_df.iloc[0,:])

# The integer codes for all the characters we want to keep
good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]

sentence_15 = sentences_cia["statement"][14]

# Iterate over the characters in the sentence, and only take those whose integer representations are in good_characters
# This will construct a list of single characters
cleaned_sentence_15_list = [s for s in sentence_15 if ord(s) in good_characters]

# Join the list together, separated by "" (no space), which creates a string again
cleaned_sentence_15 = "".join(cleaned_sentence_15_list)

def clean(sent):
    import re
    return re.sub('[^0-9a-zA-Z\s]+', '', sent)

clean_sent_15 = clean(sentence_15)
print(clean_sent_15==cleaned_sentence_15)

sentences_cia['clean_statement'] = sentences_cia['statement'].apply(clean)

# We can use the .join() method on strings to join lists together.
# The string we use the method on will become the separator -- the character(s) between each string when they are joined..
combined_statements = " ".join(sentences_cia["clean_statement"])
statement_tokens = combined_statements.split(" ")



'''
We want to count how many times each term occurs in our data, so we can find the most common items.

The problem is that the most common words in the English language are ones that are relatively uninteresting to us right now -- words like "the", "a", and so on. These words are called stopwords - words that don't add much information to our analysis.

It's common to filter out any words on a list of known stopwords. What we'll do here for the sake of simplicity is filter out any words less than five characters long. This should remove most stopwords.
'''
filtered_tokens = [s for s in statement_tokens if len(s)>4]

from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)
print(fruit_count)

filtered_token_counts = Counter(filtered_tokens)

# most common item in counter
print(fruit_count.most_common(2))
print(fruit_count.most_common(3))

common_tokens = filtered_token_counts.most_common(3)

# Let's write a function that computes the most common terms by year.

def common_term(yr):
    stat = sentences_cia.loc[sentences_cia['year']==yr, 'statement']
    stat_clean = [clean(s) for s in stat]
    stat_combine = ' '.join(stat_clean)
    stat_token = stat_combine.split(' ')
    stat_token = [s for s in stat_token if len(s)>4]
    stat_token_count = Counter(stat_token)
    return stat_token_count.most_common(3)


common_2000 = common_term('2000')
common_2013 = common_term('2013')














