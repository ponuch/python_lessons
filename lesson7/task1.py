# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись;- вывод всего справочника;- поиск по имени;
# - экспорт справочника в форматы html, xml;- чтение данных из файла;- дополнительные функции по желанию
# Требуется реализовать минимум 3 инструмента для работы со справочником.

def newRecord (name, phone):
    with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.txt", "a+") as f:
        f.write(name + " " + phone + "\n")

def openDict():
    with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.txt", "r") as f:
        while (line := f.readline().rstrip()):
            print(line)
            
def findRecord(name):
    with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if line.__contains__(name):
                return line
            
def exportHtml():
    with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.html", "w") as f_html:
            f_html.write("""<html>
                                <head>
                                    <title>Phone records</title>
                                </head>
                                <body> <ol>""")
            for line in lines:
                f_html.write("""<li>""" + line + """</li>\n""")
            f_html.write(""" </ol> 
                         </body>
                         </html>
                         """)
            
def exportXml():
    with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.txt", "r") as f:
        lines = [line.rstrip() for line in f]  
        with open("/home/ponuch/Projects/Python_lessons/lesson7/dict.xml", "w") as f_xml: 
            f_xml.write(""" <?xml version="1.0" encoding="UTF-8"?>\n""")
            f_xml.write("""<records>\n""")
            for line in lines:
                f_xml.write("""<record>""" + line + """<record>\n""")
            
            f_xml.write("""</records>\n""")
            

            
                 
newRecord("bob", "8-800-233-3435")
newRecord("alice", "8-800-233-3765")
newRecord("siri", "8-800-234-8735")
newRecord("john", "8-800-256-3490")

openDict()

print(findRecord("bob1"))

exportHtml()
exportXml()