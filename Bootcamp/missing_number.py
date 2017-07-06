def find_missing(list_a, list_b):
    if len(list_a) > 1:
      for n in list_b:
          if n in list_a:
              continue
          else:
              return n
    else:
      return 0