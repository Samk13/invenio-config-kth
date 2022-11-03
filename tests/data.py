# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

test_data = [
    {
        "id": 8812,
        "uri": "http://rdf-vocabulary.ddialliance.org/cv/TypeOfAddress/1.1/[CODE]",
        "notation": "Mailing",
        "title": "Mailing address",
        "definition": 'Includes both "street"',
        "previousConcept": 3535,
        "position": 0,
        "deprecated": False,
    },
    {
        "id": 14131,
        "uri": "https://vocabularies.cessda.eu/vocabulary/TopicClassification_[CODE]?v=4.2",
        "notation": "Health.SignsAndSymptomsPathologicalConditions",
        "title": "Signs and symptoms; pathological conditions",
        "definition": "Data on abnormal anatomical or physiological conditions",
        "previousConcept": 8961,
        "parent": "Health",
        "position": 26,
        "deprecated": False,
    },
]

res_data = [
    "https://vocabularies.cessda.eu/vocabulary/TypeOfAddress_Mailing?v=1.1&id=8812",
    "https://vocabularies.cessda.eu/vocabulary/TopicClassification_SignsAndSymptomsPathologicalConditions?v=4.2&id=14131",
]

expected_schema = [
    {
        "id": "https://vocabularies.cessda.eu/vocabulary/TypeOfAddress_Mailing?v=1.1&id=8812",
        "scheme": "CESSDA",
        "subject": "Mailing address",
    }
]
