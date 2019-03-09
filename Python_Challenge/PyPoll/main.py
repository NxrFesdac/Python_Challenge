import csv

votes = 0
Khan = 0
Correy = 0
Li = 0
tooley = 0

file = "c:/Users/cvargas/Desktop/Python_Challenge/PyPoll/election_data.csv"
texto = "c:/Users/cvargas/Desktop/Python_Challenge/PyPoll/texto.txt"

with open(file) as PyPoll:
    reader = csv.reader(PyPoll)
    header = next(reader)
    for row in reader:
        votes = votes + 1
        if row[2] == 'Khan':
            Khan = Khan + 1
        elif row[2] == 'Li':
            Li = Li + 1
        elif row[2] == 'Correy':
            Correy = Correy + 1
        else:
            tooley = tooley + 1

voters = [Khan, Correy, Li, tooley]
voters2 = ["Khan", "Correy", "Li", "tooley"]

#posicion = -1

#for vote in voters:
#    posicion = posicion + 1
#    if vote == max(voters):
#        print(posicion)

#print(max(voters))

KhanP = str(((Khan / votes) * 100))
KhanP2 = KhanP[:2] + '%'
CorreyP = str(((Correy / votes) * 100))
CorreyP2 = CorreyP[:2] + '%'
LiP = str(((Li / votes) * 100))
LiP2 = LiP[:2] + '%'
tooleyP = str(((tooley / votes) * 100))
tooleyP2 = tooleyP[:1] + '%'

printear = ''

for x in range(0,len(voters)):
    if(voters[x] == max(voters)):
        printear = 'Winner ' + voters2[x]


with open(texto, "w") as txt_file:
    txt_file.write(f'Total votes = {votes}\n'
f'Khan votes = {KhanP2} ({Khan})\n'
f'Correy votes = {CorreyP2} ({Correy})\n'
f'Li votes = {LiP2} ({Li})\n'
f'Tooley votes = {tooleyP2} ({tooley})\n'
f'{printear}')