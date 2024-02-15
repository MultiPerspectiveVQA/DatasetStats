import argparse
import json
import os

from split import get_split
from sunburst import generate_sunburst

def load_data(rootpath):
    data = list()
    with open(os.path.join(rootpath, 'metadata.jsonl'), 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def main(args):
    choices = [args.all, args.split, args.sunburst, args.wordcloud, args.pos]
    if not any(choices):
        print(f'None of the stats are selected. Existing the program')

    if args.all:
        args.split, args.sunburst, args.wordcloud, args.pos = True, True, True, True
    root = os.path.join('data', 'train') if args.data == 'train' else os.path.join('data', 'val')
    dataset = load_data(root)

    if args.split:
        get_split(dataset)

    if args.sunburst:
        generate_sunburst(dataset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='get_stats',
                    description='Driver file to generate one or all stats related to the dataset',
                    )
    parser.add_argument('-d', '--data', 
                        required=True, choices=['train', 'val'], type=str,
                        help='choose the dataset to generate stats for')
    parser.add_argument('--all',
                        required=False, action='store_true', help='generate all available stats')
    parser.add_argument('--split',
                        required=False, action='store_true', help='what proportion of ambiguous question are from VizWiz vs VQA')
    parser.add_argument('--sunburst',
                        required=False, action='store_true', help='generate sunburst diagrams')
    # parser.add_argument('--qlength', 
    #                     required=False, action='store_true', help='compare length of question ambiguous / non ambiguous questions')
    parser.add_argument('--wordcloud', 
                        required=False, action='store_true', help='generate word cloud for ambiguous / non ambiguous questions')
    parser.add_argument('--pos',
                        required=False, action='store_true', help='get pos taga and analyse their distribution for each question')
    args = parser.parse_args()
    main(args)