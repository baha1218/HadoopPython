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
