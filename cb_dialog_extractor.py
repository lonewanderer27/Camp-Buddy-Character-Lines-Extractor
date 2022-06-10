import os
import ntpath
import re
import csv

class CBDialogExtractor:
    '''
    Extracts character dialogs from Camp Buddy & Camp Buddy Scoutmasters Edition.

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
    '''

    def __init__(
        self,
        source_directory: str, 
        game: int, 
        chosen_chars: list, 
        exclude_roleplay_dialogs = True,
        export_to_file = True,
        destination_file = str,
        destination_directory = str,
        header = ['name', 'dialog'],
        delimeter = ';',
        verbose_level = 2,
        cb_toolbox_window = None
    ) -> None:
        self.window = cb_toolbox_window
        self.source_directory = source_directory
        self.game = game
        self.chosen_chars = chosen_chars
        self.exclude_roleplay_dialogs = exclude_roleplay_dialogs
        self.export_to_file = export_to_file
        self.destination_file = destination_file
        self.destination_directory = destination_directory
        self.header = header
        self.delimeter = delimeter
        self.verbose_level = verbose_level
        self.chars_aliases = {
            # Camp Buddy Scoutmasters Edition Character Aliases
            'a': 'Aiden',
            'u': 'Andre',
            'g': 'Goro',
            'yo': 'Yoshinori',
            'yu': 'Yuri',
            'l': 'Lloyd',
            'd': 'Darius',
            'j': 'Hyunjin',
            'e': 'Emilia',
            'yi': 'Yoichi',
            't': 'Taiga',
            'k': 'Keitaro',
            'hu': 'Hunter',
            'hi': 'Hiro',
            'n': 'Natsumi',
            'na': 'Naoto',
            'nag': 'Guest',
            'nas': 'Stripper',
            'r': 'Bellboy',
            'm': 'Masseur',
            'bt': 'Bartender',
            'r': 'Reimond',
            'ju': 'Justin',
            'o': 'Officiator',
            'ol': 'Doctor',
            'v': 'Vera',
            'w': 'William',
            'wo': 'Workers',
            'ar': 'Architect',
            'fo': 'Foreman',

            # Camp Buddy Character Aliases
            'f': 'Felix',
            'e': 'Eduard',
            'l': 'Lee',
            'con': 'Conductor',
            'ra': 'Rayne',
            'to': 'Toshu',
            'ic': 'Ichiru',
            'co': 'Connor',
            'ji': 'Jirou',
            'ha': 'Avan',
            'yt': 'Yuuto',
            'hr': 'Haruki',
            'no': 'Noah',
            'ch': 'Chiaki',
            'hm': 'Hina',
            'y': 'Yuki',
            'he': 'Heather',
            'ar': 'Archer',
            'ki': 'Kieran',

            # I only included the characters that it makes sense for someone
            # to get the dialogs of.
            #
            # Character aliases such as 'all' and 'Aiden & Goro' are not included here.
            #
            # And as such an error would occur if someone were to extract
            # their dialogs using their alias.
        }
        # DIALOGS WOULD BE STORED HERE
        self.dialogs = {
            1: {},  # Camp Buddy
            2: {}   # Camp Buddy Scoutmasters Edition
        }
        self.total_amount_of_files = 0
        self.valid_parameters()

    def log(self, message: str, verbose_level_of_message: int) -> None:
        if self.verbose_level == 1 and verbose_level_of_message == 1:
            print(message)
        elif self.verbose_level == 2:
            if verbose_level_of_message == 1 or verbose_level_of_message == 2:
                print(message)
        elif self.verbose_level == 3:
            if verbose_level_of_message == 3 or verbose_level_of_message == 1:
                print(message)

    def valid_parameters(self) -> None:
        '''Raises ValueError when one of the parameters are invalid'''

        if not self.source_directory:
            raise ValueError('Source directory not specified') 
        if not self.game:
            raise ValueError('Game not specified')
        if self.game != 2 and self.game != 1:
            raise ValueError(f'You specified {self.game} for game. Must be 1 or 2')
        if len(self.chosen_chars) == 0:
            raise ValueError('Chosen game characters is empty')
        for char in self.chosen_chars:
            if char not in self.chars_aliases:
                raise ValueError("Chosen game character alias doesn't exist in character aliases")
        if self.export_to_file == True:
            if len(self.destination_file) == 0:
                raise ValueError('Destination file not specified')
        elif self.export_dialogs_to_directory:
            if len(self.destination_directory) == 0:
                raise ValueError('Destination directory not specified')
        if len(self.delimeter) > 1:
            raise ValueError('Only one character is allowed as delimeter')
        if len(self.header) != 2:
            raise ValueError('Header columns must be 2')

    def calculate_progress(self, current_file_num: int) -> tuple:
        percentage = current_file_num / self.total_amount_of_files
        percentage *= 100
        percentage = round(percentage, 2)
        int_percentage = int(percentage)
        return percentage, int_percentage
    
    def get_filename_from_path(self, rpapath: str) -> str:
        return ntpath.basename(rpapath)

    def get_absolute_file_path(self, file_dir_path: str, filename: str) -> str:
        '''Returns the relative path, given the directory and filename'''

        dir = os.path.dirname(__file__)
        file_path = os.path.join(dir, file_dir_path,filename)
        return file_path

    def get_file_paths(self) -> list:
        '''Returns a list containing the absolute paths of .rpy files in a directory'''

        filepaths = []
        for file in os.listdir(self.source_directory):
            if file.endswith(f'.rpy'):
                filepaths.append(self.get_absolute_file_path(self.source_directory, file))
        return filepaths

    def strip_newline_from_text_lines(self, text_lines: list) -> list:
        '''Returns a list containing text lines of a file clean of newline symbols'''

        text_lines_stripped = []
        for text_line in text_lines:
            text_lines_stripped.append(text_line.strip())
        return text_lines_stripped

    def extract_dialogs_from_file(self, rpyfilepath: str, current_file_num: int):
        '''Extracts character dialogs from a file then outputs them into the dialog dictionary'''

        # OPEN THE FILE
        file = open(rpyfilepath, 'r')   

        # GET ALL THE LINES OF TEXTS IN THE FILE THEN REMOVE ALL NEWLINE SYMBOLS
        lines_stripped = self.strip_newline_from_text_lines(file.readlines())

        for line in lines_stripped:
            
            # IF {i} IS FOUND IN LINE, IT BELONGS TO A ROLEPLAY SCENE
            if "{i}" in line:
                if self.exclude_roleplay_dialogs:
                    continue    # IF ROLEPLAY DIALOGS ARE EXCLUDED, WE SKIP THE LINE
                else:           # OTHERWISE IF ALLOWED, WE REMOVE {i} and {/i}
                    line = line.replace("{i}",'')       # REMOVES THE {i}
                    line = line.replace("{/i}",'')      # REMOVES THE {/i}
            
            # GET THE DIALOG BETWEEN APOSTROPHES
            dialog = re.findall('"([^"]*)"', line)

            # SKIP THE LINES THAT HAVE NO DIALOG
            if len(dialog) == 0:    
                continue

            # SOME LINES DO NOT HAVE KEYWORDS, THOSE CAUSE ERRORS SO WE SURROUND IT WITH TRY
            try:
                # SPLIT THE LINE INTO LIST OF WORDS
                line_words = line.split()
                
                for char in self.chosen_chars:
                    # DETERMINE IF THE FIRST WORD MATCHES TO THE SELECTED CHARACTER KEYWORDS
                    if line_words[0] == char:
                        if char not in self.dialogs[self.game]:   
                            # CREATE THE KEY FOR THE CHARACTER IF IT DOESN'T EXIST YET
                            # THEN APPEND THE DIALOG INSIDE OF THE CHARACTER'S DIALOG LIST
                            self.dialogs[self.game][char] = [dialog[0]]
                        else:   
                            # APPEND INSIDE CHARACTER'S DIALOG LIST
                            self.dialogs[self.game][char].append(dialog[0])

                        percentage, int_percentage = self.calculate_progress(current_file_num)
                        self.log(
                            message=f'[{percentage}%] [{self.get_filename_from_path(rpyfilepath)}] {self.chars_aliases[char]}: {dialog[0]}',
                            verbose_level_of_message=3
                        )
            except:
                pass

    def export_dialogs_to_directory(self):
        '''Exports the dialogs to individual csv files to a destination directory'''

        # For each character in dialogs dictionary
        for char in self.dialogs[self.game]:

            # Create a new csv file
            file = open(self.get_absolute_file_path(self.destination_directory, self.chars_aliases[char])+'.csv', 'w')
            writer = csv.writer(file, delimiter=self.delimeter)
            writer.writerow(self.header)    # Write the header
            if len(self.dialogs[self.game]) != 0:
                for dialog in self.dialogs[self.game][char]:                # For each dialog of the character
                    writer.writerow([self.chars_aliases[char], dialog])     # Write each dialog in a row

            file.close()    # Close the file

    def export_dialogs_to_file(self):
        '''Exports dialogs to a destination csv file'''

        # Create a new csv file
        file = open(self.destination_file, 'w')
        writer = csv.writer(file, delimiter=self.delimeter)
        writer.writerow(self.header)    # Write the header columns

        # For each character in dialogs dictionary
        for char in self.dialogs[self.game]:
            if len(self.dialogs[self.game]) != 0:
                for dialog in self.dialogs[self.game][char]:                # For each dialog of the character
                    writer.writerow([self.chars_aliases[char], dialog])     # Write each dialog in a row

        file.close()    # Close the file

    def extract(self) -> None:
        '''Main Method'''
        rpyfilepaths = self.get_file_paths()
        self.total_amount_of_files = len(rpyfilepaths)

        self.log(
            message=f'Found {self.total_amount_of_files} .rpy files from directory: "{self.source_directory}"',
            verbose_level_of_message=1)
        self.log(message='Starting dialog extraction...\n', verbose_level_of_message=1)

        current_file_num = 1
        for rpyfilepath in rpyfilepaths:
            percentage, int_percentage = self.calculate_progress(current_file_num)
            self.log(
                message=f'[{percentage}%] {self.get_filename_from_path(rpyfilepath)}',
                verbose_level_of_message=2)
            self.extract_dialogs_from_file(rpyfilepath, current_file_num)
            current_file_num += 1

        if self.export_to_file:
            self.export_dialogs_to_file()
        else:
            self.export_dialogs_to_directory()
        self.log(
                message=f'\nFinished extracting dialogs, it has been saved to: "{self.destination_file if self.export_to_file else self.destination_directory}"',
                verbose_level_of_message=1)