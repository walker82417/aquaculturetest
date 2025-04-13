import random

def get_sensor_data():
    data = {
        'ph': round(random.uniform(6.5, 7.5), 2),
        'temperature': round(random.uniform(25, 35), 2),
        'turbidity': round(random.uniform(50, 100), 2),
        'flow': round(random.uniform(8, 10), 2)
    }
    return data
