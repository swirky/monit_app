import random, datetime

class Simulations:
    def get_temp_sensor1():
        return round(random.uniform(20, 30), 1)

    def get_temp_sensor2():
        return round(random.uniform(20,30),1)

    def get_humidity():
        return random.randint(0, 100)

    def get_current_datetime():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")