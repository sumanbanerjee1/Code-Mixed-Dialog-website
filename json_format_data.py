import json
import sys
import re
from tqdm import tqdm


if __name__ == '__main__':

    filenames = ["code-mixed-dataset/bengali/dialog-dstc2-tst.txt",
                    "code-mixed-dataset/english/dialog-dstc2-tst.txt",
                    "code-mixed-dataset/gujarati/dialog-dstc2-tst.txt",
                    "code-mixed-dataset/hindi/dialog-dstc2-tst.txt",
                    "code-mixed-dataset/tamil/dialog-dstc2-tst.txt"
                ]
    
    json_data = {"version":"1.0","data":[]}

    for filename in filenames:
        with open(filename,"r") as fp:
            data = fp.readlines()
        title = filename.split("/")[1]
        lang_data = {"title":title,"paragraphs":[]}
        context_str = ""
        for line in tqdm(data):
            if "\t" in line and line != "\n":
                splits = line.strip().split("\t")
                speakerA = " ".join(splits[0].split(" ")[1:]).strip()
                speakerA = re.sub("<SILENCE>","[SILENCE]",speakerA)
                speakerB = splits[1].strip()
                context_str += "Speaker A: "+speakerA+"\n\nSpeaker B: "+speakerB+"\n\n"
            elif "\t" not in line and line != "\n":
                triple = " ".join(line.strip().split(" ")[1:])
                context_str += "KB Triple: "+triple+"\n\n"
            elif line == "\n":
                context_dict = {"context":context_str}
                lang_data["paragraphs"].append(context_dict)
                context_str = ""
        json_data["data"].append(lang_data)
    

    with open("code-mixed-dataset/test-v1.0.json","w+") as fp:
        json.dump(json_data,fp)




            
        

            
    

