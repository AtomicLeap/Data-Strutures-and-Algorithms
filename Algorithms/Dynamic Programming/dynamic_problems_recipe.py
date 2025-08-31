# Dynamic programming

# Dynamic programming problems can be solved using:
# 1. Memoizatoin strategy
# 2. Tabulation strategy

# Memoization Recipe
# 1. Make it work
#   1.1 Visualize the problem as a tree.
#   1.2 Use the tree leaves as our base cases.
#   1.3 Implement the tree using recursion.
#   1.4 Test it.
# 2. Make it efficient
#   2.1 Add a memo dict/object.
#   2.2 Add a base case to return memo value.
#   2.3 Store return values into the memo.

# Tabuation Recipe
# 1. Visualize the problem as a table.
# 2. Size the table based on the inputs.
# 3. Initialize the table with default values -> use values compatible with return type.
# 4. Seed the trivial answer into the table - base case value(s).
# 5. Iterate through the table.
# 6. Fill further positions based on the current positions value.