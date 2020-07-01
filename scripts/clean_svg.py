from lxml import etree

def clean_svg(fname):
    with open(fname) as fin:
        tree = etree.parse(fin)

    for element in tree.iter():
        print(element.tag)

files = [
    'haffa-letter-A.svg',
    'haffa-letter-H.svg',
    'haffa-letter-F.svg',
    'haffa-pilot.svg',
    'haffa-airplane.svg'
]

for fname in files:
    fname = 'rst/_images/' + fname
    clean_svg(fname)
