import csv


def s17_130():
    # open the file
    data = open('example.csv', encoding='utf-8')

    # csv.reader
    csv_data = csv.reader(data)

    # reformat it into a python object list of lists
    data_lines = list(csv_data)
    for line in data_lines[:5]:
        print(line)

    all_emails = []
    for line in data_lines[1:15]:
        all_emails.append(line[3])

    # print(all_emails)

    full_names = []
    for line in data_lines[1:15]:
        full_names.append(f'{line[1]} {line[2]}')

    print(full_names)

    # write csv to a file
    file_to_output = open('to_save_file.csv', mode='w', newline='')
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerow(['a', 'b', 'c'])
    csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
    file_to_output.close()

    f = open('to_save_file.csv', mode='a', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['1', '2', '3'])
    f.close()


if __name__ == '__main__':
    s17_130()
