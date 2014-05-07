
def accumulate(coll, op):
    """
    Given a collection and an operation to perform on each element of the
    collection, returns a new collection containing the result of applying
    that operation to each element of the input collection.
    """
    return [op(item) for item in coll]

