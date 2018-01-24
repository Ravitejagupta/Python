def find_unique_delivery_id(delivery_ids):

    ids_to_occurrences = {}

    for delivery_id in delivery_ids:
        if delivery_id in ids_to_occurrences:
            ids_to_occurrences[delivery_id] += 1
        else:
            ids_to_occurrences[delivery_id]  = 1

    for delivery_id, occurrences in ids_to_occurrences.items():
        if occurrences == 1:
            return delivery_id
