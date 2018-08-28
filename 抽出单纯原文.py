file = "./desc.txt"
f = open(file,"r",encoding="utf-8")
lines = f.readlines()
f.close()
new_lines = []
for idx,line in enumerate(lines):
    if (idx) % 2 ==1:
        new_lines.append(line)

f = open("papaa.txt","w",encoding="utf-8")
f.writelines(new_lines)
f.close()
