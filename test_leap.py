import python2_test2

def test_leap():
    year1 = 2020
    year2 = 2019
    year3 = 1900
    
    value = python2_test2.leap(year1)
    assert value == True
    
    value = python2_test2.leap(year2)
    assert value == False
    
    value = python2_test2.leap(year3)
    assert value == False