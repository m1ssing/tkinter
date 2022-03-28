#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cschultz
#
# Created:     02/01/2019
# Copyright:   (c) cschultz 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
import arcpy
import os
import datetime

arcpy.env.overwriteOutput = True


MONTH = [1,2,3,4,5,6,7,8,9,10,11,12]
DATE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
YEAR = [2018,2019,2020,2021,2022,2023,2024,2025]
BOOLEAN = ["True", "False"]
MUD = ["NOT NULL", "NULL", "FORT BEND MUD 1", "MUD 2", "MUD 3", "MUD 6" ,"MUD 16", "MUD 17", "MUD 18", "MUD 19", "MUD 21", "MUD 22", "MUD 23",
       "MUD 26", "MUD 27", "MUD 28", "MUD 34", "MUD 35", "HARRIS MUD 509", "HARRIS (BRAZ) MUD 509"]
ESD = ["NOT NULL", "NULL", "'ESD 4'", "'ESD 5'"]
DISTRICT = ["ALL DISTRICTS", "'ST1'", "'ST2'", "'ST3'", "'ST4'", "'ST5'", "'ST6'", "'ST7'", "'ST8'", "'ST9'", "'ST10'", "'ST11'"]
TYPE = ["ALL CALLS", "'EMS'", "'FIRE'"]
HGAC_CITIES = ["NULL", "'ALVIN'", "'ARCOLA'", "'BROOKSIDE VILLAGE'", "'FRIENDSWOOD'", "'HOUSTON'", "'IOWA COLONY'", "'MANVEL'", "'MISSOURI CITY'", "'STAFFORD'"]
MAX = 100

root = Tk()


#Create Variables
STmonthVar = IntVar(root)
STdateVar = IntVar(root)
STyearVar = IntVar(root)
ENDmonthVar = IntVar(root)
ENDdateVar = IntVar(root)
ENDyearVar = IntVar(root)
cityLimitVar = StringVar(root)
etjVar = StringVar(root)
mudVar = StringVar(root)
fileVar = StringVar(root)
esdVar = StringVar(root)
distVar = StringVar(root)
typeVar = StringVar(root)
hgacVar = StringVar(root)


cityLimitVar.set(BOOLEAN[0])
etjVar.set(BOOLEAN[0])
mudVar.set(MUD[0])
esdVar.set(ESD[0])
distVar.set(DISTRICT[0])
typeVar.set(TYPE[0])
hgacVar.set(HGAC_CITIES[0])


#Setting start and end dates dynamically
date =datetime.date.today()
pastdate = date - datetime.timedelta(days = 90)
lst_initial_ST = []
lst_initial_ST.append(str(pastdate))
lst_initial_END=[]
lst_initial_END.append(str(date))

# ST_lst/END_lst = [ 'YYYY', 'MM', 'DD']
ST_lst = [y for x in lst_initial_ST for y in x.split("-")]
END_lst = [y for x in lst_initial_END for y in x.split("-")]

#START Year (Current date - 90 days)
def start_year():
    if ST_lst[0] == "2018":
        STyearVar.set(YEAR[0])
    elif ST_lst[0] == "2019":
        STyearVar.set(YEAR[1])
    elif ST_lst[0] == "2020":
        STyearVar.set(YEAR[2])
    elif ST_lst[0] == "2021":
        STyearVar.set(YEAR[3])
    elif ST_lst[0] == "2022":
        STyearVar.set(YEAR[4])
    elif ST_lst[0] == "2023":
        STyearVar.set(YEAR[5])
    elif ST_lst[0] == "2024":
        STyearVar.set(YEAR[6])
    elif ST_lst[0] == "2025":
        STyearVar.set(YEAR[7])

