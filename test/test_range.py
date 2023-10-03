###
from src.range_function import ranges
import pytest

def test_point():
    assert ranges([[-3, 0], [-0., 4.5]]) == [0,0]
    
    
    
### Scenario 1 - overlap at a point
- Parameters: [[-3, 0], [-0., 4.5]]
- Result: [0, 0]