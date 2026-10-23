"""
╔═══════════════════════════════════════════════════════════╗
║       DEOX SETTINGS - Configuration Management            ║
║         INI-Based Configuration Parser & Manager          ║
╚═══════════════════════════════════════════════════════════╝
"""

import configparser

class Settings:
    """
    DEOX Settings - Configuration Management System
    
    Provides a clean interface for reading and managing application settings
    from the settings.ini file. Supports multiple data types and automatic
    type conversion.
    
    Features:
        - Type-safe getters (string, boolean, int, float, float list)
        - Automatic configuration persistence
        - Section/key-based organization
        - Dynamic section creation
        - Error handling for missing values
    
    Configuration Structure:
        [Settings]    - Global application settings
        [Aimbot]      - Aimbot-specific parameters
        [Triggerbot]  - Triggerbot-specific parameters
    """

    def __init__(self):
        """
        Initializes the Settings class by reading the configuration from 'settings.ini'.
        """
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')

    def get(self, section, key):
        """
        Retrieves a string value from the configuration.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be retrieved.

        Returns:
            str: The value associated with the provided section and key.
        """
        return self.config.get(section, key)

    def get_boolean(self, section, key):
        """
        Retrieves a boolean value from the configuration.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be retrieved.

        Returns:
            bool: The boolean value associated with the provided section and key.
        """
        return self.config.getboolean(section, key)

    def get_float(self, section, key):
        """
        Retrieves a float value from the configuration.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be retrieved.

        Returns:
            float: The float value associated with the provided section and key.
        """
        return self.config.getfloat(section, key)
    
    def get_float_list(self, section, key):
        """
        Retrieves a list of float values from the configuration. The values are expected to be
        stored as a string representation of a list (e.g., "[1.0, 2.0, 3.0]").

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be retrieved.

        Returns:
            list[float]: A list of float values associated with the provided section and key.
        """
        string_value = self.config.get(section, key)
        values_as_strings = string_value.strip('[]').split(',')
        return [float(value) for value in values_as_strings]

    def get_int(self, section, key):
        """
        Retrieves an integer value from the configuration.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be retrieved.

        Returns:
            int: The integer value associated with the provided section and key.
        """
        return self.config.getint(section, key)

    def save(self):
        """
        Saves the current configuration to 'settings.ini'.
        """
        with open('settings.ini', 'w') as f:
            self.config.write(f)

    def set(self, section, key, value):
        """
        Sets a configuration value and saves the configuration to 'settings.ini'. If the section
        does not exist, it is created.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value is to be set.
            value (str): The value to set for the given section and key.
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
        self.save()