import os

output_dir = 'output'

def write_data(**kwargs):
    with open(os.path.join(output_dir, 'split_stats.txt'), 'w') as f:
        f.write(f'Number of Ambiguous Questions VQA: {kwargs["q_amb_vqa"]} \n')
        f.write(f'Number of Ambiguous Questions VizWiz: {kwargs["q_amb_vizwiz"]} \n')
        f.write(f'Number of Non Ambiguous Questions VQA: {kwargs["q_nonamb_vqa"]} \n')
        f.write(f'Number of Non Ambiguous Questions VizWiz: {kwargs["q_nonamb_vizwiz"]} \n')
        f.write(f'Total Number of Datapoints: {kwargs["total"]} \n')

def get_split(dataset):
    q_amb_vqa = 0
    q_amb_vizwiz = 0 
    q_nonamb_vqa = 0
    q_nonamb_vizwiz = 0
    for data in dataset:
        if data['ambiguous_question'] == 'Yes' and 'COCO' in data['image_filename']:
            q_amb_vqa += 1
        elif data['ambiguous_question'] == 'Yes' and 'VizWiz' in data['image_filename']:
            q_amb_vizwiz += 1
        elif data['ambiguous_question'] == 'No' and 'COCO' in data['image_filename']:
            q_nonamb_vqa += 1
        elif data['ambiguous_question'] == 'No' and 'VizWiz' in data['image_filename']:
            q_nonamb_vizwiz += 1
        else:
            print(data)
    write_data(q_amb_vqa=q_amb_vqa,
               q_amb_vizwiz=q_amb_vizwiz,
               q_nonamb_vqa=q_nonamb_vqa,
               q_nonamb_vizwiz=q_nonamb_vizwiz,
               total=len(dataset))
    