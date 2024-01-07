import os

PATH_GEN = '/home/jsorel/elaborato_reti'
HASH1='08d5cb0fd1c32f89af2a99082aeed2ef399ec1be8c5728f54a75cbdfdbfa1a63'
HASH2='441015ac40f2609e09770523322e358086ffdb5b4b5154ec7aa6b10aa17f7cbe'
HASH3='816890712f0b0e7cc96a6e99a92ed0e63f26c1b093bda1cc293d541e06472bff'
HASH4='c2833508b73244a5c6be1d0f047037951edf3f50719bbdcc9e3fa593211061b7'
HASH5='f2db50e2737d07c0e4d619769a901146e81748f563de0f6b815642db74093e2b'

subfolders = [ f.path for f in os.scandir("/home/jsorel/elaborato_reti/02_15_b2_00_00_00") if f.is_dir() ]

par_tcp_in_gen = 0.0
par_tcp_out_gen = 0.0
par_tcp_gen = 0.0


par_udp_in_gen = 0.0
par_udp_out_gen = 0.0
par_udp_gen = 0.0


avg_tcp_in_gen = 0.0
avg_tcp_out_gen = 0.0
avg_tcp_gen = 0.0
avg_tcp_duration_gen = 0.0

avg_udp_in_gen = 0.0
avg_udp_out_gen = 0.0
avg_udp_gen = 0.0
avg_duration_gen= 0.0

