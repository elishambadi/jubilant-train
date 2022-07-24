import csv

f = open('Downloads/GPF Lifetime.csv')
f1 = open('Downloads/GPF_New_upd.csv', 'w')

header = ['id', 'trade', 'update1', 'update2', 'update3']
updates = []
all_rows = []
new_row = []

csv_f = csv.reader(f)
csv_f1 = csv.writer(f1)

for row in csv_f:
    # new_row = ['','','','','']
    if ("SELL@" in row[4] or "BUY@" in row[4] or "AGAIN" in row[4]):
        new_row.append(row[0]) #id 
        new_row.append(row[4]) #trade_msg

    if (row[6] != ""):
        updates.append(row)

    all_rows.append(new_row)
    new_row = []

f.close()

for row in all_rows:
    if (row == []):
        all_rows.remove(row)
        print ("Item removed") #clearing list

for row in updates:
    csv_f1.writerow(row)
f1.close()