# Manipulator

Tool that allows you to perform various operations on a text file, including appending lines, deleting lines by content or line number, and searching for lines containing a specific string.

## Installation

To install the tool, follow these steps:

```bash
git clone https://github.com/buraaqsecsec/manipulator.git

cd manipulator
sudo pip3 install -r requirements.txt
sudo chmod +x manipulator.py
python3 manipulator.py -h
```

## Usage

The tool supports the following command-line arguments:

- `-f`, `--file`: Path to the target text file. (Required for all operations)
- `-a`, `--append`: Line to append to the file.
- `-d`, `--delete`: Line to delete from the file.
- `-s`, `--search`: Search for the line containing the specified string.
- `-dL`, `--delete_line`: Line number to delete from the file.
- `-q`, `--silent`: Suppress output for delete operations.

### Usage Examples

1. Append a line to the file:

```bash
$ cat myfile.txt
abc
xyz
test1
jkl

$ python3 manipulator.py -f myfile.txt -a "mno"

$ cat myfile.txt
abc
xyz
test1
jkl
mno
```

2. Delete a line from the file by its content:

```bash
$ cat myfile.txt
abc
xyz
test1
jkl

$ python3 manipulator.py -f myfile.txt -d "abc"
[-] Deleted the following line(s):
abc

$ cat myfile.txt
xyz
test1
jkl
```

3. Search for lines containing a specific string:

```bash
$ cat myfile.txt
abc
xyz
test1
buraaqsec
jkl

$ python3 manipulator.py -f myfile.txt -s "buraaqsec"
The search string is found on the following line(s):
4
```

4. Delete a line from the file by its line number:

```bash
$ cat myfile.txt
abc
xyz
test1
buraaqsec
jkl

$ python3 manipulator.py -f myfile.txt -dL 4
[-] Deleted the following line(s):
d

$ cat myfile.txt
abc
xyz
test1
jkl
```

5. Search for lines containing a specific string (silent mode):

```bash
$ python3 manipulator.py -f myfile.txt -d "buraaqsec" -q
$
```
