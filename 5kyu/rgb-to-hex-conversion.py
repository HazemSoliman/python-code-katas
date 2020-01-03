def rgb(r, g, b):
    hex_list = []
    for num in [r, g, b]:
        if num < 0:
            hex_list.append('00')
        elif num > 255:
            hex_list.append('FF')
        elif num < 16:
            hex_list.append('0'+hex(num)[2:].upper())
        else:
            hex_list.append(hex(num)[2:].upper())
    return ''.join(hex_list)