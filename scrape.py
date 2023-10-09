import argparse, sys
import os

from gisaid_flu_scraper import GisaidFluScraper
from gisaid_cov_scraper import GisaidCovidScraper


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', help="Path to file with credentials (alternative, default: credentials.txt)", type=str, default="credentials.txt")
    parser.add_argument('--destination', '-d', help="Destination directory (default: fastas/)", type=str, default="fastas/")
    parser.add_argument('--headless', '-q', help="Headless mode of scraping (experimental)", type=str2bool, nargs='?', default=False)
    parser.add_argument('--whole', '-w', help="Scrap whole genomes only", type=str2bool, nargs='?', default=False)
    parser.add_argument('--flu', action="store_true")
    parser.add_argument('--covid', action="store_true")

    args = parser.parse_args()
    args.headless = True if args.headless is None else args.headless
    args.whole = True if args.whole is None else args.whole  
    return parser, args


def get_credentials(args):
    if args.filename is None:
        raise ValueError
    try:
        with open(args.filename) as f:
            login = f.readline()
            passwd = f.readline()
    except FileNotFoundError:
        print("File not found.")
        raise ValueError

    whole = args.whole
    destination = args.destination
    return login, passwd, whole, destination


if __name__ == "__main__":
    parser, args = parse_args()
        
    try:
        login, passwd, whole, destination = get_credentials(args)
    except ValueError:
        print(parser.format_help())
        sys.exit(-1)
    if args.flu:
        scraper = GisaidFluScraper(args.headless, whole, destination)
        scraper.login(login, passwd)
        scraper.load_epiflu()
    elif args.covid:
        scraper = GisaidCovidScraper(args.headless, whole, destination)
        scraper.login(login, passwd)
        scraper.load_epicov()
    
    scraper.download_packages('metadata_tsv')
    scraper.download_packages('fasta.tar')
    print("New samples:", scraper.new_downloaded)
