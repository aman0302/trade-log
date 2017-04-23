import os, platform
import logging

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
        folderName = 'linux'
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
        folderName = 'linux'
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

