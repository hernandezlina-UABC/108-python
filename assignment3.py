# ************OBSOLETE/UNSUCCESSFUL*************
# Create a comparison table of the four main Python collections: rows: List, Dictionary, Set, and Tuple
# 1.  Organize the information in a table.
# If you complete the table in your VS Code project, Submit the GitHub repository URL in a comment.
# If you complete the table in your notebook, upload a clear image of your work.
# 2.  Your table must include the following columns:
# Data Structure
# Syntax Example
# Ordered
# Mutable
# Allows Duplicates
# Access Method
title= "Main Python Collections Comparison"
rows = {
        "row1": {"data structure":"List", "Syntax Example":"[10, 20, 30]", "Ordered":"Yes", "Mutable":"Yes", "Allows Duplicates":"Yes", "Access Method":"list[0]"},
        "row2": {"data structure":"Dictionary", "Syntax Example":"{KEY: VALUE}", "Ordered":"...", "Mutable":"...", "Allows Duplicates":"...", "Access Method":"dictionary.get('KEY')"},
        "row3": {"data structure":"Set", "Syntax Example":"{1, 2, 3}", "Ordered":"No", "Mutable":"...", "Allows Duplicates":"No", "Access Method":"..."},
        "row4": {"data structure":"Tuple", "Syntax Example":"('apple','banana')", "Ordered":"...", "Mutable":"No", "Allows Duplicates":"...", "Access Method":"..."},
}
columns = ["Data Structure", "Syntax Example", "Ordered", "Mutable", "Allows Duplicates", "Access Method" ]
print(title)
for row in rows:
    for col in columns:
        print(f"({row}, {col})", end=" ")
    print()