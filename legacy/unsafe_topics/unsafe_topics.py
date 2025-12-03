import os
import json


class UnsafeTopics:
    def __init__(self):

        self.unsafe_topics = list()
        self.load_unsafe_topics()

    def load_unsafe_topics(self):

        # get files with unsafe topics data
        folder_path = "unsafe_topics"
        all_items = os.listdir(folder_path)
        files_only = [item for item in all_items if os.path.isfile(os.path.join(folder_path, item))]


        # get data about each unsafe topic
        for topic in files_only:
            with open(folder_path + '/' + topic, 'r', encoding='utf-8') as file:
                data = json.load(file)
            self.unsafe_topics.append(data)

ut = UnsafeTopics()
