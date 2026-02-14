# Leetcode 799. Champagne Tower

# https://leetcode.com/problems/champagne-tower/description/

def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    # table[c] = amount in current row at position c (uncapped)
    table: list[float] = [0.0] * (query_row + 2)
    table[0] = float(poured)

    for row in range(query_row):
        next_row = [0.0] * (query_row + 2)
        for c in range(row + 1):
            overflow = max(0.0, table[c] - 1.0)
            if overflow > 0.0:
                next_row[c] += overflow / 2.0
                next_row[c + 1] += overflow / 2.0
        table = next_row

    return min(1.0, table[query_glass])

# O(query_row^2) - Time complexity
# O(query_row) - Space complexity