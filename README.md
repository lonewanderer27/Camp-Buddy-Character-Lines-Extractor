# Camp Buddy Dialog Extractor

# About

Camp Buddy Dialog Extractor is a tool that extracts dialog from Camp Buddy and Camp Buddy Scoutmasters Edition.
It can also be embedded inside another program sa library.

# Command Line Usage
```
usage: cb_dialog_extractor.py [-h] [-r EXCLUDE_ROLEPLAY_DIALOGS] [-e EXPORT_TO_FILE] [-d DESTINATION_FILE] [-D DESTINATION_DIRECTORY]<br>
                              [-H [HEADER [HEADER ...]]] [-m DELIMETER] [-v VERBOSE_LEVEL]<br>
                              source_directory game [chosen_chars [chosen_chars ...]]<br>
```

### Options
| Positional Argument | Description                                        |
|---------------------|----------------------------------------------------|
| source_directory    | Folder Containing .rpy Files                       |
| game                | 1 = Camp Buddy 2 = Camp Buddy Scoutmasters Edition |
| chosen_chars        | Characters to extract dialogs of                   |
| Optional Argument              | Description                                                                                                                                                                                                                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h, --help                     | show this help message and exit                                                                                                                                                                                                                                                                          |
| -r, --exclude_roleplay_dialogs | Exclude roleplay dialogs <br>(default: True)                                                                                                                                                                                                                                                             |
| -e, --export_to_file           | Export the dialogs to file. If False then dialogs would be exported to directory<br>(default: True)                                                                                                                                                                                                      |
| -d, --destination_file         | Export destination file path. Used if export_to_file is True. Ignored if export_to_file is False<br>(default: None)                                                                                                                                                                                      |
| -D, --destination_directory    | Export destination directory. Used if export_to_file is False. Ignored if export_to_file is True<br>(default: None)                                                                                                                                                                                      |
| -H, --header                   | Header columns (default: ['name', 'dialog'])                                                                                                                                                                                                                                                             |
| -m, --delimeter                | Symbol to separate the character name and their dialog (default: ;)                                                                                                                                                                                                                                      |
| -v, --verbose_level            | 0 = no output to terminal<br>1 = shows message when dialogs extraction has started and finished and where it was saved<br>2 = shows the percentage progress and the current file being worked on<br>3 = shows the character name and their dialog in real time as they get extracted<br><br>(default: 2) |

# Library Usage:
### Extract Keitaro's dialogs from Camp Buddy:
```
cbdialogextractor = CBDialogExtractor(source_directory='folder that contains .rpy files', game=1, chosen_chars=['k'], destination_file='Taiga_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Taiga's dialogs from Camp Buddy:
```
cbdialogextractor = CBDialogExtractor(
                        source_directory='folder that contains .rpy files', 
                        game=1, chosen_chars=['t'], 
                        destination_file='Taiga_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Taiga and Keitaro dialogs from Camp Buddy:
```
cbdialogextractor = CBDialogExtractor(
                        source_directory='folder that contains .rpy files', 
                        game=1, chosen_chars=['k','t'], 
                        destination_file='Keitaro_&_Taiga_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Yoshinori's dialogs from Camp Buddy Scoutmasters Edition:
```
cbdialogextractor = CBDialogExtractor(
                        source_directory='folder that contains .rpy files', 
                        game=2, chosen_chars=['yo'], 
                        destination_file='Yoshinori_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Yoshinori and Aiden dialogs from Camp Buddy Scoutmasters Edition:
```
cbdialogextractor = CBDialogExtractor(
                        source_directory='folder that contains .rpy files', 
                        game=2, chosen_chars=['yo', 'a'], 
                        destination_file='Yoshinori_&_Aiden_Dialogs.csv')

cbdialogextractor.extract()
```

### Class Parameters
| Parameter                | Type   | Description                                                                                                                                                                                                                                                                                                |
|--------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| source_directory         | str    | Folder Containing .rpy Files                                                                                                                                                                                                                                                                               |
| game                     | int    | 1 = Camp Buddy, 2 = Camp Buddy Scoutmasters Edition                                                                                                                                                                                                                                                        |
| chosen_chars             | list   | Characters to extract dialogs of. Refer to chars_aliases dictionary for the alias of each character                                                                                                                                                                                                        |
| exclude_roleplay_dialogs | bool   | Exclude roleplay dialogs. Default is True                                                                                                                                                                                                                                                                  |
| export_to_file           | bool   | Export the dialogs to file. Default is True                                                                                                                                                                                                                                                                |
| destination_file         | str    | Export destination file. Used if export_to_file param is True. Ignored if export_to_file param is False                                                                                                                                                                                                                             |
| destination_directory    | str    | Export destination directory. Used if export_to_file param is False. Ignored if export_to_file param is True                                                                                                                                                                                               |
| header                   | list   | Header columns. Default is ['name', 'dialog']                                                                                                                                                                                                                                                              |
| delimeter                | str    | Symbol to separate the character name and their dialog. Default is ;                                                                                                                                                                                                                                       |
| verbose_level            | int    | 0 = no output to terminal<br>1 = shows message when dialogs extraction has started and finished and where it was saved<br>2 = shows the percentage progress and the current file being worked on<br>3 = shows the character name and their dialog in real time as they get extracted. <br><br>Default is 2 |
| cb_toolbox_window        | object | Camp Buddy Toolbox PySimpleGUI Window object. Only used when embedded in Camp Buddy Toolbox program<br>Default is None                                                                                                                                                                                     |
