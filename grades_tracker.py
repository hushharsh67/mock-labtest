import csv


#--------- Start of Functions to be implemented -----------------------

##########################################################
# Function to get the student with the highest score     #
# Parameters:                                            #
#  'students': List containing the CSV file contents     #
#                                                        #
# Return value:                                          #
#   'top': Student dictionary with the highest score     #
#          or None if students is empty                  #
##########################################################
def get_top_student(students):
    top = None

    # Add your implementation from here
    #HINT: Loop through students and compare scores


    return top

##################################################################
# Function to calculate the average score of all students       #
# Parameters:                                                    #
#  'students': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    average: Calculated average score (0 if empty)              #
##################################################################
def calc_average_score(students):
    average = 0

    # Add your implementation from here
    #HINT: Add up all the scores, then divide by len(students)


    return average

##################################################################
# Function to count the students who passed (score >= 50)       #
# Parameters:                                                    #
#  'students': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    count: Number of students with score >= 50                  #
##################################################################
def count_passed(students):
    count = 0

    # Add your implementation from here


    return count

#--------- End of Functions to be implemented -----------------------


def display_menu():
    print("\n" + "=" * 40)
    print("----- Grades Tracker -----")
    print("=" * 40)
    print("Select option")
    print("1 - Display all students")
    print("2 - Display statistics")
    print("3 - Display top student")
    print("Q - Quit")
    print("=" * 40)


def load_csv():
    print("\nLoading CSV file database")

    students = []

    try:
        with open('grades.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                students.append({
                    'name': row['name'],
                    'subject': row['subject'],
                    'score': float(row['score'])
                })
    except FileNotFoundError:
        print("Error: grades.csv file not found!")
    except Exception as e:
        print(f"Error loading CSV: {e}")

    return students


def display_all_students(students):
    print("\nAll Students")
    print("=" * 50)
    print(f"{'Name':<15} {'Subject':<20} {'Score':<15}")
    print("-" * 50)

    for s in students:
        print(f"{s['name']:<15} {s['subject']:<20} {s['score']:<15.0f}")

    print("=" * 50)


def display_statistics(students):
    average = calc_average_score(students)
    passed = count_passed(students)

    print("\nStatistics")
    print("=" * 50)
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {average:.1f}")
    print(f"Students Passed: {passed}")
    print("=" * 50)


def main():
    while True:
        display_menu()
        choice = input("Enter selection => ").strip().upper()

        students = load_csv()

        if choice == '1':
            display_all_students(students)
        elif choice == '2':
            display_statistics(students)
        elif choice == '3':
            top = get_top_student(students)

            if top:
                print("\nTop Student")
                print("=" * 50)
                print(f"Name: {top['name']}")
                print(f"Subject: {top['subject']}")
                print(f"Score: {top['score']:.0f}")
                print("=" * 50)
            else:
                print("\nNo students found!")

        elif choice == 'Q':
            print("\nThank you for using Grades Tracker!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
