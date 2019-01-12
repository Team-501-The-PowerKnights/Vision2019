import sys
import configparser


def runConfig(cfg):
   """
   reads a  configuration file (config.ini) in standard format.
   [header]
   config_item  = value

   quotations are not required.
   """
   config = configparser.ConfigParser()

   die=0

   if cfg is None:
       print("INFO: reading configuration from config.ini")
       #try:
       config.read('config.ini')
       #except:
       #   print("ERROR: Unable to read config.ini Dying.")
       #   sys.exit(1)
   else:
       config = cfg

   try:
      os = config['os']['operatingSystem']
      camera = config['camera']['cameraDevice']
      green_upper = config['mask']['green_upper']
      green_upper = list(map(int, green_upper.split(',')))
      # convert the config item into a list so that things don't blow up
      green_lower = config['mask']['green_lower']
      green_lower = list(map(int, green_lower.split(',')))
      freqFrameNT = int(config['framerate']['freqFrameNT'])
      debug = config['debug']['debug']
      search = config['search']['search']
      vertx = int(config['vertices']['vertx'])
      verty = int(config['vertices']['verty'])
   except:
      print("ERROR: config.ini does not contain correct parameters. see ./config.correct ")
      sys.exit(1)

   if not os:
      print("INFO: os configuration not present")
   if not camera:
      print("ERROR: camera configuration not present")
      die=1
   sacrificial = None
   try:
      sacrificial = red_upper[2]
      sacrificial = red_lower[2]
      sacrificial = blue_upper[2]
      sacrificial = blue_lower[2]
      sacrificial = green_upper[2]
      sacrificial = green_lower[2]
   except IndexError:
      print("ERROR: calibration configuration incomplete")
      die = 1
   if not sacrificial:
      die = 1
   if not freqFrameNT:
      print("INFO: framerate not specified, using default of 10.")
      freqFrameNT = 10
   if not vertx:
      print("Vertices incomplete")
      die = 1
   if not verty:
      print("Vertices incomplete")
      die = 1
   if die > 0:
      print("FATAL ERROR: unable to load vision configuration. Exiting.")
      sys.exit(1)
   if debug == '1':
      debug = True
   else:
      debug = False
   if search == '1':
      search = True
   else:
      search = False
   if debug:
      print("INFO: debug set.")
   red = {"red_upper": red_upper, "red_lower": red_lower}
   blue = {"blue_upper": blue_upper, "blue_lower": blue_lower}
   green = {"green_upper": green_upper, "green_lower": green_lower}
   calibration = {"red": red, "blue": blue, "green": green, "debug": debug, "search": search}

   return os, camera, calibration, freqFrameNT, vertx, verty


def write_cal(cal):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('mask', 'green_upper', ','.join(cal['green']['green_upper']))  # convert lists into single strings
    config.set('mask', 'green_lower', ','.join(cal['green']['green_lower']))

    print('Validating configuration and writing to disk.')
    runConfig(config)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return True