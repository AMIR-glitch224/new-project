n = int(input("Enter the number of matrices:"))
i = 1
t1 = []
t2 = []
row_column = []
flag = False
key = input("Would you like me to add or multiply?")
while True:
    while i <= n :
        row = int(input("Enter the number of rows:"))
        column = int(input("Enter the number of columns:"))
        row_column.append(row) 
        row_column.append(column) 
        if flag == True and key == "add" :
            if row_column[0] == row_column[2] and row_column[1] == row_column[3] :
                pass
            else :
                flag1 = 0
                print("Matrix addition is not possible")
                break    
        if flag == True and key == "multiply" :   
            if row_column[1] == row_column[2] :
                pass
            else :
                print("Matrix multiplication is not possible")
                flag1 = 0
                break
        while True :
            number = input("Enter the numbers:")
            if len(number.split(" ")) == row * column :
                i2 = 0
                index1 = 0
                index2 = column
                while i2 < row :
                    x = number.split(" ")[index1:index2]
                    if i == 1 :
                        t1.append(x)
                    else :
                        t2.append(x)
                    index1 = index2
                    index2 += column
                    i2 += 1
                break
            else:
                print("try again")
        if i >= 2 :
            while True : 
                t3 = []
                if key == "multiply" : 
                    row1 = row_column[0]
                    column1 = row_column[3]
                    for i5 in range(row_column[0]) :
                        t = []
                        for i3 in range(row_column[3]) :
                            sum = 0
                            for i4 in range(row_column[2]):
                                x1 = int(t1[i5][i4])*int(t2[i4][i3])
                                sum += x1
                            t.append(sum)
                        t3.append(t)
                    flag1 = 1           
                elif key == "add" :
                    for i3 in range(row_column[0]) :
                        t = []
                        for i4 in range(row_column[1]):
                            x1 = int(t1[i3][i4])+int(t2[i3][i4])
                            t.append(x1)
                        t3.append(t) 
                flag1 = 1
                break
            for m in range(row_column[0]) :
                print(t3[m]) 
            t2 = []
            t1 = t3
            row_column = [row_column[0],row_column[3]]    
        i += 1   
        flag = True                               
    if flag1 != 0 or i - 1 == n :
        break      
# در ادامه باید دترمینان ان را محاسبه کنیم
def det2 (tn) :
    sumd = tn[0][0]*tn[1][1] - tn[1][0]*tn[0][1]

    
    
    
                    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
