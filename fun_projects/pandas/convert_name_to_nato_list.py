import pandas


data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
key_val_dict = {data_frame._get_value(index,"letter"): data_frame._get_value(index,"code") for index, row in data_frame.iterrows()}

user_name = input("Enter Your Name : ")

converted = {letter.upper(): key_val_dict[letter.upper()] for letter in user_name if len(letter.strip()) != 0 }
print(converted)