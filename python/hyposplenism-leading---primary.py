# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"27514.0","system":"readv2"},{"code":"102207.0","system":"readv2"},{"code":"31041.0","system":"readv2"},{"code":"34310.0","system":"readv2"},{"code":"48198.0","system":"readv2"},{"code":"59784.0","system":"readv2"},{"code":"64291.0","system":"readv2"},{"code":"2759.0","system":"readv2"},{"code":"1393.0","system":"readv2"},{"code":"102966.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hyposplenism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hyposplenism-leading---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hyposplenism-leading---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hyposplenism-leading---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
