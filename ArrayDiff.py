def array_diff(a, b):
    if not b:
        return a

    for i in b:
        if i in a:
            for j in range(a.count(i)):
                a.remove(i)
        
    return a 
   
  

array_diff([1,2,2,3], [1,2])
