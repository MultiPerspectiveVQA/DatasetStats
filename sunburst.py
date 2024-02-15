import plotly.express as px
import pandas as pd
import os

def generate_image(questions, figname):
    root = 'output'
    levels = [[],[],[],[],[],[]]
    word_counts = {}
    for question in questions:
        words = question.split()[:6]
        for i in range(0,6):
            if len(words)<i+1:
                levels[i].append(None)
            else:
                levels[i].append(words[i])

    df_dict = dict()
    path = list()
    for i, ch in enumerate(['A', 'B', 'C', 'D', 'E', 'F']):
        if len(levels[i]) > 0:
            df_dict[ch] = levels[i]
            path.append(ch)
        else:
            break
    df_dict['G'] = [1]*len(levels[0])

    df = pd.DataFrame(
        df_dict
    )
    df = df.fillna('.')
    # print(df)
    # print(df_dict)
    # print(path)
    fig = px.sunburst(df, path=path, values='G')
    fig.write_image(os.path.join(root, figname), scale=2.0)

def generate_sunburst(dataset):
    q_amb_vqa, q_amb_vizwiz = list(), list()
    q_amb = list()

    ob_amb_vqa, ob_amb_vizwiz = list(), list()
    ob_amb = list()
    for data in dataset:
        if data['ambiguous_question'] == 'Yes' and 'COCO' in data['image_filename']:
            q_amb_vqa.append(data['question'])
            ob_amb_vqa.append(data['object_lookup'])
        elif data['ambiguous_question'] == 'Yes' and 'VizWiz' in data['image_filename']:
            q_amb_vizwiz.append(data['question'])
            ob_amb_vizwiz.append(data['object_lookup'])
        if data['ambiguous_question'] == 'Yes':
            q_amb.append(data['question'])
            ob_amb.append(data['object_lookup'])
            
    generate_image(q_amb_vqa, 'sb_amb_q_vqa.png')
    generate_image(q_amb_vizwiz, 'sb_amb_q_vizwiz.png')
    generate_image(ob_amb_vqa, 'sb_amb_oq_vqa.png')
    generate_image(ob_amb_vizwiz, 'sb_amb_oq_vizwiz.png')
        
