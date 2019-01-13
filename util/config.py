import sys
import configparser


def run_config(cfg):
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
        try:
            config.read('config.ini')
        except:
            print('ERROR: unable to read config.ini. Dying.')
            sys.exit(1)
        os = None
        camera = None
        green_upper = None
        green_lower = None
        nt_update_frequency = None
        debug = None
        search = None
    else:
        config = cfg

    try:
        os = config['os']['operating_system']
        camera = config['camera']['camera_device']
        green_upper = config['mask']['green_upper']
        green_upper = list(map(int, green_upper.split(',')))
        # convert the config item into a list so that things don't blow up
        green_lower = config['mask']['green_lower']
        green_lower = list(map(int, green_lower.split(',')))
        nt_update_frequency = int(config['framerate']['nt_update_frequency'])
        debug = config['debug']['debug']
        search = config['search']['search']
    except:
        print("ERROR: config.ini does not contain correct parameters. see ./config.correct ")
        # sys.exit(1)

    if not os:
        print("INFO: os configuration not present")
        os = "linux"
    if not camera:
        print("ERROR: camera configuration not present.")
        die = 1
    sacrificial = None
    try:
        sacrificial = green_upper[2]
        sacrificial = green_lower[2]
    except IndexError:
        print("ERROR: calibration configuration incomplete.")
        die = 1
    except TypeError:
        print("ERROR: calibration configuration incorrect.")
        die = 1
    if not sacrificial:
        die = 1
    if not nt_update_frequency:
        print("INFO: framerate not specified, using default of 10.")
        nt_update_frequency = 10
    if not debug:
        print("INFO: debug not specified, not debugging.")
    if not search:
        print("INFO: search not specified, searching for targets.")




    if die > 0:
        print("FATAL ERROR: unable to load vision configuration. Exiting.")
        sys.exit(1)

    if debug == '1':
        debug = True
    else:
        debug = False
    if search == '0':
        search = False
    else:
        search = True

    if debug:
        print('INFO: debug set.')

    green = {'green_upper': green_upper, 'green_lower': green_lower}
    calibration = {'green': green}

    return os, camera, calibration, nt_update_frequency, debug, search


def write_cal(cal):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('mask', 'green_upper', ','.join(cal['green']['green_upper']))  # convert lists into single strings
    config.set('mask', 'green_lower', ','.join(cal['green']['green_lower']))

    print('Validating configuration and writing to disk.')
    run_config(config)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return True