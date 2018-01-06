def greedyapproach(list_word,length):
    newword_list = []

    for i in list_word:
        s = len(i)
        if len(newword_list) == 0:
            if s <= length:
                newword_list.append(i)
        else:
            if len(newword_list[(len(newword_list)-1)])+1+s <= length:
                newword_list[(len(newword_list)-1)] += " "
                newword_list[(len(newword_list) - 1)] += i
            else:
                newword_list.append(i)

    return newword_list



print("Eneter The Length to Wrap:")
length = int(input())

file1 = open("plaintext.txt","r")
file1_data = file1.read()
data_len = len(file1_data)

split_data = file1_data.split(" ")

print("No Of Word=",len(split_data))

final_data = greedyapproach(split_data,length)

#find the cost
sum = 0
for i in final_data:
    sum = sum + pow((length-len(i)),2)

#write the data into file
file2 = open("wraptext.txt","wt")
for i in final_data:
    print(i)
    file2.write(i+'\n')

print("Total Cost=",sum)