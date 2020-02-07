
def pattern_count(text,pattern):
    count=0
    for letter_index in range(len(text)-len(pattern)):

        if text[letter_index:letter_index+len(pattern)]==pattern:

            count=count +1

    return count

f=open('data.txt')
inp=f.read()
t=inp.split('\n')
text=t[0]
pattern=t[1]
print(pattern_count(text, pattern))

#correct solution for all datasets in challenge