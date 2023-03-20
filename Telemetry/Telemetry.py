import time
import struct
# as time progresses, the next_send value is automatically lower

class TelemetryField:
    #* PASS
    def __init__(self, priority, desired_interval, id, val=0):
        self.priority = priority
        self.desired_interval = desired_interval #interval of 0 is everytime
        self.val = val
        self.next_send = time.time() + desired_interval
        self.id = id

    #* PASS
    def get_info(self):
        return [self.val, self.priority, self.desired_interval, self.next_send, self.id]

    #* PASS
    def update(self, new_val):
        self.val = new_val


class Telemetry: 
    #* PASS
    def __init__(self):
        self.fields = {}

        return

    #* PASS
    def register_field(self, priority, desired_interval, name, val=0):
        new_field = TelemetryField(priority, desired_interval, len(self.fields) + 1,  val)
        self.fields[name] = new_field
        return

    #* PASS
    def update_field(self, field_name, new_value):
        field = self.fields[field_name]
        field.update(new_value)

    #* PASS: for Debugging
    def print_fields(self):
        for key in self.fields:
            field = self.fields[key]
            print({key: field.get_info()})

    #* PASS
    def get_telemetry_frame(self, num_vals=3):
        needs_sending = []
        priorities = []
        
        # getting list of all fields that need to be sent
        for key in self.fields:
            field = self.fields[key]
            field_info = field.get_info()

            if field_info[3] <= time.time():
                needs_sending.append({key: field_info})
                priorities.append(field_info[1])

        #? debugging: if nothing has to send
        if len(priorities) == 0:
            return []
    
        # ordering list by priority
        priorities.sort(reverse=True)
    
        # minimum priority val that needs to be sent
        min_priority = priorities[-1]

        send_list = []
        for obj in needs_sending:
            for key in obj:
                data = obj[key]
                if (data[1] >= min_priority):
                    # for field that is sending
                    send_list.append(obj)
                    data[3] = time.time()
                
            
        return send_list

    #* PASS
    # returns field id, value
    def get_cleaned_telemetry_frame(self, num_vals=3):
        #? get original frame
        frame = self.get_telemetry_frame(num_vals)
        cleaned_frame = []

        #? data structure: [{'field_name': [value, priority, interval, name]}]
        for dict in frame:
            [data] = [(dict[name][-1], dict[name][0]) for name in dict]
            cleaned_frame.append(data)

        return cleaned_frame


    #* PASS: Send tuple (unpacking string, data)
    # data: supposed to send  field id, field value
    def get_packed_telemetry_frame(self, num_vals=3):
        # contains array of tuples (field_id, value)
        initial_frame = self.get_cleaned_telemetry_frame(num_vals)

        # will send string format for unpacking. need to build string
        packing_string_format = ""
        data_to_be_packed = []
        for pair in initial_frame:
            packing_string_format += "I" 
            data_to_be_packed.append(pair[0])  # add field id
            #?need to add error handling if value to send is not int
            packing_string_format += "i"
            data_to_be_packed.append(pair[1]) # add field value to send

        packed_frame = struct.pack(packing_string_format, *data_to_be_packed)

        return (packing_string_format, packed_frame)