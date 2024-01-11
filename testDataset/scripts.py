a = ""
for i in range(1,29):
    a += "./Image_1/" + str(i) +".jpg\n"
with open("train.txt","a") as file:
    file.write(a)