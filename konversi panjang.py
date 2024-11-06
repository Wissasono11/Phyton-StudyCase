def meter_ke_kilo(meter):
    return meter / 1000

def meter_ke_mil(meter):
    return meter / 1609.34

def meter_ke_yard(meter):
    return meter * 1.09361

def meter_ke_foot(meter):
    return meter * 3.28084

def kilometer_ke_meter(kilometer):
    return kilometer * 1000

def mile_ke_meter(mile):
    return mile * 1609.34

def yard_ke_meter(yard):
    return yard / 1.09361

def foot_ke_meter(foot):
    return foot / 3.28084

def convert_length(value, from_unit, ke_unit):
    # Convert the input value ke meters first
    if from_unit == 'meter':
        meter_value = value
    elif from_unit == 'kilometer':
        meter_value = kilometer_ke_meter(value)
    elif from_unit == 'mile':
        meter_value = mile_ke_meter(value)
    elif from_unit == 'yard':
        meter_value = yard_ke_meter(value)
    elif from_unit == 'foot':
        meter_value = foot_ke_meter(value)
    else:
        return None
    
    # Convert from meters ke the desired unit
    if ke_unit == 'meter':
        return meter_value
    elif ke_unit == 'kilometer':
        return meter_ke_kilo(meter_value)
    elif ke_unit == 'mile':
        return meter_ke_mil(meter_value)
    elif ke_unit == 'yard':
        return meter_ke_yard(meter_value)
    elif ke_unit == 'foot':
        return meter_ke_foot(meter_value)
    else:
        return None

# Conkeh penggunaan
value = 1000  # nilai yang akan dikonversi
from_unit = 'meter'  # unit asal
ke_unit = 'kilometer'  # unit tujuan

converted_value = convert_length(value, from_unit, ke_unit)
print(f"{value} {from_unit} = {converted_value} {ke_unit}")
