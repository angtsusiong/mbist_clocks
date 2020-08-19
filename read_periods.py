if __name__ == '__main__':

    csv_file = 'mbist_clks.csv'
    csv_out_file = 'mbist_clks_out.csv'
    log_file = 'dft_ac_scan.latest.log'

    csv_list = open(csv_file, 'r').read().splitlines()
    log_list = open(log_file, 'r').read().splitlines()
    outfile = open(csv_out_file, 'w')

    period_list = []
    for line in log_list:
        if 'PERIOD MONITOR() : ENDT' in line:
            period_list.append(line.split()[-2])

    for i, line in enumerate(csv_list):
        line_list = line.split(',')
        if i == 0:
            line_list.insert(1, 'Actual Period')
        elif i == len(period_list):
            break
        else:
            line_list.insert(1, period_list[i-1])
        outfile.write(', '.join(line_list) + '\n')
