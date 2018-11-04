from funcionario import *

g = Gerente("Hermano",1500)
p = Presidente("Steve Jobs",5000)
d = Diretor("Trump",2000)


for obj in [g,p,d]:
    obj.addBonificacao()
    print(obj,"\n")

