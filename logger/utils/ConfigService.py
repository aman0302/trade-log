from logger.utils.ExecutablePath import *

class ConfigService():
    def __init__(self):
        self.id_mapping = {}
        self.config_file={}
        self.count =0


    def get_smallcase_id(self, smallcase_name):
        if smallcase_name in self.id_mapping:
            return self.id_mapping[smallcase_name]

        else:
            with open(get_mapping_file()) as f:
                for line in f:
                    if line is not None or line is not '':
                        (key, val) = line.split(':')
                        self.id_mapping[key] = val

            if smallcase_name in self.id_mapping:
                return self.id_mapping[smallcase_name]

            else:
                self.count= 0
                f = open(get_count_file(),'r')
                self.count = int(f.readline())
                f.close()
                f = open(get_count_file(), 'w')
                value = self.count + 1
                f.write(str(value))
                f.close()

                smallcase_id = "SM" + str(self.count + 1);
                with open(get_mapping_file(), "a") as f:
                    f.write(smallcase_name+":"+ smallcase_id+"\n")

                return smallcase_id
