import os

def fetch_criteria():
    criteria_folder_path = 'src/sorting_criteria'
    file_prefix = "sorting_criteria_"
    criteria = []
    
    for filename in os.listdir(criteria_folder_path):
        if filename.startswith(file_prefix):
            filename = os.path.splitext(filename)[0]
            criteria.append(filename[len(file_prefix):].replace('_', ' '))
    
    return criteria
