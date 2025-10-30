"""
This module defines functions to calculate the characteristic velocity and thrust coefficient of a rocket using user-defined parameters.
It validates inputs, calculates, and then returns the desired value. 
"""


import numpy as np

def find_characteristic_velocity(gamma, R, T0):
    """
    Determine the characteristic velocity using given inputs.

    PARAMETERS:
    Ratio of Specific Heats (unitless), must be between 1 and 1.8
    Specific Gas Constant (J kg^-1 K^-1), must be greater than 0
    Stagnation Temperature (K), must be greater than 0

    RETURNS:
    Characteristic Velocity (m/s)
    """

    ############ INPUT VALIDATION ############
    # Type Validation
    for i in [gamma, R, T0]:
        if not i.isnumeric():
            raise TypeError("Inputs must be numeric.")
    
    # Domain Validation
    if gamma < 1 or gamma > 1.8:
        raise ValueError("Ratio of Specific Heats must be greater than 1 or less than 1.8.")
    if T0 < 0:
        raise ValueError("Stagnation Temperature in Kelvin must be greater than 0.")
    if R < 0:
        raise ValueError("Specific Gas Constant must be greater than 0.")
    

    ############ CALCULATION ############
    # Use Inputs to solve for characteristic velocity
    c_star = np.sqrt((1/gamma) * ((2/(gamma + 1))^((gamma + 1)/(gamma - 1))) * R * T0)

    # return characteristic velocity in m/s
    return c_star


def find_thrust_coefficient(PaR, PeR, AR, gamma):
    """
    Determine the thrust coefficient using given inputs.

    PARAMETERS:
    Ambient Pressure to Stagnation Pressure Ratio (unitless), must be greater than 1
    Exit Pressure to Stagnation Pressure Ratio (unitless), must be greater than 1
    Area Ratio (unitless), must be greater than 1
    Ratio of Specific Heats (unitless), must be between 1 and 1.8

    RETURNS:
    Characteristic Velocity (m/s)
    """

    ############ INPUT VALIDATION ############
    # Type Validation
    for i in [PaR, PeR, AR, gamma]:
        if not i.isnumeric():
            raise TypeError("Inputs must be numeric.")
    
    # Domain Validation
    if gamma < 1 or gamma > 1.8:
        raise ValueError("Ratio of Specific Heats must be greater than 1 or less than 1.8.")
    if PaR <= 1 or PeR <= 1:
        raise ValueError("Pressure Ratios must be greater than 1.")
    if AR < 1:
        raise ValueError("Area Ratio must be greater than 1.")
    

    ############ CALCULATION ############
    # Use Inputs to solve for characteristic velocity
    CF = np.sqrt(((2*gamma^2)/(gamma - 1)) * ((2/(gamma + 1))^((gamma + 1)/(gamma - 1))) * (1-PeR^((gamma - 1)/gamma))) + AR * (PeR - PaR)

    # return characteristic velocity in m/s
    return CF
