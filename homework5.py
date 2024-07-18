immutable_var=("a",1,"b",2,"c",3)
print(immutable_var)
mutable_list=["Rolls-Royce", "Ferrari"]
mutable_list.append("Bugatti")
print(mutable_list)
immutable_var[0]=0 #значения элементов кортежа нельзя изменить, потому что кортеж не поддерживает обращение по элементам
