from PIL import Image

# infile = 'D:\工作\AUDI_L3_WP1_Virtual_Drive\BSV\Panorama\Panoramapano@lng=116.4641lat=39.966324.jpeg'
# outfile = 'D:\工作\AUDI_L3_WP1_Virtual_Drive\BSV\StaticImage\StaticImagestatic@lng=116.5221lat=40.019363.jpg'
# img = Image.open(infile)
# jgz = Image.open(outfile)
# target = Image.new('RGB', (1324, 512))
# target.paste(jgz, (0, 0))
# target.paste(img, (300, 0))
# target_resize = target.resize((600, 320), Image.ANTIALIAS)
# target_resize.save('new.jpg')


def image_edit(geo_add):
    _dir = 'D://工作//AUDI_L3_WP1_Virtual_Drive//Beijing_Virtual_Drive//'
    _panorama_file_name = 'airport_express//ae_tocity//pano_bj_ae_tocity//Panoramapano@lng=' + str(geo_add[0]) + 'lat=' + \
        str(geo_add[1]) + '.jpeg'
    _static_file_name = 'airport_express//ae_tocity//stat_bj_ae_tocity//StaticImagestatic@lng=' + str(geo_add[0]) + 'lat=' + \
        str(geo_add[1]) + '.jpeg'
    _panorama = Image.open(_dir + _panorama_file_name)
    _static = Image.open(_dir + _static_file_name)
    _target = Image.new('RGB', (1324, 512))
    _target.paste(_static, (0, 0))
    _target.paste(_panorama, (300, 0))
    _file_name = 'pic@lng=' + str(geo_add[0]) + ',lat=' + str(geo_add[1]) + '.jpg'
    _target_dir = 'D://工作//AUDI_L3_WP1_Virtual_Drive//Beijing_Virtual_Drive//airport_express//ae_tocity//full_bj_ae_tocity//'
    _target_path = _target_dir + _file_name
    _target.save(_target_path)
    return _target_dir, _file_name
    return _target_dir, _file_name


def read_path_points(file):
    _points = []
    with open(file, 'r') as _file_handler:
        _contents = _file_handler.readlines()
        for _content in _contents:
            _content_sorted = _content.split(',', 2)
            _content_sorted[0] = float(_content_sorted[0][1:])
            _content_sorted[1] = float(_content_sorted[1])
            _content_sorted[2] = _content_sorted[2][:-2]
            print(_content_sorted[2])
            _points.append([_content_sorted[0], _content_sorted[1], _content_sorted[2]])
        return _points


def image_resize(dir_pic, name_pic):
    _path = dir_pic + name_pic
    _pic = Image.open(_path)
    _pic_resized_path = dir_pic + '//resized_full//' + name_pic
    _pic_resized = _pic.resize((620, 280), Image.ANTIALIAS)
    _pic_resized.save(_pic_resized_path)


points = read_path_points('D://工作//AUDI_L3_WP1_Virtual_Drive//Beijing_Virtual_Drive//airport_express//ae_tocity//file_list.txt')
#
for point in points:
    (dir_full, file_name) = image_edit([point[0], point[1]])
    image_resize(dir_full, file_name)
