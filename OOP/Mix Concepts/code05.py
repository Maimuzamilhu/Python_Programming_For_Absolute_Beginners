"""File Handling and Error Handling:
You are building a text file parser for a configuration file. The file contains settings in the format key=value. Implement a class called ConfigParser that reads the file, parses the settings, and stores them in a dictionary. Handle errors such as missing keys, invalid values, and file not found. How would you ensure robust error handling while reading and processing the configuration file?"""

import configparser

class ConfigParser:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def read_config(self):
        try:
            self.config.read(self.filename)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return

        settings_dict = {}
        for section in self.config.sections():
            for key, value in self.config.items(section):
                settings_dict[key] = value

        return settings_dict

if __name__ == "__main__":
    config_file = "my_config.ini"  # Replace with your actual configuration file
    parser = ConfigParser(config_file)
    settings = parser.read_config()

    if settings:
        print("Settings read successfully:")
        for key, value in settings.items():
            print(f"{key}: {value}")
    else:
        print("Error occurred while reading the configuration file.")
