# 🧬 RNA Perfect Matching Solver

Rosalind platformundaki "Perfect Matchings and RNA Secondary Structures" problemini çözen Python scripti.

🌍 **Languages / Diller / Sprachen:**  
[🇹🇷 Türkçe](#-türkçe) | [🇬🇧 English](#-english) | [🇩🇪 Deutsch](#-deutsch)

---

## 🇹🇷 Türkçe

## 📋 Problem Açıklaması
RNA moleküllerinde baz çiftleri (A-U ve C-G) oluşturarak ikincil yapılar meydana gelir. Bu program, verilen bir RNA dizisindeki mümkün olan tüm mükemmel eşleşmelerin (perfect matchings) sayısını hesaplar.

## 🚀 Kullanım
    python rna_solver.py

Script içindeki `your_input` kısmına Rosalind'den aldığınız veriyi yapıştırın.

## 📊 Örnek

**Input:**
    >Rosalind_23
    AGCUAGUCAU

**Output:**
    12

## 🧮 Algoritma
Program şu adımları takip eder:
1. RNA dizisindeki A, U, C, G bazlarını sayar
2. A sayısı = U sayısı ve C sayısı = G sayısı kontrolü yapar
3. Perfect matching sayısını formül ile hesaplar: n! × m!
   - n = A (veya U) sayısı
   - m = C (veya G) sayısı

## 📦 Gereksinimler
- Python 3.6+
- Standart kütüphaneler (math)

## 📝 Lisans
MIT License

## 👨‍💻 Geliştirici
Biyoinformatik problemleri için Mustafa Behram Bozkurt geliştirilmiştir.

## 🔗 Kaynaklar
- http://rosalind.info/problems/pmch/

---

## 🇬🇧 English

## 📋 Problem Description
Python script that solves the "Perfect Matchings and RNA Secondary Structures" problem on the Rosalind platform.

RNA molecules form secondary structures through base pairing (A-U and C-G). This program calculates the total number of possible perfect matchings in a given RNA sequence.

## 🚀 Usage
    python rna_solver.py

Paste your Rosalind input into the `your_input` section inside the script.

## 📊 Example

**Input:**
    >Rosalind_23
    AGCUAGUCAU

**Output:**
    12

## 🧮 Algorithm
The program follows these steps:
1. Count the number of A, U, C, and G bases in the RNA sequence
2. Check if A = U and C = G
3. Compute the number of perfect matchings using: n! × m!
   - n = number of A (or U)
   - m = number of C (or G)

## 📦 Requirements
- Python 3.6+
- Standard libraries (math)

## 📝 License
MIT License

## 👨‍💻 Developer
Developed by Mustafa Behram Bozkurt for bioinformatics problems.

## 🔗 Resources
- http://rosalind.info/problems/pmch/

---

## 🇩🇪 Deutsch

## 📋 Problembeschreibung
Python-Skript zur Lösung des Problems "Perfect Matchings and RNA Secondary Structures" auf der Rosalind-Plattform.

RNA-Moleküle bilden Sekundärstrukturen durch Basenpaarung (A-U und C-G). Dieses Programm berechnet die Anzahl aller möglichen perfekten Matchings in einer gegebenen RNA-Sequenz.

## 🚀 Verwendung
    python rna_solver.py

Fügen Sie die Rosalind-Eingabe in den Abschnitt `your_input` im Skript ein.

## 📊 Beispiel

**Eingabe:**
    >Rosalind_23
    AGCUAGUCAU

**Ausgabe:**
    12

## 🧮 Algorithmus
Das Programm führt folgende Schritte aus:
1. Zählt die Basen A, U, C und G in der RNA-Sequenz
2. Prüft, ob A = U und C = G
3. Berechnet die Anzahl perfekter Matchings mit: n! × m!
   - n = Anzahl von A (oder U)
   - m = Anzahl von C (oder G)

## 📦 Anforderungen
- Python 3.6+
- Standardbibliotheken (math)

## 📝 Lizenz
MIT License

## 👨‍💻 Entwickler
Das Mustafa Behram Bozkurt Projekt wurde entwickelt, um Probleme der Bioinformatik anzugehen.

## 🔗 Ressourcen
- http://rosalind.info/problems/pmch/
