# Algorithm Documentation

## Perfect Matchings in RNA Secondary Structures

### Problem Statement

Given an RNA string `s`, calculate the total number of perfect matchings of basepair edges in the bonding graph of `s`.

### Background

#### RNA Base Pairing

RNA is single-stranded and contains four nucleotide bases:
- **Adenine (A)** pairs with **Uracil (U)**
- **Cytosine (C)** pairs with **Guanine (G)**

These base pairs form through hydrogen bonding, similar to DNA but with uracil replacing thymine.

#### Secondary Structure

When RNA folds upon itself, complementary bases can form pairs, creating secondary structures like:
- Hairpin loops
- Stem loops
- Pseudoknots

### Graph Theory Formulation

#### Bonding Graph

For an RNA string `s = s₁s₂...sₙ`:

1. **Nodes**: Each nucleotide `sᵢ` becomes a node
2. **Adjacency Edges**: Connect consecutive nucleotides in sequence (forming a path or circle)
3. **Basepair Edges**: Connect complementary bases:
   - `{A, U}` edges (dashed)
   - `{C, G}` edges (dashed)

#### Perfect Matching

A **perfect matching** M is a subset of basepair edges where:
- Every node appears in exactly one edge
- No two edges share a node

### Mathematical Solution

#### Counting Formula

Let:
- `nₐ` = number of adenines (A)
- `nᵤ` = number of uracils (U)  
- `nᴄ` = number of cytosines (C)
- `nɢ` = number of guanines (G)

**Constraint**: For a perfect matching to exist:
```
nₐ = nᵤ  AND  nᴄ = nɢ
```

**Formula**:
```
Perfect Matchings = nₐ! × nᴄ!
```

#### Proof

1. **A-U Pairings**: There are `nₐ` adenines and `nᵤ` uracils. The number of ways to match them in a perfect matching is the number of permutations: `nₐ!`

2. **C-G Pairings**: Similarly, there are `nᴄ!` ways to match cytosines with guanines.

3. **Independence**: The choice of A-U pairings is independent of C-G pairings.

4. **Total**: By the multiplication principle:
   ```
   Total = nₐ! × nᴄ!
   ```

### Example Walkthrough

#### Input
```
>Rosalind_23
AGCUAGUCAU
```

#### Step 1: Count Bases
```
A: 3 occurrences (positions 1, 5, 9)
G: 2 occurrences (positions 2, 6)
C: 2 occurrences (positions 3, 7)
U: 3 occurrences (positions 4, 8, 10)
```

#### Step 2: Verify Balance
```
A = U? → 3 = 3 ✓
C = G? → 2 = 2 ✓
```

#### Step 3: Calculate
```
Perfect Matchings = 3! × 2!
                  = 6 × 2
                  = 12
```

### Implementation

```python
import math

def count_perfect_matchings(rna_string):
    count_A = rna_string.count('A')
    count_U = rna_string.count('U')
    count_C = rna_string.count('C')
    count_G = rna_string.count('G')
    
    if count_A != count_U or count_C != count_G:
        return 0
    
    return math.factorial(count_A) * math.factorial(count_C)
```

### Time Complexity

- **Counting bases**: O(n) where n = length of RNA string
- **Factorial calculation**: O(n) for each factorial
- **Total**: O(n)

### Space Complexity

O(1) - only storing counters and result

### Edge Cases

1. **Empty string**: Returns 1 (empty matching)
2. **Single base**: Returns 0 (cannot form pair)
3. **Unbalanced bases**: Returns 0 (no perfect matching exists)
4. **All same base**: Returns 0 (no complementary bases)

### Related Concepts

- **Catalan Numbers**: Count non-crossing perfect matchings
- **RNA Folding Prediction**: Uses dynamic programming
- **Maximum Matching**: Finding largest matching (not necessarily perfect)
- **Bipartite Matching**: Can model A-U and C-G as bipartite graphs

### References

1. [Rosalind PMCH Problem](http://rosalind.info/problems/pmch/)
2. Combinatorics and Graph Theory in Bioinformatics
3. RNA Secondary Structure Prediction Algorithms

---

**Note**: This simplified model assumes all bases can potentially pair with any complementary base. In reality, RNA secondary structure prediction must consider:
- Spatial constraints
- Energy minimization
- Non-crossing constraints (planarity)
- Pseudoknots

These factors make real RNA folding prediction an NP-hard problem!
