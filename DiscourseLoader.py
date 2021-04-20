import os

class DiscourseLoader:
    def __init__(self, path):
        self.raw_relations = self.loadCorpus(path) #each raw_relation is a two-part tuple, [0] is raw annotation, [1] is raw text

    #This method takes the path to the pdtb3 corpus and returns a tuple of the raw text of the discourse fields and the filename
    def loadCorpus(self, path):
        #This section loads the raw annotations
        relations = []
        ann_path = path+'gold/'
        for folder in os.listdir(ann_path):
            if(folder == '.DS_Store'):
                continue
            for fn in os.listdir(ann_path+folder):
                f = open(ann_path+'/'+folder+'/'+fn, 'r')
                for line in f.readlines():
                    relations.append([line,path+'raw/'+folder+'/'+fn])

        return relations
