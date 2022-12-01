file = open('./input.txt', encoding='utf-8')
lines = file.readlines()

cur_total = 0
totals = [] 

for line in lines:
    if not line.strip():       
        totals.append(cur_total)
        cur_total = 0
    else:
        cleaned_line = int(repr(line.strip())[1:-1])
        cur_total += int(cleaned_line)
        
sorted_totals = sorted(totals)

print(sorted_totals[-1])
print(sorted_totals[-3:])



    


