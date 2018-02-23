import SIM808lib as s

if __name__ == '__main__':
    port = s.portOpen("/dev/ttyUSB0", baudrate=9600, timeout=5)
    s.check(port)
    #s.set_baudrate(9600,port)
    #s.set_settings(port)
    s.power_gps_on(port)
    s.gps_status(port)
    try:
        x = s.get_coordinate(port)
        l = x.split(",")
        #print(l)
        altitude = float(l[1])/100
        north = float(l[3])/100
        east = float(l[5])/100
        print("Altitude = {}").format(altitude)
        print("North = {}").format(north)
        print("East = {}").format(east)
    except KeyboardInterrupt:
        s.close_gps(port)
        print("That is all!")