import sys

class Value:

  type:wolClass=None
  value:str=''

#-------------------------
  getter:wolFunction=None
  setter:wolFunction=None
#-------------------------
  """
   @param wolClass
   @param val
   @param modifer 
  """
  def __init__(self,wolClass:wolClass,val:str='<null:void',modifer:SecurityModifer=SecurityModifer):
     self.value=val
     self.type=wolClass

     self.getter=wolFunction(modifer)
     self.setter=wolFunction(modifer) 

     
     
class SecurityModifer:
 pass

class wolClass:
 pass

class wolFunction:
  pass

class wolValue:
   pass
  
class ThrowVMException(Exception):
  def __init__(self,msg):
     self.msg=msg    

   

class Stack:
 
 def __init__(self):  
  self.classes={}
  self.functions={}
  self.values={}

 def __str__(self):
  
    return 'Stack items:\nclasses'+str(self.classes)+'\nfunctions:'+str(self.functions)+'\nvalues'+str(self.values)
 

class Vm:
  def __init__(self):
#-----------------------------------
     self.mainstack:Stack=Stack()
#-----------------------------------
 
#----------------------
     self.buffer=[]
#----------------------

    
     self.wol_args:list=[]
    
  def initBaseTypes(self)->None:
     pass

  def isWhiteSpace(self,current:str):

     if current==' ':
        return true

     return false

  def execute(input_:str)->None:      

    #----------------------
    stack=Stack()
    #----------------------

   

    isVmWorks=True

    position:int=0
    current:str=input_[0]
    while(isVmWorks):

        while(self.isWhiteSpace(current)):  #skip whitespaces
            position+=1
            if (position > len(input_)):
                    
                raise ThrowVMException("Build-file have only whitespaces", position)                                         

            current:str=input_[position]
        while(self.isWhiteSpace(current) is False): #get word
            self.buffer.append(current)
            position+=1
            try:
               current = input_[position]
            except IndexError:
              raise ThrowVMException("Build-file have only one word", position) 
        if self.buffer=='_loads':
           self.buffer=[]
           while(isWhiteSpace(current)):
              position+=1
              if (position > len(input_)):
                raise  ThrowVMException("Start of loads struct not found", position);                        
              current=input_[position]
           if (current=='{'):
                  self.buffer=[]
                  while(current!='}'): # get loads body  
                      self.buffer.append(current)
                      position+=1
                      if (position > len(input_)):
                         raise  ThrowVMException("End of loads struct not found", position)               
                


        elif self.buffer=='stack':pass
        elif self.buffer=='end':return
        elif self.buffer=='}':
          pass
        elif self.buffer=='main':pass

        else:
           raise Exception('Unknown keyword '+self.buffer+' at position:'+str(position))
           
           
   
    def parse(stack_code:str)->Stack:  
      pass
             
#===========================
version ="1.0.0"
info="World of Legends Virtual Machine\nVersion:"+version+"\nAuthor: Arkadiy Vitalyev."
if __name__=='__main__':

  if len(sys.argv)==1:
   print(info)
  else:
    if(sys.argv[1]=='-info'):
        print(info)
    else: 
      programFileName=sys.argv[1]

      vm=Vm()
      vm.initBaseTypes()

      input_:list=['stack { } end']# отпарсим из файла
      vm.execute(input_)

#================================= 

  
