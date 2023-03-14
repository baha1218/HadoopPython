dnf install python3
dnf install python3-pip
pip3 install pyspark

apt-get install python3
apt-get install python3-pip
pip3 install pyspark


docker exec -ti f4 bash
apt install nano
mkdir 
nano text.txt
hadoop fs -mkdir /user
hadoop fs -mkdir /user/root
hadoop fs -put text.txt

Vérifiez sur le webui dans Utilities/Browse the file system

sur namenode
/usr/local/spark/sbin/start-master.sh

sur datanode
/usr/local/spark/sbin/start-worker.sh spark://namenode:7077


hadoop fs -mkdir /spark-logs

nano test.py

from pyspark import SparkContext

# Instantiation d'un SparkContext
sc = SparkContext()

# Lecture d'un fichier texte : le fichier est décomposé en lignes.
lines = sc.textFile("text.txt")

# Décomposition de chaque ligne en mots
word_counts = lines.flatMap(lambda line: line.split(' ')) \
                   .map(lambda word: (word, 1)) \
                   .reduceByKey(lambda count1, count2: count1 + count2) \
                   .collect()

# Chaque paire (clé, valeur) est affichée
for (word, count) in word_counts:
    print(word, count)

python3 test.py






dans datanode 
wget https://www.data.gouv.fr/fr/datasets/r/7400c7d1-8db6-43b2-9235-aae564223963 
mv 7400c7d1-8db6-43b2-9235-aae564223963 fr-esr-parcoursup.csv
hadoop fs -put fr-esr-parcoursup.csv
nano test_park.py



python3 test_park.py


nano result_spark.py
hadoop fs -cat /user/root/result-parcoursup.csv/part-00000-9d5a5330-f923-4806-a095-dd8740e8a120-c000.csv

copiez l'output et créer un fichier result.txt supprimer la premiere ligne et ajouter le contenu de la slide script result suite

fili,form_lib_voe_acc,fil_lib_voe_acc,sum(voe_tot)
IFSI,D.E secteur sanitaire,D.E Infirmier,1391246
Ecole d'Ingénieur,Formations  des écoles d'ingénieurs,Formation d'ingénieur Bac + 5,626037
PASS,Licence - Sciences - technologies - santé,Parcours d'Accès Spécifique Santé (PASS),512607
Licence,Licence - Droit-économie-gestion,Droit,321999
BTS,BTS - Services,Management Commercial Opérationnel,291727
DUT,DUT - Service,Techniques de commercialisation,214800
DUT,DUT - Service,Gestion des entreprises et des administrations,205799
CPGE,Classe préparatoire scientifique,MPSI,198311
BTS,BTS - Services,Négociation et digitalisation de la Relation Client,193432
CPGE,Classe préparatoire scientifique,PCSI,183942

executer sur windows 
C:\Users\bmanaa\Documents\HadoopPython
pip install matplotlib
cat result.txt | python3 result_spark.py

