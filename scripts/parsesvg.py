from lxml import etree

fname = 'rst/_images/haffa-letter-h.svg'
fin = open(fname)
tree = etree.parse(fin)

for element in tree.iter():
    if element.tag.split("}")[1] == 'path':
	    print(element.get('d'))

