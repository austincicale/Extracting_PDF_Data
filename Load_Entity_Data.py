import pandas as pd

def load_entity_data(filepath='entity_data.csv'):
    entity_data = pd.read_csv(filepath)
    return entity_data.set_index('client_name').to_dict()['entity_id']
