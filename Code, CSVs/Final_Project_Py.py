import pandas as pd

def load_file(path):
    # check if it is a csv
    if str(path).split('.')[-1] == "csv":
        df = pd.read_csv(path)
    # check if it is excel
    elif str(path).split('.')[-1] in ["xls", "xlsx"]:
        df = pd.read_excel(path)
    else:
        raise ValueError("Unsupported file type. Please use a CSV or Excel file.")
    
    return df


def show_details(df):
    pd.set_option('display.max_columns', None)  #for showing all the columns of a df
    #print(f"HEAD OF DF:\n{df.head()}\n\n")
    print("DF-INFO:\n")  
    df.info()
    print(      
        f"\nALL COLUMNS:\n {df.columns}\n\n"
        f"DESCRIPTION OF DF:\n{df.describe()}\n\n"
        f"DF-SHAPE: {df.shape}\n\n"
        f"COUNT OF UNIQUE VALUES:\n {df.nunique()}\n\n"
        f"DF-DATATYPES:\n{df.dtypes}"    
    )


