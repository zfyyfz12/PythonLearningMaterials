on = input('输入要备份的文件名')
index = on.rfind('.')
if index > 0:  # eg:”.txt“ 这个文件名不合法
    nn = on[:index] + '[备份]' + on[index:]
oldF = open(on, 'rb')
newF = open(nn, 'wb')
while True:
    con = oldF.read(1024)
    if len(con) != 0:
        newF.write(con)
    else:
        break
