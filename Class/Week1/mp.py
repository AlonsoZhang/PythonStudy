# Author:Alonso Zhang

class mate():
    def __init__(self,list1,list2):
        '''
        :param list1:
        :param list2:
        '''
        self.lst1 = list1
        self.lst2 = list2
    def sort(self,cnt):
        print(self.lst1)
        print(self.lst2)
        for i in self.lst2:
            print(i * cnt)
        for j in self.lst1:
            print(j * cnt)

if __name__ == "__main__":
    list1 = range(1,2000)
    list2 = range(1,2000)
    st=mate(list1,list2)
    st.sort(2)