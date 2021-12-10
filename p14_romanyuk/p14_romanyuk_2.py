import json
with open('image_info_test-dev2017.json') as file:
    d = json.load(file)
print('The number of images:', len(d['images']))
unique_categories = set()
for i in d['categories']:
    unique_categories.add(i['name'])
print('The number of available categories:',len(unique_categories))
for i in d['images']:
    if i['file_name'] == '000000000001.jpg':
        url = i['coco_url']
        height = i['height']
        width = i['width']
        id = i['id']
        print('Coco_url:', url, 'height:', height, 'width:', width, 'id:', id)
lst = []
for i in d['images']:
    lst.append(i['id'])
max_id = max(lst)
max_number = '{}'.format(max_id).zfill(12) + '.jpg'
print('The name of the photo with the largest number:', max_number)