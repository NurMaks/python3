# import libraries
import pandas as pd
import glob
from difflib import SequenceMatcher

# This function read csv files
def read_CSV(name):
    df = pd.read_csv(name+".csv")
    return df

def check_League(liga, files):
    for arr in files:
        if SequenceMatcher(None, arr, liga).ratio() > 0.85:
            liga = arr
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
    liga = check_League(liga, files)
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
    league = ""
    status = ""
    weight = ""
    number = ""
    clubs = []
    for i in range(2, len(answer)):
        if answer[i]=="who" or answer[i]=="that":
            status = "Matches "+answer[i+1]
            weight = answer[i+2]
            number = int(answer[i+4])
            break
        league += answer[i]+" "
    if "all league" in league:
        for liga in files:
            df = read_CSV(liga)
            for i, match in zip(range(0,len(df["Clubs"])), df[status]):
                try:
                    if weight=="more" and int(match)>number-1:
                        clubs.append(get_Info_DataFrame(df, i))
                    elif weight=="less" and int(match)<number+1:
                        clubs.append(get_Info_DataFrame(df, i))
                except:
                    pass
    else:
        liga = check_League(league, files)
        print(liga)
    print(clubs)


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
        elif "clubs in" in answer and answer.split(" ")[0]=="clubs":
            print(get_Res(answer, files))

if __name__== "__main__":
    main()