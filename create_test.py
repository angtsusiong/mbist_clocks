

if __name__ == '__main__':
    print('PyCharm')

    csv_file = 'mbist_clks.csv'
    test_file = 'dft_mbist_clks.e'

    csv_file = open(csv_file, 'r').read().splitlines()
    outfile = open(test_file, 'w')

    clock_path_list = []

    for line in csv_file:
        clock_path = (line.split(',')[0])
        if 'Memory clock pin' not in clock_path:
            clock_path_list.append(clock_path.replace('/', '.'))

    for path in clock_path_list:
        outfile.write('def_hwp PIXCK_CLK of bit = "' + path + '";\n')




