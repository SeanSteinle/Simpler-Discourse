import os

class DiscourseUnit:
    def __init__(self, raw_relation):
        fields = raw_relation[0].split('|')

        #data members
        self.type_definitions_path = 'rel_type_definitions.txt'
        self.text_path = raw_relation[1]
        self.Relation = Relation(fields[0], fields[7], fields[8]) #connective=7, class=8
        self.Arg1 = Arg(fields[14], self.text_path)
        self.Arg2 = Arg(fields[20], self.text_path)

    def highlightDiscourse(self, text_file, output_file, color1='orange', color2='red', color_con='green', context_len=250): #output needs to be html
        htmlFile = '''
           <!DOCTYPE html>
        <html>
        	<head></head>
        	<body>
                <p>{0}</p>
        	</body>
        </html>
        '''
        #<p style="color:blue;">{1}</p>

        #gets text from raw text file
        text_f = open(self.text_path, 'r')
        lines = text_f.read()
        text_f.close()

        #replaces args + conn w/ html color args + conn
        lines = lines.replace('.START', '')
        repl_1 = '<font style="color:{0};">{1}</font>'.format(color1, self.Arg1.text)
        repl_2 = '<font style="color:{0};">{1}</font>'.format(color2, self.Arg2.text)
        repl_con = '<font style="color:{0};">{1}</font>'.format(color_con, self.Relation.connective)
        lines = lines.replace(self.Arg1.text, repl_1)
        lines = lines.replace(self.Arg2.text, repl_2)
        lines = lines.replace(self.Relation.connective, repl_con)

        #finds boundaries of text
        start = lines.find(repl_1)
        end = lines.find(repl_2) + len(repl_2) + len(repl_con)

        #check that boundaries are within total text window
        if(start-context_len<=0):
            start = 0
        else:
            start = start-context_len
        if(end+context_len>=len(lines)):
            end = 0
        else:
            end = end+context_len
        context = lines[start:end]

        #ADD STUFF FOR ARG

        #opens html, writes raw text
        html_f = open(output_file, 'w')
        html_f.write(self.Relation.type + " (" + self.Relation.semantic_class + "): ")
        html_f.write(self.Relation.type_definition)
        html_f.write(htmlFile.format(context))
        html_f.close()

class Arg():
    def __init__(self, raw_substring, text_path):
        self.text = self.getText(raw_substring, text_path)

    #gets the text of the argument. can be in one or multiple chunks.
    def getText(self, raw_substring, text_path):
        #print(raw_substring[:-1])
        if(raw_substring[-1]==';'):
            raw_substring = raw_substring[:-1]
        if(';' not in raw_substring):
            nums = raw_substring.split("..")
            f = open(text_path, 'r')
            text = f.read()
            f.close()
            return text[int(nums[0]):int(nums[1])]
        else: #this case is for multi-part args...
            pairs = raw_substring.split(";")
            f = open(text_path, 'r')
            text = f.read()
            texts = ""
            for pair in pairs:

                nums = pair.split("..")
                #print("text",text)
                #print("rs",raw_substring)
                #print("pair",pair)
                #print("nums",nums)
                texts+=text[int(nums[0]):int(nums[1])]+" "
            return texts

class Relation():
    def __init__(self, rel_type, connective, semantic_class):
        self.type = rel_type
        self.types_dict = self.defineTypes()
        self.type_definition = self.types_dict[rel_type]
        self.semantic_class = semantic_class
        self.connective = connective

    def defineTypes(self):
        defs = '''Explicit - Has an explicit discourse connective. Examples include since, because and therefore.
Implicit - Must be inferred, lack the cues of explicit connectives.
AltLex - Lack an explicit connective, but contain other phrasal or construction-based evidence for the relation that holds between the arguments. Cases where a discourse relation is inferred between adjacent sentences but where providing an implicit connective leads to redundancy in the expression of the relation.
AltLexC - Lack an explicit connective, but contain other phrasal or construction-based evidence for the relation that holds between the arguments. They are a type of AltLex construction, they can be found on their own, separate from other AltLex tokens but have the same fields as AltLex. Examples include so, such and too.
Hypophora - Involves a question posed in Arg1 and answer in Arg2. Explicitly marked question-response pairs.
EntRel - A relation holds between an entity mentioned in Arg1 and the contents of Arg2.
NoRel - Annotated only between adjacent sentences within a paragraph that are not linked to each other by a discourse relation.'''
        defs = defs.split('\n')
        dict = {}
        for d in defs:
            type, definition = d.split(' - ')
            dict[type] = definition
        return dict
