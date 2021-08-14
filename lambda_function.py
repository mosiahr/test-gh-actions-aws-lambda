from app import get_list_of_sort_title, CircularBuffer


circular_buffer_res = CircularBuffer(3)
list_i = [0]

def lambda_handler(event, context):
    titles = get_list_of_sort_title()
    i = list_i.pop()
    
    while len(circular_buffer_res) < 2:
        circular_buffer_res.append(titles[i])
        i = i + 1
    
    circular_buffer_res.append(titles[i])
    
    if i < len(titles) - 1:
        list_i.append(i + 1)
    else:
        i = 0
        list_i.append(i)
    
    return circular_buffer_res.get()