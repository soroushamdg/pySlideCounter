import glob
import pptx
import os
class pySlideCounter():
    def __init__(self,path):
        self.path = path
        os.chdir(self.path)
        self.file_names = glob.glob('*.pptx')
        self.counter = 0
    def count(self):
        for prs_name in self.file_names:
            per = pptx.Presentation(prs_name)
            self.counter += len(per.slides)
        return self.counter
