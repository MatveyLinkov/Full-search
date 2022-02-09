def get_spn(toponym):
    coord = [float(value) for key in toponym['boundedBy']['Envelope']
             for value in toponym['boundedBy']['Envelope'][key].split()]
    return f'{coord[2] - coord[0]},{coord[3] - coord[1]}'
