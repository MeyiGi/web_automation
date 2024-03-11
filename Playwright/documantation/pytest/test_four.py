import pytest
from test_three import Task

def test_asdict():
    t_task = Task("do something", "Jack", True, 21)
    t_dict = t_task._asdict()
    expected = {"summary" : "do something", "owner" : "Jack", "done" : True, "id" : 21}
    
    assert t_dict == expected
    
@pytest.mark.important_test
def test_replace():
    t_before = Task("do homework", "Daniel", False)
    t_after = t_before._replace(id=10, done=True)
    t_after = t_after._asdict()
    expected = {"summary" : "do homework", "owner" : "Daniel", "done" : True, "id" : 10}
    
    assert t_after == expected