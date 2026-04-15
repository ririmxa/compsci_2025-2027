#Class Definition & Encapsulation:DONE
#Define a class named SmartDevice.
#It must have three private attributes: device_id (string), is_on (boolean, default False), and base_power_draw (integer, representing watts).
#Implement appropriate public getter and setter methods to access and modify all attributes, ensuring encapsulation (e.g., power draw cannot be set to a negative number).

#Methods:DONE
#Implement a toggle_power() method that switches the is_on state (if it is True, make it False, and vice versa).
#Implement a get_current_usage() method. If is_on is True, it returns the base_power_draw. If is_on is False, it returns 0.

#Instantiation & Testing (Main Program):
#Instantiate at least three different SmartDevice objects (e.g., a TV, a Fan, a Speaker) with different base power draws.
#Write a short test that turns some devices on, leaves others off, and calculates the total current power usage of all devices combined.

#Documentation:
#Include a few lines of comments to shortly describe the logic implemented in that section of the program. A few words about what is being implemented would suffice.

#Class Definition & Encapsulation:
class SmartDevice:
    def __init__ (self, device_id, base_power_draw=0, is_on=False):
        self.__device_id = device_id
        self.__is_on = is_on
        self.__base_power_draw = base_power_draw
    def get_device_id(self):
        return self.__device_id
    def get_is_on(self):
        return self.__is_on
    def get_base_power_draw(self):
        return self.__base_power_draw
    def set_device_id(self, device_id):
        self.__device_id = device_id
    def set_is_on(self, is_on):
        self.__is_on = bool(is_on)
    def set_base_power_draw(self, power):
        if  power < 0:
            raise ValueError("Power draw cannot be negative.") #when power less than zero
        else:
            self.__base_power_draw = power 
    def toggle_power(self):
        self.__is_on = not self.__is_on #changes the power from on and off
    def get_current_usage(self):
        return self.__base_power_draw if self.__is_on else 0 #checks if device is on or off when on - returns current power, when off - returns 0
    

class SmartLight(SmartDevice):
    def __init__(self, device_id, brightness=100, is_on=False, base_power_draw=0):
        super().__init__(device_id,base_power_draw, is_on)
        self.__brightness = brightness
    def get_brightness(self):
        return self.__brightness
    def set_brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness= value
    def get_current_usage(self):
        if not self.get_is_on():
            return 0
        return (self.__brightness / 100) * self.get_base_power_draw()
    


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, target_temperature, is_on, base_power_draw):
        super().__init__(device_id, base_power_draw, is_on)
        self.__target_temperature = target_temperature
    def get_target_temperature(self):
        return self.__target_temperature
    def set_target_temperature(self, temp):
        self.__target_temperature = float(temp)
    def get_current_usage(self):
        if not self.get_is_on():
            return 0
        return self.get_base_power_draw() + 500
    
class Room:
    def __init__(self, room_name):
        self.__room_name= room_name
        self.__device_list = []
    def get_room_name(self):
        return self.__room_name
    def add_device(self, device):
        self.__device_list.append(device)
    def get_room_power_usage(self):
        total = 0
        for device in self.__device_list:
            total += device.get_current_usage()
        return total


#Instantiation & Testing (Main Program):
living_room = Room("Living Room")
kitchen = Room("Kitchen")

object1 = SmartDevice("TV", base_power_draw = 200)
object2 = SmartThermostat("Heater", 22.0, False, 150)
object3 = SmartLight("Lamp", 100, False, 50)

object1.toggle_power() #turns TV on
object2.toggle_power() 

devices = [object1, object2, object3]
total_usage = sum(device.get_current_usage() for device in devices) #adds all the object from "devices" and calculates the overall sum

print ("Device Status:")
for x in devices:
    print(f"{x.get_device_id()}: On = {x.get_is_on()}, Usage = {x.get_current_usage()}W")

print(f"Total Current Power Usage: {total_usage}W")

