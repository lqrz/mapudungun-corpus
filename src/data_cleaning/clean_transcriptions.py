import glob
import re
from pathlib import Path
from typing import Union, NoReturn
import sys


def clean_annotations(text: str) -> str:
    """Clean line annotations."""
    replacements = [
        "<*spa>",
        "*spa>",
        "<*spa",
        "<spa>",
        "< spa>",
        "< *spa>",
        " spa>",
        "<spa",
        "<uh>", "<uhm>", "<hm>", "<uh.",
        "<noise>",
        "-/", "/-", "+/", "/+", "<%>",
        "<p>",
        "<cough>", "<smack>",
        "<!", "<(",
    ]
    for r in replacements:
        text = text.replace(r, "")
    return text


def assert_paths(path_input:str, path_output:str) -> Union[None, NoReturn]:
    """Assert paths."""
    # asserts
    assert not path_input.endswith('/'), path_input
    assert not path_output.endswith('/'), path_output


def clean(path_input:str, path_output:str) -> None:
    """Clean files."""
    filepaths = glob.glob(f'{path_input}/*.trl')
    for f in filepaths:
        lines = []
        fin = open(f, 'r', encoding='iso-8859-1')
        fout = open(f'{path_output}/{Path(f).stem}.txt', 'w', encoding='utf-8') 
        for ix, l in enumerate(fin.readlines()):
            if l.startswith(';'): continue
            # lowercase
            l = l.lower()
            # left strip spaces and newline
            l = l.rstrip(' ').rstrip('\n').rstrip(' ')
            # fix starting dialog tags (e.g. 'nmlch-nfmcqA2_x_0308_nfmcq_00:fey')
            l = re.sub(r'(\d{2}):\s*', r'\1: ', l)
            # remove starting dialog tag 
            l = re.sub(r'^.+_\d{4}_.+_\d{2}: ', '', l)
            # remove annotations
            l = clean_annotations(text=l)
            # clean mapuche tags
            l = re.sub(r'<!1[^\s>]*>', '', l)
            l = re.sub(r'<!1[^\s>]+$', '', l)
            l = re.sub(r'<!1[^\s>]+\s', '', l)
            # *(?:>(?:\s+)?|\s+|$)', '', l)
            # clean remaining tags
            l = re.sub(r'<[^>]+>', '', l)
            
            # left and right strip spaces
            l = l.strip(' ')
            # remove resulting empty lines
            if l == "": continue
            # if '<' in l: f, ix, l # debug
            _ = lines.append(l)
            _ = fout.write(l+'\n')


if __name__ == '__main__':
    _ = assert_paths(path_input=sys.argv[1], path_output=sys.argv[2])
    _  = clean(path_input=sys.argv[1], path_output=sys.argv[2])
    
# path_input = '../../data/raw/transcriptions/*.trl'
# path_output = '../../data/cleaned/transcriptions'
