from itertools import chain

def make_employee(name, skills):
    return {'name': name, 'skills': skills}

def make_skill(name, ability):
    return {'name': name, 'ability': ability}

EMPLOYEES = [
    make_employee('Alice', [make_skill('python', 8), make_skill('java', 5)]),
    make_employee('Bob', [make_skill('python', 4)]),
    make_employee('Caroline', [make_skill('java', 7), make_skill('c', 8), make_skill('project management', 6)]),
    make_employee('Dave', [make_skill('c', 1), make_skill('project management', 2)]),
    make_employee('Erin', [make_skill('java', 3), make_skill('python', 8), make_skill('forth', 7)]),
    make_employee('Gav', [make_skill('python', 6), make_skill('c', 6)]),
]

def employees_with_skill_level(employees, desired_skill, minimum_ability):
    found = []
    for employee in employees:
        for skill in employee['skills']:
            if skill['name'] == desired_skill and skill['ability'] >= minimum_ability:
                found.append(employee)

    return found

def make_work_package(desired_skill, minimum_ability, required_staff_count):
    return {
        'desired_skill': desired_skill,
        'minimum_ability': minimum_ability,
        'required_staff_count': required_staff_count
    }

def can_staff_project(employees, project):
    eligible_employees = employees_with_skill_level(
        employees,
        project['desired_skill'],
        project['minimum_ability'])
    return (len(eligible_employees) >= project['required_staff_count'], eligible_employees)

def can_staff_multiple_projects(employees, projects):
    staff = employees
    total_success = True
    all_selected_staff = []
    for p in projects:
        success, required_staff = can_staff_project(staff, p)
        total_success = total_success and success
        all_selected_staff += required_staff
        staff = [x for x in staff if x not in all_selected_staff]
    return (total_success, all_selected_staff)

def get_all_skills(employees):
    all_skills = []
    for employee in employees:
        for skill in employee['skills']:
            skill_name = skill['name']
            if skill_name not in all_skills:
                all_skills.append(skill_name)
    return all_skills

def get_all_skills_two(employees):
    flattened_list = []
    for skills in [employee['skills'] for employee in employees]:
        flattened_list.extend(skills)
    return set([skill['name'] for skill in flattened_list])

def get_all_skills_three(employees):
    flattened_list = chain.from_iterable([employee['skills'] for employee in employees])
    return set([ skill['name'] for skill in flattened_list ])

def get_best_employee(employees):
    averages = []
    for employee in employees:
        skills = employee['skills']
        total_ability_score = sum([skill['ability'] for skill in skills])
        average = total_ability_score / len(skills)
        averages.append({'name': employee['name'], 'average_ability': average})

    return max(averages, key=lambda item: item['average_ability'])

def get_best_employee_two(employees):
    averages = [get_averages_for_employee(employee) for employee in employees]
    return max(averages, key=lambda item: item['average_ability'])

def get_averages_for_employee(employee):
    skills = employee['skills']
    total_ability_score = sum([skill['ability'] for skill in skills])
    average = total_ability_score / len(skills)
    return {'name': employee['name'], 'average_ability': average}


if __name__ == '__main__':
    package = make_work_package('python', 6, 3)
    success, employees = can_staff_project(EMPLOYEES, package)
    print(success)
    print(employees)

    package2 = make_work_package('forth', 5, 1)
    packages = [package, package2]
    success, employees = can_staff_multiple_projects(EMPLOYEES, packages)
    print(success)
    print(employees)

    # This should print every skill we have, but only one copy
    # of each; if four people know python, it should only print
    # 'python' once.
    skills = get_all_skills(EMPLOYEES)
    skills = get_all_skills_two(EMPLOYEES)
    skills = get_all_skills_three(EMPLOYEES)
    print("Here are all the skills we have in our staff:")
    for skill in skills:
        print(skill)

    # To find the best employee, calculate the average of all
    # their ability scores.
    best = get_best_employee(EMPLOYEES)
    print(f'Our best employee is {best["name"]}, with an average ability of {best["average_ability"]}')

    # If you want a final exercise, print a report with every
    # skill in the company, the average ability for that skill,
    # and the names of the people with that skill. e.g.
    #
    # javascript (6.8): Simon, Suzie, Sam
    # C++ (2.4): Jules, Jools, Julie, Julia
    # Perl (7.0): Babs, Bill
