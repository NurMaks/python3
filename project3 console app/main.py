# import libraries
import pandas as pd
import glob
from difflib import SequenceMatcher

# This function read csv files
def read_CSV(name):
    df = pd.read_csv(name+".csv")
    return df

def check_League(liga, files, coef):
    check = False
    temp = liga
    for arr in files:
        if SequenceMatcher(None, liga, arr).ratio() > coef:
            liga = arr
            check = True
            break
    if temp == liga and not check:
        return check_League(liga, files, coef-0.02)
    return liga

# This function return top clubs <number> from <League name>
def get_Top(answer, files):
    answer = answer.split(" ")
    number = int(answer[1])
    liga = ""
    for ind in range(4,len(answer)):
        if ind == len(answer)-1:
            liga += answer[ind]
        else:
            liga += answer[ind]+" "
    liga = check_League(liga, files, 0.9)
    try:
        df = read_CSV(liga)
        return df.head(number).iloc[:,:5]
    except:
        return "Error. There is no such league or you entered incorrectly."

def get_Info_DataFrame(df, i):
    arr = {}
    arr["Clubs"] = df["Clubs"][i]
    arr["Matches won"] = df["Matches won"][i]
    arr["Matches drawn"] = df["Matches drawn"][i]
    arr["Matches lost"] = df["Matches lost"][i]
    arr["Points"] = df["Points"][i]
    return arr

def get_Res(answer, files):
    answer = answer.split()
    status = "Matches "+answer[2]
    weight = answer[3]
    number = int(answer[5])
    league = ""
    for q in answer[8:]:
        league += q+" "
    league = league[:-1].title()
    clubs = []
    def compile(liga):
        df = read_CSV(liga)
        for i, match in zip(range(0,len(df["Clubs"])), df[status]):
            try:
                if match == "-":
                    match = 0
                if weight=="more" and int(match)>number-1:
                    clubs.append(get_Info_DataFrame(df, i))
                elif weight=="less" and int(match)<number+1:
                    clubs.append(get_Info_DataFrame(df, i))
            except:
                pass
    if "All League" in league or len(league)==0:
        for liga in files:
            compile(liga)
    else:
        liga = check_League(league, files, 0.9)
        compile(liga)
    df = pd.DataFrame(clubs)
    return df


def main():
    # read .csv files in this repositories
    csv = glob.glob("*.csv")
    files = []
    # split and save only names of files (it is names of League)
    for file in csv:
        files.append(file.split(".")[0])
    # Endless loop for receiving requests
    while True:
        answer = input(">>")
        if answer == "exit" or answer == "close" or answer == "end":
            break
        
        if answer.split(" ")[0] == "top":
            print(get_Top(answer, files))

        elif ("clubs that" in answer and answer.split(" ")[0]=="clubs" and "and" not in answer):
            df = get_Res(answer, files)
            status = "Matches "+answer.split()[2]
            df = df.groupby([status,"Clubs"]).mean()
            print(df.sort_values(by=[status,'Points'], ascending=False))

        elif ("clubs that" in answer and answer.split(" ")[0]=="clubs" and "and" in answer):
            print(get_comboRes(answer, files))

if __name__== "__main__":
    main()