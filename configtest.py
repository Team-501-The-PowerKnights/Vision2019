from util.stopwatch import stopwatch
from util.config import run_config

sw=stopwatch('sw')
sw.start()
try:
    config = run_config(None)
except:
    print('ERROR: unable to read configuration.')
print('INFO: ' + str(config))
timer = sw.get()
print('INFO: stopwatch: %.3f' % timer)
