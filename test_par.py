import mathlib

def test_calc_square_1():
    result =mathlib.calc_square(5)
    assert result==25


def test_calc_square_2():
    result =mathlib.calc_square(9)       
    assert result==81


def test_calc_square_3():
    result =mathlib.calc_square(10)
    assert result==100
     # here again repetition of code.

    

    
    import mathlib
    import pytest

    @pytest.mark.parametrize("test_input, test_output",
              [
              (5,25),
              (9,81),
              (10,100)




              ]
    
    
    )
    def test_calc_square(test_input, expected_output):
        result= mathlib.calc_square(test_input)
        assert result ==expected_output
    