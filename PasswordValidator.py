from re import compile, VERBOSE


regex = (
    '^'
)
def valid(password):
    passwordRegex = re.compile(r'''(
        ^(?=.*?[A-Z])                
        (?=.*?[0-9])                 
        (?=.*?[a-z])          
        .{6,}                             
        $
        )''', re.VERBOSE)    
    mo = passwordRegex.search(password)
    if (not mo):
     
        return False
    else:
        return True


valid('ghdfj32')