import os
import json


class Publishers:
    def __init__(self):

        self.publishers = list()
        self.load_publishers()

    def load_publishers(self):

        # get files with publishers data
        folder_path = "./publishers/publishers"
        all_items = os.listdir(folder_path)
        files_only = [item for item in all_items if os.path.isfile(os.path.join(folder_path, item))]

        # get data about each publisher
        all_publishers = list()
        for publisher in files_only:
            with open(folder_path + '/' + publisher, 'r', encoding='utf-8') as file:
                data = json.load(file)
            all_publishers.append(data)

        # filter publisher by not empty info
        # TODO: delete this, add into to each publisher
        for publisher in all_publishers:
            if publisher != {}:
                self.publishers.append(publisher)
