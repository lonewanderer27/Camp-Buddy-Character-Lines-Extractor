# Camp Buddy Dialog Extractor

# About

Camp Buddy Dialog Extractor is a tool that extracts dialog from Camp Buddy and Camp Buddy Scoutmasters Edition.
It can also be embedded inside another program sa library.

# How to Use:

## As a Library:
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

# Parameters
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
