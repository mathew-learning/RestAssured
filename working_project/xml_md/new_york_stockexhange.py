import xml.etree.ElementTree

key_words = ['Company', 'Last', 'Change', 'Min', 'Max']
key_widths = [40, 15, 10, 10, 10, 10]


def show_head():
    for (n,w) in zip(key_words, key_widths):
        print(n.ljust(w), end='|')
    print()
    print("-"*sum(key_widths))


def show_prop(prop):
    for (n,w) in zip(key_words, key_widths):
        if str(n) == 'Company':
            print(str(prop.text).ljust(w), end='|')
        else:
            print(str(prop.attrib[str(n).lower()]).ljust(w), end='|')
    print()


show_head()


def show(prop):
    show_prop(prop)


try:
    tree = xml.etree.ElementTree.parse('nyse.xml')
except FileNotFoundError:
    print("file doesn't exit")
else:
    ny_se = tree.getroot()
for stock in ny_se.findall('quote'):
    attrbu = stock
    show(attrbu)

