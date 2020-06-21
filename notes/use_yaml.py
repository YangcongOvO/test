import yaml


'''
存在yaml中的数据
字典：key: "value"
列表：- element
字符："example"
布尔值：True
整数：123
日期：2020-02-02 20:02:02.000
'''


def write_yaml():
    yaml_data = {"search_data":{"test01":[233]}}
    with open("path_of_yaml.yaml", "w") as f:
        yaml.dump(yaml_data, f, encoding='utf-8', allow_unicode=True)


def read_yaml():
    with open("path_of_yaml.yaml", "w") as f:
        yaml_data = yaml.load(f)
        print(yaml_data)