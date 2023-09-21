# Leen Said 2220356194

# I'm aware that my username is incorrect. I have previously
# discussed this issue in an email I sent earlier.

# edit: my code is displaying the list with proper whitespaces on python editors like vscode and pycharm

# import copy to create a deep copy of the main list
import copy


# Function to read the lines from the input text file
def read():
    f0 = open("doctors_aid_inputs.txt", "r")
    read = f0.readlines()
    return read


#  Function to write the output to the output text file
def export():
    f1 = open("doctors_aid_outputs.txt", "a")
    return f1


# Create the list in which patients' information will be recorded
patient_list = []

# create(x) function creates a new row in the list patient_list
# parameter x will take the line in input file that starts with "create"


def create(x):
    e = export()
    # split x where there exists a comma
    patient = x.split(",")
    # remove create from the string
    patient[0] = patient[0].replace("create ", "")
    # remove unnecessary white space
    patient[1] = patient[1].strip()
    patient[2] = patient[2].strip()
    patient[3] = patient[3].strip()
    patient[4] = patient[4].strip()
    patient[5] = patient[5].strip()
    patient = patient[0 : len(patient) + 1]
    t_f = patient in patient_list
    # if the patient's information already exists in the table
    if t_f:
        write_this = "Patient ", patient[0], " cannot be recorded due to duplication.\n"
        e.writelines(write_this)
    else:
        # append new record to patient_list
        patient_list.append(patient)
        write_this = "Patient ", patient[0], " is recorded.\n"
        e.writelines(write_this)


# function lookFor(test) determines if an item exists in the multidimensional list
def lookFor(test):
    for k in patient_list:
        if k[0] == test:
            return True
    else:
        return False


# function remove_item(item) removes a patient's record
def remove_item(item):
    e = export()
    for k in patient_list:
        if k[0] == item:
            # remove the row from the table
            patient_list.remove(k)
            write_this = "Patient ", item, " is removed.\n"
            e.writelines(write_this)

    # if patient's name doesn't already exist in the record
    else:
        write_this = "Patient ", item, " cannot be removed due to absence\n"
        e.writelines(write_this)


# function convert_to_float(frac_str) converts a string fraction to a float
def convert_to_float(frac_str):
    num, denom = frac_str.split("/")
    num = int(num)
    denom = int(denom)
    cal = num / denom
    return cal


# function probability(y) calculates the probability using values from the table
def probability(y):
    e = export()
    # find if the patient's name exists in the table
    if lookFor(y):
        # find the index of the patient's record in the table (row index)
        for p in patient_list:
            if p[0] == y:
                index_prob = patient_list.index(p)  # this is the row index
                # incidence is found in patient_list row index = index_prob, column index = 3
                # call function convert_to_float() since incidence is a string fraction
                incidence = convert_to_float(patient_list[index_prob][3])
                # accuracy is found in patient_list row index = index_prob, column index = 1
                accuracy = float(patient_list[index_prob][1])
                # formula for probability
                prob = incidence / (1 - accuracy + incidence)
                # find probability as a percentage
                prob = round(prob * 100, 2)
                # find the type of cancer the patient has
                type_of_cancer = patient_list[index_prob][2]
                write_this = (
                    "Patient ",
                    y,
                    " has a probability of ",
                    str(prob),
                    "% of having ",
                    type_of_cancer,
                    ". \n",
                )
                e.writelines(write_this)
                return prob
    # if the patient's name cannot be found in the records
    else:
        write_this = "Probability for ", y, " cannot be calculated due to absence. \n"
        e.writelines(write_this)


# This function does the same job as probability(y) function except printitng the output
def prob_for_recommendation(yy):
    e = export()
    # find if the patient's name exists in the table
    if lookFor(yy):
        # find the index of the patient's record in the table (row index)
        for p in patient_list:
            if p[0] == yy:
                index_prob = patient_list.index(p)  # this is the row index
                # incidence is found in patient_list row index = index_prob, column index = 3
                # call function convert_to_float() since incidence is a string fraction
                incidence = convert_to_float(patient_list[index_prob][3])
                # accuracy is found in patient_list row index = index_prob, column index = 1
                accuracy = float(patient_list[index_prob][1])
                # formula for probability
                prob = incidence / (1 - accuracy + incidence)
                # find probability as a percentage
                return prob