#START Month (Current Date - 90 days)
def start_month():
    if ST_lst[1] == "01":
        STmonthVar.set(MONTH[0])
    elif ST_lst[1] == "02":
        STmonthVar.set(MONTH[1])
    elif ST_lst[1] == "03":
        STmonthVar.set(MONTH[2])
    elif ST_lst[1] == "04":
        STmonthVar.set(MONTH[3])
    elif ST_lst[1] == "05":
        STmonthVar.set(MONTH[4])
    elif ST_lst[1] == "06":
        STmonthVar.set(MONTH[5])
    elif ST_lst[1] == "07":
        STmonthVar.set(MONTH[6])
    elif ST_lst[1] == "08":
        STmonthVar.set(MONTH[7])
    elif ST_lst[1] == "09":
        STmonthVar.set(MONTH[8])
    elif ST_lst[1] == "10":
        STmonthVar.set(MONTH[9])
    elif ST_lst[1] == "11":
        STmonthVar.set(MONTH[10])
    elif ST_lst[1] == "12":
        STmonthVar.set(MONTH[11])

#START Date(Current Date - 90 days)
def start_date():
    if ST_lst[2] >= "01" and ST_lst[2] <= "10":
        if ST_lst[2] == "01":
            STdateVar.set(DATE[0])
        elif ST_lst[2] == "02":
            STdateVar.set(DATE[1])
        elif ST_lst[2] == "03":
            STdateVar.set(DATE[2])
        elif ST_lst[2] == "04":
            STdateVar.set(DATE[3])
        elif ST_lst[2] == "05":
            STdateVar.set(DATE[4])
        elif ST_lst[2] == "06":
            STdateVar.set(DATE[5])
        elif ST_lst[2] == "07":
            STdateVar.set(DATE[6])
        elif ST_lst[2] == "08":
            STdateVar.set(DATE[7])
        elif ST_lst[2] == "09":
            STdateVar.set(DATE[8])
        elif ST_lst[2] == "10":
            STdateVar.set(DATE[9])
    if ST_lst[2] >= "11" and ST_lst[2] <= "20":
        if ST_lst[2] == "11":
            STdateVar.set(DATE[10])
        elif ST_lst[2] == "12":
            STdateVar.set(DATE[11])
        elif ST_lst[2] == "13":
            STdateVar.set(DATE[12])
        elif ST_lst[2] == "14":
            STdateVar.set(DATE[13])
        elif ST_lst[2] == "15":
            STdateVar.set(DATE[14])
        elif ST_lst[2] == "16":
            STdateVar.set(DATE[15])
        elif ST_lst[2] == "17":
            STdateVar.set(DATE[16])
        elif ST_lst[2] == "18":
            STdateVar.set(DATE[17])
        elif ST_lst[2] == "19":
            STdateVar.set(DATE[18])
        elif ST_lst[2] == "20":
            STdateVar.set(DATE[19])
    if ST_lst[2] >= "21" and ST_lst[2] <= "31":
        if ST_lst[2] == "21":
            STdateVar.set(DATE[20])
        elif ST_lst[2] == "22":
            STdateVar.set(DATE[21])
        elif ST_lst[2] == "23":
            STdateVar.set(DATE[22])
        elif ST_lst[2] == "24":
            STdateVar.set(DATE[23])
        elif ST_lst[2] == "25":
            STdateVar.set(DATE[24])
        elif ST_lst[2] == "26":
            STdateVar.set(DATE[25])
        elif ST_lst[2] == "27":
            STdateVar.set(DATE[26])
        elif ST_lst[2] == "28":
            STdateVar.set(DATE[27])
        elif ST_lst[2] == "29":
            STdateVar.set(DATE[28])
        elif ST_lst[2] == "30":
            STdateVar.set(DATE[29])
        elif ST_lst[2] == "31":
            STdateVar.set(DATE[30])

#END Year (Current date)
def end_year():
    if END_lst[0] == "2019":
        ENDyearVar.set(YEAR[1])
    elif END_lst[0] == "2020":
        ENDyearVar.set(YEAR[2])
    elif END_lst[0] == "2021":
        ENDyearVar.set(YEAR[3])
    elif END_lst[0] == "2022":
        ENDyearVar.set(YEAR[4])
    elif END_lst[0] == "2023":
        ENDyearVar.set(YEAR[5])
    elif END_lst[0] == "2024":
        ENDyearVar.set(YEAR[6])
    elif END_lst[0] == "2025":
        ENDyearVar.set(YEAR[7])

