import json
from algorithm_record import AlgRecord


def json_parser(data_string):
    data = json.loads(data_string)
    alg_records = []
    for record in data['results']:
        if record['type'] == 'Algorithm':
            alg_records.append(AlgRecord(record['name'], record['count'], record['internal'], record['mantidVersion']))
    return alg_records
