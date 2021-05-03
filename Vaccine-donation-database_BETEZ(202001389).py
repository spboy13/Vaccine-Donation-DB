# Database for Vaccine Donations
# Created as part of EEE 121 Probset Part IV Requirement
# Submitted by: Arthur E. Betez Jr.

############################################################################################################

# HOW TO USE

# The user will be given guides as soon as he/she runs the program
# Follow input formats
# One can use (copy-paste) the following sample entry inputs:
# 639188936587 Sinovac 100 220101
# 639231231233 Astrazeneca 200 220102
# 639390234234 Pfizer 500 220330
# 639431231223 Moderna 400 220328
# 639191232573 Moderna 450 220715
# 639543548573 Astrazeneca 200 211205

############################################################################################################

# REMARKS

# 1. Although the priority functions were achieved in less than O(n) time complexity,
#    the program itself does NOT run in less than O(n) time complexity.
#    This is due to the fact that we need the entry_list sorted before running the binary search approach.
# 2. The priority function 3 take for granted the fact that the entry_list is sorted
# 3. Sorting algorithm's time complexity depends on python's implementation of .sort() function 

# Priority Functions Time Complexities:
# Priority Function 1: O(1)
# Priority Function 2: O(1)
# Priority Function 3: O(log n)

############################################################################################################

# CONSTRAINTS AND FORMATS

# Vaccine Brands:
# Pfizer
# Moderna
# Astrazeneca
# Sinovac

# Date Format:
# YYMMDD (this way, we can treat is as integer with: lower numeric value = earlier date)

# Contact Number Format:
# 639.....

# Entry Format:
# contact_number Brand doses expiration_date

############################################################################################################




# Binary Search Helper Function (For Priority Function 3)
# Reference: EEE 121 Week 6 (Recursion Divide and Conquer): || 6.2 Divide and Conquer.ipynb Notebook File ||
def binary_search(sn_list, key, start, end):
  # Base Case
    if end - start == 1:
        return sn_list[start] if sn_list[start][0] == key else "Stock Number Not Found in Database!" 
    elif end <= start:    
        return "Stock Number Not Found in Database!"        

    mid = (end + start) // 2 
    if key > sn_list[mid][0]:
        return binary_search(sn_list, key, mid, end)  
    elif key < sn_list[mid][0]:
        return binary_search(sn_list, key, start, mid)  
    else:
        return sn_list[mid] 


# Class for vaccine brands. Has 4 instances (each for every brand)
# Used to store total number of vaccine doses per brand (Priority Function 1)
class vaccineBrand:
    def __init__(self, name, initial_quantity = 0):
        self.name = name
        self.quantity = 0
        
    def add_quantity(self, amount):
        self.quantity += amount
        

