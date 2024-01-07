import os 
import matplotlib.pyplot as plt 
#import pandas as pd 

PATH = '/home/jsorel/elaborato_reti_ale'
PATH_CATTURE = '/home/jsorel/elaborato_reti_ale/02_15_b2_00_00_00'
os.chdir(PATH)


#1 Malware

subfolders = [ f.path for f in os.scandir(PATH_CATTURE) if f.is_dir() ]
i=0
n_occorrenze_GOOGLE_LLC = 0
n_occorrenze_FranTech_Solution = 0
n_occorrenze_IANA = 0



for i in range(0,40,5):
    #print(i)
    PATH_SING_CATTURA = subfolders[i]
    os.chdir(PATH_SING_CATTURA)
    file1 = open('tr_tcp.csv', 'r')
    for line in file1.readlines():
        temp = line 
        list1 = temp.split(',')
        if 'Google LLC' in list1:
            n_occorrenze_GOOGLE_LLC=n_occorrenze_GOOGLE_LLC+1
        if 'FranTech Solutions' in list1:
            n_occorrenze_FranTech_Solution = n_occorrenze_FranTech_Solution +1
        if 'Internet Assigned Numbers Authority' in list1:
            n_occorrenze_IANA = n_occorrenze_IANA + 1
    

    file1.close()
    categorie = ['Google LLC', 'FranTech Solutions', 'Non specificato']
    valori = [n_occorrenze_GOOGLE_LLC, n_occorrenze_FranTech_Solution, n_occorrenze_IANA]
    plt.bar(categorie, valori, color=['#6d8faa', '#82a5ac', '#93b2b1'], width=0.7, edgecolor='black', linewidth=1.2)
    #plt.grid()
    plt.xlabel('Domini')
    plt.ylabel('occorrenze')
    plt.title('Malware 1')
    plt.savefig(PATH+'/Malware_1_occorrenze.jpeg')
    plt.clf()
    i=i+5


#2 Malware

subfolders = [ f.path for f in os.scandir(PATH_CATTURE) if f.is_dir() ]
i=0
n_occorrenze_GOOGLE_LLC = 0
n_occorrenze_FranTech_Solution = 0
n_occorrenze_IANA = 0



for i in range(1,40,5):
    print(i)
    PATH_SING_CATTURA = subfolders[i]
    os.chdir(PATH_SING_CATTURA)
    file1 = open('tr_tcp.csv', 'r')
    for line in file1.readlines():
        temp = line 
        list1 = temp.split(',')
        if 'Google LLC' in list1:
            n_occorrenze_GOOGLE_LLC=n_occorrenze_GOOGLE_LLC+1
        if 'RIPE Network Coordination Centre' in list1:
            n_occorrenze_FranTech_Solution = n_occorrenze_FranTech_Solution +1
        if 'Internet Assigned Numbers Authority' in list1:
            n_occorrenze_IANA = n_occorrenze_IANA + 1
    

    file1.close()
    categorie = ['Google LLC', 'RIPE Network Coordination Centre', 'Non specificato']
    valori = [n_occorrenze_GOOGLE_LLC, n_occorrenze_FranTech_Solution, n_occorrenze_IANA]
    plt.bar(categorie, valori, color=['#6d8faa', '#82a5ac', '#93b2b1'], width=0.7, edgecolor='black', linewidth=1.2)
    #plt.grid()
    plt.xlabel('Domini')
    plt.ylabel('occorrenze')
    plt.title('Malware 2')
    plt.savefig(PATH+'/Malware_2_occorrenze.jpeg')
    plt.clf()
    i=i+5

#3 Malware

subfolders = [ f.path for f in os.scandir(PATH_CATTURE) if f.is_dir() ]
i=0
n_occorrenze_GOOGLE_LLC = 0
n_occorrenze_FranTech_Solution = 0
n_occorrenze_IANA = 0



