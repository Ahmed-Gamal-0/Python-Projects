import string
import random


def generate_password():
    
    # all the letters from A to Z in upper case --> ABCDEFGHIJKLMNOPQRSTUVWXYZ
    s1 = string.ascii_uppercase 

    # all the letters from A to Z in lower case --> abcdefghijklmnopqrstuvwxyz
    s2 = string.ascii_lowercase

    #all the numbers from 0 to 9 --> 0 1 2 3 4 5 6 7 8 9
    s3 = string.digits

    #all the special character -->  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    s4 = string.punctuation
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    
    password_length = int(input("Enter Password Length: "))
    
                
    # make the elements in list randomly ordered
    random.shuffle(s)


    generated_password = ( "".join( s[0:password_length] ) )
    print(generated_password)
    
    

    
    
    
generate_password()