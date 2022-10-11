from dict_list import DictList

A = DictList([
    {"id" : 1, "drink" : "coffee", "price" : 10, "quantity" : 2},
    {"id" : 2, "drink" : "tea", "price" : 8, "quantity" : 3}])

A["total_price"] = A.map(lambda row: row["price"] * row["quantity"])