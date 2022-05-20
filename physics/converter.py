# Temperature Converter

def kelvin_to_celcius(temperature: float) -> float:
    return temperature-273

def kelvin_to_farenheit(temperature: float) -> float:
    return temperature*1.8-459.67

def kelvin_to_rankine(temperature:float) -> float:
    return temperature*1.8

def fahrenheit_to_kelvin(temperature: float) -> float:
    return (temperature+459.67)/1.8

def fahrenheit_to_celcius(temperature: float) -> float:
    return (temperature-32)*1.8

def fahrenheit_to_rankine(temperature: float) -> float:
    return temperature+459,67

def celcius_to_kelvin(temperature: float) -> float:
    return temperature+273

def celcius_to_fahrenheit(temperature: float) -> float:
    return temperature*1.8+32

def celcius_to_rankine(temperature: float) -> float:
    return ((temperature+1.8)+32)+459.67

def rankine_to_kelvin(temperature: float) -> float:
    return temperature/1.8

def rankine_to_fahrenheit(temperature: float) -> float:
    return temperature-459.67

def rankine_to_celcius(temperature: float) -> float:
    return ((temperature-32)-459.67)/1.8
