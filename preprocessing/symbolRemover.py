INPUT = "corpus/fa.txt"
OUTPUT = "corpus/fa-new.txt"

with open(OUTPUT, 'w', encoding='utf8') as o:
    with open(INPUT, 'r', encoding='utf8') as f:
        line = f.readline()
        while line:
            t = ""
            for i in line:
                if i not in '-,؟.!?':
                    t = t + i
            o.write(t)
            line = f.readline()
