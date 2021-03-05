import os
import sys
import shutil


class Renamer:
    cnt = 1 # Its counter and it will use for directory renaming later

    def __init__(self, _wallpaper_dir):
        self.wallpaper_dir = _wallpaper_dir

    def cnt_files(self): # Count files
        # Return number of files that are in wallpaper directory
        return len(os.listdir(self.wallpaper_dir))

    def int_len(self, number):
        # This function will return number of digits of "number" variable
        number_of_digits = 0

        while number > 0:
            number //= 10
            number_of_digits += 1

        return number_of_digits

    def max_files(self):
        """
        For example this function return 10 if we have 3 file in directory of 1000 if we have 242 file in directory
        This function will return return 10 power len of numbere
        This will use for file naming. For example if we have 5 file files name will be 01, 02, 03, 04 and 05
        """

        return 10 ** self.int_len(self.cnt_files())

    def rename(self):
        for file in os.listdir(self.wallpaper_dir):
            current_file_name = self.wallpaper_dir + "/" + file
            new_file_name = self.wallpaper_dir + "/" + "0" * (self.int_len(self.max_files()) - self.int_len(self.cnt_files())) + str(self.cnt)

            shutil.move(current_file_name, new_file_name)
            self.cnt += 1


# assign wallpapeer_dir value from command line argument
wallpaper_dir = sys.argv[1]

renamer = Renamer(wallpaper_dir)
renamer.rename()
