from datetime import datetime
import random
import math
import copy

# Example data structure of employees
employees = {
    "Alice": {
        "hours": 20,
        "trained": ["cashier", "bakery", "12"],
        "availability": {"Mon": ["08:00-12:00"], "Wed": ["14:00-18:00"], "Fri": ["09:00-13:00"]}
    },
    "Bob": {
        "hours": 25,
        "trained": ["deli", "stock", "17"],
        "availability": {"Tues": ["10:00-15:00"], "Thurs": ["12:00-17:00"]}
    },
    "Charlie": {
        "hours": 30,
        "trained": ["meat", "produce", "21"],
        "availability": {"Mon": ["13:00-18:00"], "Wed": ["08:00-13:00"], "Fri": ["12:00-17:00"]}
    },
    "Beta": {
        "hours": 15,
        "trained": ["fish", "cashier", "9"],
        "availability": {"Tues": ["09:00-12:00", "13:00-15:00"], "Thurs": ["10:00-13:00"]}
    },
    "Ethan": {
        "hours": 32,
        "trained": ["bakery", "deli", "25"],
        "availability": {"Mon": ["10:00-14:00", "15:00-19:00"], "Wed": ["10:00-14:00"]}
    },
    "Alpha": {
        "hours": 20,
        "trained": ["produce", "fish", "14"],
        "availability": {"Tues": ["08:00-12:00"], "Thurs": ["14:00-18:00"], "Sat": ["10:00-14:00"]}
    },
    "George": {
        "hours": 28,
        "trained": ["stock", "cashier", "18"],
        "availability": {"Wed": ["09:00-13:00", "14:00-18:00"], "Fri": ["08:00-12:00"]}
    },
    "Hannah": {
        "hours": 22,
        "trained": ["deli", "bakery", "16"],
        "availability": {"Mon": ["10:00-14:00"], "Thurs": ["11:00-15:00"], "Sat": ["09:00-13:00"]}
    },
    "Ian": {
        "hours": 35,
        "trained": ["meat", "stock", "29"],
        "availability": {"Tues": ["10:00-15:00", "16:00-19:00"], "Fri": ["10:00-15:00"]}
    },
    "Julia": {
        "hours": 24,
        "trained": ["produce", "fish", "20"],
        "availability": {"Mon": ["08:00-12:00", "13:00-17:00"], "Wed": ["14:00-18:00"]}
    },
    "Kevin": {
        "hours": 18,
        "trained": ["cashier", "stock", "13"],
        "availability": {"Mon": ["16:00-20:00"], "Wed": ["16:00-20:00"], "Fri": ["16:00-20:00"]}
    },
    "Laura": {
        "hours": 22,
        "trained": ["bakery", "deli", "19"],
        "availability": {"Tues": ["16:00-20:00"], "Thurs": ["16:00-20:00"], "Sat": ["10:00-14:00", "15:00-19:00"]}
    },
    "Mike": {
        "hours": 30,
        "trained": ["produce", "meat", "23"],
        "availability": {"Mon": ["08:00-12:00", "13:00-17:00"], "Tues": ["08:00-12:00"], "Wed": ["08:00-12:00", "13:00-17:00"], "Thurs": ["08:00-12:00"], "Fri": ["08:00-12:00", "13:00-17:00"]}
    },
    "Sigma": {
        "hours": 16,
        "trained": ["fish", "cashier", "11"],
        "availability": {"Sat": ["09:00-13:00", "14:00-18:00"], "Sun": ["10:00-14:00", "15:00-19:00"]}
    },
    "Oscar": {
        "hours": 20,
        "trained": ["stock", "deli", "15"],
        "availability": {"Mon": ["16:00-20:00"], "Tues": ["16:00-20:00"], "Thurs": ["16:00-20:00"], "Fri": ["16:00-20:00"]}
    }
}
# Example data structure of Shift times
shift_times = {
    "Mon": [("08:00", "12:00", "Bakery"), ("12:00", "16:00", "Cashier"), ("16:00", "20:00", None)], # IMPORTANT: if no shift type, make sure there is None!!!!!
    "Tues": [("10:00", "14:00", "Deli"), ("14:00", "18:00", "Stock"), ("18:00", "22:00", None)],
    "Wed": [("08:00", "12:00", "Produce"), ("12:00", "16:00", "Meat"), ("16:00", "20:00", None)],
    "Thurs": [("10:00", "14:00", "Fish"), ("14:00", "18:00", "Bakery"), ("18:00", "22:00", None)],
    "Fri": [("08:00", "12:00", "Cashier"), ("12:00", "16:00", "Deli"), ("16:00", "20:00", None)],
    "Sat": [("09:00", "13:00", "Stock"), ("13:00", "17:00", "Produce")],
    "Sun": [("10:00", "14:00", "Meat"), ("14:00", "18:00", "Fish")]
}
# Example data structure of manually added shifts
manual_shifts = {
    "Mon": {"Alice": ("08:00", "12:00", "Bakery"), "Ethan": ("12:00", "16:00", "Cashier")},
    "Wed": {"Bob": ("10:00", "14:00", "Deli"), "Ian": ("14:00", "18:00", "Meat")},
    "Fri": {"Charlie": ("16:00", "20:00", None)},
    "Sat": {"Beta": ("09:00", "13:00", "Stock")}
}
employees1 = {
    "Manager" : {
        "hours" : 40,
        "trained" : ["sandwich", "salad", "deli close", "hot side close", "manager"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Assistant Manager 1" : {
        "hours" : 37.5,
        "trained" : ["sandwich", "salad", "deli close", "hot side close", "manager"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Assistant Manager 2" : {
        "hours" : 37.5,
        "trained" : ["sandwich", "salad", "deli close", "hot side close", "manager"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 1" : {
        "hours" : 25,
        "trained" : ["sandwich", "salad", "deli close", "hot side close"],
        "availability" : {"Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 2" : {
        "hours" : 24,
        "trained" : ["sandwich", "salad", "deli close", "hot side close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 3" : {
        "hours" : 26,
        "trained" : ["sandwich", "salad", "deli close", "hot side close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 4" : {
        "hours" : 24,
        "trained" : ["sandwich", "salad", "deli close", "hot side close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 5" : {
        "hours" : 15,
        "trained" : ["sandwich", "salad", "deli close", "hot side close"],
        "availability" : {"Mon" : ["13:00-21:00"], "Tues" : ["13:00-21:00"], "Wed" : ["13:00-21:00"], "Thurs" : ["13:00-21:00"], "Fri" : ["13:00-21:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 6" : {
        "hours" : 15,
        "trained" : ["deli close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 7" : {
        "hours" : 15,
        "trained" : ["sandwich","hot side close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 8" : {
        "hours" : 8,
        "trained" : ["deli close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 9" : {
        "hours" : 15,
        "trained" : ["sandwich", "deli close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    },
    "Employee 10" : {
        "hours" : 10,
        "trained" : ["deli close"],
        "availability" : {"Mon" : ["00:00-23:00"], "Tues" : ["00:00-23:00"], "Wed" : ["00:00-23:00"], "Thurs" : ["00:00-23:00"], "Fri" : ["00:00-23:00"], "Sat"  : ["00:00-23:00"], "Sun" : ["00:00-23:00"]}
    }
}

shift_times1 = {
    "Mon": [("15:00", "21:00", "deli close"), ("08:00", "16:00", "salad"), ("06:00", "13:00", "sandwich"), ("15:00","21:00","hot side close"), ("12:00","18:00", None), ("16:00", "21:00", "deli close")],
    "Tues":  [("15:00","21:00","hot side close"), ("06:00", "13:00", "sandwich"), ("16:00", "21:00", "deli close")],
    "Wed": [("15:00","21:00","hot side close"), ("16:00", "21:00", "deli close"),("06:00", "13:00", "sandwich")],
    "Thurs": [("08:00", "16:00", "salad"), ("06:00", "13:00", "sandwich"), ("15:00","21:00","hot side close"), ("15:00", "21:00", "deli close"), ("16:00", "21:00", "deli close"), ("12:00", "18:00", None)],
    "Fri": [("06:00", "13:00", "sandwich"),("15:00","21:00","hot side close"),("08:00", "16:00", "salad"),("16:00", "21:00", "deli close")],
    "Sat": [("06:00", "13:00", "sandwich"),("15:00","21:00","hot side close"),("08:00", "16:00", "salad"), ("15:00", "21:00", "deli close"), ("10:00", "16:00", None)],
    "Sun": [("10:00", "16:00", None), ("08:00", "16:00", "salad"), ("15:00", "21:00", "deli close"), ("15:00","21:00","hot side close"), ("16:00", "21:00", "deli close"), ("06:00", "13:00", "sandwich")]
}
manual_shifts1 = {
    "Mon": {"Manager": ("10:00","19:00","manager"),},
    "Tues": {"Manager": ("10:00","19:00","manager"), "Assistant Manager 1": ("08:00","16:00","sandwich"), "Assistant Manager 2" : ("13:00","21:00", "deli close")},
    "Wed": {"Manager": ("11:00","20:00","manager"), "Assistant Manager 1": ("08:00","16:00","sandwich"), "Assistant Manager 2" : ("13:00","21:00", "deli close")},
    "Thurs" : {"Manager": ("13:00","22:00","manager"), "Assistant Manager 1": ("09:00","17:00", "manager"), "Assistant Manager 2" : ("13:00","21:00", "deli close")},
    "Fri" : {"Assistant Manager 1": ("13:00","21:00", "deli close"), "Assistant Manager 2" : ("10:00","18:00","manager")},
    "Sat" : {"Assistant Manager 1": ("13:00","21:00", "deli close"), "Assistant Manager 2" : ("09:00","17:00", "manager")}, 
    "Sun" : {"Manager": ("08:00","17:00","manager"),},
}

class Employee:
    def __init__(self, name, required_hours,hours_scheduled, shift_types, availability, num_shifts_scheduled):
        self.name = name
        self.required_hours = required_hours # number of hours required to work each week
        self.hours_scheduled = hours_scheduled # numbers of hours given to work
        self.shift_types = shift_types
        self.availability = availability
        self.num_shifts_scheduled = num_shifts_scheduled # number of shifts in a week an employee is scheduled for

    def getRequiredHours(self):
        return self.required_hours
    def setRequiredHours(self, hours):
        self.required_hours = hours

    def getHoursScheduled(self):
        return self.hours_scheduled
    def setHoursScheduled(self, hours):
        self.hours_scheduled = hours

    def getShiftTypes(self):
        return self.shift_types
    def setShiftTypes(self, types):
        self.shift_types = types

    def getAvailability(self):
        return self.availability
    def setAvailability(self, availability):
        self.availability = availability
    
    def addShift(self):
        self.num_shifts_scheduled += 1
    def removeShift(self):
        self.num_shifts_scheduled -=1
    def getNumShiftsScheduled(self):
        return self.num_shifts_scheduled

    

def initialSolution(employees, shift_times):
    # Implement initial solution
    days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
    schedule = {day: [] for day in days}
    for day,shifts in shift_times.items():
        for shift in shifts:
            start_time,end_time,shift_type = shift

            shift_start = datetime.strptime(start_time, "%H:%M")
            shift_end = datetime.strptime(end_time, "%H:%M")

            time_difference = shift_end - shift_start
            total_seconds = int(time_difference.total_seconds())
            total_hours = total_seconds/3600

            shift_time = f"{shift_start.strftime('%H:%M')}-{shift_end.strftime('%H:%M')}"

            selected_employee_key = random.choice(list(employees.keys()))
            selected_employee = employees[selected_employee_key]

            # Subtract times for shifts with lunches
            if total_hours == 8:
                total_hours -= 0.5
            elif total_hours == 9:
                total_hours -= 1

            selected_employee.setHoursScheduled(selected_employee.getHoursScheduled()+total_hours)
            selected_employee.addShift()
            schedule[day].append((shift_time, selected_employee.name, shift_type))
    
    return schedule

def cost(employees, schedule):
    # Evaluate the schedule based on current constraints and return a value for cost
    # The lower the cost, the better the solution
    cost = 0
    for day, assigned_shifts in schedule.items():
        for i, shift in enumerate(assigned_shifts):
            shift_time, employee_name, shift_type = shift
            
            # Increase cost if employee is not trained for shift
            ## If shift_type is None then this will evaluate to true
            if shift_type not in employees[employee_name].getShiftTypes():
                cost += 0.1
            # Increase cost if employee is not available for shift
            if day not in employees[employee_name].getAvailability().keys():
                cost += 0.1
            else: # Increase cost if shift is not within the employees availability for that day

                # Turn the shift_times into datetimes so we can compare times
                # TODO: Probably refactor into helper functions
                shift_start_str, shift_end_str = shift_time.split('-')
                start_time = datetime.strptime(shift_start_str, '%H:%M').time()
                end_time = datetime.strptime(shift_end_str, '%H:%M').time()

                for each_shift in employees[employee_name].getAvailability()[day]:
                    shift_start_str1, shift_end_str1, = each_shift.split('-')
                    start_time1 = datetime.strptime(shift_start_str1, '%H:%M').time()
                    end_time1 = datetime.strptime(shift_end_str1, '%H:%M').time()

                    # Check if shift falls within the employees availability
                    if not (start_time1 <= start_time and end_time1 <= end_time):
                        cost += 0.1

            # Compare the shfit with other shifts to see if the employee works more than one shift in the same day
            for j, shift2 in enumerate(assigned_shifts):
                _, employee_name2, _ = shift2
                if i!=j:
                    # Increase cost if name is in another shift in the same day
                    if employee_name == employee_name2:
                        cost += 0.1
    
    # Increase cost if the employee does not meet their required hours
    for employee_name, employee in employees.items():
        if employee.getHoursScheduled() > 40.0:
            cost += 0.1
        hours_difference = employee.getRequiredHours() - employee.getHoursScheduled() 

        if hours_difference > 0:
            cost += 0.01*hours_difference

        if employee.getNumShiftsScheduled() > 5:
            cost += 0.1
    return cost
            

def neighbor(schedule, employees):
    # Swap a random job to a different worker and return schedule
    # Pick random shift from a random day
    day, shifts = random.choice(list(schedule.items())) 
    shift = random.choice(shifts)
    shift_time, employee_name, shift_type = shift

    # Pick a random employee to work this new_shift and replace the shift
    random_employee_name = (random.choice(list(employees.values()))).name

    # Change hours_scheduled for the employees
    new_shift = (shift_time, random_employee_name, shift_type) 

    # Adjust number of hours worked for random employee selected
    start_time, end_time = shift_time.split('-')
    total_hours = getShiftLength(start_time,end_time)
    employees[random_employee_name].setHoursScheduled(employees[random_employee_name].getHoursScheduled() + total_hours)
    employees[random_employee_name].addShift()

    # Adjust number of hours worked for employee that is losing their shift
    employees[employee_name].setHoursScheduled(employees[employee_name].getHoursScheduled() - total_hours)
    employees[employee_name].removeShift()

    # Remove old shift and add new shift
    schedule[day].remove(shift)
    schedule[day].append(new_shift)

    return schedule


def respectManualShifts(schedule, manual_shifts,employees):
    # Takes in a schedule and manual shifts and overwrites the manual shifts back into the schedule
    for day, shift_dict in manual_shifts.items():
        for employee_name, shift in shift_dict.items():
            # Find the time the shift occurs at
            start_time, end_time, shift_type = shift
            total_hours = getShiftLength(start_time, end_time)
            shift_time = f"{start_time}-{end_time}"

            # check the shifts in the actual schedule to see if there's a matching time and type to replace
            if shift not in schedule[day]:
                shift_found_to_swap = False
                for scheduled_shift in schedule[day]:
                    shift_time1, employee_name1, shift_type1 = scheduled_shift
                    if shift_time == shift_time1 and shift_type == shift_type1:
                        # Handle changed worked hours for employee losing and getting shift
                        employees[employee_name].setHoursScheduled(employees[employee_name].getHoursScheduled() + total_hours)
                        employees[employee_name].addShift()
                        employees[employee_name1].setHoursScheduled(employees[employee_name1].getHoursScheduled() - total_hours)
                        employees[employee_name1].removeShift()

                        schedule[day].remove(scheduled_shift)
                        schedule[day].append((shift_time,employee_name,shift_type))
                        shift_found_to_swap = True
                    
                if not shift_found_to_swap:
                    employees[employee_name].setHoursScheduled(employees[employee_name].getHoursScheduled() + total_hours)
                    employees[employee_name].addShift()
                    schedule[day].append((shift_time,employee_name,shift_type))

    return schedule

def getShiftLength(start_time, end_time):
    # Input start time and end time as strings in the form of Hour:Minute and returns float with hours worked
    shift_start = datetime.strptime(start_time, "%H:%M")
    shift_end = datetime.strptime(end_time, "%H:%M")
    shift_length = ((shift_end-shift_start).total_seconds()) / 3600.0

    # Handle lunch breaks
    if shift_length == 8.0:
        return shift_length - 0.5
    elif shift_length == 9.0:
        return shift_length - 1
    
    return shift_length


def simulatedAnnealing(employees, shift_times, manual_shifts, initial_temperature, cooling_rate, num_iterations):
    # Create a solution and then add in Manually required shifts
    current_solution = initialSolution(employees, shift_times)
    current_solution = respectManualShifts(current_solution, manual_shifts, employees)

    current_cost = cost(employees, current_solution)
    temperature = initial_temperature
    costs = []
    for _ in range(num_iterations):
        # Create new solution and make sure we keep Manual shifts, then check its cost
        copy_employees = copy.deepcopy(employees)
        new_solution = neighbor(copy.deepcopy(current_solution), copy_employees)
        new_solution = respectManualShifts(new_solution, manual_shifts, copy_employees) # Make sure any manual shifts that were overwritten are replaced
        new_cost = cost(copy_employees, new_solution)

        # Check if we improved solution or acceptable in terms of randomness
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost
            employees = copy_employees

        temperature *= 1 - cooling_rate 
        costs.append(current_cost)

    return current_solution, current_cost, costs, employees

def printSchedule(schedule):
    for day, shifts in schedule.items():
        print(f"{day}:")
        for shift in shifts:
            shift_time, employee_name, shift_type = shift
            print(f"  {shift_time}: {employee_name} [Type: {shift_type}]")
        if not shifts:
            print("  No shifts scheduled")
        print()

def createEmployees(employees_dictionary):
    # Takes employees in their data structure as a dictionary and returns a dictiomary of employees names as keys and Employee type objects as values.
    employees = {}
    for employee, values in employees_dictionary.items():
        employees.update({employee : Employee(employee,employees_dictionary[employee]["hours"],0, employees_dictionary[employee]["trained"], employees_dictionary[employee]["availability"], 0)})
    return employees

def mainProcess(employees_unstructured, shift_times, manual_shifts):
    employees = createEmployees(employees_unstructured)
    
    # Test values (NOT FINAL)
    initial_temperature = 100000.0
    cooling_rate = 0.20
    num_iterations = 10000

    optimal_schedule, optimal_cost, costs, new_employees = simulatedAnnealing(employees, shift_times, manual_shifts, initial_temperature, cooling_rate, num_iterations)
    
    for name, employee in new_employees.items():
        print(name, ": ", employee.getNumShiftsScheduled(), " shifts")
    return optimal_schedule, optimal_cost, costs, new_employees
   
if __name__ == '__main__':
    mainProcess(employees1, shift_times1, manual_shifts1)
