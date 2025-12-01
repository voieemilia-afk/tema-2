elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]
elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"
interogari_nume = ["Ana", "Mara", "Elena", "stop"]
absente = [1, 0, 2, 3, 0]
print("Lista elevilor cu notele lor:")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print("\n Nota maximă și minimă:")
nota_max = max(note)
nota_min = min(note)
elev_max = [elevi[i] for i in range(len(note)) if note[i] == nota_max]
elev_min = [elevi[i] for i in range(len(note)) if note[i] == nota_min]
print(f"Nota maximă: {nota_max}, elev(i): {', '.join(elev_max)}")
print(f"Nota minimă: {nota_min}, elev(i): {', '.join(elev_min)}")
print("\n Media clasei:")
media = sum(note)/len(note)
print(f"Media clasei: {media:.2f}")
print("\n Elevii promovați:")
for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])
print("\n +1 punct fiecărei note (max 10):")
for i in range(len(note)):
    note[i] = min(note[i]+1, 10)
print("Note actualizate:", note)
print("\n Adaugă elevul predefinit:")
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("Elevi:", elevi)
print("Note:", note)
print("\n Șterge elevul predefinit:")
if elev_de_sters in elevi:
    index = elevi.index(elev_de_sters)
    elevi.pop(index)
    note.pop(index)
print("Elevi după ștergere:", elevi)
print("Note după ștergere:", note)

print("\n Lista elevilor cu notele după actualizări:")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print("\n Căutări de nume cu while:")
i = 0
while i < len(interogari_nume):
    nume = interogari_nume[i]
    if nume == "stop":
        break
    if nume in elevi:
        index = elevi.index(nume)
        print(f"{nume} are nota {note[index]}")
    else:
        print(f"{nume} nu există în catalog")
    i += 1

print("\n Număr promovați / respinși:")
promovati = sum(1 for n in note if n >= 5)
respinsi = sum(1 for n in note if n < 5)
print(f"Promovați: {promovati}, Respinși: {respinsi}")

print("\n Media promovaților:")
note_promovati = [n for n in note if n >= 5]
if note_promovati:
    media_promovati = sum(note_promovati)/len(note_promovati)
    print(f"Media promovaților: {media_promovati:.2f}")
else:
    print("Nu există elevi promovați")




