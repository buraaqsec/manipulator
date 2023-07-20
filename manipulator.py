import argparse
import re

def append_line(filename, line):
    with open(filename, 'a') as file:
        file.write(line + '\n')

def delete_line(filename, line, quiet):
    deleted_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        deleted = False
        for current_line in lines:
            if not re.search(r'\b{}\b'.format(re.escape(line)), current_line):
                file.write(current_line)
            else:
                deleted = True
                if not quiet:
                    deleted_lines.append(current_line.strip())

        if not deleted and not quiet:
            print('No match')

    return deleted_lines

def search_line(filename, search_string):
    found_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for idx, current_line in enumerate(lines, 1):
        if re.search(r'\b{}\b'.format(re.escape(search_string)), current_line):
            found_lines.append(idx)

    return found_lines


def delete_line_by_number(filename, line_number, quiet):
    deleted_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        deleted = False
        for idx, current_line in enumerate(lines, 1):
            if idx != line_number:
                file.write(current_line)
            else:
                deleted = True
                if not quiet:
                    deleted_lines.append(current_line.strip())

        if not deleted and not quiet:
            print('[-] No matching line number found for deletion.')

    return deleted_lines
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Path to the file', required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--append', help='Line to append')
    group.add_argument('-d', '--delete', help='Line to delete')
    group.add_argument('-dL', '--delete_line', type=int, help='Line number to delete')
    group.add_argument('-s', '--search', help='Search for the line')
    parser.add_argument('-q', '--quiet', action='store_true', help='quiet mode')
    args = parser.parse_args()


    if args.append:
        append_line(args.file, args.append)
    elif args.delete:
        deleted_lines = delete_line(args.file, args.delete, args.quiet)
        if not args.quiet and deleted_lines:
            print('[-] Deleted line(s):')
            for line in deleted_lines:
                print(line)
    elif args.delete_line:
        deleted_lines = delete_line_by_number(args.file, args.delete_line, args.quiet)
        if not args.quiet and deleted_lines:
            print('[-] Deleted line(s):')
            for line in deleted_lines:
                print(line)
    elif args.search:
        found_lines = search_line(args.file, args.search)
        if found_lines:
            print('[+] String found on the following line(s):')
            for line in found_lines:
                print(line)
        else:
            print('[-] String was not found.')


if __name__ == '__main__':
    main()
