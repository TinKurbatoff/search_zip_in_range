from uszipcode import SearchEngine
import argparse	

# Default VERBOSITY level
VERBOSITY = False


class ZIPcodesInRange(object):
    """docstring for ClassName"""
    def __init__(self, default_range=30):
        self.range = default_range
        
    def if_exists(self, zip):
        search = SearchEngine(simple_zipcode=True, db_file_dir="/tmp")  # # set simple_zipcode=False to use rich info
        zipcode = search.by_zipcode(zip)
        if zipcode.zipcode:
            return True
        else:
            return False

    def search(self, zip,range,results=0):
        #
        search = SearchEngine(simple_zipcode=True, db_file_dir="/tmp")  # set simple_zipcode=False to use rich info database
        if not self.if_exists(zip):
            return ''
        zipcode = search.by_zipcode(zip)
        if VERBOSITY:
            print('ZIP search results:')
            print(zipcode)
        if VERBOSITY:
            print('Center coordiante: Lat:{} Long:{}'.format(zipcode.lat, zipcode.lng))
        res = search.by_coordinates(zipcode.lat, zipcode.lng, radius=range, returns=results)
        return res

    def list_search(self, _zip, _range, _results=0):
        #
        _data = []
        for zips in self.search(_zip, _range, _results):
            _data.append(zips.zipcode)
        return _data


def main():
    global VERBOSITY; 
    parser = argparse.ArgumentParser(description='Prints all zipcodes in range')
    parser.add_argument('zip', metavar='<zip code>', help='the base ZIP code for search ')
    parser.add_argument('--dist', dest='distance', type=int, 
                    default=30,
                    help='range for ZIP codes search')
    parser.add_argument('--lim', dest='limit', type=int, 
                    default=0,
                    help='limit results to number')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true", default=False)
    args = parser.parse_args()

    VERBOSITY = args.verbose;
    print('—————————————————————————————————————')
    if VERBOSITY:
        print( 'ZIP:{}, Distance:{}'.format(args.zip, args.distance))
    ZIPinRange = ZIPcodesInRange(10)
    data = ZIPinRange.list_search(args.zip, args.distance, args.limit)
    print( data )



if __name__ == '__main__':
    main()