from uszipcode import SearchEngine
import argparse	

# Default VERBOSITY level
VERBOSITY = False

def ZIPcodesInRange(zip,range,results=0):
    #
    search = SearchEngine(simple_zipcode=True, db_file_dir="/tmp")  # set simple_zipcode=False to use rich info database
    zipcode = search.by_zipcode(zip)
    if VERBOSITY:
        print('ZIP search results:')
        print(zipcode)
    if VERBOSITY:
        print('Center coordiante: Lat:{} Long:{}'.format(zipcode.lat, zipcode.lng))
    res = search.by_coordinates(zipcode.lat, zipcode.lng, radius=range, returns=results)
    return res

def ZIPcodesInRangeList(_zip,_range,_results=0):
    #
    _data = []
    for zips in ZIPcodesInRange(_zip, _range, _results):
        _data.append(zips.zipcode)
    return _data


def main():
    parser = argparse.ArgumentParser(description='Prints all zipcodes in range')
    parser.add_argument('zip', metavar='<zip code>', help='the base ZIP code for search ')
    parser.add_argument('--dist', dest='distance', type=int, 
                    default=30,
                    help='range for ZIP codes search')
    parser.add_argument('--lim', dest='limit', type=int, 
                    default=0,
                    help='limit results to number')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_false")
    VERBOSITY = args.verbosity;

    if VERBOSITY:
        print('—————————————————————————————————————')
    args = parser.parse_args()
    if VERBOSITY:
        print( 'ZIP:{}, Distance:{}'.format(args.zip, args.distance))
    data = ZIPcodesInRangeList(args.zip, args.distance,args.limit)
    print( data )



if __name__ == '__main__':
    main()