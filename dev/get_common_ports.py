import csv


if __name__ == '__main__':
    used_ports = set()
    with open('iana.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            port = row['Port Number'].strip()
            if port:
                try:
                    used_ports.add(int(port))
                except ValueError:
                    port_from, port_to = port.split('-')
                    used_ports.update(range(int(port_from), int(port_to) + 1))

    start = 0
    end = 0
    for i in range(1024, 65536):
        if i not in used_ports:
            if i+1 not in used_ports:
                end += 1
            else:
                if start == end:
                    print(start)
                else:
                    print(f'[{start}, {end}]')
                start = end = i
        else:
            start = end = i + 1

    if start == end:
        print(start)
    else:
        print(f'[{start}, {end}]')
