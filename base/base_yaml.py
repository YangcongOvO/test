import yaml

def yaml_reader(file_name):
    with open("data/" + file_name + ".yaml", "r", encoding='utf-8') as f:
        return yaml.safe_load(f)

def txt_written(list, file_name):
    with open(file_name + ".txt", "a", encoding="utf-8") as f:
        f.write(list)
        f.write("\n")

def txt_over_written(list, file_name):
    with open(file_name + ".txt", "w", encoding="utf-8") as f:
        f.write(list)
        f.write("\n")