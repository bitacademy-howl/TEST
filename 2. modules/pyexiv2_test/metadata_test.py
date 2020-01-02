try:
    import pyexiv2
    pyexivexists = True
except:
    pyexivexists = False

def tag_image(file_name, Modules, Experiment, Category, Description):
    if pyexivexists:
        metadata = pyexiv2.Image(file_name)
        try:
            _dict = metadata.read_exif()
            # print(_dict)

        except IOError:
            print("Not an image")

        else:
            _dict['Exif.Image.Software'] = Modules
            _dict['Exif.Image.Make'] = Experiment
            _dict['Exif.Photo.MakerNote'] = Category
            _dict['Exif.Image.ImageDescription'] = Description

            # metadata.modify_all({"EXIF":_dict})
            metadata.modify_exif(_dict)
            # print(metadata.read_all())
            # metadata.clear_all()

        finally:
            meta_reload = pyexiv2.Image(file_name)
            print(meta_reload.read_exif())
            # print(metadata.read_all())
            # metadata.clear_all()
    else:
        print("PyExiv not present")

    return 1

def read_exif(file_name):
    if pyexivexists:
        metadata = pyexiv2.Image(file_name)
        try:
            _dict = metadata.read_exif()
            # print(_dict)

        except IOError:
            print("Not an image")

        else:
            meta_reload = pyexiv2.Image(file_name)
            print(meta_reload.read_exif())
            print(metadata.read_all())
            # metadata.clear_all()
    else:
        print("PyExiv not present")

    return 1


file_name = "D:\\workspace\\Python\\2. modules. Befs_un0ric\\Befs_Un0rick_modify\\json\\images\\20191201a-1. Basic.png"
read_exif(file_name)
# tag_image(file_name, "matty", "20180516a", "graph", "희웅")