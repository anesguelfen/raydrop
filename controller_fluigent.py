from fluigent_sdk import FluigentDevice

def apply_pressure(channel_pressures):
    controller = FluigentDevice()
    for channel, pressure in channel_pressures.items():
        controller.set_pressure(channel, pressure)
    print("Fluigent pressures applied.")

if __name__ == "__main__":
    pressures = {
        1: 150,  
        2: 120,
        3: 100
    }
    apply_pressure(pressures)