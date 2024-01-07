import os 

subfolders = [ f.path for f in os.scandir("/home/jsorel/elaborato_reti/02_15_b2_00_00_00") if f.is_dir() ]

for i in range (0,40):
    PATH = subfolders[i]
    os.chdir(PATH)
    os.system('touch ip_check.txt')
    file_text = open('ip_check.txt', 'w')
    file0 = open('hash_file.txt', 'r')
    hash = file0.readline()
    strtemp= hash + '\n'
    file_text.write(strtemp)
    file0.close()
    file_text.close()
    file1 = open("tr_tcp.csv", 'r')
    for line in file1.readlines():
        temp = line 
        list1=temp.split(',')
        temp = list1[1]
        templist = temp.split(':')

        dest_ip=templist[0]
        ip_name = list1[12]
        #print(dest_ip+' '+ip_name)

        file2 = open("/home/jsorel/elaborato_reti/ips.txt", 'r')

        for line_ in file2.readlines():
            found = False
            temp2 = line_
            list2= temp2.split(',')
            prova = ''
            if(list2[0] == hash):
                for stringa in list2:
                    if(dest_ip == stringa):
                        found = True
                        break
                    found = False
            if (found == False):
                file3 = open(PATH+'/ip_check.txt', 'a+')
                file3.seek(0)
                data = file3.read(100)
                if len(data) > 0 :
                    file3.write("\n")
                    strtemp = '(traffico tcp) trovato utleriore ip: '+ dest_ip+ ' ' + ip_name
                    #print(dest_ip + ' ' + ip_name + ' ' + prova)
                    file3.write(strtemp)
                    file3.close()
            else:
                file3 = open(PATH+'/ip_check.txt', 'a+')
                file3.seek(0)
                data = file3.read(100)
                if len(data) > 0 :
                    file3.write("\n")
                    strtemp = '(traffico tcp) Risultati conformi con quanto trovato su Virus_Total'
                    file3.write(strtemp)
                    file3.close()
    file1.close()
    file2.close()

    file1 = open("tr_udp.csv", 'r')
    for line in file1.readlines():
        temp = line 
        list1=temp.split(',')
        temp = list1[1]
        templist = temp.split(':')

        dest_ip=templist[0]
        ip_name = list1[12]

        file2 = open("/home/jsorel/elaborato_reti/ips.txt", 'r')

        for line_ in file2.readlines():
            found = False
            temp2 = line_
            list2= temp2.split(',')
            if(list2[0] == hash):
                for stringa in list2:
                    if(dest_ip == stringa):
                        found = True
                        
                        break
                    found = False
                    #print(dest_ip + ' '+stringa)
            if (found == False):
                file3 = open(PATH+'/ip_check.txt', 'a+')
                file3.seek(0)
                data = file3.read(100)
                if len(data) > 0 :
                    file3.write("\n")
                    strtemp = '(traffico udp) trovato utleriore ip: '+ dest_ip+ ' ' + ip_name
                    file3.write(strtemp)
                    file3.close()
            else:
                file3 = open(PATH+'/ip_check.txt', 'a+')
                file3.seek(0)
                data = file3.read(100)
                if len(data) > 0 :
                    file3.write("\n")
                    strtemp = '(traffico udp) Risultati conformi con quanto trovato su Virus_Total'
                    file3.write(strtemp)
                    file3.close()
    file1.close()
    file2.close()
    








