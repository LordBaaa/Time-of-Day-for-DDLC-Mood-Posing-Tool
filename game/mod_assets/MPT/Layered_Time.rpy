#https://github.com/LordBaaa
#Please Give credit if used in any way

init python:
    class Layered_Time:
        def __init__(self, path = "", absolute_path = False):
            """Creates DynamicDisplayables of the images used in MPT so they can have effects applied to them"""
        
            #Init Vars
            self.path = path
            self.effect_matrix = im.matrix.identity() #Default matri
            self.absolute_path = absolute_path

        def layered_path(self, img_str, absolute_path):
            """Gets the full layered path
                IN:
                   img_str - String for the name of the image
                   absolute_path: Bool that tells if you want to use and absolute or relative path"""
                   
            #Use Absolute path
            if absolute_path:
                return img_str
                
            #Use Relative Path
            else:
                return "{0}{1}".format(self.path, img_str)

        def matrix_effects(self, st,at, image): #Matrix Test
            """Returns a MatrixColor Object for the specified image using set effect matrix
                IN:
                    Image - String for the image
            Uses current effect_matrix for the class for the matrix to use 
            """

            return im.MatrixColor(self.layered_path(image, self.absolute_path), self.effect_matrix),None
        
        def change_effects_values(self, st,at, new_matrix):
            """Sets the classes effect matrix to the new matrix
            the clear.png is just a place holder ot allow the image to funtion to work
            it is kind of like side loading code since it cant be executed directly without having an image involved
            
            IN:
                new_matrix - matrix value that will be set as the classes matrix"""
            
            self.effect_matrix = new_matrix
            return "mod_assets/MPT/clear.png", None
        
        def set_effects(self, matrix):
            """Defines an effect. This code makes a DynamicDisplayable to execute the code changes for a new matrix.
            if references change_effects_values which returns a place holder images so no work is done it just sideloads code"""
            
            return DynamicDisplayable(self.change_effects_values, matrix)
        
        def set_image_with_effects(self, image):
            """Sets and image as a dynamic displayable that can be changed in self.matrix_effects:"""
            
            return DynamicDisplayable(self.matrix_effects, image)
            
        def verify_param(self, name, value, expected_type, length = None, supress = False, return_error_str= False):
            """Checks if the type() of a value matches another type
                IN:
                    key - name of the effect/function
                    value - value we want to use for this function
                    length - paramiter telling how long to expect the value to be
                    supress - Bool telling us if we want to ignore errors or not
                    return_error_str - Bool telling us if we want an error message
                    
            """

            #returns string or supress not both
            
            #Defaults
            valid_type = False
            vaild_length = False
            length_present = False
            value_type = type(value)
            error_str = ""

            #If the types are the same
            if value_type == expected_type:
                valid_type = True
                
            #If length is specified
            if length is not None:
                length_present = True
                
                try:
                    value_length = len(value)
                    
                    #Checks if the lenght is valid
                    if value_length == length:
                        vaild_length = True
                except:
                    #if there is an error it sets the lengh to invalid
                    vaild_length = False
                    value_length = None
                    
            #if there is not specified lenght it is fine       
            else:
                vaild_length = True


            #If the type of length are invalid
            if valid_type == False or vaild_length == False:
                
                #Create error string
                error_str = "{} was expecting {} {} but got {} {}".format(name, expected_type, "of length {}".format(length) if length_present else "", value_type, "of length {}".format(value_length) if length_present else "")
                #if suppress if off print the error string
                if supress == False:
                    print error_str
            
            #Returns an error string if if we want one
            if return_error_str == True:
                return valid_type and vaild_length, error_str
            
            #Else we just evaluate the type and lenght checks to make a final determination of if it is valid
            else:
                return valid_type and vaild_length

            
        def verify_effect_params(self, key, value):
            """Makes sure that the effects are valid
                IN:
                    key - Name to validate
                    value - value to validate
            """
            
            effect_dict = {
                "tint": {"type" : [tuple, renpy.python.RevertableList.__bases__[0], type(renpy.python.RevertableList())], "length" : 3},
                "hue": {"type" : [int, float]},
                "saturation": {"type" : [int, float]}, 
                "contrast": {"type" : [int, float]}, 
                "brightness": {"type" : [int, float]}, 
                "colorize" : {"type" : [tuple, renpy.python.RevertableList.__bases__[0], type(renpy.python.RevertableList())], "length" : 2},
                "desaturate": {"type" : [int, float]}, 
                "identity": None, 
                "invert": None, 
                "opacity": {"type" : [int, float]}
                }
            
            #Sets expected_data with the values for a specific effect
            expected_data = effect_dict.get(key)
            #You need to fix this!


            #if the key exists...
            if expected_data is not None:
                
                #If it needs a value (excludes identity and invert)
                if expected_data.get("type") is not None:
                    
                    #Gets the valid types
                    expected_types = expected_data.get("type")
                    
                    #Init Vars
                    truth_list = []

                    
                    #Iterates through the expected (valid) types
                    for expected_type in expected_types:
                        #Validates that the type() of the value matches the type expected for this key
                        verify_data = self.verify_param(key, value, expected_type, expected_data.get("length"), supress = True, return_error_str = True)
                        truth_list.append(verify_data[0])
                    
                    #if any of the values are true then return true that it is a valid parameter
                    if True in truth_list:
                        return True


            #if no expected data then just return true, this would be for invert and identity
            else:
                return True

                
        def multiply_matricies_from_key(self, base, key, value):
            """Multiplies base matrix with one generated by the value specified
                IN:
                    base - original matrix
                    key - which effect to use
                    value - value to send to the function specified by key
                    
            """
            
            #Creates New matrix
            try:
                #Comlicated to look at but it is a one lined condtional statment, It basically just says if they type is a tuple or a list add a * before the value, else just do it straight up
                exec("new_matrix = im.matrix.{}({}{})".format(key, "*" if type(value) in [tuple, renpy.python.RevertableList.__bases__[0], type(renpy.python.RevertableList())] else "", value if value is not None else ""))
                
            except:
                
                new_matrix = im.matrix.identity()
                
            return base * new_matrix
        
        
        
        def define_effect(self, **kwargs):
            """ Defines the effect you want to use
                IN:
                    kwargs - this can be any of the Matrix color effects
            """
            
            #Start by generating a default matrix
            effect_matrix = im.matrix.identity()
            
            #Get the values for the effect
            for effect_key in kwargs:
                current_value = kwargs.get(effect_key)
                
                #Verifies the paramiters before it is used 
                if self.verify_effect_params(effect_key, current_value):
                    
                    #If Valid 
                    effect_matrix = self.multiply_matricies_from_key(effect_matrix, effect_key, kwargs[effect_key])

            return effect_matrix
            
            

        
    def set_layered_time_shortcuts(path, absolute_path = False):
        """Defines the function on a global scale
            IN:
                path - String to the files if is a relative path
                absolute_path - Bool teling us if we are using absolute or relative path
        """
        global siwf, se, define_effect
        layered_time = Layered_Time(path)
        siwf = layered_time.set_image_with_effects
        se = layered_time.set_effects

        return
        