# Main Class 
# Handles entries, sorting, and returning data
class vaccineDatabase:
    def __init__(self):
        self.entry_list = [] # Initialize dynamic array for all donation entries
        
        self.expiry_dates = [] # Initialize dynamic array for all expiration dates
        
        # Create the vaccineBrand instances, 1 for each vaccine brand
        self.quantity_pfizer = vaccineBrand("Pfizer") 
        self.quantity_moderna = vaccineBrand("Moderna")
        self.quantity_astrazeneca = vaccineBrand("Astrazeneca")
        self.quantity_sinovac = vaccineBrand("Moderna")
        
        
    # Updates each brand's total number of doses (runs everytime a new donation entry is added)    
    def update_quantity(self, brand, doses):
        if brand == "Pfizer":
            self.quantity_pfizer.add_quantity(doses)
        elif brand == "Moderna":
            self.quantity_moderna.add_quantity(doses)
        elif brand == "Astrazeneca":
            self.quantity_astrazeneca.add_quantity(doses)
        elif brand == "Sinovac":
            self.quantity_sinovac.add_quantity(doses)
        else:
            print("Error in updating vaccine quantity: Brand not recognized")
                
    # Updates the expiry_dates dynamic array (Makes sure that earliest is at index 0)
    # Time Complexity: O(1)
    def update_expiry_dates(self, expiry_date, brand):
        if len(self.expiry_dates) == 0:
            self.expiry_dates.append([expiry_date, brand])
        else:
            if expiry_date > self.expiry_dates[0][0]:
                self.expiry_dates.append([expiry_date, brand])
            else:
                self.expiry_dates.insert(0, [expiry_date, brand])
        

    # Add entry method
    # After adding entry to entry_list dynamic array,
    # Updates the doses quantities and expiry_dates dynamic array
    def add_entry(self, stock_number, brand, doses, expiry_date):
        self.entry_list.append([stock_number, brand, doses, expiry_date])
        
        self.update_quantity(brand, doses)
        
        self.update_expiry_dates(expiry_date, brand)
        
        self.entry_list.sort()
        
    
    # Returns the total number of vaccines in a specific brand
    def total_vaccine(self, brand):
        if brand == "Pfizer":
            return self.quantity_pfizer.quantity
        elif brand == "Moderna":
            return self.quantity_moderna.quantity
        elif brand == "Astrazeneca":
            return self.quantity_astrazeneca.quantity
        elif brand == "Sinovac":
            return self.quantity_sinovac.quantity
        else:
            print("Error in returning total vaccine: Brand not recognized")
            
    
    # Priority Function 2: returns the earliest expiration date (found at index 0 of dynamic array)
    # Time complexity: O(1)
    def earliest_expiry(self):
        return self.expiry_dates[0]
    
    # Priority Function 3: returns the entry with the specific contact/stock_number
    # Time complexity: O(log n)
    def find_entry(self, stock_number):
        n = len(self.entry_list)
        sn_list = self.entry_list
        
        return binary_search(sn_list, stock_number, 0, n)
        


# Driver function for inputting new entries
def add_input():
    entries = int(input("Number of Entries: "))
    print("")

    for i in range(1, entries + 1, 1):
        inputList = input(f"entry {i}: ").split()
        db.add_entry(int(inputList[0]), inputList[1], int(inputList[2]), int(inputList[3]))
    print("")

    
# Priority Function 1: Outputs the total number of doses per vaccine brand
# Time Complexity: O(1)
def priority_func_1():
    print("Total Vaccines Per Brand")   
    print(f"   Pfizer: {db.total_vaccine('Pfizer')}")
    print(f"   Moderna: {db.total_vaccine('Moderna')}")
    print(f"   Astrazeneca: {db.total_vaccine('Astrazeneca')}")
    print(f"   Sinovac: {db.total_vaccine('Sinovac')}")
    print("")


# Driver Function for priority function 2
def priority_func_2():
    print(f"   Soonest Expiration Date (YYMMDD): {db.earliest_expiry()}")    
    print("")
        
# Driver Function for priority function 3
def priority_func_3():
    key = int(input("Search Entry (enter contact number): "))
    print(f"   Entry: {db.find_entry(key)}")
    print("")


        

        
        
        
        
# Program Starts Here

if __name__ == "__main__":
    db = vaccineDatabase()      
    print("Please follow this entry format: contact_number Brand doses expiration_date")
    print("")

    print("Contact Number:  639...")
    print("Brand:           Pfizer, Moderna, Astrazeneca, Sinovac (case-sensitive)")
    print("Doses:           Any Positive Integer")
    print("Expiration Date: YYMMDD")
    print("")
    
    print("FUNCTIONS LIST")
    print("[a] Add Entries")
    print("[b] Print Total Doses per Brand")
    print("[c] Get Earliest Expiration Date")
    print("[d] Search for a Donation Entry")
    print("[x] Exit")
    print("")

    flag = True
    
    while flag == True:   
        userInput = input("Select corresponding function letter: ")

        if userInput == 'a':
            add_input()
        elif userInput == 'b':
            priority_func_1()
        elif userInput == 'c':
            priority_func_2()
        elif userInput == 'd':
            priority_func_3()
        elif userInput == 'x':
            print("Exiting Program...")
            flag = False
        else:
            Print("Invalid Input... Exiting Program")
            flag = False