#END Month (Current Date)
def end_month():
    if END_lst[1] == "01":
        ENDmonthVar.set(MONTH[0])
    elif END_lst[1] == "02":
        ENDmonthVar.set(MONTH[1])
    elif END_lst[1] == "03":
        ENDmonthVar.set(MONTH[2])
    elif END_lst[1] == "04":
        ENDmonthVar.set(MONTH[3])
    elif END_lst[1] == "05":
        ENDmonthVar.set(MONTH[4])
    elif END_lst[1] == "06":
        ENDmonthVar.set(MONTH[5])
    elif END_lst[1] == "07":
        ENDmonthVar.set(MONTH[6])
    elif END_lst[1] == "08":
        ENDmonthVar.set(MONTH[7])
    elif END_lst[1] == "09":
        ENDmonthVar.set(MONTH[8])
    elif END_lst[1] == "10":
        ENDmonthVar.set(MONTH[9])
    elif END_lst[1] == "11":
        ENDmonthVar.set(MONTH[10])
    elif END_lst[1] == "12":
        ENDmonthVar.set(MONTH[11])

#END Date
def end_date():
    if END_lst[2] >= "01" and END_lst[2] <= "10":
        if END_lst[2] == "01":
            ENDdateVar.set(DATE[0])
        elif END_lst[2] == "02":
            ENDdateVar.set(DATE[1])
        elif END_lst[2] == "03":
            ENDdateVar.set(DATE[2])
        elif END_lst[2] == "04":
            ENDdateVar.set(DATE[3])
        elif END_lst[2] == "05":
            ENDdateVar.set(DATE[4])
        elif END_lst[2] == "06":
            ENDdateVar.set(DATE[5])
        elif END_lst[2] == "07":
            ENDdateVar.set(DATE[6])
        elif END_lst[2] == "08":
            ENDdateVar.set(DATE[7])
        elif END_lst[2] == "09":
            ENDdateVar.set(DATE[8])
        elif END_lst[2] == "10":
            ENDdateVar.set(DATE[9])
    if END_lst[2] >= "11" and END_lst[2] <= "20":
        if END_lst[2] == "11":
            ENDdateVar.set(DATE[10])
        elif END_lst[2] == "12":
            ENDdateVar.set(DATE[11])
        elif END_lst[2] == "13":
            ENDdateVar.set(DATE[12])
        elif END_lst[2] == "14":
            ENDdateVar.set(DATE[13])
        elif END_lst[2] == "15":
            ENDdateVar.set(DATE[14])
        elif END_lst[2] == "16":
            ENDdateVar.set(DATE[15])
        elif END_lst[2] == "17":
            ENDdateVar.set(DATE[16])
        elif END_lst[2] == "18":
            ENDdateVar.set(DATE[17])
        elif END_lst[2] == "19":
            ENDdateVar.set(DATE[18])
        elif END_lst[2] == "20":
            ENDdateVar.set(DATE[19])
    if END_lst[2] >= "21" and END_lst[2] <= "31":
        if END_lst[2] == "21":
            ENDdateVar.set(DATE[20])
        elif END_lst[2] == "22":
            ENDdateVar.set(DATE[21])
        elif END_lst[2] == "23":
            ENDdateVar.set(DATE[22])
        elif END_lst[2] == "24":
            ENDdateVar.set(DATE[23])
        elif END_lst[2] == "25":
            ENDdateVar.set(DATE[24])
        elif END_lst[2] == "26":
            ENDdateVar.set(DATE[25])
        elif END_lst[2] == "27":
            ENDdateVar.set(DATE[26])
        elif END_lst[2] == "28":
            ENDdateVar.set(DATE[27])
        elif END_lst[2] == "29":
            ENDdateVar.set(DATE[28])
        elif END_lst[2] == "30":
            ENDdateVar.set(DATE[29])
        elif END_lst[2] == "31":
            ENDdateVar.set(DATE[30])

