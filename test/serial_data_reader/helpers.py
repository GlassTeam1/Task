from serial.tools.list_ports import comports


DEFAULT_BD = 9600


def configure_serial():
    ports = comports()
    if not ports:
        print('找不到串口')
        exit()

    for i, p in enumerate(ports):
        print({i}, {p.device})

    port_number = int(input('使用哪个端口（编号）?')) if len(ports) > 1 else 0
    bd = input('连接速度（默认为9600）:')
    bd = DEFAULT_BD if bd == '' else int(bd)
    selected_port = ports[port_number]

    return selected_port, bd