import argparse

parser = argparse.ArgumentParser(description="demo")
#two methods
parser.add_argument('--name',type=str,help="ur name")
parser.add_argument('sex',help="ur sex")

args=parser.parse_args()
print(f"ur name is {args.name} and u are {args.sex}")