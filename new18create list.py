change_list=[1,2,3,4,5,"hello","job",True,False,None,[1,2,3,4,5,6,7,8,9,10]]
print(change_list)
change_list[0]="change1"
print(change_list)
change_list[-1]="change_last"
print(change_list)
change_list[0:3]=["hello"]
print(change_list)
change_list.insert(4,"bobby")
print(change_list)
change_list.append("appended")
print(change_list)