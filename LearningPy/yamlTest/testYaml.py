import yaml


def readYamlAndPrint():
    data = yaml.load_all(open('data.yaml', "r"), Loader=yaml.FullLoader)
    for doc in data:
       for k, v in doc.items():
            print("key: ",k, "value: ", v)


readYamlAndPrint()
