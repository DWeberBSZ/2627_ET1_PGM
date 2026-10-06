a = "text"


ist_int = isinstance(a, int)

if ist_int:
    print("Die Variable ist vom Datentyp Integer")
    
else: # kein Integer
    # restliche Fälle überprüfen (andere Datentypen)
    ist_float = isinstance(a, float) # ...
    
    if ist_float:
        print("Die Variable ist vom Datentyp float")
        
    else: 
        ist_bool = isinstance(a, bool)
        
        if ist_bool:
            print("Die Variable ist vom Datentyp Bool")
            
        else: 
            ist_String = isinstance(a, str)
            
            if ist_String:
                print("Die Variable ist vom Datentyp str")
            
