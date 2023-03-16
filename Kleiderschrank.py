# Erstellen der Listen
kleiderschrank = ["Hose", "T-Shirt", "Kleid"]
kommode = ["Schuhe", "Socken", "Mützen"]

# Ausgabe jedes Elements des Kleiderschranks
print(kleiderschrank[0])  # Ausgabe: Hose
print(kleiderschrank[1])  # Ausgabe: T-Shirt
print(kleiderschrank[2])  # Ausgabe: Kleid

# Ausgabe aller Elemente des Kleiderschranks mit einer For-Schleife
for kleidungsstueck in kleiderschrank:
    print(kleidungsstueck)

# Hinzufügen eines Pullovers zum Kleiderschrank
kleiderschrank.append("Pullover")

# Hinzufügen des Inhalts der Kommode zum Kleiderschrank
kleiderschrank.extend(kommode)

# Ausgabe aller Elemente des erweiterten Kleiderschranks mit einer For-Schleife
for kleidungsstueck in kleiderschrank:
    print(kleidungsstueck)
