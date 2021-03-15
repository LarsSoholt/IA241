'''
Lab 9 class
'''

class car:
    
    maker = 'toyota' 
    
    def _init_report_maker(self,input_model):
        self.model = input_model  
        
    def report(self):
        return self.model, self.maker
        
my_corolla = car('corolla')

#my_highlander = car('highlander')

print(my_corolla.model)

my_corolla.maker = 'ford'
print(my_corolla.maker)

import Lec8

