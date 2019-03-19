import os
from configparser import ConfigParser
from pathlib import Path

CONF_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'confs')
CONF_SUFFIX = '.ini'


class ConfigurationManager:
    @staticmethod
    def list_confs():
        conf_list = [
            Path(f).stem
            for f in os.listdir(CONF_PATH)
            if os.path.isfile(os.path.join(CONF_PATH, f)) and Path(f).suffix == CONF_SUFFIX
        ]

        return conf_list

    @staticmethod
    def get_confs(domain):
        conf_file = os.path.join(CONF_PATH, f'{domain}{CONF_SUFFIX}')
        cfg = ConfigParser()
        cfg.read(conf_file)
        return cfg

    @staticmethod
    def get_confs_values(domain):
        conf_file = os.path.join(CONF_PATH, f'{domain}{CONF_SUFFIX}')
        cfg = ConfigParser()
        cfg.read(conf_file)
        result = {}
        for section in cfg.sections():
            if section not in result:
                result[section] = {}
            for option in cfg.options(section):
                result[section][option] = cfg.get(section, option)
        return result

    @staticmethod
    def set_conf(domain, value):
        conf_file = os.path.join(CONF_PATH, f'{domain}{CONF_SUFFIX}')
        cfg = ConfigParser()
        cfg.read(conf_file)

        for section in value:
            for option in value[section]:
                cfg.set(section, option, value[section][option])
        with open(conf_file,'w') as f:
            cfg.write(f)