#Formatting the GUI
STdate_txt = Label(root, text= "Start Date: ")
STdate_txt.grid(row = 0, column = 0)

STmonth_txt = Label(root, text= "Month: ")
STmonth_txt.grid(row= 0, column = 1)

STmonth_menu = OptionMenu (root, STmonthVar, *MONTH)
STmonth_menu.grid(row=0, column = 2)

STnumdate_txt = Label(root, text= "Date: ")
STnumdate_txt.grid(row= 0, column = 3)

STdate_menu = OptionMenu(root, STdateVar, *DATE)
STdate_menu.grid(row=0, column= 4)

STyear_txt = Label(root, text="Year: ")
STyear_txt.grid(row=0, column = 5)

STyear_menu = OptionMenu(root, STyearVar, *YEAR)
STyear_menu.grid(row=0, column = 6)

ENDdate_txt = Label(root, text= "End Date: ")
ENDdate_txt.grid(row = 1, column = 0)

ENDmonth_txt = Label(root, text= "Month: ")
ENDmonth_txt.grid(row= 1, column = 1)

ENDmonth_menu = OptionMenu (root, ENDmonthVar, *MONTH)
ENDmonth_menu.grid(row=1, column = 2)

ENDnumdate_txt = Label(root, text= "Date: ")
ENDnumdate_txt.grid(row= 1, column = 3)

ENDdate_menu = OptionMenu(root, ENDdateVar, *DATE)
ENDdate_menu.grid(row=1, column= 4)

ENDyear_txt = Label(root, text="Year: ")
ENDyear_txt.grid(row=1, column = 5)

ENDyear_menu = OptionMenu(root, ENDyearVar, *YEAR)
ENDyear_menu.grid(row=1, column = 6)

cityLimit_txt = Label(root, text= "City Limit ? ")
cityLimit_txt.grid(row=4, column = 1)

cityLimit_menu = OptionMenu(root, cityLimitVar, *BOOLEAN)
cityLimit_menu.grid(row= 4, column= 2)

etj_txt = Label(root, text = "ETJ ? ")
etj_txt.grid(row= 4, column= 3)

etj_menu = OptionMenu(root, etjVar, *BOOLEAN)
etj_menu.grid(row=4, column= 4)

dist_txt = Label(root, text = "District ? ")
dist_txt.grid(row=4, column = 5)

dist_menu = OptionMenu(root, distVar, *DISTRICT)
dist_menu.grid(row=4, column= 6)

type_txt = Label(root, text = "Call Type ? ")
type_txt.grid(row=4, column= 7)

type_menu = OptionMenu(root, typeVar, *TYPE)
type_menu.grid(row=4, column= 8)

mud_txt = Label(root, text = "MUD ? ")
mud_txt.grid(row= 5, column= 1)

mud_menu = OptionMenu(root, mudVar, *MUD)
mud_menu.grid(row=5, column= 2)

esd_txt = Label(root, text = "ESD ? ")
esd_txt.grid(row= 5, column= 3)

esd_menu = OptionMenu(root, esdVar, *ESD)
esd_menu.grid(row=5, column= 4)

hgac_text = Label(root, text= "Other Municipality ? ")
hgac_text.grid(row= 5, column = 5)

hgac_menu = OptionMenu(root, hgacVar, *HGAC_CITIES)
hgac_menu.grid(row= 5, column = 6)

inci_num = Entry(root)
inci_num.grid(row=6, column= 1)

inci_num_text = Label(root, text = "Incidient Number ? ")
inci_num_text.grid(row=6, column = 0)

filter_txt = Label(root, text = " ")
filter_txt.grid(row=7, column = 0)

STDate = Label(root, text =" ")
STDate.grid(row=7, column = 0)

ENDDate = Label(root, text =" ")
ENDDate.grid(row=8, column = 0)

filter_txt = Label(root, text = " ")
filter_txt.grid(row=12, column = 0)

filter_inci_txt = Label(root, text = " ")
filter_inci_txt.grid(row=13, column = 1)

filter_CL_txt = Label(root, text = " ")
filter_CL_txt.grid(row=13, column = 1)

