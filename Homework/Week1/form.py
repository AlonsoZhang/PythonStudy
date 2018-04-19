# Author:Alonso Zhang


def menu():
    print('''菜单列表：
        1-->S:返回上一级
        2-->M:返回首页菜单
        3-->查找下一级行政单位请输入名称
        4-->Q:退出系统''')


def province_one():
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    provice = []
    for line in readlines:
        line = line.strip('\n')
        provice.append(line.split('\t')[0])
    province = sorted(set(provice), key=provice.index)
    row = 1
    print('省级菜单：')
    for data in province:
        print('  ', row, data)
        row += 1
    menu()
    promit = input("请选择操作:")
    if promit == 'S':
        main()
    elif promit == 'Q':
        print("系统退出！")
    else:
        city(promit)


def city(provincename):
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    city2 = []
    for line in readlines:
        line = line.strip('\n')
        if line.split('\t')[0] == provincename:
            city2.append(line.split('\t')[1])
    city2 = sorted(set(city2), key=city2.index)
    row = 1
    print('市级菜单：')
    for data in city2:
        print('  ', row, data)
        row += 1
    menu()
    promit1 = input("请选择操作:")
    if promit1 == 'S':
        province_one()
    elif promit1 == 'Q':
        print("系统退出！")
    else:
        area(provincename, promit1)


def area(provincename, cityname):
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    area1 = []
    for line in readlines:
        line = line.strip('\n')
        if line.split('\t')[0] == provincename and line.split('\t')[1] == cityname:
            area1.append(line.split('\t')[2])
        area1 = sorted(set(area1), key=area1.index)
    row = 1
    print('区级菜单：')
    for data in area1:
        print('  ', row, data)
        row += 1
    menu()
    promit2 = input("请选择操作:")
    if promit2 == 'S':
        city(provincename)
    elif promit2 == 'Q':
        print("系统退出！")
    else:
        print('输入无效!')


def main():
    menu()
    runever = True
    while runever:
        promit3 = input("请选择操作(A:查找所有省份,Q:退出系统")
        if promit3 == 'A':
            province_one()
        elif promit3 == 'Q':
            print("系统退出！")
            runever = False
        else:
            print('请输入有效信息：')


print(__name__)

if __name__ == "__main__":
    main()
