from litevision.lib import GUInterface
from litevision.res.glob import *
from litevision.lib import database

is_running = True

if __name__ == "__main__":
    while is_running:
        settings = database.read_json()
        screen_mode = settings['screen_mode']
        resolution = settings['resolution']

        app = GUInterface()
        print(app.is_running)
        app.run()
        print("stopped running")
        app.kill()

        settings = database.read_json()

        print(screen_mode, "and", settings['screen_mode'])
        print(resolution, "and", settings['resolution'])
        if settings['screen_mode'] != screen_mode:
            print("mode change detected!")
            app = None
            print("objet cleaned")
            print("restarting loop")
        elif settings['resolution'] != resolution:
            print("size change detected!")
            app = None
            print("object cleaned")
            print("restarting loop")
        else:
            is_running = False