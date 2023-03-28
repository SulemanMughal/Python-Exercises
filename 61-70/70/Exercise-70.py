
import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
    
    
def moving_min(prices, window_size):
    moving_mins = []
    idx = 0
    
    while idx < len(prices) - window_size + 1:
        current_window = prices[idx: idx + window_size]
        window_min = min(current_window)
        moving_mins.append(window_min)
        idx += 1
    
    return moving_mins