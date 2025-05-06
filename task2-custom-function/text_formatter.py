def format_text(text,prefix="",suffix="",capitalize=False,max_length=None): # function definition
 
 text=input("Enter the text: ")
 """
 this program will compute a formatted text by setting prefix, and suffix
 on it, the following er parameters which will hepl us to get desired output
 """
 # these are parameters
 if not isinstance(text, str):
    raise TypeError("The texst must be a string.")
 if not isinstance(prefix,str):
   raise TypeError("prefix must be a string also")
 if not isinstance(suffix,str):
   raise TypeError("suffix also must be a string")
 if not isinstance(capitalize,bool):
   raise TypeError("capital must be a bool")
 if max_length is not None:
   if not isinstance(max_length,int) and max_length <=0:
    raise TypeError("maximum length must be a positive number")
   result=f"{prefix}{text}{text}"

 if capitalize:
   result=result.capitalize()
 if max_length:
   result=result[:max_length]
   return result
 #part of displaying information and error handling
if __name__ == "__main__":
     print("the formatted text is here: ")
     text=input("Enter the text you want: ")
     prefix=input("Enter the prefix: ")
     suffix=input("Enter the suffix: ")
     capitalizing=input("do you want to capitalize? if (default=no)?: ")
     capitalize= capitalizing == "yes"
     maxLength=input("enter the maximum length of your text(OR SKIP): ").strip()
     max_length=None
     if max_length:
        try:
            max_length=int(maxLength)
            if maxLength <0:
             raise ValueError
        except ValueError:
          print("the text length must be a positive number")
try:
       result=format_text(prefix,text,suffix)
       print(f"formatted text is: {result}")
except Exception as err:
     print(f"the error occured is {err}")
