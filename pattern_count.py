#statements starting with # are comments and  will not be executed, included by programmer to convey how code works to the reader

#defining a function that takes total text and pattern to be searched as inputs and returns the number of occurences of pattern in text
#len function gives the length of a string

#text[i:i+len(pattern)] selects part of text starting with the letter 
# in i th index upto but not including (i+length of pattern) index,
# strings are indexed from 0 onwards, so if pattern is three letters in total, at the first run of for loop(just repeats the code written after for statement len(text)-len(pattern) times) , #the above code selects 0th, 1st and 2nd letters of text

def pattern_count(text,pattern):
    count=0
    for letter_index in range(len(text)-len(pattern)):

        if text[letter_index:letter_index+len(pattern)]==pattern:

            count=count +1

    return count

if __name__ == "__main__":
    print(pattern_count('CGATATATCCATAG', 'ATA'))

#output obtained 3 same as in example