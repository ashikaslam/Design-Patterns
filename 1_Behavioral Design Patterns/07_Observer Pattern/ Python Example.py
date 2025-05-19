"""
Observer Pattern Example in Python

Scenario: Weather Station
- The WeatherStation (Subject) updates its temperature.
- Different displays (Observers) react to this change: phone display, window display, and web dashboard.
"""

from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []  # List to keep track of observers
        self._temperature = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        # Notify all observers about the temperature update
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        # Change the temperature and notify observers
        print(f"\n[WeatherStation] Temperature updated to {temperature}")
        self._temperature = temperature
        self.notify()

# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"[PhoneDisplay] Temperature is now {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"[WindowDisplay] It's {temperature}°C outside")

class WebDashboard(Observer):
    def update(self, temperature):
        print(f"[WebDashboard] Displaying temperature: {temperature}°C")

# Client code to demonstrate the Observer Pattern
if __name__ == "__main__":
    station = WeatherStation()

    phone = PhoneDisplay()
    window = WindowDisplay()
    web = WebDashboard()

    # Attach observers to the subject
    station.attach(phone)
    station.attach(window)
    station.attach(web)

    # Change temperature and notify observers
    station.set_temperature(25)
    station.set_temperature(30)

    # Detach one observer and update again
    station.detach(window)
    station.set_temperature(22)

"""
Explanation:
- We use abstract base classes for Observer and Subject to define required interfaces.
- WeatherStation holds the state and notifies all observers on changes.
- Each display class implements the Observer interface and responds to state changes.
- This is a clean example of the Observer Pattern in real-world use.
"""
