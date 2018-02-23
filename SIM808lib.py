import serial


def portOpen(port="/dev/ttyUSB0", baudrate=9600, timeout=5):
    return serial.Serial(port, baudrate, timeout)


def check(port):
    port.write('AT'+'\r\n')
    rx1 = port.read(7)
    print(rx1)


def set_baudrate(x,port):
    port.write('AT+IPR=' + str(x) + '\r\n')
    rx2 = port.read(12)
    print(rx2)


def set_settings(port):
    port.write('AT&W'+'\r\n')
    rx3 = port.read(20)
    print(rx3)


def power_gps_on(port):
    port.write('AT+CGPSPWR=1'+'\r\n')
    rx4 = port.read(20)
    print(rx4)


def gps_status(port):
    port.write('AT+CGPSSTATUS?'+'\r\n')
    rx5 = port.read(50)
    print(rx5)


def get_coordinate(port):
    port.write('AT+CGPSOUT=32'+'\r\n')
    rx6 = port.read(70)
    return str(rx6)


def close_gps(port):
    port.write('AT+CGPSPWR=0'+'\r\n')
    rx7 = port.read(20)
    print(rx7)
