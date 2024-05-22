class universty:
  def __init__(self, name):
         self.name = name
         self.department = {}

   def add_department(self,department_name)
      if department_name not in  self.department:
         self.department[department_name] = department(department_name)
            print(f"Department {department_name} added to {self.name} university")
      else:
            print(f"Department {department_name} already exists in {self.name} university")

   def allocate_asset( self, department_name, asset_name, asset_type, asset_value):
      if department_name in self.department:
         self.department[department_name].allocate_asset(asset_name, asset_type, asset_value)
      else:
            print(f"department'{department_name}' does not exist in {self.name} university")

class department:
   def __init__(self,name):
         self.name = name
         self.allocate_asset=[]

   def allocate_asset(self,asset):
         self.allocate_asset.append(asset)
            print(f"{asset} allocated to {self.name}.")

class Asset:
   def __init__(self, asset_name, asset_type, asset_value):
         self.asset_name = asset_name
         self.asset_type = asset_type

   def __str__(self):
               return f"{self.asset_type}: {self.asset_name}"

#creating universty
   university = universty("Islamiya universty")

#departments            
   uni.add_department("software engineering")
   uni.add_department("civil engineering")

#allocating assets
   uni. allocate_asset("software engineering", "laptop", "computer", "lab")
   uni. allocate_asset("civil engineering", "laptop", "computer","geometroy")