filter_ETJ_txt = Label(root, text = " ")
filter_ETJ_txt.grid(row=13, column = 2)

filter_dist_txt = Label(root, text = " ")
filter_dist_txt.grid(row=13, column = 3)

filter_type_txt = Label(root, text = " ")
filter_type_txt.grid(row=13, column = 4)

filter_MUD_txt = Label(root, text = " ")
filter_MUD_txt.grid(row=14, column = 1)

filter_ESD_txt = Label(root, text = " ")
filter_ESD_txt.grid(row=14, column = 2)

filter_hgac_txt = Label(root, text = " ")
filter_hgac_txt.grid(row=14, column = 3)

##preset_txt = Label(root, text= "Query Presets: ")
##preset_txt.grid(row =0, column=8)
##
##preset_txt = Label(root, text= "Dates: ")
##preset_txt.grid(row =1, column=8)


count = Label(root, text=" ", fg = "red")
count.grid(row=15, column = 0)

error = Label(root, text=" ")
error.grid(row=21, column=0)

FireHouse_hope = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\PythonFiles\\GISVIEWER_GISDB.sde\\cop_sde.DBO.LoadingDock\\cop_sde.DBO.FireCalls"

status = Label(root, text = '', bd = 1, anchor = W)

status.grid(row=22, column = 0, columnspan = 6, sticky=W+E)

status['text'] = "STATUS: The Program is Currently IDLE..."



