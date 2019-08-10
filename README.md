# NPTEL Course Downloader [Deprecated]
[![Build Status](https://travis-ci.org/dewanshrawat15/nptel-downloader.svg?branch=master)](https://travis-ci.org/dewanshrawat15/nptel-downloader)

The ```script.py``` file once triggered automatically starts downloading the videos from the course page which contains those lecture videos.

## Requirement
Any system with python 3 (preferably 3.6) and terminal.

## Usage
If you have to just download videos or basically use the script to download videos:
- Navigate to the file directory where the downloaded file (the script file) is stored using the cd command in terminal or cmd.
- Trigger ```python script.py``` or ```python3 script.py``` according to the operating system needs.
- Enter the url of the Video Lecture Course that you want to download.

## Description
nptel-downloader is a command-line program to download videos from the nptel course page. It requires the Python interpreter, 3.6+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.
```python main.py [-h] [-u URL] [-f FORMAT]```

## Options
```
-h, --help                        Print this help message box and exit
-u, --url                         Enter the nptel course page url
-f --format                       Enter the format in which the videos have to be downloaded.
                                  Supported formats are MP4, 3GP, FLV
```
## Known Issue
None as of now. Currently, I'm trying to add a Resume Downloads Feature. Feel free to open an issue if any!

## License
> The MIT License
