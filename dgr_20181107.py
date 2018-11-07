######Shis tika pildiits ~/RTR105 mapee, izmanotojot teksts.txt
######
##handle = open("teksts.txt")
##print(handle)
##for Shis in handle:
##    print(Shis)
##count = 0
##handle.seek(0)
##for line in handle:
##    count = count + 1
##print('Line count:', count)
##
##fhand = open('teksts.txt')
##inp = fhand.read()
##print(len(inp))
##print(inp[:20])
##
##fhand = open('teksts.txt')
##for line in fhand:
##    if line.startswith('Shis'):
##        print(line)
##
##fhand = open('teksts.txt')
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('Shis'):
##        print(line)
##
##fhand = open('teksts.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not 'n' in line:
##        continue
##    print(line)
##
##try:
##    fname =input("Enter the file name: ")
##    fhand = open(fname)
##    count = 0
##    for line in fhand:
##        if line.startswith('Shis'):
##            count = count + 1
##    print("There were", count, 'subject lines in' , fname)
##except:
##    print('No such file found')
##
##fname =input("Enter the file name: ")
##try:
##    fhand = open(fname)   
##except:
##    print('No such file found:', fname)
##
##count = 0
##for line in fhand:
##    if line.startswith('Shis'):
##        count = count + 1
##print("There were", count, 'subject lines in' , fname)

