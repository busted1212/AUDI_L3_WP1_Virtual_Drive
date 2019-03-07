def read_path_points(file):
    _points = []
    with open(file, 'r') as _file_handler:
        _contents = _file_handler.readlines()
        for _content in _contents:
            _content_sorted = _content.split(',', 2)
            _content_sorted[0] = float(_content_sorted[0][1:])
            _content_sorted[1] = float(_content_sorted[1])
            _content_sorted[2] = _content_sorted[2][:-2]
            _points.append([_content_sorted[0], _content_sorted[1], _content_sorted[2]])
        return _points


if __name__ == '__main__':
    points = read_path_points('D://工作//AUDI_L3_WP1_Virtual_Drive//Beijing_Virtual_Drive//airport_express//ae_tocity//file_list.txt')
    print(type(points[0][0]))
