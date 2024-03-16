import pytest

class NotInRange(Exception):
    #Exception = 'Vales not in Range'
    def __init__(self, Exception='value not in range'):
        #self.input = input_
        self.Exception = Exception
        super().__init__(self.Exception)

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
            if a not in range(10,20):
                raise NotInRange
    