# function recommendation(mm) provides treatment recommendation based on the patient's data
def recommendation(mm):
    e = export()
    # find if patient's name exists in the table
    if lookFor(mm):
        # find the index of the patient's record in the table (row index)
        for q in patient_list:
            if q[0] == mm:
                index_risk = patient_list.index(q)  # row index
                # risk is found in patient_list row index = index_risk, column index = 5
                risk = float(patient_list[index_risk][5])
                # call function probability(mm)
                proba = prob_for_recommendation(mm)
                if risk < proba:
                    write_this = "System suggests ", mm, " NOT to have the treatment\n"
                    e.writelines(write_this)
                else:

                    write_this = "System suggests ", mm, " to have the treatment\n"
                    e.writelines(write_this)

    # if patient's name does Not exist in the table
    else:
        write_this = (
            "Recommendation for ",
            mm,
            " cannot be calculated due to absence.\n",
        )
        e.writelines(write_this)


# function list_t(z) turns list into a table


def list_t(z):
    # creating table structure & column headers
    q = (
        "Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n"
        "Name\tAccuracy	Name\t\t\tIncidence	Name\t\t\tRisk\n"
        "-------------------------------------------------------------------------\n"
    )
    # make the columns in the table align with proper whitespaces
    for k in z:
        if len(k[0]) < 4:
            q += k[0] + "\t\t"
        elif len(k[0]) < 8:
            q += k[0] + "\t"
        else:
            q += k[0]

        if len(k[1]) < 4:
            q += k[1] + "\t\t\t"
        elif len(k[1]) < 8:
            q += k[1] + "\t\t"
        elif len(k[1]) < 12:
            q += k[1] + "\t"
        else:
            q += k[1]

        if len(k[2]) < 4:
            q += k[2] + "\t\t\t\t"
        elif len(k[2]) < 8:
            q += k[2] + "\t\t\t"
        elif len(k[2]) < 12:
            q += k[2] + "\t\t"
        elif len(k[2]) < 16:
            q += k[2] + "\t"
        else:
            q += k[2]

        q += k[3] + "\t"

        if len(k[4]) < 4:
            q += k[4] + "\t\t\t\t"
        elif len(k[4]) < 8:
            q += k[4] + "\t\t\t"
        elif len(k[4]) < 12:
            q += k[4] + "\t\t"
        elif len(k[4]) < 16:
            q += k[4] + "\t"
        else:
            q += k[4]

        q += k[5] + "\n"

    e = export()
    e.writelines(q)


# read lines from the input file by calling function read()

for pat in read():

    if pat.startswith("create"):
        # pat is line from the input text file which starts with "create"
        # call create(x)
        create(pat)
        # take a deep copy of patient_list as list02
        list02 = copy.deepcopy(patient_list)

    elif pat.startswith("remove"):
        # pat is line from the input text file which starts with "remove"
        # split pat at whitespace
        pat = pat.split()
        # pat[1] is the patient's name
        # call remove_item(item)
        remove_item(pat[1])
        # take a deep copy of patient_list as list02
        list02 = copy.deepcopy(patient_list)

    elif pat.startswith("probability"):
        # pat is line from the input text file which starts with "probability"
        # split pat at whitespace
        pat = pat.split()
        # pat[1] is the patient's name
        # call probability(y)
        probability(pat[1])

    elif pat.startswith("recommendation"):
        # pat is line from the input text file which starts with "recommendation"
        # split pat at whitespace
        pat = pat.split()
        # pat[1] is the patient's name
        # call recommendation(mm)
        recommendation(pat[1])

    elif pat.startswith("list"):
        for i in list02:
            for g in i:
                g = g.strip()
            i[1] = float(i[1]) * 100
            i[1] = str(i[1]) + "%"
            i[5] = float(i[5]) * 100
            i[5] = str(int(i[5])) + "%"
        # call list_t(z)
        list_t(list02)

    else:
        e = export()
        write_this = "Incorrect input, please try again."
        e.writelines(write_this)
