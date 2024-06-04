import logging
from typing import List
from multiprocessing import Pool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_lists(lists: List[List[int]]) -> List[int]:
    if not lists:
        logging.error("Empty list provided")
        return []
    
    try:
        with Pool() as pool:
            result = pool.map(sum, lists)
        return result
    except Exception as e:
        logging.error(f"An error occurred during addition: {e}")
        raise