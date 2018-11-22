import logging
import csv
from operator import itemgetter

logger = logging.getLogger(__name__)

class ClientsCsv(object):

    def __init__(self, csv_file):
        self.rows = []
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            if ",".join(header) != "timestamp (s),# clients,Hatch rate (#clients/s)":
                logger.warning('Clients csv file header invalid (expected "timestamp (s)","# clients","Hatch rate (#clients/s)"')
            timestamps = []
            for line_number, elements in enumerate(reader):
                if elements != []:
                    if len(elements) != 3:
                        raise ValueError("invalid row %d contains %d elements (3 required)" %
                        (line_number+2,len(elements)))
                    elements = list(map(int,elements))
                    if elements[0] in timestamps:
                        raise ValueError("invalid row %d contains duplicate timestamp %d" %
                                         (line_number+2,elements[0]))                                         
                    timestamps.append(elements[0])
                    if all(i >= 0 for i in elements):
                        self.rows.append(elements)
                    else:
                        raise ValueError("invalid row %d contains non-negative integers" %
                                         line_number+2)
            
        self.rows = sorted(self.rows, key=itemgetter(0))
        if self.rows == []:
            raise ValueError("csv file contains no data")
        print("building a csv")
