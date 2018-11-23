import logging
import csv
from operator import itemgetter

logger = logging.getLogger(__name__)

class ClientsCsv(object):

    def __init__(self, csv_file):
        self.rows = []
        self.initial_conditions = None
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
        first_row = self.rows[0]
        print(first_row)
        if first_row[0] == 0:
            # First row has timestamp 0
            self.initial_conditions = first_row
            del(self.rows[0])
        if self.rows == []:
            raise ValueError("csv file requires at least 2 rows of data")
