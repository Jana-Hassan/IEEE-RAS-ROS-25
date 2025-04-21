
def word_counter():
    file = input("Enter File Name: ")
    
    try:
        f = open(file, "r")
        words = []
        
        for l in f:
            l = l.strip()
            l = l.lower()
            line = l.split(" ")
            
            for w in line:
                if w:
                    words.append(w)
    
        f.close()
        
        w_counter = {}
        for w in set(words):
            w_counter[w] = words.count(w)
        
        if w_counter:
            for word, count in w_counter.items():
                print(f"{word}: {count}")
        else:
            print("File is empty!")
    
    except FileNotFoundError:
        print(f"{file} not found!")
    


word_counter()





