import json
def count(file:str):
    """Ouvre le fichier JSON, et compte le nombre d'éléments présents dans la structure."""
    with open(file, "r", encoding="utf-8") as file:
        elementsCount = len(json.load(file))
        return elementsCount


def written_by(file:str, writer) -> str:
    """Ouvre le fichier JSON, et cherche les enregistrements écrits par Vince Gilligan"""
    writer_name = None
    with open(file,"r", encoding="utf-8") as file:
        text = file.read()
        file.seek(0)
        json_data = json.load(file)
        print(type(text))
        print(json_data[0]['Writer'])
        writer_name = writer
    return writer_name

def longest_title(file:str):
    """Ouvre le fichier JSON, et cherche le film avec le nom le plus long"""
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
        json_data = json.load(file)
        longestTitle = None
        for i in text:
            title = json_data[i]['Title']
            if len(title) > longestTitle:
                longestTitle = title
        return longestTitle

