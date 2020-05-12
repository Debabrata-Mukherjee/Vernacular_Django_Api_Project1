class validation_function:

    
    def check_presence(self,value,list1):     # checks if value is present in list1
        if value in list1:
            return True 
        else:
            return False
    
    def validate_finite_values_entity(self,values,supported_values,invalid_trigger,key,support_multiple,pick_first):
        pick_first = False
        filled = True 
        partially_filled = False
        trigger = ''
        parametres = {}

        flag = 0

        if len(supported_values) == 0 or len(values) == 0:
            filled = False 
            partially_filled = False 
            trigger = invalid_trigger
            flag = 1 
        else:
            index = 0 
            for dict_values in values:
                answer = self.check_presence(self,dict_values["value"],supported_values)

                if answer==False:              # Case of Invalid Input
                    filled = False 
                    partially_filled = True 
                    trigger = invalid_trigger
                    flag = 1 
                    break 
                if index == 0:                 
                    if answer:                # If first input value is valid
                        pick_first = True    
                index += 1 

        if flag == 0:
            parametres[key] = []
            for dict_values in values:
                parametres[key].append(dict_values["value"])

        SlotValidationResult = {}                           # Computing Final Result
        SlotValidationResult['filled'] = filled
        SlotValidationResult['partially_filled'] = partially_filled
        SlotValidationResult['trigger'] = trigger 
        SlotValidationResult['parametres'] = parametres

        return SlotValidationResult
            
                    
                    
                
            

        
        
        
 