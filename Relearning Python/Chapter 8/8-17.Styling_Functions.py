"""
 Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""
def make_sandwhich(*demands):
    """Prints out all the things the user wants in their sandwhich"""
    print(f"You wanted {len(demands)} things in your sandwhich:")
    for i in demands:
        print(f"- {i}")
        
make_sandwhich('meat1', 'meat2', 'meat3')