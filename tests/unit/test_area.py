import pytest
from src.area import calculate_area_square

def test_calculate_area_square():  
    assert calculate_area_square(2) == 4  
    assert calculate_area_square(2.5) == 6.25
    assert calculate_area_square(3) == 9

  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-1) 

def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  