def func(ord_list, num):
  result = True if num in ord_list else False
  return result

if __name__ == "__main__":
    l = [-1,3,5,6,8,9]


# using binary search

def find(ordered_list, element):
  start_index = 0
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = int((end_index + start_index) / 2) 

    if middle_index == start_index or middle_index == end_index:
        if ordered_list[middle_index] == element or ordered_list[end_index] == element:
            return True
        else:
            return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element:
        return True
    elif middle_element > element:
        end_index = middle_index
    else:
        start_index = middle_index

if __name__=="__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 8))