def match_entity_id(data, entity_data):
    """
    Match client names with entity IDs.

    Parameters:
    data (dict): A dictionary containing extracted data fields.
    entity_data (dict): A dictionary mapping client names to entity IDs.

    Returns:
    dict: A dictionary containing extracted data fields with entity IDs matched.
    """
    client_name = data.get('client_name')
    if client_name in entity_data:
        data['entity_id'] = entity_data[client_name]
    else:
        data['entity_id'] = 'Unknown'
    return data
