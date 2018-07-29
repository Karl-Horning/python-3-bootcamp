def compact(collection):
    return [item for item in collection if item]

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]