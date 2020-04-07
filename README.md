# Educational Keylogger

This is a eduactional keylogger for a **MAC**. I am not responsible for the use that you give.

## Requeriments

To use this keylogger you need:
 - Python 3
 - [Pynput](https://pypi.org/project/pynput/)
 - [Os](https://pypi.org/project/os-sys/)
 - [Datetime](https://pypi.org/project/DateTime/)
 
## Usage

First give the necessary permissions and then execute de bash file.
The bash file makes python program run in background with the flag 'nohup'.
 - Command: 
```shell script
$ ./script_keylogger.sh
```
To finish the process, press 'F1'. This is configured in the pyhton file.

A new file is created in the data folder when the process ends. the file name is the date of use.
 Inside the top there will be the start date, in the body the keyboard events and in the bottom
 the date of the end of the process.


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