for i in range(2,40,5):
    print(i)
    PATH_SING_CATTURA = subfolders[i]
    os.chdir(PATH_SING_CATTURA)
    file1 = open('tr_tcp.csv', 'r')
    for line in file1.readlines():
        temp = line 
        list1 = temp.split(',')
        if 'Google LLC' in list1:
            n_occorrenze_GOOGLE_LLC=n_occorrenze_GOOGLE_LLC+1
        if 'RIPE Network Coordination Centre' in list1:
            n_occorrenze_FranTech_Solution = n_occorrenze_FranTech_Solution +1
        if 'Internet Assigned Numbers Authority' in list1:
            n_occorrenze_IANA = n_occorrenze_IANA + 1
    

    file1.close()
    categorie = ['Google LLC', 'RIPE Network Coordination Centre', 'Non specificato']
    valori = [n_occorrenze_GOOGLE_LLC, n_occorrenze_FranTech_Solution, n_occorrenze_IANA]
    plt.bar(categorie, valori, color=['#6d8faa', '#82a5ac', '#93b2b1'], width=0.7, edgecolor='black', linewidth=1.2)
    #plt.grid()
    plt.xlabel('Domini')
    plt.ylabel('occorrenze')
    plt.title('Malware 3')
    plt.savefig(PATH+'/Malware_3_occorrenze.jpeg')
    plt.clf()
    i=i+5

#4 Malware

subfolders = [ f.path for f in os.scandir(PATH_CATTURE) if f.is_dir() ]
i=0
n_occorrenze_GOOGLE_LLC = 0
n_occorrenze_FranTech_Solution = 0
n_occorrenze_IANA = 0



for i in range(3,40,5):
    print(i)
    PATH_SING_CATTURA = subfolders[i]
    os.chdir(PATH_SING_CATTURA)
    file1 = open('tr_tcp.csv', 'r')
    for line in file1.readlines():
        temp = line 
        list1 = temp.split(',')
        if 'Google LLC' in list1:
            n_occorrenze_GOOGLE_LLC=n_occorrenze_GOOGLE_LLC+1
        if 'RIPE Network Coordination Centre' in list1:
            n_occorrenze_FranTech_Solution = n_occorrenze_FranTech_Solution +1
        if 'Internet Assigned Numbers Authority' in list1:
            n_occorrenze_IANA = n_occorrenze_IANA + 1
    

    file1.close()
    categorie = ['Google LLC', 'RIPE Network Coordination Centre', 'Non specificato']
    valori = [n_occorrenze_GOOGLE_LLC, n_occorrenze_FranTech_Solution, n_occorrenze_IANA]
    plt.bar(categorie, valori, color=['#6d8faa', '#82a5ac', '#93b2b1'], width=0.7, edgecolor='black', linewidth=1.2)
    #plt.grid()
    plt.xlabel('Domini')
    plt.ylabel('occorrenze')
    plt.title('Malware 4')
    plt.savefig(PATH+'/Malware_4_occorrenze.jpeg')
    plt.clf()
    i=i+5    

    #4 Malware

subfolders = [ f.path for f in os.scandir(PATH_CATTURE) if f.is_dir() ]
i=0
n_occorrenze_GOOGLE_LLC = 0
n_occorrenze_FranTech_Solution = 0
n_occorrenze_IANA = 0



for i in range(4,40,5):
    print(i)
    PATH_SING_CATTURA = subfolders[i]
    os.chdir(PATH_SING_CATTURA)
    file1 = open('tr_tcp.csv', 'r')
    for line in file1.readlines():
        temp = line 
        list1 = temp.split(',')
        if 'Google LLC' in list1:
            n_occorrenze_GOOGLE_LLC=n_occorrenze_GOOGLE_LLC+1
        if 'RIPE Network Coordination Centre' in list1:
            n_occorrenze_FranTech_Solution = n_occorrenze_FranTech_Solution +1
        if 'Internet Assigned Numbers Authority' in list1:
            n_occorrenze_IANA = n_occorrenze_IANA + 1
    

    file1.close()
    categorie = ['Google LLC', 'RIPE Network Coordination Centre', 'Non specificato']
    valori = [n_occorrenze_GOOGLE_LLC, n_occorrenze_FranTech_Solution, n_occorrenze_IANA]
    plt.bar(categorie, valori, color=['#6d8faa', '#82a5ac', '#93b2b1'], width=0.7, edgecolor='black', linewidth=1.2)
    #plt.grid()
    plt.xlabel('Domini')
    plt.ylabel('occorrenze')
    plt.title('Malware 5')
    plt.savefig(PATH+'/Malware_5_occorrenze.jpeg')
    plt.clf()
    i=i+5    