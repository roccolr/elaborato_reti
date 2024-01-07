import matplotlib.pyplot as plt 
import os

PATH = '/home/jsorel/elaborato_reti_ale'
os.chdir(PATH)

#malware 1
mal_csv = open('malware_1_avg.csv', 'r')
dim_pts= []
time_pts = []
i = 0
for line in mal_csv.readlines():
    if(i<8):
        temp = line 
        list1 = temp.split(',')
        #print(list1)
        dim_pts.append(float(list1[2]))
        time_pts.append(float(list1[3]))
    i=i+1
mal_csv.close()
dim_pts_trunc = [round(numero, 1) for numero in dim_pts]
time_pts_trunc = [round(numero, 1) for numero in time_pts]
#plt.plot(dim_pts, 'g*', time_pts, 'ro')
plt.scatter(time_pts, dim_pts)
plt.grid()
plt.xlabel("Durata della conversazione")
plt.ylabel("Dimensione totale del flusso TCP (byte)")
plt.title("Malware 1")
plt.savefig(PATH+'/malware1.jpeg')
plt.clf()

#malware 2
mal_csv = open('malware_2_avg.csv', 'r')
dim_pts= []
time_pts = []
i = 0
for line in mal_csv.readlines():
    if(i<8):
        temp = line 
        list1 = temp.split(',')
        #print(list1)
        dim_pts.append(float(list1[2]))
        time_pts.append(float(list1[3]))
    i=i+1

dim_pts_trunc_ = [round(numero, 1) for numero in dim_pts]
time_pts_trunc_ = [round(numero, 1) for numero in time_pts]
#plt.plot(dim_pts, 'g*', time_pts, 'ro')

plt.scatter(time_pts, dim_pts)
plt.grid()
plt.xlabel("Durata della conversazione")
plt.ylabel("Dimensione totale del flusso TCP (byte)")
plt.title("Malware 2")
plt.savefig(PATH+'/malware2.jpeg')
mal_csv.close()
plt.clf()

#malware 3
mal_csv = open('malware_3_avg.csv', 'r')
dim_pts= []
time_pts = []
i = 0
for line in mal_csv.readlines():
    if(i<8):
        temp = line 
        list1 = temp.split(',')
        #print(list1)
        dim_pts.append(float(list1[2]))
        time_pts.append(float(list1[3]))
    i=i+1
mal_csv.close()

dim_pts_trunc = [round(numero, 1) for numero in dim_pts]
time_pts_trunc = [round(numero, 1) for numero in time_pts]
#plt.plot(dim_pts, 'g*', time_pts, 'ro')
plt.scatter(time_pts, dim_pts)
plt.grid()
plt.xlabel("Durata della conversazione")
plt.ylabel("Dimensione totale del flusso TCP (byte)")
plt.title("Malware 3")
plt.savefig(PATH+'/malware3.jpeg')
plt.clf()

#malware 4
mal_csv = open('malware_4_avg.csv', 'r')
dim_pts= []
time_pts = []
i = 0
for line in mal_csv.readlines():
    if(i<8):
        temp = line 
        list1 = temp.split(',')
        #print(list1)
        dim_pts.append(float(list1[2]))
        time_pts.append(float(list1[3]))
    i=i+1
mal_csv.close()

dim_pts_trunc = [round(numero, 1) for numero in dim_pts]
time_pts_trunc = [round(numero, 1) for numero in time_pts]
#plt.plot(dim_pts, 'g*', time_pts, 'ro')
plt.scatter(time_pts, dim_pts)
plt.grid()
plt.xlabel("Durata della conversazione")
plt.ylabel("Dimensione totale del flusso TCP (byte)")
plt.title("Malware 4")
plt.savefig(PATH+'/malware4.jpeg')
plt.clf()

#malware 5
mal_csv = open('malware_5_avg.csv', 'r')
dim_pts= []
time_pts = []
i = 0
for line in mal_csv.readlines():
    if(i<8):
        temp = line 
        list1 = temp.split(',')
        #print(list1)
        dim_pts.append(float(list1[2]))
        time_pts.append(float(list1[3]))
    i=i+1
mal_csv.close()

dim_pts_trunc = [round(numero, 1) for numero in dim_pts]
time_pts_trunc = [round(numero, 1) for numero in time_pts]
#plt.plot(dim_pts, 'g*', time_pts, 'ro')
plt.scatter(time_pts, dim_pts)
plt.grid()
plt.xlabel("Durata della conversazione")
plt.ylabel("Dimensione totale del flusso TCP (byte)")
plt.title("Malware 5")
plt.savefig(PATH+'/malware5.jpeg')

plt.clf()