class Area(object):
    def __init__(self, id, area_name):
        self.id = id,
        self.area_name = area_name

    def object_to_dict(self):
        return {
            "id": self.id,
            "area_name": self.area_name
        }

    def show_area_name(self):
        area_name = self.area_name
        s = "这里是: " + area_name + "。"
        return s
