import os 
import matplotlib.pyplot as plt 
import pandas as pd 

PATH = '/home/jsorel/elaborato_reti'

os.chdir(PATH)

file_gen = open ('AVG_TABLE.csv','a+')

#malware1
file1 = open ('malware_1_avg.csv', 'r')
linee = file1.readlines()
str_1 = linee[9]+'\n'
file1.close()

file_gen.write(str_1)

#malware2
file1 = open ('malware_2_avg.csv', 'r')
linee = file1.readlines()
str_1 = linee[9]+'\n'
file1.close()

file_gen.write(str_1)

#malware3
file1 = open ('malware_3_avg.csv', 'r')
linee = file1.readlines()
str_1 = linee[9]+'\n'
file1.close()

file_gen.write(str_1)

#malware4
file1 = open ('malware_4_avg.csv', 'r')
linee = file1.readlines()
str_1 = linee[9]+'\n'
file1.close()

file_gen.write(str_1)

#malware5
file1 = open ('malware_5_avg.csv', 'r')
linee = file1.readlines()
str_1 = linee[9]+'\n'
file1.close()

file_gen.write(str_1)

file_gen.close()

nomi_righe = ['APK1','APK2','APK3','APK4','APK5']
nomi_colonne = ['AVG_TCP_IN', 'AVG_TPC_OUT', 'AVG_TCP', 'AVG_TCP_DURATION', 'AVG_UDP_IN', 'AVG_UDP_OUT', 'AVG_UDP', 'AVG_UDP_DURATION']

df = pd.read_csv('AVG_TABLE.csv')

# Imposta le dimensioni della figura
larghezza_cella = 1.5  # Larghezza di ciascuna cella
altezza_cella = 0.5   # Altezza di ciascuna cella
larghezza_figura = (len(nomi_colonne)+1) * larghezza_cella
altezza_figura = (len(nomi_righe) + 1) * altezza_cella  # +1 per includere la riga delle etichette delle colonne

plt.figure(figsize=(15, 6))
#plt.figure(figsize=(larghezza_figura, altezza_figura))

# Crea la tabella
tabella = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='left', colColours=['#f2f2f2']*len(df.columns))


# Imposta lo stile della tabella
tabella.auto_set_font_size(False)
tabella.set_fontsize(10)

# Nasconde gli assi
plt.axis('off')

# Aggiungi un titolo
plt.title('Medie per APK')

# Salva la figura come immagine
plt.savefig('tabella_media.jpeg')

