"""

This script demonstrates the Singleton Design Pattern in Python.
We use a metaclass to ensure that only one instance of a given class exists.
"""

class SingletonMeta(type):
    """
    This is a metaclass for creating Singleton classes.
    It overrides the __call__ method to control instance creation.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        If an instance of the class doesn't exist, create it.
        Otherwise, return the existing instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    """
    This class represents application configuration.
    It uses SingletonMeta to ensure only one instance exists.
    """
    def __init__(self):
        self.settings = {
            "debug": True,
            "database": "SQLite",
            "version": "1.0.0"
        }

    def update_setting(self, key, value):
        """Update a specific configuration setting."""
        self.settings[key] = value

    def get_setting(self, key):
        """Retrieve a configuration setting by key."""
        return self.settings.get(key)

    def show_config(self):
        """Print all configuration settings."""
        print("Current App Configuration:")
        for key, value in self.settings.items():
            print(f"  {key}: {value}")

# Client code demonstrating the Singleton behavior
def main():
    """
    The client tries to create two configuration instances,
    but only one shared instance is maintained.
    """
    config1 = AppConfig()
    config2 = AppConfig()

    config1.show_config()

    # Modify config using one instance
    config1.update_setting("debug", False)

    # Access config using the second instance
    print("\nAfter modifying config1:")
    config2.show_config()

    # Verify both instances are the same
    print("\nAre config1 and config2 the same instance?", config1 is config2)

if __name__ == "__main__":
    main()
