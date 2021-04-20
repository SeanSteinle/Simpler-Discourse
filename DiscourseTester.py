from DiscourseLoader import DiscourseLoader
from DiscourseUnit import DiscourseUnit

print("loading corpus...")
corpus = DiscourseLoader('C:/Users/seans/Desktop/School/Sem6/AI_Ethics/discourse/pdtb3/pdtbMerge-v9-3/')
print("printing stuff...")
#print(corpus.raw_relations[5][1])
d = DiscourseUnit(corpus.raw_relations[6])
print(d.Relation.type)
print(d.Relation.type_definition)
print(d.Arg1.text)
print(d.Arg2.text)
print(d.highlightDiscourse(d.text_path, 'out.html'))

#for i in range(5):
#    print(i)
#    DiscourseUnit(corpus.raw_relations[i])
