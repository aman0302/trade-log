import csv

from logger.utils.ExecutablePath import *

class FileWriter:

    def write(self, smallcases):
        for smallcase in smallcases:
            file = open(get_dump_location(smallcase.name), "a+", newline='')
            file.write('\t'.join(smallcase.get_ordered_data()) + '\n')
            # wr = csv.writer(file )
            # wr.writerow(smallcase.get_ordered_data())
            file.close()