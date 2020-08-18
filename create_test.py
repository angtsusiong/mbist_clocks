

if __name__ == '__main__':
    print('PyCharm')

    csv_file = 'mbist_clks.csv'
    test_file = 'dft_mbist_clks.e'

    csv_file = open(csv_file, 'r').read().splitlines()
    outfile = open(test_file, 'w')

    for line in csv_file:
        clock_path = (line.split(',')[0])
        clock_path = clock_path.replace('/', '.')
        # print(clock_path)
        outfile.write('def_hwp PIXCK_CLK of bit = "' + clock_path + '";\n')




