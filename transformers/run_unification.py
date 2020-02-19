import numpy
import os
import pickle as pkl
import random
import math
from tqdm import tqdm

path_to_java_corpus = "/mnt/media/Corpora/extern/Github_Java_Corpus/java_projects"
path_to_output = "/mnt/media/Corpora/extern/Github_Java_Corpus/transformers/unified_corpus/"

separator = "<|endoftext|>"
file_ending = ".java"
split = [.8, .085, .115]



def export_unified_file(file_list, file_name):
    export_file = open(os.path.join(path_to_output, file_name), "a")
    success = 0
    error = 0
    error_files = []
    for file_path in tqdm(file_list):
        try:
            with open(file_path, "r", encoding="utf8") as f:
                text = f.read()
            export_file.write(text + "\n")
            export_file.write(separator + "\n")
            success += 1
        except (UnicodeDecodeError, FileNotFoundError) as e:
            error += 1
            error_files.append(file_path)
    export_file.close()
    with open(os.path.join(path_to_output, file_name + ".details"), "w") as f:
        text = "success = %d\n" % success
        text += "errors = %d\n" % error
        text += "failed files:\n"
        for e in error_files:
            text += "%s\n" % e
        f.write(text)

def main():
    ## load the filelist from the file
    with open("file_list.pkl", "rb") as f:
        file_list = pkl.load(f)

    random.shuffle(file_list)

    training_size = math.floor(len(file_list) * split[0])
    validation_size = math.floor(len(file_list) * split[1])
    test_size = math.floor(len(file_list) * split[2])
    training_files = file_list[:training_size]
    validation_files = file_list[training_size:training_size+validation_size]
    test_files = file_list[training_size+validation_size:]
    export_unified_file(training_files, "github_java.train.raw")
    export_unified_file(validation_files, "github_java.valid.raw")
    export_unified_file(test_files, "github_java.test.raw")

if __name__ == "__main__":
    main()
