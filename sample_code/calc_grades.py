import csv
import sys
import statistics


INPUT_FILE_INDEX=1
STUDENT_NAME_INDEX=0
MEAN_INDEX=0
MEDIAN_INDEX=1
VAR_INDEX=2


subjects_and_grades=dict()
studs=dict()


#This is the main function, it gets a csv file representing a list of students and their grades in different subjcts.
# It parses it and prints various statistics
#
# The first line of the file must contain a list of all the subjects (one word or more)
# All the lines starting from the seond must begin with the students name, followed by the grades in each subject (numbers only)
def main():
	parse_csv(sys.argv[INPUT_FILE_INDEX])
	print_stats()
	

def calc_stats(num_list):
	res=list()
	res.append(statistics.mean(num_list))
	res.append(statistics.median(num_list))
	res.append(statistics.pvariance(num_list, res[MEDIAN_INDEX])) #giving mean for optimization (avoiding re-caluculation)
	return res



def print_stats():
	print("stats")
	
	print("\n\t####### Students #######\n")
	for stud in studs:
		stud_grades=list()
		
		print("\nStudent: "+str(stud))
		
		print("\tGrades:")
		for subject in studs[stud]:
			stud_grades.append(int(studs[stud][subject]))
			print("\t\t"+str(subject)+": "+str(studs[stud][subject]))
		
		stud_stats=calc_stats(stud_grades)
		print("\tMean: "+format(stud_stats[MEAN_INDEX], '.2f')+" Median: "+format(stud_stats[MEDIAN_INDEX], '.2f')+" Variance: "+format(stud_stats[VAR_INDEX], '.2f'))


	print("\n\t####### Subjects #######\n")
	for subject in subjects_and_grades:
		grades_list=[int(y) for y in subjects_and_grades[subject]] #making it a list of integers for the statistics functions in calc_stats(...)
		
		print("\nSubject: "+str(subject)+" \n\tGrades: "+str(grades_list))
		statistics.mean(grades_list)
		subject_stats=calc_stats(grades_list)
		
		print("\tMean: "+format(subject_stats[MEAN_INDEX], '.2f')+" Median: "+format(subject_stats[MEDIAN_INDEX], '.2f')+" Variance: "+format(subject_stats[VAR_INDEX], '.2f'))



	
def read_info(parse_info, subjects):
	
	stud_name=parse_info[STUDENT_NAME_INDEX]
	studs[stud_name]=dict()
	grades_per_stud=dict()
	for i in range(1, len(parse_info)):
		cur_subject=subjects[i-1]
		cur_grade=parse_info[i]
		grades_per_stud[cur_subject]=cur_grade
		subjects_and_grades[cur_subject].append(cur_grade)
	
	studs[stud_name]=grades_per_stud




def parse_csv(csv_input_file):
	with open(csv_input_file, 'r') as f:
		reader = list(csv.reader(f))
		subjects=reader[0]
		for subject in subjects: #not using ubjects_and_grads=dict.fromkeys(subjects) as to not have them point at the same list
			global subjects_and_grades
			subjects_and_grades[subject]=list()
		
		for row in reader[1:]:
			#sending subjects (as oppose to deducing the list from subjects_and_grades.keys()) to maintain the order
			read_info(row, subjects) 


if __name__ == "__main__": main()