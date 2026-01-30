# Leetcode 2977. Minimum Cost to Convert String II

# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description

# Key idea
"""
Because two operations may only be disjoint or exactly the same interval, 
the final edit plan is:
- pick a set of non-overlapping intervals that you will “work on”;
- within any chosen interval [l..r], you’re allowed to apply any number of 
    substring replacements on that exact same interval, so inside the 
    interval you can do a multi-step conversion:
            source[l..r] →⋯→ target[l..r]
- outside chosen intervals, characters must already match (source[i] == target[i]), 
    because you never touch them.

So the problem becomes:
1. For any length L, compute the minimum cost to convert one length - L string 
    into another using the given rules (can chain rules). This is a shortest-path 
    problem on a graph of strings.
2. Then do a DP over positions to choose disjoint intervals covering exactly the 
    mismatching parts.

Step 1: shortest paths per length
Rules only apply between strings of the same length.

For each length L:
- Collect all strings of that length that appear in original or changed 
    (at most 200 total since arrays size ≤ 100).
- Build a directed weighted graph: original[i] -> changed[i] with weight cost[i] 
    (take min if duplicates).
- Compute all-pairs shortest paths (Floyd–Warshall is fine here because nodes ≤ 200).

Let distL[a][b] = min cost to convert string a to b (both length L), possibly via 
intermediate strings.

Important:
- If source_sub != target_sub, then both must be present in the node set of that 
    length, otherwise conversion is impossible for that interval (since operations 
    can only produce strings that appear in rules).

Step 2: interval DP (weighted interval covering)
Let dp[i] = minimum cost to convert source[0..i-1] into target[0..i-1].
Transition from position i:
- If source[i] == target[i], you can leave this char untouched:
    dp[i+1] = min(dp[i+1], dp[i])

- For every rule length L, consider interval [i .. i+L-1]:
    - let s = source[i:i+L], t = target[i:i+L]
    - if s == t, you can also skip it:
            dp[i+L]=min(dp[i+L],dp[i])
    - else if distL[s][t] exists:
            dp[i+L]=min(dp[i+L],dp[i]+distL[s][t])
This guarantees disjointness because DP moves forward and never overlaps intervals.
"""

from collections import defaultdict

INF = 10**30
MASK = (1 << 64) - 1
BASE = 911382323  # fixed base; 64-bit overflow arithmetic is fine

def min_cost_substring_conversion(
    source: str,
    target: str,
    original: list[str],
    changed: list[str],
    cost: list[int]
) -> int:
    n = len(source)

    # ---------- Rolling hash (uint64) ----------
    def build_prefix(s: str):
        pref = [0] * (len(s) + 1)
        pows = [1] * (len(s) + 1)
        for i, ch in enumerate(s):
            pows[i + 1] = (pows[i] * BASE) & MASK
            pref[i + 1] = (pref[i] * BASE + (ord(ch) - 96)) & MASK  # 'a'->1
        return pref, pows

    prefS, pows = build_prefix(source)
    prefT, _ = build_prefix(target)

    def get_hash(pref, l: int, r: int) -> int:
        # hash of s[l:r]
        return (pref[r] - (pref[l] * pows[r - l] & MASK)) & MASK

    def hash_str(s: str) -> int:
        h = 0
        for ch in s:
            h = (h * BASE + (ord(ch) - 96)) & MASK
        return h

    # ---------- Build per-length node sets ----------
    len_to_nodes: dict[int, List[str]] = defaultdict(list)
    len_to_node_index: dict[int, dict[str, int]] = defaultdict(dict)

    for a, b in zip(original, changed):
        L = len(a)
        if a not in len_to_node_index[L]:
            len_to_node_index[L][a] = len(len_to_nodes[L])
            len_to_nodes[L].append(a)
        if b not in len_to_node_index[L]:
            len_to_node_index[L][b] = len(len_to_nodes[L])
            len_to_nodes[L].append(b)

    # ---------- Build per-length hash->candidates for fast substring -> node lookup ----------
    # maps: L -> hash64 -> list of (string, idx)
    len_to_hashmap: dict[int, dict[int, list[tuple[str, int]]]] = {}
    for L, nodes in len_to_nodes.items():
        hm = defaultdict(list)
        idx_map = len_to_node_index[L]
        for s in nodes:
            hm[hash_str(s)].append((s, idx_map[s]))
        len_to_hashmap[L] = hm

    def node_id_from_substring(pref, i: int, L: int, base_str: str) -> int:
        """
        Returns node index if base_str[i:i+L] is in node set for length L, else -1.
        Uses hash to avoid slicing unless needed.
        """
        hm = len_to_hashmap.get(L)
        if hm is None:
            return -1
        h = get_hash(pref, i, i + L)
        if h not in hm:
            return -1
        # Possible match: verify by slicing and comparing to candidates
        sub = base_str[i:i + L]
        for cand, idx in hm[h]:
            if cand == sub:
                return idx
        return -1

    # ---------- Floyd-Warshall per length ----------
    len_to_dist: dict[int, list[list[int]]] = {}
    for L, nodes in len_to_nodes.items():
        m = len(nodes)
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        idx_map = len_to_node_index[L]
        # direct edges (take min for duplicates)
        for a, b, c in zip(original, changed, cost):
            if len(a) != L:
                continue
            u = idx_map[a]
            v = idx_map[b]
            if c < dist[u][v]:
                dist[u][v] = c

        # Floyd-Warshall
        for k in range(m):
            dk = dist[k]
            for i in range(m):
                dik = dist[i][k]
                if dik >= INF:
                    continue
                di = dist[i]
                base_val = dik
                for j in range(m):
                    nd = base_val + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        len_to_dist[L] = dist

    lengths = sorted(len_to_nodes.keys())

    # ---------- DP over positions ----------
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] >= INF:
            continue

        # leave 1 char untouched
        if source[i] == target[i]:
            if dp[i] < dp[i + 1]:
                dp[i + 1] = dp[i]

        # try each rule-length interval starting at i
        for L in lengths:
            j = i + L
            if j > n:
                break

            # if substrings equal, can skip whole block
            hs = get_hash(prefS, i, j)
            ht = get_hash(prefT, i, j)
            if hs == ht and source[i:j] == target[i:j]:
                if dp[i] < dp[j]:
                    dp[j] = dp[i]
                continue

            # need actual conversion
            sid = node_id_from_substring(prefS, i, L, source)
            if sid == -1:
                continue
            tid = node_id_from_substring(prefT, i, L, target)
            if tid == -1:
                continue

            d = len_to_dist[L][sid][tid]
            if d >= INF:
                continue
            ndp = dp[i] + d
            if ndp < dp[j]:
                dp[j] = ndp

    return -1 if dp[n] >= INF else dp[n]

# O(100 * 200^3) = 8 * 10^8 - Time complexity
# O(4 * 10^6) - Space complexity

print(min_cost_substring_conversion(
        "abcd", "acbe",
        ["a","b","c","c","e","d"],
        ["b","c","b","e","b","e"],
        [2,5,5,1,2,20]
    ))  # 28
print(min_cost_substring_conversion(
        "abcdefgh", "acdeeghh",
        ["bcd","fgh","thh"],
        ["cde","thh","ghh"],
        [1,3,5]
    ))  # 9
print(min_cost_substring_conversion(
        "abcdefgh", "addddddd",
        ["bcd","defgh"],
        ["ddd","ddddd"],
        [100,1578]
    ))  # -1
