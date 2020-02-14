from pattern_count import pattern_count

def most_frequent(text,k):
    hist={}
    for i in range(len(text)-k):
        pattern=text[i:i+k]
        count=pattern_count(text,pattern)
        hist[pattern]=count

    maximum=max(hist.values())

    for key in hist:
        if hist[key]==maximum:
            print(key)
    
    


if __name__=="__main__":
    f=open('data_frequent.txt')
    inp=f.read()
    t=inp.split('\n')
    text=t[0]
    print(text)
    
    k=t[1]
    print(k)
    most_frequent(text,int(k))
