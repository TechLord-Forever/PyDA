from interface import app
from concurrent.futures import ThreadPoolExecutor
from disassembler.Disassembler import Disassembler
from settings.settings import SettingsManager
from server.PyDAServer import PyDAServer
from cProfile import Profile
from pstats import Stats

class PyDA:
    def __init__(self):
        settings_manager = SettingsManager() # Set up the settings_manager
        max_workers = settings_manager.getint('application', 'max-workers') # Get the max workers from settings manager
        profiler_on = settings_manager.getint('debugging', 'profiler-on') # Get whether there is a profiler
        executor = ThreadPoolExecutor(max_workers=max_workers, profiler_on=profiler_on) # Set up the thread executor
        dis = Disassembler(settings_manager) # Build the disassembler
        server = PyDAServer('0.0.0.0',9000) # Set up the PyDA server
        if profiler_on:
            profile = Profile()
            profile.enable()
        app.build_and_run(settings_manager, dis, executor, server)
        if profiler_on:
            profile.disable()
            stats = executor.getProfileStats()
            if stats == None:
                stats = Stats(profile)
            else:
                stats.add(profile)
            with open('profile.stats', 'wb') as statsfile:
                stats.stream = statsfile
                stats.sort_stats('cumulative').print_stats()

if __name__ == '__main__':
    pyda = PyDA()
