# Removing the `lock` object before pickling

import pickle
import threading

a_dict = {
    'website': 'bobbyhadz.com',
    'topic': 'Python',
    'lock_object': threading.Lock()
}

del a_dict['lock_object']

with open('example.pickle', 'wb') as file_handle:
    pickle.dump(a_dict, file_handle, protocol=pickle.HIGHEST_PROTOCOL)