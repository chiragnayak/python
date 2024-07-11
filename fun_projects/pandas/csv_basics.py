import csv
import pandas

with open("nato_phonetic_alphabet.csv", "r") as nato_file:
    data = csv.reader(nato_file)
    for row in data:
        print(row)

# no need to have file_object, directly pass the file name to panda library
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data_frame)

# print column letter
print(data_frame["letter"])

# print column code
print(data_frame["code"])

# convert to dict (comes with index like below)
"""
{'letter': {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}, 
'code': {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot', 6: 'Golf', 7: 'Hotel', 8: 'India', 9: 'Juliet', 10: 'Kilo', 11: 'Lima', 12: 'Mike', 13: 'November', 14: 'Oscar', 15: 'Papa', 16: 'Quebec', 17: 'Romeo', 18: 'Sierra', 19: 'Tango', 20: 'Uniform', 21: 'Victor', 22: 'Whiskey', 23: 'X-ray', 24: 'Yankee', 25: 'Zulu'}}
"""
data_frame_dict = pandas.DataFrame.to_dict(data_frame)
print(data_frame_dict)

# extract a usable dictionary method # 1
key_val_dict = {row[1].letter:row[1].code for row in data_frame.iterrows()}
print(key_val_dict)

# extract a usable dictionary method # 2
key_val_dict_2 = {data_frame._get_value(index,"letter"): data_frame._get_value(index,"code") for index, row in data_frame.iterrows()}
print(key_val_dict_2)