def confirm():

    status['text'] = "STATUS: The Program is Performing the Query..."
    status.update_idletasks()
    startDate = "{}-{}-{}"
    endDate = "{}-{}-{}"
    strDate_start=  startDate.format(STyearVar.get(), STmonthVar.get(), STdateVar.get())
    strDate_end =   endDate.format(ENDyearVar.get(), ENDmonthVar.get(), ENDdateVar.get())

    STDate_result = ("Start Date is: "+ strDate_start)
    STDate['text'] = STDate_result

    ENDDate_result = ("End Date is: "+ strDate_end)
    ENDDate['text'] = ENDDate_result

    tblview = arcpy.MakeTableView_management(FireHouse_hope, "outTable")
    rows = arcpy.SearchCursor("outTable")
    fireHouse_path = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\FireHouse.gdb"
    fireHouse_name = "GUI_Table"
    fireHouse_table = fireHouse_path +"\\"+fireHouse_name
    arcpy.Delete_management(fireHouse_table)
    if os.path.exists(fireHouse_table):
        arcpy.Delete_management(fireHouse_table)
    else:
        pass

    def query(cL_etj, ESD, MUD, DISTRICT, CALLTYPE, HGAC, INCIDENT):
        if INCIDENT != "":
            query_inci = INCIDENT
            return query_inci
        query = "alm_date >= '{} 00:00:00' AND alm_date <= '{} 00:00:00'" + cL_etj + ESD + MUD + DISTRICT + CALLTYPE + HGAC
        querytest = query.format(strDate_start, strDate_end)
        print (querytest)
        return querytest


    def cityLimit_etj(Cvar, Evar):
        if Cvar == "True" and Evar == "True":
            cl_etj = " AND CityorETJ IN ('CITY LIMIT', 'ETJ')"
        elif Cvar == "True" and Evar == "False":
            cl_etj = " AND CityorETJ IN ('CITY LIMIT')"
        elif Cvar == "False" and Evar == "True":
            cl_etj = " AND CityorETJ IN ('ETJ')"
        elif Cvar == "False" and Evar == "False":
            cl_etj = ""
        return cl_etj
    def esd(var):
        if var in ["'ESD 4'", "'ESD 5'"]:
            esd_string = " AND ESD = {}"
            esd = esd_string.format(var)
        elif var == "NULL":
            esd_string = " AND ESD IS {}"
            esd = esd_string.format(var)
        elif var == "NOT NULL":
            esd = ""
        return esd
    def mud(var):
        if var in ["FORT BEND MUD 1", "MUD 2", "MUD 3", "MUD 6" ,"MUD 16", "MUD 17", "MUD 18", "MUD 19", "MUD 21", "MUD 22", "MUD 23",
       "MUD 26", "MUD 27", "MUD 28", "MUD 34", "MUD 35", "HARRIS MUD 509", "HARRIS (BRAZ) MUD 509"]:
            mud_string = " AND MUD = {}"
            mud = mud_string.format(var)
        elif var == "NULL":
            mud_string = " AND MUD IS {}"
            mud = mud_string.format(var)
        elif var == "NOT NULL":
            mud = ""
        return mud
    def district(var):
        if var in ["'ST1'", "'ST2'", "'ST3'", "'ST4'", "'ST5'", "'ST6'", "'ST7'", "'ST8'", "'ST9'", "'ST10'", "'ST11'"]:
            dist_string = " AND DISTRICT = {}"
            dist = dist_string.format(var)
        elif var == "ALL DISTRICTS":
            dist = ""
        return dist

    def calltype(var):
        if var in ["'EMS'", "'FIRE'"]:
            ct_string = " AND TYPE = {}"
            ct = ct_string.format(var)
        elif var == "ALL CALLS":
            ct = ""
        return ct
    def hgac(var):
        if var in ["'ALVIN'", "'ARCOLA'", "'BROOKSIDE VILLAGE'", "'FRIENDSWOOD'", "'HOUSTON'", "'IOWA COLONY'", "'MANVEL'", "'MISSOURI CITY'", "'STAFFORD'"]:
            hgac_string = " AND HGAC_Area_Cities = {}"
            hgac = hgac_string.format(var)
        elif var == "NULL":
            hgac = ""
        return hgac
    def incident(var):
        var_string = str(var)
        print (var_string)
        incident_string = "inci_no = '{}'"
        incident = incident_string.format(var_string)
        if var == "":
            incident = ""
        return incident


    cL_etj = cityLimit_etj(cityLimitVar.get(), etjVar.get())
    ESD = esd(esdVar.get())
    MUD = mud(mudVar.get())
    DISTRICT = district(distVar.get())
    CALLTYPE = calltype(typeVar.get())
    HGAC = hgac(hgacVar.get())
    INCIDENT = incident(str(inci_num.get()))
    queries = query(cL_etj, ESD, MUD, DISTRICT, CALLTYPE, HGAC, INCIDENT)
    active_table = arcpy.TableToTable_conversion("outTable", fireHouse_path, fireHouse_name, queries)


    del tblview
    count_result = ("Count: " + str(int(arcpy.GetCount_management(fireHouse_table).getOutput(0))))
    count['text'] = count_result

    filter_txt    ['text'] = "Filters:"
    if INCIDENT != "":
        filter_inci_txt['text'] = "Inci #: " + str(inci_num.get())
    else:
        filter_CL_txt ['text'] = "City Limit is " + str(cityLimitVar.get())
        filter_ETJ_txt['text'] = "ETJ is " + str(etjVar.get())
        filter_MUD_txt['text'] = "MUD is " + str(mudVar.get())
        filter_ESD_txt['text'] = "ESD is " + str(esdVar.get())
        filter_dist_txt['text'] = "Fire District is " + str(distVar.get())
        filter_type_txt['text'] = "Call Type is " + str(typeVar.get())
        filter_hgac_txt['text'] = "Other Municipalities is " + str(hgacVar.get())
    print (queries)



    fileInput = Label (root, text="Save As: ")
    fileInput.grid(row=16, column =0)
    excelFile = Entry(root)
    excelFile.grid(row=16, column =1)
    status['text'] = "STATUS: The Program is Currrently IDLE..."
    status.update_idletasks()

    def create_excel():
        status['text'] = "STATUS: The Program is Exporting the Query to Excel File"
        status.update_idletasks()
        tblview2 = arcpy.MakeTableView_management(fireHouse_table, "outTable2")
        fileExport = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\PythonFiles\\FireHouse_excel\\"
        entry = str(excelFile.get())
        arcpy.TableToExcel_conversion("outTable2", "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\PythonFiles\\FireHouse_excel\\" + entry + ".xls")
        del tblview2
        status['text'] = "STATUS: The Program is Currrently IDLE..."
        status.update_idletasks()

    excel = Button (root, text= "Export to Excel", command = create_excel)
    excel.grid(row=16, column= 3)

