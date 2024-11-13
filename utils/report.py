
# report resulf of pubmed_auto_search.py
from beans.pubmed_instance import pubmed_instance
from typing import List

def report_result(result: List[pubmed_instance]):
    for item in result:
        item.self_report()

def report_missing_result(result: List[pubmed_instance]):
    for item in result:
        item.self_missing_report()