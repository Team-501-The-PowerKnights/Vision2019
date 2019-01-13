from util.stopwatch import stopwatch
from util.config import run_config

sw=stopwatch('sw')
sw.start()
config = run_config(None)

print(config)
timer = sw.get()
print('stopwatch: %.3f' % timer)
