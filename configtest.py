from util.stopwatch import stopwatch
from util.config import runConfig

sw=stopwatch('sw')
sw.start()
config = runConfig(None)

print(config)
timer = sw.get()
print('stopwatch: %.3f' % timer)
