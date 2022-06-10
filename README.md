# Camp Buddy Dialog Extractor - Extract dialogs from Camp Buddy & Camp Buddy Scoutmasters Edition

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
cbdialogextractor = CBDialogExtractor(source_directory='folder that contains .rpy files', game=1, chosen_chars=['t'], destination_file='Taiga_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Taiga and Keitaro dialogs from Camp Buddy:
```
cbdialogextractor = CBDialogExtractor(source_directory='folder that contains .rpy files', game=1, chosen_chars=['k','t'], destination_file='Keitaro_&_Taiga_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Yoshinori's dialogs from Camp Buddy Scoutmasters Edition:
```
cbdialogextractor = CBDialogExtractor(source_directory='folder that contains .rpy files', game=2, chosen_chars=['yo'], destination_file='Yoshinori_Dialogs.csv')

cbdialogextractor.extract()
```
### Extract Yoshinori and Aiden dialogs from Camp Buddy Scoutmasters Edition:
```
cbdialogextractor = CBDialogExtractor(source_directory='folder that contains .rpy files', game=2, chosen_chars=['yo', 'a'], destination_file='Yoshinori_&_Aiden_Dialogs.csv')

cbdialogextractor.extract()
```

# Class Parameters

param   source_directory:           Folder Containing .rpy Files
type    source_directory:           (str)

param   game:                       1 = Camp Buddy, 2 = Camp Buddy Scoutmasters Edition
type    game:                       (int)   

param   chosen_chars:               Characters to extract dialogs of. Refer to chars_aliases dictionary for the alias of each character.
type    chosen_chars:               (list)

param   exclude_roleplay_dialogs:   Exclude roleplay dialogs. Default is True
type    exclude_roleplay_dialogs:   (bool)

param   export_to_file:             Export the dialogs to file. Default is True. If False then dialogs would be exported to directory.
type    export_to_file:             (bool)

param   destination_file:           Export destination file path. Used if export_to_file param is True. Ignored if export_to_file param is False.
type    destination_file:           (str)

param   destination_directory:      Export destination directory. Used if export_to_file param is False. Ignored if export_to_file param is True.
type    destination_directory:      (str)

param   header:                     Header columns. Default is ['name', 'dialog']
type    header:                     (list)

param   delimeter:                  Symbol to separate the character name and their dialog. Default is ;
type    delimeter:                  (str)

param   verbose_level:              0 = no output to terminal, 1 = shows message when dialogs extraction has started and finished and where it was saved, 2 = shows the percentage progress and the current file being worked on, 3 = shows the character name and their dialog in real time as they get extracted. Default is 2
type    verbose_level:              (int)

param   cb_toolbox_window:          Camp Buddy Toolbox PySimpleGUI Window object. Only used when embedded in Camp Buddy Toolbox program. Default is None.
type    cb_toolbox_window:          (object)
