# Base class
class SmartApp:
    def __init__(self, name, version, user):
        self.name = name
        self.version = version
        self.user = user
        self.daily_usage = 0  # in minutes

    def update_usage(self, minutes):
        self.daily_usage += minutes
        print(f"{self.name}: Added {minutes} minutes of usage. Total: {self.daily_usage} minutes.")

    def app_info(self):
        print(f"App: {self.name}, Version: {self.version}, User: {self.user}")


# Child class with encapsulation
class MudaSaver(SmartApp):
    def __init__(self, version, user):
        super().__init__("Muda Saver", version, user)
        self.__waste_activities = []

    def log_activity(self, activity):
        self.__waste_activities.append(activity)
        print(f"Activity logged: {activity}")

    def suggest_improvement(self):
        if not self.__waste_activities:
            print("No wasteful activities logged yet. Keep going! ✅")
        else:
            print("🧠 Suggestions:")
            for activity in self.__waste_activities:
                print(f" - Consider reducing time on: {activity}")

    def summary_report(self):
        print("\n📊 MUDA SAVER REPORT")
        self.app_info()
        print(f"Total usage today: {self.daily_usage} minutes")
        print("Logged wasteful activities:")
        for i, activity in enumerate(self.__waste_activities, 1):
            print(f"  {i}. {activity}")

    # Getter method (Encapsulation)
    def get_waste_activities(self):
        return self.__waste_activities.copy()