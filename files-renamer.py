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
        for file in sorted(os.listdir(self.wallpaper_dir)):
            current_file_name = self.wallpaper_dir + "/" + file
            file_extension = current_file_name.split(".")[-1]
            new_file_name = "0" * (self.int_len(self.cnt_files()) - self.int_len(self.cnt)) + str(self.cnt)

            files = [os.path.splitext(filename)[0] for filename in os.listdir(self.wallpaper_dir)]
            files = sorted(files)

            if new_file_name in files:
                self.cnt += 1
                continue
            else:
                if os.path.isdir(current_file_name):
                    shutil.move(current_file_name, self.wallpaper_dir + "/" + new_file_name)
                else:
                    shutil.move(current_file_name, self.wallpaper_dir + "/" + new_file_name + "." + file_extension)


            self.cnt += 1


# assign files_dir value from command line argument
files_dir = sys.argv[1]

renamer = Renamer(files_dir)
renamer.rename()
