

'''
from session10 import hello 
import sys

if len(sys.argv) !=2:
    print ("too few line arguments")

else:
    hello (sys.argv[1])
'''


'''
from session10 import square

def test_square():
    if square(2)!=4:
        print("2 squared is not equal to 4")
    if square(3) !=9:
        print ("3 square is not equal to 9")
    if square(4) !=16:
        print ("4 square is not equal to 16")
    else:
        print ("everything is correct")

if __name__=="__main__":
    test_square()

'''


'''
from session10 import square
import pytest

def test_square():
    assert square(2) == 4 
    assert square(3) == 9 
    assert square(4) == 16 
    assert square (-2) == 4 
    assert square (-3) == 9 

    if __name__ == "__main__":
        main()
'''


'''
def test_square():
    try:
        assert square(2) == 4 
    except AssertionError:
        sys.exit("2 square not equal to 4")
    try:
        assert square(3) == 9 
    except AssertionError:
        sys.exit("3 square not equal to 9")
    try:
        assert square(4) == 16 
    except AssertionError:
        sys.exit("4 square not equal to 16")
    try:
        assert square(-2) == 4 
    except AssertionError:
        sys.exit("-2 square not equal to 4")
    try:
        assert square(-3) == 9 
    except AssertionError:
        sys.exit("-3 square not equal to 9")

 if __name__ == "__main__":
    test_square()
    '''


'''
from session10 import square
import pytest

def test_positive():
    assert square(2) == 4 
    assert square(3) == 9 
    assert square(4) == 16 

def test_negative():
    assert square (-2) == 4 
    assert square (-3) == 9 
    assert square (-5) == 25 

def test_zero():
    assert square(0) == 0 

def test_string():
    with pytest.raises(TypeError):
        square('cat')
'''

'''
import pytest

def test_greet():
    assert greet ("harry") == "hello harry"
    assert greet ("hermoine") == "hello hermione"
'''




from session10 import ciphered
import pytest

def test_characters():
    assert ciphered('a') == "y"
    assert ciphered('z') == "o"
    assert ciphered('m') == "a"

def test_strings():
    assert ciphered('hi') == "ef"
    assert ciphered('good') == "vqqs"

