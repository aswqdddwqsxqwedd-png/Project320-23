import pytest
import functionInoyatov

def test_funcinoyatov():
    assert functionInoyatov.inoyatov (25,5)==5
    assert functionInoyatov.inoyatov (3,1)==3
    assert functionInoyatov.inoyatov (12,2)==6
    assert functionInoyatov.inoyatov (15,3)==5
    assert functionInoyatov.inoyatov (48,8)==6
    assert functionInoyatov.inoyatov (36,6)== 5
