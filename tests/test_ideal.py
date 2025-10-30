"""
This module tests and validates output from the ideal.py module. 
"""

from rocket_relations.ideal import find_characteristic_velocity
from rocket_relations.ideal import find_thrust_coefficient


def test_char_vel():
    assert find_characteristic_velocity(1.2, 350, 3500) == 1706.6214

def test_thrust_coeff():
    assert find_thrust_coefficient(0.02, 0.0125, 10, 1.2) == 1.5423079