def unit_window():
    window = Toplevel(root)
    stdate_txt= Label(window, text="Start Date : ")
    stdate_txt.grid(row=1, column=0)
    enddate_txt = Label(window, text="End Date : ")
    enddate_txt.grid(row=2, column=0)

    # Start Month
    stmonthformat_label = Label(window, text="(MM)")
    stmonthformat_label.grid(row=0, column=2)

    stmonth_label = Label(window, text="Month : ")
    stmonth_label.grid(row=1, column=1)

    STmonth_menu = OptionMenu(window, STmonthVar, *MONTH)
    STmonth_menu.grid(row=1, column=2)


    # Start Day
    stdayformat_label = Label(window, text="(DD)")
    stdayformat_label.grid(row=0, column=4)

    stday_label = Label(window, text="Day : ")
    stday_label.grid(row=1, column=3)
    STdate_menu = OptionMenu(window, STdateVar, *DATE)
    STdate_menu.grid(row=1, column=4)

    #Start Year
    styearformat_label = Label(window, text = "(YYYY)")
    styearformat_label.grid(row=0, column=6)

    styear_label = Label(window, text="Year : ")
    styear_label.grid(row=1, column=5)
    STyear_menu = OptionMenu(window, STyearVar, *YEAR)
    STyear_menu.grid(row=1, column=6)

    # End Month
    endmonth_label = Label(window, text="Month : ")
    endmonth_label.grid(row=2, column=1)
    ENDmonth_menu = OptionMenu(window, ENDmonthVar, *MONTH)
    ENDmonth_menu.grid(row=2, column=2)

    # End Day
    endday_label = Label(window, text="Day : ")
    endday_label.grid(row=2, column=3)

    ENDdate_menu = OptionMenu(window, ENDdateVar, *DATE)
    ENDdate_menu.grid(row=2, column=4)

    # End Year
    endyear_label = Label(window, text="Year : ")
    endyear_label.grid(row=2, column=5)

    ENDyear_menu = OptionMenu(window, ENDyearVar, *YEAR)
    ENDyear_menu.grid(row=2, column=6)

    Units_sde = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\PythonFiles\\GISVIEWER_GISDB.sde\\cop_sde.DBO.FIRECALLUNITS"

    def unit_confirm():

        status['text'] = "STATUS: The Program is Performing the Query..."
        status.update_idletasks()
        startDate = "{}-{}-{}"
        endDate = "{}-{}-{}"
        strDate_start = startDate.format(STyearVar.get(), STmonthVar.get(), STdateVar.get())
        strDate_end = endDate.format(ENDyearVar.get(), ENDmonthVar.get(), ENDdateVar.get())

        STDate_result = ("Start Date is: " + strDate_start)
        STDate['text'] = STDate_result

        ENDDate_result = ("End Date is: " + strDate_end)
        ENDDate['text'] = ENDDate_result

        tblview = arcpy.MakeTableView_management(Units_sde, "outTable")
        rows = arcpy.SearchCursor("outTable")
        units_path = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\FireHouse.gdb"
        units_name = "UNITS_GUI_Table"
        units_table = units_path + "\\" + units_name
        arcpy.Delete_management(units_table)
        if os.path.exists(units_table):
            arcpy.Delete_management(units_table)
        else:
            pass

    unit_query = Button(window, text="Start Unit Query")
    unit_query.grid(row=6, column=1)

    window.title("Units Query")
    window.mainloop()



unit = Button(root, text= "Open Unit Query", command= unit_window)
unit.grid(row=9, column=3)
confirm = Button(root, text= "Run Query", command= confirm)
confirm.grid(row=9, column = 1)

start_year()
start_month()
start_date()
end_year()
end_month()
end_date()

root.title("FireHouse Query")

root.minsize(600, 300)

mainloop()