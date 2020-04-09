import mysql.connector
import sys
import pandas
import json
import os
import sqlite3

#for i in mycursor:
    #print(i)



#################################################################################################
######################         RECUPERATION DES JSON        #####################################
#################################################################################################

#importer les fichier json et les netoyer en format data frame 
# ajout du fichier json saison1 
table= []
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season1.json') as json_data:
    #Pour stocker les données du fichier JSON dans un dictionnaire python il existe la fonction load() du module python json:
    data_dict = json.load(json_data)
    print(data_dict)
    #Une fois les données dans le dictionnaire que nous avons intitulé data_dict il est alors possible de stocker les données dans une chaine de caractères data_str en passant par la fonction dump
    data_str = json.dumps(data_dict)
    print(data_str)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
# Remettre les données dans un dictionnaire
data_dict_01 = json.loads(data_str)
print(data_dict_01)    
# j'ai observer sur les donner avec beaucoup de NAN 
saison1=pandas.read_json(data_str)
print(saison1)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s1=saison1.dropna()
print(s1)
S1= s1.to_dict('index')
print(S1)

#on repéte la méme action pour tout les dossier json avec les saisons


# operation avec fichier json saison2
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season2.json') as json_data2:
    #Pour stocker les données du fichier JSON dans un dictionnaire python il existe la fonction load() du module python json:
    data_dict2 = json.load(json_data2)
    print(data_dict2)
    data_str2 = json.dumps(data_dict2)
    print(data_str2)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
data_dict_02 = json.loads(data_str2)
print(data_dict_02)    
# j' observer sur les données avec beaucoup de NAN 
saison2=pandas.read_json(data_str2)
print(saison2)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s2=saison2.dropna()
print(s2)
S2= s2.to_dict('index')
print(S2)

# operation avec fichier json saison3
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season3.json') as json_data3:
    #Pour stocker les données du fichier JSON dans un dictionnaire python il existe la fonction load() du module python json:
    data_dict3 = json.load(json_data3)
    print(data_dict3)
    data_str3 = json.dumps(data_dict3)
    print(data_str3)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
data_dict_03 = json.loads(data_str3)
print(data_dict_03)    
# j' observer sur les données avec beaucoup de NAN 
saison3=pandas.read_json(data_str3)
print(saison3)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s3=saison3.dropna()
print(s3)
S3= s3.to_dict('index')
print(S3)

# operation avec fichier json saison4
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season4.json') as json_data4:
    data_dict4 = json.load(json_data4)
    print(data_dict4)
    data_str4 = json.dumps(data_dict4)
    #print(data_str4)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
data_dict_04 = json.loads(data_str4)
#print(data_dict_04)    
# j' observer sur les données avec beaucoup de NAN 
saison4=pandas.read_json(data_str4)
#print(saison4)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s4=saison4.dropna()
#print(s4)
S4= s4.to_dict('index')
#print(S4)
S4= s4.to_dict('index')
print(S4)



# operation avec fichier json saison5
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season5.json') as json_data5:
    data_dict5 = json.load(json_data5)
    print(data_dict5)
    data_str5 = json.dumps(data_dict5)
    print(data_str5)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
data_dict_05 = json.loads(data_str5)
print(data_dict_05)    
# j' observer sur les données avec beaucoup de NAN 
saison5=pandas.read_json(data_str5)
print(saison5)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s5=saison5.dropna()
print(s5)
S5= s5.to_dict('index')
print(S5)

# operation avec fichier json saison6
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season6.json') as json_data6:
    data_dict6 = json.load(json_data6)
    print(data_dict6)
    data_str6 = json.dumps(data_dict6)
    print(data_str6)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné 
data_dict_06 = json.loads(data_str6)
print(data_dict_06)    
# j' observer sur les données avec beaucoup de NAN 
saison6=pandas.read_json(data_str6)
print(saison6)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s6=saison6.dropna()
print(s6)
S6= s6.to_dict('index')
print(S6)


# operation avec fichier json saison7
with open('/Users/ano/Desktop/dossierpython/game-of-thrones-srt/season7.json') as json_data7:
    #Pour stocker les données du fichier JSON dans un dictionnaire python il existe la fonction load() du module python json:
    data_dict7 = json.load(json_data7)
    print(data_dict7)
    #Une fois les données dans le dictionnaire que nous avons intitulé data_dict il est alors possible de stocker les données dans une chaine de caractères data_str en passant par la fonction dump
    data_str7 = json.dumps(data_dict7)
    print(data_str7)
    #on transforme le fichier ouvert en data frame avec pandas que je remet dans une autre variable que je print et verifie les donné
    # Remettre les données dans un dictionnaire
data_dict_07 = json.loads(data_str7)
print(data_dict_07)    
# j' observer sur les données 
saison7=pandas.read_json(data_str7)
print(saison7)
# je supprime touts les NAN avec dropna() et je mets le touts dans levariable S1
s7=saison7.dropna()
print(s7)
S7= s7.to_dict('index')
print(S7)

print(S7.keys())
print(S7.values())

#################################################################################################
######################          CREATION DE LA BASE         #####################################
#################################################################################################



mydb= mysql.connector.connect(host="localhost",
                               user="root", password="Mhajjar3", database= "DATA")

cursor = mydb.cursor()

# ce try execept n'est utile qu'en phase de developpement
try :
    cursor.execute("drop table got;")
    print('dropped')
except :
    print("n'existe pas")

# representation de la bdd souhaitée :
    
# id | saison  | num_episode |    nom_episode    | ligne_id |    sub     |
#-----------------------------------------------------------------------
#  1 | season1 |   S01E01    | Winter is coming  |    1     | Easy, boy. |


cursor.execute("""
CREATE TABLE IF NOT EXISTS got (
    id int(5) NOT NULL AUTO_INCREMENT,
    saison varchar(10) NOT NULL,
    num_episode varchar(200) NOT NULL,
    nom_episode varchar(200) NOT NULL,
    ligne_id int(5) NOT NULL,
    subtitle varchar(200) NOT NULL,
    PRIMARY KEY(id)
);
""")

#cursor.execute("show tables")
for key,value in s1.items():
    	cursor.execute("INSERT INTO got (saison, num_episode, nom_episode, ligne_id, subtitle)VALUES (%s, %s, %s, %s, %s)", S1)

cursor.commit()
cursor.close()