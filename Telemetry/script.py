import random
fields = ['temp', 'power', 'satellite', 'cubesat', 'battery', 'beacon', 'blink', 'imu', 'time', 'abc', 'def', 'ghi']
for x in fields:
    num = random.randint(0, 100)
    num2 = random.randint(0, 10)
    print("telem.register_field(" + str(num) + ", " + str(num2) + ", '" + x + "')")