# #find the first non-repeating character in the string


input_str = "pypyt"
for char in input_str:
      if input_str.count(char)==1:
            print("First repeating character:",char)
             
            break
      else:
            print("No non-repeating character found!")
          
