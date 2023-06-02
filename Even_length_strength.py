Question13-Python program to print even length words in a string

def print_even_length_words(string):
    
    words = string.split()

    
    for word in words:
        if len(word) % 2 == 0:
            print(word)


sentence = "Python is a great language for programming"

print("Even-length words in the string:")
print_even_length_words(sentence)

output:
Even-length words in the string:
Python
is
great
language
for
