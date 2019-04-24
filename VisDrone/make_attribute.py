import pandas as pd
import os


if __name__ == '__main__':
    xlsx_path = 'E:/visdrone/2019/data/visdrone2019_sot/attribute.xlsx'
    attr_path = "E:/visdrone/2019/data/visdrone2019_sot/attributes"
    data = pd.read_excel(xlsx_path)
    attrs = data.values
    # data = pd.DataFrame(data)
    print(attrs[0])
    for attr in attrs:
        attr_name = attr[0] + '_attr.txt'
        attr_file = os.path.join(attr_path, attr_name)
        print(attr_file)
        line = "," .join([str(i) for i in attr[1:]])
        line = line + '\n'
        # print(line)
        with open(attr_file, 'w', newline='\n') as w:
            w.writelines(line)
