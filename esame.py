class ExamException(Exception):
    pass


class Diff:
    def __init__(self,ratio=1):
        self.ratio = ratio
        #####################
        if type(ratio) == str:
            raise ExamException("Ratio è una stringa")
        
        if type(ratio) != int and type(ratio) != float:
            raise ExamException("la ratio non è un intero o un float")

        if ratio == 0 :
            raise ExamException("ratio è = 0 ")

        if ratio == None:
            raise ExamException("ratio nullo")
        ########################

    def compute(self,lista):
        ########################
        if type(lista) != list:
            raise ExamException("lista non è una lista")
        
        for i in lista:
            if type(i) == str:
                raise ExamException("gli elementi della lista devono essere tutti numeri")

        if lista == []:
            raise ExamException("lista vuota")

        if len(lista) == 1:
            raise ExamException("non si puo fare la differenza per 1")
        

        


        ###########################

        ris = []
        for i in range(len(lista)-1):
            a = lista[i+1]-lista[i]
            a = a/self.ratio
            ris.append(a)
        return ris

#diff = Diff(-1)
#result = diff.compute([2,4,8,16])
#print(result)