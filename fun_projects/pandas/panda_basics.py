column_wise_data = {
    "column_1" : ["Indore", "Jabalpur", "Allahabad"],
    "column_2" : [100, 200, 300]
}

# iterate as normal dictionary
for key, values in column_wise_data.items():
    print(key, values)

import pandas

print("create frame from dictionary and print the frame")
panda_frame = pandas.DataFrame(column_wise_data)
print(panda_frame)

print("print each row from panda frame using iterrows()")
for row_index, row in panda_frame.iterrows():
    print(row)