# 👀 Observer Pattern – Behavioral Design Pattern
# 📌 Scenario: Weather Monitoring System 🌦️
# Imagine you're designing a weather monitoring system where multiple displays (observers) must automatically update whenever the temperature changes. Instead of manually notifying each display, we use the Observer pattern to achieve real-time updates.

# ❌ Without Observer Pattern (Manual Updates, Hardcoded)

class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.displays = []  # Manually tracking displays

    def add_display(self, display):
        self.displays.append(display)

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify_displays()  # Manually notifying each display

    def notify_displays(self):
        for display in self.displays:
            display.update(self.temperature)


class TemperatureDisplay:
    def update(self, temperature):
        print(f"🌡️ Display updated: Temperature is now {temperature}°C")


# Client Code
station = WeatherStation()
display1 = TemperatureDisplay()
display2 = TemperatureDisplay()

station.add_display(display1)
station.add_display(display2)

station.set_temperature(25)  # Displays get updated
station.set_temperature(30)  # Displays get updated

# 💣 Problems
# Manual display management – Every time a new display is added, the WeatherStation must track it.
# Tightly coupled – The WeatherStation directly calls update(), making it hard to reuse or extend.

# ✅ With Observer Pattern (Flexible, Decoupled, Automatic Updates)
# Step 1: Subject (Observable) Interface
class Subject:
    def __init__(self):
        self._observers = []  # Stores observers

    def attach(self, observer):
        self._observers.append(observer)  # Register observer

    def detach(self, observer):
        self._observers.remove(observer)  # Unregister observer

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)  # Notify all observers


# Step 2: Concrete Subject (Weather Station)
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    def set_temperature(self, temp):
        self._temperature = temp
        print(f"\n🌡️ Weather Station: Temperature updated to {temp}°C")
        self.notify(temp)  # Notify observers


# Step 3: Observer Interface
class Observer:
    def update(self, data):
        pass  # Abstract method


# Step 4: Concrete Observers (Different Displays)
class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"📺 Temperature Display: {temperature}°C")


class MobileAppDisplay(Observer):
    def update(self, temperature):
        print(f"📱 Mobile App Alert: Temperature is {temperature}°C")


# Step 5: Client Code
station = WeatherStation()
display1 = TemperatureDisplay()
display2 = MobileAppDisplay()

# Attach observers
station.attach(display1)
station.attach(display2)

# Change temperature (Observers get notified automatically)
station.set_temperature(25)
station.set_temperature(30)

# 🔑 Key Benefits
# ✅ Decoupled & Extensible – New observers (e.g., a web dashboard) can be added without modifying existing code.
# ✅ Automatic Updates – No need to manually call update functions; all observers get notified automatically.
# ✅ Real-time Data Flow – Useful for systems that require live updates.

# 💡 Where is this Used?
# 🔹 Stock Market Apps – When a stock price changes, all investor dashboards update automatically.
# 🔹 Social Media Notifications – When someone likes your post, all devices (mobile, web) get notified.
# 🔹 Messaging Apps – WhatsApp Web syncs messages instantly when received on mobile.
# 🔹 Event-driven Systems – Microservices communicating through event listeners.

