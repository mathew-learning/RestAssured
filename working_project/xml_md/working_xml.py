import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('cars.xml')
car_sales = tree.getroot()
print(car_sales.tag)
for car in car_sales.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price' :
            print(prop.attrib, end='')
        print(' =', prop.text)

new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
car_sales.append(new_car)
tree.write('newcars.xml', method='')