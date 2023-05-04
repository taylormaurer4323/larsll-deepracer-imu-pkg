from BMI160_i2c import Driver

print('Attempt of initialization')
sensor = Driver(0x68, 2)
