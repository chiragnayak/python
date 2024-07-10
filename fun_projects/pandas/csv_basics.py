import csv
import pandas

with open("nato_phonetic_alphabet.csv", "r") as nato_file:
    data = csv.reader(nato_file)
    for row in data:
        print(row)

# no need to have file_object, directly pass the file name to panda library
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data_frame)

print(data_frame["letter"])
print(data_frame["code"])

data_frame_dict = pandas.DataFrame.to_dict(data_frame)
print(data_frame_dict)

key_val_dict = {row[1].letter:row[1].code for row in data_frame.iterrows()}
print(key_val_dict)