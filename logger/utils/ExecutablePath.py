import os, platform


def get_geckodriver_path():
    system = platform.system()
    folderName = ''
    fileName = ''
    print(system)

    if system == 'Darwin':
        folderName = 'mac'
        fileName = 'geckodriver'

    if system == 'Windows':
        folderName = 'win32'
        fileName = 'geckodriver.exe'

    if system == 'Linux':
        folderName = 'pilinux'
        fileName = 'geckodriver'

    return compose_path(folderName, fileName)


def get_chromedriver_path():
    system = platform.system()
    folderName = ''
    fileName = ''
    print(system)

    if system == 'Darwin':
        folderName = 'mac'
        fileName = 'chromedriver'

    if system == 'Windows':
        folderName = 'win32'
        fileName = 'chromedriver.exe'

    if system == 'Linux':
        folderName = 'pilinux'
        fileName = 'chromedriver'

    return compose_path(folderName, fileName)


def get_credentials_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'secrets', 'credentials.json'))


def get_google_drive_secret_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'secrets', 'google_drive_secret.json'))


def get_log_file_name():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'application.log'))


def compose_path(folderName, fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'driver', folderName, fileName))


def get_dump_location(file_name):
    return os.path.abspath(os.path.join(os.path.expanduser("~"), 'Dropbox', 'Zerodha', 'Smallcase', file_name))


def get_mapping_file():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'id_mapping'))


def get_config_file():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'config_file'))


def get_count_file():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'count'))


def get_excel_file_heading():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'excel'))


def get_reverse_pickup_excel_file_heading():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'reverse_pickup_excel'))


def get_reverse_pickup_awb_file_location():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'ReverseAWBs'))


def get_forward_pickup_awb_file_location():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'ForwardAWBs'))


def get_upload_excel_file_location():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'EComExpress.xls'))


def get_reverse_pickup_excel_file_location():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'ReversePickup.xls'))
