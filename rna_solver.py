"""
RNA Perfect Matching Solver
Rosalind Bioinformatics Problem Solver
"""

import math


def count_perfect_matchings(rna_string):
    """
    RNA string'indeki perfect matching sayısını hesaplar.
    
    Args:
        rna_string (str): RNA dizisi (A, U, C, G bazlarından oluşur)
    
    Returns:
        int: Perfect matching sayısı
    
    Perfect matching için:
    - A sayısı = U sayısı olmalı
    - C sayısı = G sayısı olmalı
    
    Formül: n! × m! 
    (n = A veya U sayısı, m = C veya G sayısı)
    """
    
    # Her bazın sayısını say
    count_A = rna_string.count('A')
    count_U = rna_string.count('U')
    count_C = rna_string.count('C')
    count_G = rna_string.count('G')
    
    # Eşitlik kontrolü (perfect matching için gerekli)
    if count_A != count_U or count_C != count_G:
        print("UYARI: Perfect matching mümkün değil!")
        print(f"A={count_A}, U={count_U}, C={count_C}, G={count_G}")
        return 0
    
    # n! × m! hesapla
    result = math.factorial(count_A) * math.factorial(count_C)
    
    return result


def read_fasta_file(filename):
    """
    FASTA formatındaki dosyayı okur
    
    Args:
        filename (str): Dosya yolu
    
    Returns:
        tuple: (rna_id, rna_string)
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    rna_id = lines[0].strip()
    rna_string = ''.join(line.strip() for line in lines[1:])
    
    return rna_id, rna_string


def solve_from_input(input_text):
    """
    Kopyala-yapıştır yapılan input'u işler
    
    Args:
        input_text (str): FASTA formatında RNA verisi
    
    Returns:
        int: Perfect matching sayısı
    """
    lines = input_text.strip().split('\n')
    rna_id = lines[0]
    rna_string = ''.join(lines[1:])
    
    result = count_perfect_matchings(rna_string)
    
    print(f"RNA ID: {rna_id}")
    print(f"RNA String: {rna_string}")
    print(f"A: {rna_string.count('A')}, U: {rna_string.count('U')}")
    print(f"C: {rna_string.count('C')}, G: {rna_string.count('G')}")
    print(f"\nPerfect Matchings: {result}")
    
    return result


def main():
    """Ana program"""
    
    print("=" * 60)
    print("RNA PERFECT MATCHING SOLVER")
    print("=" * 60)
    
    # ÖRNEK TEST
    print("\n📝 ÖRNEK TEST")
    print("-" * 60)
    sample_input = """>Rosalind_23
AGCUAGUCAU"""
    
    solve_from_input(sample_input)
    
    # GERÇEK PROBLEM
    print("\n" + "=" * 60)
    print("🧬 GERÇEK PROBLEM")
    print("=" * 60)
    print("Aşağıdaki 'your_input' değişkenine verinizi yapıştırın:\n")
    
    # ====== BURAYA VERİNİZİ YAPIŞTIRIN ======
    your_input = """>Rosalind_23
AGCUAGUCAU"""
    
    result = solve_from_input(your_input)
    
    # Sonucu dosyaya yaz
    with open('output.txt', 'w') as f:
        f.write(str(result))
    
    print(f"\n✅ Sonuç 'output.txt' dosyasına kaydedildi: {result}")


if __name__ == "__main__":
    main()
```

### 3. **.gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Output files
output.txt

# OS
.DS_Store
Thumbs.db
