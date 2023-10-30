import json

with open("in.txt", encoding='utf-8') as file:
    lines = [row.strip() for row in file]

plus_text = '''
верни json { 
"text": текст,
"description": придумай смешной комментарий к тексту
},  

текст -
'''

for i,line in enumerate(lines):
    text = f'{plus_text}{line}'
    with open(f'out/{i}.json', 'w', encoding='utf-8') as outfile:
        json.dump(text, outfile, indent=4, ensure_ascii=False)

    print(i)