for i in range(0,40):
    PATH = subfolders[i]
    os.chdir(PATH)
    tr_tcp= open('tr_tcp.csv', 'r')
    tr_udp = open('tr_udp.csv', 'r')
    avg_tcp_in=0.0
    avg_tcp_out=0.0
    avg_tcp=0.0
    avg_udp_in=0.0
    avg_udp_out=0.0
    avg_udp=0.0
    n_tcp = 0
    n_udp=0
    
    par_tcp_in = 0
    par_tcp_out = 0
    par_tcp = 0
    par_tcp_duration = 0.0

    for line in tr_tcp.readlines():
        
        temp = line 
        list1 = temp.split(',')
        val = (int)((list1[3].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        par_tcp_in = par_tcp_in + val

        val = (int)((list1[5].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        par_tcp_out = par_tcp_out + val 
        
        val = (int)((list1[7].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        
        val_dur = (float)(list1[9])
        par_tcp_duration = par_tcp_duration + val_dur

        par_tcp= par_tcp + val

        n_tcp = n_tcp + 1 
    
    par_udp_in = 0
    par_udp_out = 0
    par_udp = 0
    par_udp_duration = 0.0

    for line in tr_udp.readlines():
        
        temp = line 
        list1 = temp.split(',')
        val = (int)((list1[3].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        par_udp_in = par_udp_in + val

        val = (int)((list1[5].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        par_udp_out = par_udp_out + val 
        
        val = (int)((list1[7].split(' '))[0])
        if((list1[3].split(' '))[1] == 'kB'):
            val = val * 1000
        par_udp= par_udp + val

        val_dur = (float)(list1[9])
        par_udp_duration = par_udp_duration + val_dur

        n_udp = n_udp + 1
    
    #print(n_tcp, n_udp, par_tcp, par_udp)

    avg_tcp = (float)(par_tcp / n_tcp) 
    avg_tcp_in = (float)(par_tcp_in / n_tcp) 
    avg_tcp_out = (float)(par_tcp_out / n_tcp)
    avg_duration_tcp = (float)(par_tcp_duration/n_tcp)
    avg_duration_udp = (float)(par_tcp_duration/n_udp)
    avg_udp = (float)(par_udp / n_udp) 
    avg_udp_in = (float)(par_udp_in / n_udp) 
    avg_udp_out = (float)(par_udp_out / n_udp)

    
    os.system('rm -f avg_traffic.txt')
    os.system('touch avg_traffic.txt')
    output = open('avg_traffic.txt', 'a+')

    strtemp1 = 'TCP AVG --IN: ' + str(avg_tcp_in) + ' --OUT: ' + str(avg_tcp_out) + ' -- TOTAL: ' + str(avg_tcp)+ ' ' + ' DURATION: ' +str(avg_duration_tcp) +'\n'
    strtemp2 = 'UDP AVG --IN: ' + str(avg_udp_in) + ' --OUT: ' + str(avg_udp_out) + ' -- TOTAL: ' + str(avg_udp)+ ' ' + ' DURATION: ' + str(avg_duration_udp)
    output.write(strtemp1)
    output.write(strtemp2)
    output.close()

    #hash

    hash= open('hash_file.txt', 'r')
    hash_str = hash.readline()

    os.chdir(PATH_GEN)
    #os.system('rm -f *.csv')
    if(hash_str == HASH1):
        hash1= open('malware_1_avg.csv', 'a')
        hash_token = str(avg_tcp_in) + ',' + str(avg_tcp_out) + ',' + str(avg_tcp) + ','+str(avg_duration_tcp) + ',' + str(avg_udp_in) + ',' + str(avg_udp_out) + ',' + str(avg_udp) + ',' + str(avg_duration_udp) + '\n'
        hash1.write(hash_token)
        hash1.close()

    if(hash_str == HASH2):
        hash1= open('malware_2_avg.csv', 'a')
        hash_token = str(avg_tcp_in) + ',' + str(avg_tcp_out) + ',' + str(avg_tcp) + ','+str(avg_duration_tcp) + ',' + str(avg_udp_in) + ',' + str(avg_udp_out) + ',' + str(avg_udp) + ',' + str(avg_duration_udp) + '\n'
        hash1.write(hash_token)
        hash1.close()

    if(hash_str == HASH3):
        hash1= open('malware_3_avg.csv', 'a')
        hash_token = str(avg_tcp_in) + ',' + str(avg_tcp_out) + ',' + str(avg_tcp) + ','+str(avg_duration_tcp) + ',' + str(avg_udp_in) + ',' + str(avg_udp_out) + ',' + str(avg_udp) + ',' + str(avg_duration_udp) + '\n'
        hash1.write(hash_token)
        hash1.close()

    if(hash_str == HASH4):
        hash1= open('malware_4_avg.csv', 'a')
        hash_token = str(avg_tcp_in) + ',' + str(avg_tcp_out) + ',' + str(avg_tcp) + ','+str(avg_duration_tcp) + ',' + str(avg_udp_in) + ',' + str(avg_udp_out) + ',' + str(avg_udp) + ',' + str(avg_duration_udp) + '\n'
        hash1.write(hash_token)
        hash1.close()

    if(hash_str == HASH5):
        hash1= open('malware_5_avg.csv', 'a')
        hash_token = str(avg_tcp_in) + ',' + str(avg_tcp_out) + ',' + str(avg_tcp) + ','+str(avg_duration_tcp) + ',' + str(avg_udp_in) + ',' + str(avg_udp_out) + ',' + str(avg_udp) + ',' + str(avg_duration_udp) + '\n'
        hash1.write(hash_token)
        hash1.close()



    par_udp_in_gen = par_udp_in_gen + avg_udp_in
    par_udp_out_gen = par_udp_out_gen + avg_udp_out
    par_udp_gen = par_udp_gen + avg_udp
    par_tcp_duration = par_tcp_duration + avg_duration_tcp

    par_tcp_in_gen = par_tcp_in_gen + avg_tcp_in
    par_tcp_out_gen = par_tcp_out_gen + avg_tcp_out
    par_tcp_gen = par_tcp_gen + avg_tcp
    par_udp_duration = par_udp_duration + avg_duration_udp

tr_tcp.close()
tr_udp.close()


avg_tcp_in_gen = (float)(par_tcp_in_gen/40)
avg_tcp_out_gen = (float)(par_tcp_out_gen/40)
avg_tcp_gen = (float)(par_tcp_gen/40)
avg_tcp_duration_gen = (float)(par_tcp_duration/40)

avg_udp_in_gen = (float)(par_udp_in_gen/40)
avg_udp_out_gen = (float)(par_udp_out_gen/40)
avg_udp_gen = (float)(par_udp_gen/40)
avg_udp_duration_gen = (float)(par_udp_duration/40)


os.chdir(PATH_GEN)
os.system('rm -f general_avg.txt')
os.system('touch general_avg.txt')

file_general = open('general_avg.txt', 'a+')

file_general.seek(0)
data = file_general.read(100)
strtemp1= 'Media generale TCP: ' + str(avg_tcp_gen) + ' ' + 'Media TCP_IN: ' + str(avg_tcp_in_gen) + ' Media TCP_OUT: ' + str(avg_tcp_out_gen) + ' AVG DURATION TCP: ' + str(avg_tcp_duration_gen) + '\n'
strtemp2 = 'Media generale UDP: ' + str(avg_udp_gen) + ' ' + 'Media UDP_IN: ' + str(avg_udp_in_gen) + ' Media UDP_OUT: ' +str(avg_udp_out_gen)  + ' AVG DURATION UDP: ' + str(avg_udp_duration_gen)
file_general.write(strtemp1)
file_general.write(strtemp2)

file_general.close()


file_daemon = open(PATH_GEN+'/malware_1_avg.csv', 'a+')
file_daemon.seek(0)
list_tcp_in = list()
list_tcp_out = list()
list_tcp = list()
list_tcp_dur = list()
list_udp_in = list()
list_udp_out = list()
list_udp = list()
list_udp_dur = list()

for lines in file_daemon.readlines():
    #print('DEBUG')
    temps = lines
    listone = temps.split(',')
    #print(temps)
    list_tcp_in.append(listone[0])
    list_tcp_out.append(listone[1])
    list_tcp.append(listone[2])
    list_tcp_dur.append(listone[3])
    list_udp_in.append(listone[4])
    list_udp_out.append(listone[5])
    list_udp.append(listone[6])
    list_udp_dur.append(listone[7])

n_list_tcp_in = list(map(float, list_tcp_in))
n_list_tcp_out = list(map(float, list_tcp_out))
n_list_tcp = list(map(float, list_tcp))
n_list_tcp_duration = list(map(float, list_tcp_dur))

n_list_udp_in = list(map(float, list_udp_in))
n_list_udp_out = list(map(float, list_udp_out))
n_list_udp = list(map(float, list_udp))
n_list_udp_duration = list(map(float, list_udp_dur))


#print(list_tcp)
media_tcp_in = sum(n_list_tcp_in)/len(n_list_tcp_in)
media_tcp_out = sum(n_list_tcp_out)/len(n_list_tcp_out)
media_tcp = sum(n_list_tcp)/len(n_list_tcp)
media_tcp_durata = sum(n_list_tcp_duration)/len(n_list_tcp_duration)
media_udp_in = sum(n_list_udp_in)/len(n_list_udp_in)
media_udp_out = sum(n_list_udp_out)/len(n_list_udp_out)
media_udp = sum(n_list_udp)/len(n_list_udp)
media_udp_durata = sum(n_list_udp_duration)/len(n_list_udp_duration)

str_to_append = '\n'+ str(media_tcp_in)+','+str(media_tcp_out) + ',' + str(media_tcp) + ',' + str(media_tcp_durata) + ',' +str(media_udp_in)+','+str(media_udp_out) + ',' + str(media_udp) + ',' + str(media_udp_durata) 
file_daemon.write(str_to_append)
file_daemon.close()

file_daemon = open(PATH_GEN+'/malware_2_avg.csv', 'a+')
file_daemon.seek(0)
list_tcp_in = list()
list_tcp_out = list()
list_tcp = list()
list_tcp_dur = list()
list_udp_in = list()
list_udp_out = list()
list_udp = list()
list_udp_dur = list()

for lines in file_daemon.readlines():
    #print('DEBUG')
    temps = lines
    listone = temps.split(',')
    #print(temps)
    list_tcp_in.append(listone[0])
    list_tcp_out.append(listone[1])
    list_tcp.append(listone[2])
    list_tcp_dur.append(listone[3])
    list_udp_in.append(listone[4])
    list_udp_out.append(listone[5])
    list_udp.append(listone[6])
    list_udp_dur.append(listone[7])

n_list_tcp_in = list(map(float, list_tcp_in))
n_list_tcp_out = list(map(float, list_tcp_out))
n_list_tcp = list(map(float, list_tcp))
n_list_tcp_duration = list(map(float, list_tcp_dur))

n_list_udp_in = list(map(float, list_udp_in))
n_list_udp_out = list(map(float, list_udp_out))
n_list_udp = list(map(float, list_udp))
n_list_udp_duration = list(map(float, list_udp_dur))


#print(list_tcp)
media_tcp_in = sum(n_list_tcp_in)/len(n_list_tcp_in)
media_tcp_out = sum(n_list_tcp_out)/len(n_list_tcp_out)
media_tcp = sum(n_list_tcp)/len(n_list_tcp)
media_tcp_durata = sum(n_list_tcp_duration)/len(n_list_tcp_duration)
media_udp_in = sum(n_list_udp_in)/len(n_list_udp_in)
media_udp_out = sum(n_list_udp_out)/len(n_list_udp_out)
media_udp = sum(n_list_udp)/len(n_list_udp)
media_udp_durata = sum(n_list_udp_duration)/len(n_list_udp_duration)

str_to_append = '\n'+ str(media_tcp_in)+','+str(media_tcp_out) + ',' + str(media_tcp) + ',' + str(media_tcp_durata) + ',' +str(media_udp_in)+','+str(media_udp_out) + ',' + str(media_udp) + ',' + str(media_udp_durata) 
file_daemon.write(str_to_append)
file_daemon.close()

file_daemon = open(PATH_GEN+'/malware_3_avg.csv', 'a+')
file_daemon.seek(0)
list_tcp_in = list()
list_tcp_out = list()
list_tcp = list()
list_tcp_dur = list()
list_udp_in = list()
list_udp_out = list()
list_udp = list()
list_udp_dur = list()

for lines in file_daemon.readlines():
    #print('DEBUG')
    temps = lines
    listone = temps.split(',')
    #print(temps)
    list_tcp_in.append(listone[0])
    list_tcp_out.append(listone[1])
    list_tcp.append(listone[2])
    list_tcp_dur.append(listone[3])
    list_udp_in.append(listone[4])
    list_udp_out.append(listone[5])
    list_udp.append(listone[6])
    list_udp_dur.append(listone[7])

n_list_tcp_in = list(map(float, list_tcp_in))
n_list_tcp_out = list(map(float, list_tcp_out))
n_list_tcp = list(map(float, list_tcp))
n_list_tcp_duration = list(map(float, list_tcp_dur))

n_list_udp_in = list(map(float, list_udp_in))
n_list_udp_out = list(map(float, list_udp_out))
n_list_udp = list(map(float, list_udp))
n_list_udp_duration = list(map(float, list_udp_dur))


#print(list_tcp)
media_tcp_in = sum(n_list_tcp_in)/len(n_list_tcp_in)
media_tcp_out = sum(n_list_tcp_out)/len(n_list_tcp_out)
media_tcp = sum(n_list_tcp)/len(n_list_tcp)
media_tcp_durata = sum(n_list_tcp_duration)/len(n_list_tcp_duration)
media_udp_in = sum(n_list_udp_in)/len(n_list_udp_in)
media_udp_out = sum(n_list_udp_out)/len(n_list_udp_out)
media_udp = sum(n_list_udp)/len(n_list_udp)
media_udp_durata = sum(n_list_udp_duration)/len(n_list_udp_duration)

str_to_append = '\n'+ str(media_tcp_in)+','+str(media_tcp_out) + ',' + str(media_tcp) + ',' + str(media_tcp_durata) + ',' +str(media_udp_in)+','+str(media_udp_out) + ',' + str(media_udp) + ',' + str(media_udp_durata) 
file_daemon.write(str_to_append)
file_daemon.close()

file_daemon = open(PATH_GEN+'/malware_4_avg.csv', 'a+')
file_daemon.seek(0)
list_tcp_in = list()
list_tcp_out = list()
list_tcp = list()
list_tcp_dur = list()
list_udp_in = list()
list_udp_out = list()
list_udp = list()
list_udp_dur = list()

for lines in file_daemon.readlines():
    #print('DEBUG')
    temps = lines
    listone = temps.split(',')
    #print(temps)
    list_tcp_in.append(listone[0])
    list_tcp_out.append(listone[1])
    list_tcp.append(listone[2])
    list_tcp_dur.append(listone[3])
    list_udp_in.append(listone[4])
    list_udp_out.append(listone[5])
    list_udp.append(listone[6])
    list_udp_dur.append(listone[7])

n_list_tcp_in = list(map(float, list_tcp_in))
n_list_tcp_out = list(map(float, list_tcp_out))
n_list_tcp = list(map(float, list_tcp))
n_list_tcp_duration = list(map(float, list_tcp_dur))

n_list_udp_in = list(map(float, list_udp_in))
n_list_udp_out = list(map(float, list_udp_out))
n_list_udp = list(map(float, list_udp))
n_list_udp_duration = list(map(float, list_udp_dur))


#print(list_tcp)
media_tcp_in = sum(n_list_tcp_in)/len(n_list_tcp_in)
media_tcp_out = sum(n_list_tcp_out)/len(n_list_tcp_out)
media_tcp = sum(n_list_tcp)/len(n_list_tcp)
media_tcp_durata = sum(n_list_tcp_duration)/len(n_list_tcp_duration)
media_udp_in = sum(n_list_udp_in)/len(n_list_udp_in)
media_udp_out = sum(n_list_udp_out)/len(n_list_udp_out)
media_udp = sum(n_list_udp)/len(n_list_udp)
media_udp_durata = sum(n_list_udp_duration)/len(n_list_udp_duration)

str_to_append = '\n'+ str(media_tcp_in)+','+str(media_tcp_out) + ',' + str(media_tcp) + ',' + str(media_tcp_durata) + ',' +str(media_udp_in)+','+str(media_udp_out) + ',' + str(media_udp) + ',' + str(media_udp_durata) 
file_daemon.write(str_to_append)
file_daemon.close()

file_daemon = open(PATH_GEN+'/malware_5_avg.csv', 'a+')
file_daemon.seek(0)
list_tcp_in = list()
list_tcp_out = list()
list_tcp = list()
list_tcp_dur = list()
list_udp_in = list()
list_udp_out = list()
list_udp = list()
list_udp_dur = list()

for lines in file_daemon.readlines():
    #print('DEBUG')
    temps = lines
    listone = temps.split(',')
    #print(temps)
    list_tcp_in.append(listone[0])
    list_tcp_out.append(listone[1])
    list_tcp.append(listone[2])
    list_tcp_dur.append(listone[3])
    list_udp_in.append(listone[4])
    list_udp_out.append(listone[5])
    list_udp.append(listone[6])
    list_udp_dur.append(listone[7])

n_list_tcp_in = list(map(float, list_tcp_in))
n_list_tcp_out = list(map(float, list_tcp_out))
n_list_tcp = list(map(float, list_tcp))
n_list_tcp_duration = list(map(float, list_tcp_dur))

n_list_udp_in = list(map(float, list_udp_in))
n_list_udp_out = list(map(float, list_udp_out))
n_list_udp = list(map(float, list_udp))
n_list_udp_duration = list(map(float, list_udp_dur))


#print(list_tcp)
media_tcp_in = sum(n_list_tcp_in)/len(n_list_tcp_in)
media_tcp_out = sum(n_list_tcp_out)/len(n_list_tcp_out)
media_tcp = sum(n_list_tcp)/len(n_list_tcp)
media_tcp_durata = sum(n_list_tcp_duration)/len(n_list_tcp_duration)
media_udp_in = sum(n_list_udp_in)/len(n_list_udp_in)
media_udp_out = sum(n_list_udp_out)/len(n_list_udp_out)
media_udp = sum(n_list_udp)/len(n_list_udp)
media_udp_durata = sum(n_list_udp_duration)/len(n_list_udp_duration)

str_to_append = '\n'+ str(media_tcp_in)+','+str(media_tcp_out) + ',' + str(media_tcp) + ',' + str(media_tcp_durata) + ',' +str(media_udp_in)+','+str(media_udp_out) + ',' + str(media_udp) + ',' + str(media_udp_durata) 
file_daemon.write(str_to_append)
file_daemon.close()