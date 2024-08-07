def get(msg):
    print(f'Enter the {msg.upper()} value: ', end='')
    val = input().strip()
    return val.title()

def efficiency(distance, fuel):
    return distance/fuel

def efficiency_quotient_for_car(efficiency):
    if efficiency>20:
        return 'EXCELLENT'
    elif efficiency>=15 and efficiency<=20:
        return 'GOOD'
    elif efficiency>=10 and efficiency<15:
        return 'AVERAGE'
    else:
        return 'POOR'
    
def efficiency_quotient_for_bike(efficiency):
    if efficiency>30:
        return 'EXCELLENT'
    elif efficiency>=20 and efficiency<=30:
        return 'GOOD'
    elif efficiency>=15 and efficiency<20:
        return 'AVERAGE'
    else:
        return 'POOR'

def check_efficiency(vehicle_type):
    distance = float(get('Distance'))
    fuel = float(get('Fuel Amount'))
    if fuel == 0 or distance ==0:
        print('Invalid Details')
        return 0,0,'Invalid'
    else:
        res = 'Invalid'
        match vehicle_type:
            case 'Car':
                res = efficiency_quotient_for_car(efficiency(distance, fuel))
            case 'Bike':
                res = efficiency_quotient_for_bike(efficiency(distance, fuel))
            case _:
                print('Invalid Vehicle Type')
        return distance, fuel, res
        
def form_print(check):
    if check[2]=='Invalid':
        print("Oops!!! Form can't be generated")
    else:
        print('Fuel Efficiency Details')
        print('*'*20)
        print(f'Vehicle Type : {vehicle_type}')
        print(f'Distance : {check[0]}')
        print(f'Fuel : {check[1]}')
        print(f'Efficiency : {check[2]}')

vehicle_type = get('Vehicle Type')
form_print(check_efficiency(vehicle_type))

