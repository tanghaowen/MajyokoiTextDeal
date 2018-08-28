import re
import json
ori_file_path = "D:\\Galgame\\魔女こいにっき\\NewSC\\text.txt"
des_file = "./desc.txt"

sentense_map = []

pattern_ori_sentense = re.compile(r"(○\d+\○)")
pattern_des_sentense = re.compile(r"(●\d+\●)")
pattern_kuohao = re.compile(r"「(.*？)」")

f =  open(ori_file_path,"r",encoding="utf-8")
lines_ori = f.readlines()
lines_des = []
f.close()

for idx,line in enumerate(lines_ori):
    re_res = pattern_ori_sentense.match(line)

    if re_res:
        if_match_sentense_start = True
        start, end = re_res.span()
        new_line_ori_without_dot = line[end:]
        lines_des.append(new_line_ori_without_dot)
        sentense_map.append([idx, len(lines_des) - 1])
        """

        next_idx = idx+1
        next_line = lines_ori[next_idx]

        re_res = pattern_des_sentense.match(next_line)

        start,end = re_res.span()
        new_line_des_without_dot = next_line[end:]

        if "「" in new_line_des_without_dot:
            new_line_des_without_dot = "「」\n"
            



            lines_des.append(new_line_des_without_dot)
            

"""
f = open(des_file,"w",encoding="utf-8")
f.writelines(lines_des)
f.close()

f = open("sentense_map.txt","w")
json.dump(fp=f,obj=sentense_map)
f.close()