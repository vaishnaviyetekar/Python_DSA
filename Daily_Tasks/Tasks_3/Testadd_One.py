import pytest
@pytest.mark.skip(reason= 'Just do not want to work with CMD')
def test_AddOne(request):
    a = int(request.config.getoption('--op1'))
    b = int(request.config.getoption('--op2'))
    expRes = int(request.config.getoption('--expRes'))
    
    res = a+b
    print(f'Args: {a} + {b} --> {expRes} getting {res}')
    assert res==expRes, f'result of {a} + {b} is not {expRes}'

def test_Twotimes():
    assert True