from litevision.lib import GUInterface
from litevision.res.glob import *
from litevision.lib import database

is_running = True

if __name__ == "__main__":
    # for some reason this works to a max of ??? times and its killing me
    while is_running:
        settings = database.read_json()
        screen_mode = settings['screen_mode']
        resolution = settings['resolution']
        print("app starting..")

        app = GUInterface()
        app.run()
        print("stopped running")
        app.kill()

        settings = database.read_json()
        # check changes that require reset and if any are made instead of completely killing everything
        # just kill the object app set it to None and restart the loop
        print(screen_mode, "->", settings['screen_mode'])
        print(resolution, "->", settings['resolution'])
        if screen_mode != settings['screen_mode']:
            app = None
        elif resolution != settings['resolution']:
            app = None
        else:
            print("no changes..\nstopping main")
            is_running = False