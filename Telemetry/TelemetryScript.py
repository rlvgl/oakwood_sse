import Telemetry 
import time
import struct


# Telemetry.register_field(priority, desired_interval, name, val)
telem = Telemetry.Telemetry()
telem.register_field(58, 7, 'temp')
telem.register_field(63, 4, 'power', 6)
telem.register_field(15, 8, 'satellite')
telem.register_field(0, 10, 'cubesat')
telem.register_field(77, 1, 'battery', 43)
telem.register_field(76, 8, 'beacon')
telem.register_field(100, 10, 'blink')
telem.register_field(95, 10, 'imu')
telem.register_field(98, 8, 'time')
# telem.register_field(48, 10, 'abc')
# telem.register_field(71, 4, 'def')
# telem.register_field(36, 9, 'ghi')

#? Testing print_fields
# telem.print_fields()

#? Testing update_field
# telem.update_field('temp', 10)
# telem.print_fields()

#? Testing get_telemetry_frame
# time.sleep(5)
# print(telem.get_cleaned_telemetry_frame())

#? Testing get_packed_telemetry_frame
time.sleep(10)
data = telem.get_packed_telemetry_frame()
print(struct.unpack(data[0], data[1]))