init python:
    #set global standards
    layered_time = Layered_Time(None)
    define_effect = layered_time.define_effect


    #Time of Day matrix definitions
    invert_matrix = define_effect(invert = None)
    
    #Values from  Koya-Sato /DDLC-Modding-Starter-Pack   
    # Time of Day Codes
    dawn_matrix = define_effect(tint = (0.5, 0.4, 0.6))
    dawn2_matrix = define_effect(tint = (0.4, 0.3, 0.5))
    morning_matrix = define_effect(tint = (0.8, 0.7, 0.6))
    morning2_matrix = define_effect(tint = (0.8, 0.6, 0.5))
    sunset_matrix = define_effect(tint = (1.0, 0.8, 0.8))
    sunset2_matrix = define_effect(tint = (1.0, 0.8, 0.6))
    evening_matrix = define_effect(tint = (0.6, 0.6, 0.7))
    evening2_matrix = define_effect(tint = (0.4, 0.4, 0.5))
    night_matrix = define_effect(tint = (0.4, 0.4, 0.6))
    night2_matrix = define_effect(tint = (0.2, 0.2, 0.4))
    
    """You can use any of the matrices that are used by MatrixColor
    the valid ones are 
                "tint": A 3 value tuple eg (0.2, 0.2, 0.4)
                "hue": which can take a int or float
                "saturation", "contrast" , "brightness", opacity", "desaturate" which all take either an int or a float
                "identity" and "invert" which both take None
                and "colorize" tuple of length 2
                
                Some examples
                
                Colorize
                Colorize takes 2 colors 1 for black 1 for white,
                define_effect(colorize = ("FF003B", "4CFF00"))
                
                Invert
                define_effect(invert = None)
                
                Saturation
                define_effect(saturation = 100)
                
                Tint
                define_effect(tint = (0.2, 0.2, 0.4))

    """



init python:
   set_layered_time_shortcuts("", absolute_path = True)



            




        




