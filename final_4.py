import os
import regex as re
#import pandas as pd


os.chdir("/home/jsorel/elaborato_reti")

subfolders = [ f.path for f in os.scandir("/home/jsorel/elaborato_reti/02_15_b2_00_00_00") if f.is_dir() ]
i=0
for i in range(0,40):

    #print(subfolders)
    PATH = subfolders[i]
    #cmd = 'cd' + ' ' + PATH
    #print(cmd)
    os.chdir(PATH)
    os.system("pwd")
    os.system("tshark -r traffic.pcap -z conv,tcp -q>temp.txt")

    file1 = open('temp.txt','r')
    

    file2 = open('temp2.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("Filter")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp2.txt','r')
    

    file2 = open('temp3.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("Conversations")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp3.txt','r')
    

    file2 = open('temp4.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("|")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp4.txt','r')
    

    file2 = open('temp5.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("==")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()



    file1 = open('temp5.txt', 'r')
    file2 = open('temp6.txt', 'w')

    for line in file1.readlines():
        temp = line
        

        file2.write(temp.replace("<->", ""))

    file1.close()
    file2.close()

    file1 = open('temp6.txt', 'r')
    file2 = open('tr_tcp.csv', 'w')

    for line in file1.readlines():
        temp = line
        temp.replace(',','.')
        list1 =  temp.split()
        list1 = [list1[0], list1[1],list1[2], ''.join(list1[3]+' '+list1[4]),list1[5], ''.join( list1[6]+' '+list1[7]),list1[8], ''.join(list1[9]+' '+list1[10]), list1[11], list1[12]]
        list1[5]=re.sub(',','.',list1[5])
        list1[6]=re.sub(',','.',list1[6])
        #print(list1)
        #list1.remove('bytes')
        #list1.remove('kb')
        l=list1[1].split(':',1)
        mario='tshark -r traffic.pcap -T fields -e frame.time_epoch -e frame.protocols -e dns.a -e dns.qry.name -e tls.handshake.extensions_server_name -e http.host  -Y "(dns.a=={}) && (dns.flags.response==1)">t_temp.txt'.format(l[0])
        luigi = 'whois {} |grep -i "orgname\|org-name" > whois___.txt'.format(l[0])
        os.system(mario)
        os.system(luigi)
        file3=open('t_temp.txt','r')

        s=file3.readline()
        #print(s)
        list2 =  s.split('\t')
        #print(list2)
        #print(list2.__len__())
        if(list2.__len__()>1):
            list2 = [list2[0], list2[1],list2[3],list2[4]]
        file4 = open('whois___.txt', 'r')
        list3= ['', '']
        j = 0
        for line__ in file4.readlines():
            if(j>1):
                break
            temp__ = line__ 
            list__=temp__.split('        ')
            #print(list__)
            if(list__.__len__()>1):
                list__[1]=re.sub('\n', '', list__[1])
                list3[j] = list__[1]
            j=j+1

        list=list1+list2+list3
        
        #print(list)

        strrr = ','.join(list)
#        print(strrr)
        file2.write(strrr+'\n')
        file3.close()
        file4.close()


    file1.close()
    file2.close()
    #read_file = pd.read_csv ('tr_tcp.txt')
    #read_file.to_csv ('tr_tcp.csv', index=None)

    os.system("rm -f temp.txt temp2.txt temp3.txt temp4.txt temp5.txt temp6.txt t_temp.txt whois___.txt")
    i = i+1


os.chdir("/home/jsorel/elaborato_reti")

subfolders = [ f.path for f in os.scandir("/home/jsorel/elaborato_reti/02_15_b2_00_00_00") if f.is_dir() ]

k=0
for k in range(0,40):

    #print(subfolders)
    PATH = subfolders[k]
    #cmd = 'cd' + ' ' + PATH
    #print(cmd)
    os.chdir(PATH)
    os.system("pwd")
    os.system("tshark -r traffic.pcap -z conv,udp -q>temp.txt")

    file1 = open('temp.txt','r')
    

    file2 = open('temp2.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("Filter")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp2.txt','r')
    

    file2 = open('temp3.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("Conversations")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp3.txt','r')
    

    file2 = open('temp4.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("|")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()

    file1 = open('temp4.txt','r')
    

    file2 = open('temp5.txt','w')
    
    for line in file1.readlines():
    
        if not (line.__contains__("==")):
        
            #print(line)
            
            file2.write(line)
    
    file2.close()
    file1.close()



    file1 = open('temp5.txt', 'r')
    file2 = open('temp6.txt', 'w')

    for line in file1.readlines():
        temp = line
        

        file2.write(temp.replace("<->", ""))

    file1.close()
    file2.close()

    file1 = open('temp6.txt', 'r')
    file2 = open('tr_udp.csv', 'w')

    for line in file1.readlines():
        temp = line
        temp.replace(',','.')
        list1 =  temp.split()
        list1 = [list1[0], list1[1],list1[2], ''.join(list1[3]+' '+list1[4]),list1[5], ''.join( list1[6]+' '+list1[7]),list1[8], ''.join(list1[9]+' '+list1[10]), list1[11], list1[12]]
        list1[5]=re.sub(',','.',list1[5])
        list1[6]=re.sub(',','.',list1[6])
        #print(list1)
        #list1.remove('bytes')
        #list1.remove('kb')
        l=list1[1].split(':',1)
        mario='tshark -r traffic.pcap -T fields -e frame.time_epoch -e frame.protocols -e dns.a -e dns.qry.name -e tls.handshake.extensions_server_name -e http.host  -Y "(dns.a=={}) && (dns.flags.response==1)">t_temp.txt'.format(l[0])
        luigi = 'whois {} |grep -i "orgname\|org-name" > whois___.txt'.format(l[0])
        os.system(mario)
        os.system(luigi)
        file3=open('t_temp.txt','r')

        s=file3.readline()
        #print(s)
        list2 =  s.split('\t')
        #print(list2)
        #print(list2.__len__())
        if(list2.__len__()>1):
            list2 = [list2[0], list2[1],list2[3],list2[4]]
        file4 = open('whois___.txt', 'r')
        list3= ['', '']
        j = 0
        for line__ in file4.readlines():
            if(j>1):
                break
            temp__ = line__ 
            list_=temp__.split('        ')
            if(list_.__len__()>1):
                list_[1]=re.sub('\n', '', list_[1])
                #print(list__)
                list3[j] = list_[1]
            j=j+1


        list=list1+list2+list3
        
        #print(list)

        strrr = ','.join(list)
#        print(strrr)
        file2.write(strrr+'\n')
        file3.close()
        file4.close()


    file1.close()
    file2.close()
    #read_file = pd.read_csv ('tr_udp.txt')
    #read_file.to_csv ('tr_udp.csv', index=None)

    os.system("rm -f temp.txt temp2.txt temp3.txt temp4.txt temp5.txt temp6.txt t_temp.txt whois___.txt")
    k = k+1

print("FINE ESECUZIONE")