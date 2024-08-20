import tkinter as tk
from tkinter import ttk
from Support.Database.pipeprodfunc import *
from datetime import datetime, timedelta
import os

#ToDO
#1. Generate Frame for each view(Job, Element, Pipe, Port)
#2. Make functions for buttons and inputs(Make sure that data in inputs is easly sherable)
#3. Send data to MySQL database
#4. Update database so name will be ID(this will check if name is not placed couple times already

#this is for selection of language
language_Select = []
#this is for selection of names for all names
language_DataName = []
#this is for storing of names for all languages
language_DataTable = []


def GUI_Summary_save_to_txt(TimeOrderPipePortSummaryPerDate_Final={}, TimeOrderTreview={}, DatesToDisplay={}):
    file_name = "Summary.txt"
    file_path = os.getcwd()
    file_path = os.path.join(file_path, 'Debug', file_name)
    #remove content from file
    file1 = open(file_path, 'r+')
    file1.truncate(0)  # need '0' when using r+
    file1.close()

    #fill with updated report
    file1 = open(file_path, 'a')
    for day in TimeOrderPipePortSummaryPerDate_Final:
        file1.write(str(day) + '\t')
        for part in TimeOrderPipePortSummaryPerDate_Final[day]:
            file1.write(str(part) + ' = ')
            file1.write(str(TimeOrderPipePortSummaryPerDate_Final[day][part]) + '\t')
        file1.write( '\n')
    file1.close()

    return True

def GUI_Summary_save_to_pdf(TimeOrderPipePortSummaryPerDate_Final={}, TimeOrderTreview={}, DatesToDisplay={}):

    file_name = "Summary.txt"
    file_path = os.getcwd()
    file_path = os.path.join(file_path, 'Debug', file_name)
    #remove content from file
    file1 = open(file_path, 'r+')
    file1.truncate(0)  # need '0' when using r+
    file1.close()

    # fill with updated report
    file1 = open(file_path, 'a')
    for day in TimeOrderPipePortSummaryPerDate_Final:
        file1.write(str(day) + '\t')
        for part in TimeOrderPipePortSummaryPerDate_Final[day]:
            file1.write(str(part) + ' = ')
            file1.write(str(TimeOrderPipePortSummaryPerDate_Final[day][part]) + '\t')
        file1.write('\n')
    file1.close()

    return True

def GUI_trace_function(message, messageLvl=0):
    print(str(messageLvl)+'; ' + message)

    log = bottom_frame_label_app_event_log['text'] + '\n'
    log_temp = str(datetime.now()) + '  :   ' + str(messageLvl) + ': ' + message
    log = log + log_temp
    bottom_frame_label_app_event_log.config(text=log)

    if debug_log == True:
        file_name = debug_log_name + ".txt"
        file_path = os.getcwd()
        file_path = os.path.join(file_path, 'Debug', file_name)
        file1 = open(file_path, 'a')
        file1.write(log_temp + '\n')
        file1.close()

def GUI_dummy_function():
    GUI_trace_function('GUI_dummy_function')

def GUI_GoTo_TimeSummary():
    GUI_trace_function('GUI_GoTo_TimeSummary')
    ctr_mid_TimeSummary.grid_forget()
    ctr_mid_Job.grid_forget()
    ctr_mid_Element.grid_forget()
    ctr_mid_Pipe.grid_forget()
    ctr_mid_Port.grid_forget()

    ctr_mid_TimeSummary.grid(row=0, column=1, sticky="nsew")

def GUI_GoTo_Job():
    GUI_trace_function('GUI_GoTo_Job')
    ctr_mid_TimeSummary.grid_forget()
    ctr_mid_Job.grid_forget()
    ctr_mid_Element.grid_forget()
    ctr_mid_Pipe.grid_forget()
    ctr_mid_Port.grid_forget()

    ctr_mid_Job.grid(row=0, column=1, sticky="nsew")

def GUI_GoTo_Element():
    GUI_trace_function('GUI_GoTo_Element')
    ctr_mid_TimeSummary.grid_forget()
    ctr_mid_Job.grid_forget()
    ctr_mid_Element.grid_forget()
    ctr_mid_Pipe.grid_forget()
    ctr_mid_Port.grid_forget()

    ctr_mid_Element.grid(row=0, column=1, sticky="nsew")

def GUI_GoTo_Pipe():
    GUI_trace_function('GUI_GoTo_Pipe')
    ctr_mid_TimeSummary.grid_forget()
    ctr_mid_Job.grid_forget()
    ctr_mid_Element.grid_forget()
    ctr_mid_Pipe.grid_forget()
    ctr_mid_Port.grid_forget()

    ctr_mid_Pipe.grid(row=0, column=1, sticky="nsew")

def GUI_GoTo_Port():
    GUI_trace_function('GUI_GoTo_Port')
    ctr_mid_TimeSummary.grid_forget()
    ctr_mid_Job.grid_forget()
    ctr_mid_Element.grid_forget()
    ctr_mid_Pipe.grid_forget()
    ctr_mid_Port.grid_forget()

    ctr_mid_Port.grid(row=0, column=1, sticky="nsew")

def GUI_MySQL_DatabaseSettings():
    GUI_trace_function('GUI_MySQL_DatabaseSettings')
    # ToDo
    # Here popup options for database configurations
    GUI_MySQL_database_settings_TopLvl = tk.Toplevel()
    GUI_MySQL_database_settings_TopLvl.title('GUI_MySQL_database_settings_TopLvl')
    GUI_MySQL_database_settings_IP_label = tk.Label(GUI_MySQL_database_settings_TopLvl,
                                                    text="IP: ", background="green", width=10)
    GUI_MySQL_database_settings_IP = tk.Entry(GUI_MySQL_database_settings_TopLvl,
                                              textvariable=GUI_MySQL_database_settings_IP_text, text="Select",
                                              background="green", width=10)
    GUI_MySQL_database_settings_port_label = tk.Label(GUI_MySQL_database_settings_TopLvl,
                                                      text="Port: ", background="green", width=10)
    GUI_MySQL_database_settings_port = tk.Entry(GUI_MySQL_database_settings_TopLvl,
                                                textvariable=GUI_MySQL_database_settings_port_text,
                                                text=language_DataTable.get("Select").get(language_Select),
                                                background="green", width=10)
    GUI_MySQL_database_settings_db_name_label = tk.Label(GUI_MySQL_database_settings_TopLvl,
                                                         text="DB name: ", background="green", width=10)
    GUI_MySQL_database_settings_db_name = tk.Entry(GUI_MySQL_database_settings_TopLvl,
                                                   textvariable=GUI_MySQL_database_settings_db_name_text,
                                                   text=language_DataTable.get("Select").get(language_Select),
                                                   background="green", width=10)
    GUI_MySQL_database_settings_host_name_label = tk.Label(GUI_MySQL_database_settings_TopLvl,
                                                           text="Host name: ", background="green", width=10)
    GUI_MySQL_database_settings_host_name = tk.Entry(GUI_MySQL_database_settings_TopLvl,
                                                     textvariable=GUI_MySQL_database_settings_host_name_text,
                                                     text=language_DataTable.get("Select").get(language_Select),
                                                     background="green", width=10)
    GUI_MySQL_database_settings_host_pass_label = tk.Label(GUI_MySQL_database_settings_TopLvl,
                                                           text="Host pass: ", background="green", width=10)
    GUI_MySQL_database_settings_host_pass = tk.Entry(GUI_MySQL_database_settings_TopLvl,
                                                     textvariable=GUI_MySQL_database_settings_host_pass_text,
                                                     text=language_DataTable.get("Select").get(language_Select),
                                                     background="green", width=10)

    GUI_MySQL_database_settings_IP_label.grid(row=0, column=0)
    GUI_MySQL_database_settings_IP.grid(row=0, column=1)
    GUI_MySQL_database_settings_port_label.grid(row=1, column=0)
    GUI_MySQL_database_settings_port.grid(row=1, column=1)
    GUI_MySQL_database_settings_db_name_label.grid(row=2, column=0)
    GUI_MySQL_database_settings_db_name.grid(row=2, column=1)
    GUI_MySQL_database_settings_host_name_label.grid(row=3, column=0)
    GUI_MySQL_database_settings_host_name.grid(row=3, column=1)
    GUI_MySQL_database_settings_host_pass_label.grid(row=4, column=0)
    GUI_MySQL_database_settings_host_pass.grid(row=4, column=1)

def GUI_MySQL_DatabaseInfo(db):
    GUI_trace_function("GUI_MySQL_DatabaseInfo")
    info = DB_Info(db)
    db_info = 'Database name: ' + info[1] + '\n' + 'IP: ' + info[1] + '\n' + \
              'Port: ' + info[1] + '\n' + 'Host: ' + info[0] + '\n'
    bottom_frame_label_database_info.config(text=db_info)

def GUI_MySQL_search_return_entry(toplvl, treeview, entry):
    GUI_trace_function('GUI_MySQL_search_return')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        treeview_name = treeview_name[0]
        entry.set(treeview_name)
        break
    toplvl.destroy()

def GUI_MySQL_delete_from_database(toplvl, treeview, db, table):
    GUI_trace_function('GUI_MySQL_delete_from_database')
    #ToDo
    # Need to add here reference to Database destroy data function
    selected_items = treeview.selection()
    for selected_item in selected_items:
        items = treeview.item(selected_item)
        items = items.get('values')
        DB_Delete(db, table, items[0])
        treeview.delete(selected_item)

def GUI_MySQL_search_return_treeview(toplvl, treeview, entry, columnsRead, columnsWrite):
    GUI_trace_function('GUI_MySQL_search_return_treeview')
    # ToDo
    # Add popup window with list of defined elements for selection after clicking add button
    GUI_trace_function('GUI_MySQL_search_return')
    defaultNum = 0
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        items = entry.get_children()
        item = 0
        for i in items:
            item = int(i) + 1
        # check witch index is available and add record
        values = ()
        for i in columnsRead:
            values = (*values, treeview_name[i])
        #Fill blank values
        size = columnsWrite - len(values)
        for i in range(size):
            values = (*values, defaultNum)
        #enter valus
        entry.insert(parent='', index=item, iid=item, values=values)
    toplvl.destroy()
    # Get name and place it ito table

def GUI_treeview_return(treeview):
    GUI_trace_function('GUI_treeview_return')
    # ToDo
    # Add popup window with list of defined elements for selection after clicking add button
    items = treeview.get_children()
    items_value = []
    item = 0
    for i in items:
        treeview_temp = treeview.item(i)
        items_value.append( treeview_temp.get('values'))
        item = item + 1
    return items_value

def GUI_treeview_delete(treeview_):
    GUI_trace_function('GUI_treeview_delete')
    selected_items = treeview_.selection()
    for selected_item in selected_items:
        treeview_.delete(selected_item)

def GUI_TimePlan_GetTimeString(day=0, month=0, year=0):
    datestr = ""
    date = datetime.now() + timedelta(days=day)
    dateyear = str(date.year)
    if len(dateyear) < 4:
        dateyear = dateyear
    datemonth = str(date.month)
    if len(datemonth) < 2:
        datemonth = "0" + datemonth
    dateday = str(date.day)
    if len(dateday) < 2:
        dateday = "0" + dateday
    print(dateyear)
    print(datemonth)
    print(dateday)
    print(date.strftime("%A"))
    datestr = str(dateyear) + "." + str(datemonth) + "." + str(dateday)

    return datestr

def GUI_TimePlan_Update():
    GUI_trace_function("GUI_TimePlan_Update")

    DB_data = DB_Select_General(db, "Job", 'JobID', 'Name', 'Description',
                                'PipelineElementID_1', 'Ammount_1', 'DateExecuted_1', 'AmmountExecuted_1', 'DateToExecute_1',
                                'PipelineElementID_2', 'Ammount_2', 'DateExecuted_2', 'AmmountExecuted_2', 'DateToExecute_2',
                                'PipelineElementID_3', 'Ammount_3', 'DateExecuted_3', 'AmmountExecuted_3', 'DateToExecute_3',
                                'PipelineElementID_4', 'Ammount_4', 'DateExecuted_4', 'AmmountExecuted_4', 'DateToExecute_4',
                                'PipelineElementID_5', 'Ammount_5', 'DateExecuted_5', 'AmmountExecuted_5', 'DateToExecute_5',
                                'PipelineElementID_6', 'Ammount_6', 'DateExecuted_6', 'AmmountExecuted_6', 'DateToExecute_6',
                                'PipelineElementID_7', 'Ammount_7', 'DateExecuted_7', 'AmmountExecuted_7', 'DateToExecute_7',
                                'PipelineElementID_8', 'Ammount_8', 'DateExecuted_8', 'AmmountExecuted_8', 'DateToExecute_8',
                                'PipelineElementID_9', 'Ammount_9', 'DateExecuted_9', 'AmmountExecuted_9', 'DateToExecute_9',
                                'PipelineElementID_10', 'Ammount_10', 'DateExecuted_10', 'AmmountExecuted_10', 'DateToExecute_10',
                                'PipelineElementID_11', 'Ammount_11', 'DateExecuted_11', 'AmmountExecuted_11', 'DateToExecute_11',
                                'PipelineElementID_12', 'Ammount_12', 'DateExecuted_12', 'AmmountExecuted_12', 'DateToExecute_12',
                                'PipelineElementID_13', 'Ammount_13', 'DateExecuted_13', 'AmmountExecuted_13', 'DateToExecute_13',
                                'PipelineElementID_14', 'Ammount_14', 'DateExecuted_14', 'AmmountExecuted_14', 'DateToExecute_14',
                                'PipelineElementID_15', 'Ammount_15', 'DateExecuted_15', 'AmmountExecuted_15', 'DateToExecute_15',
                                'PipelineElementID_16', 'Ammount_16', 'DateExecuted_16', 'AmmountExecuted_16', 'DateToExecute_16',
                                'PipelineElementID_17', 'Ammount_17', 'DateExecuted_17', 'AmmountExecuted_17', 'DateToExecute_17',
                                'PipelineElementID_18', 'Ammount_18', 'DateExecuted_18', 'AmmountExecuted_18', 'DateToExecute_18',
                                'PipelineElementID_19', 'Ammount_19', 'DateExecuted_19', 'AmmountExecuted_19', 'DateToExecute_19',
                                'PipelineElementID_20', 'Ammount_20',  'DateExecuted_20', 'AmmountExecuted_20', 'DateToExecute_20')

    if not isinstance(DB_data, set):
        elementsDict = {}
        elementsList = []

        for x in DB_data:
            j = 0
            elements_description = ""
            elementDict = {}
            i = 0
            elementJobName = str(x[1])
            for z in x[3:]:
                if 1 == 1:
                    if i == 0:#Element name
                        elementDict.update({'JobsName': elementJobName})
                        elementDict.update({'JobsElementNumber': j})
                        if str(z) != "None":
                            elementDict.update({'Name': str(z)})
                        else:
                            elementDict.update({'Name': ""})
                    elif i == 1:#Element ammount
                        if str(z) != "None":
                            elementDict.update({'Ammount': str(z)})
                        else:
                            elementDict.update({'Ammount': ""})
                    elif i == 2:#Element date executed
                        if str(z) != "None":
                            elementDict.update({'DateExecuted': str(z)})
                        else:
                            elementDict.update({'DateExecuted': ""})
                    elif i == 3:#Element ammount executed
                        if str(z) != "None":
                            elementDict.update({'AmmountExecuted': str(z)})
                        else:
                            elementDict.update({'AmmountExecuted': ""})
                    elif i == 4:#Element date to execute
                        if str(z) != "None":
                            elementDict.update({'DateToExecute': str(z)})
                        else:
                            elementDict.update({'DateToExecute': ""})

                    i += 1
                    if i > 4:
                        j += 1
                        print(elementDict)
                        if str(elementDict.get('Name')) != "":
                            elementsDict.update({elementJobName + "__" + str(j) + "__" + str(elementDict.get('Name')): elementDict})
                            elementsList.append(elementDict)
                        i = 0
                        elementDict = {}

            print(elementsDict)

        print("End of MySQL pull")
        print(elementsDict)
        print(elementsList)

        #Reorder all by all Dates
        TimeOrder = {} #This will be dictionary that contains all elements from jobs, date as key, value is dictionary with keys as names of element and values as ammounts to execute
        TimeOrderNameList = []
        for x in elementsList:
            print(x)
            date = x.get('DateToExecute')
            if date == "":
                temp = TimeOrder.get("NotAsigned")
                if type(temp) == type([]):
                    temp.append(x)
                else:
                    temp = [x]
                TimeOrder.update({"NotAsigned": temp})
            else:
                temp = TimeOrder.get(x.get("DateToExecute"))
                if type(temp) == type([]):
                    temp.append(x)
                else:
                    temp = [x]
                TimeOrder.update({x.get("DateToExecute"): temp})
                TimeOrderNameList.append(x.get("DateToExecute"))


        for item in TimeSummary_entry_production_job_leftouts_table.get_children():
            TimeSummary_entry_production_job_leftouts_table.delete(item)
        Summary = ""
        display = ()
        i = 1
        if type(TimeOrder.get("NotAsigned")) != type(None):
            display += (str(len(TimeOrder.get("NotAsigned"))),)
            TimeSummary_entry_production_job_leftouts_table.insert(parent='', index=int(i), iid=int(i), values=(display))
            i += 1
            for x in TimeOrder.get("NotAsigned"):
                display = (str(x),)
                TimeSummary_entry_production_job_leftouts_table.insert(parent='', index=int(i), iid=int(i), values=(display))
                i += 1


        print("TimeOrder:")
        print(TimeOrder)
        print("TimeOrderNameList:")
        print(TimeOrderNameList)
        #TimeSummary_entry_element_table.insert(parent='', index=int(1), iid=int(1), values=(str(""), GUI_TimePlan_GetTimeString(0), str(x)))
        #DatesToDisplay = DatesToDisplay
        i = 1
        #TimeOrderPipePortSummaryPerDate
        #TODO
        #First to order by element/bat
        #Order all pipes and ports in number of prts needed to have in given day
        #First steps for element/bat
        TimeOrderPipePortSummaryPerDate = {}
        for x in TimeOrder:
            temp = []
            temp_element_store = {}
            temp_element_ammount = 0
            temp = TimeOrder.get(x)
            for y in temp:
                temp_element = y.get("Name")
                temp_element_ammount = (temp_element_store.get(temp_element))
                if type(temp_element_ammount) == type(None):
                    temp_element_ammount = 0
                else:
                    temp_element_ammount = int(temp_element_ammount)
                temp_element_ammount = int(temp_element_ammount) + int(y.get("Ammount"))
                temp_element_store.update({temp_element: temp_element_ammount})
            TimeOrderPipePortSummaryPerDate.update({x: temp_element_store})
        print("TimeOrderPipePortSummaryPerDate")
        print(TimeOrderPipePortSummaryPerDate)
        #rework all elements/bats for pipe and ports
        TimeOrderPipePortSummaryPerDate_Final = {} #This will be dictionary that contains all pipes and ports per date,
        # date as key, value is dictionary with keys as names of pipes and ports and values as ammounts to execute
        DB_data = DB_Select_General(db, "Element", 'ElementID', 'Name', 'Description', 'PipeName',
                                    'PortID_1', 'PortID_2', 'PortID_3', 'PortID_4', 'PortID_5',
                                    'PortID_6', 'PortID_7', 'PortID_8', 'PortID_10', 'PortID_11',
                                    'PortID_12', 'PortID_13', 'PortID_14', 'PortID_15', 'PortID_16',
                                    'PortID_17', 'PortID_18', 'PortID_19', 'PortID_20')
        for date in TimeOrderPipePortSummaryPerDate:
            TimeOrderPipePortSummaryPerDate_FinalPerDay = {}
            for element_in_date in TimeOrderPipePortSummaryPerDate[date]:
                #find element in DB response
                for DB_element in DB_data:
                    print(DB_element)
                    if DB_element[1] == element_in_date:
                        break
                if TimeOrderPipePortSummaryPerDate_FinalPerDay.get("Rura " + DB_element[3]) == None:
                    TimeOrderPipePortSummaryPerDate_FinalPerDay["Rura " + DB_element[3]] = TimeOrderPipePortSummaryPerDate[date][element_in_date]
                else:
                    TimeOrderPipePortSummaryPerDate_FinalPerDay["Rura " + DB_element[3]] = TimeOrderPipePortSummaryPerDate_FinalPerDay.get("Rura " + DB_element[3]) + TimeOrderPipePortSummaryPerDate[date][element_in_date]

                for port_number in range(4, len(DB_element)):
                    if DB_element[port_number] != None:
                        if TimeOrderPipePortSummaryPerDate_FinalPerDay.get("Mufa " + DB_element[port_number]) == None:
                            TimeOrderPipePortSummaryPerDate_FinalPerDay["Mufa " + DB_element[port_number]] = TimeOrderPipePortSummaryPerDate[date][element_in_date]
                        else:
                            TimeOrderPipePortSummaryPerDate_FinalPerDay["Mufa " + DB_element[port_number]] = TimeOrderPipePortSummaryPerDate_FinalPerDay.get("Mufa " + DB_element[port_number]) + TimeOrderPipePortSummaryPerDate[date][element_in_date]

            TimeOrderPipePortSummaryPerDate_Final[date] = TimeOrderPipePortSummaryPerDate_FinalPerDay

        #First line as summary
        for item in TimeSummary_entry_element_table_summary.get_children():
            TimeSummary_entry_element_table_summary.delete(item)
        for j in range(1):
            display = ()
            for x in DatesToDisplay:
                print(x)
                record_txt = ""
                found = False
                for y in TimeOrderPipePortSummaryPerDate_Final:#TimeOrderPipePortSummaryPerDate:
                    pos = y.find(x)
                    if pos > -1:
                        found = True
                        records = TimeOrderPipePortSummaryPerDate_Final.get(y)#TimeOrderPipePortSummaryPerDate.get(y)
                        record_txt = ""
                        if len(records) > j:
                            for z in records:
                                record_txt = record_txt + str(z) + ": " + str(records.get(z)) + ";\n"
                            display = display + (record_txt,)
                        else:
                            display = display + ("",)
                        break
                if not found:
                    display = display + ("",)
            TimeSummary_entry_element_table_summary.insert(parent='', index=int(j), iid=int(j), values=(display))

        TimeOrderTreview = {}
        display = ()
        found = False
        ammount = 0
        found = False
        for item in TimeSummary_entry_element_table.get_children():
            TimeSummary_entry_element_table.delete(item)
        for i in TimeOrder:
            if len(TimeOrder.get(i)) > ammount and i != "NotAsigned":
                ammount = len(TimeOrder.get(i))
        for j in range(0, ammount+1):
            display = ()
            for x in DatesToDisplay:
                print(x)
                record_txt = ""
                found = False
                for y in TimeOrderNameList:
                    pos = y.find(x)
                    if pos > -1:
                        found = True
                        records = TimeOrder.get(y)
                        record_txt = ""
                        if len(records) > j:
                            z = records[j]
                            record_jobsname = z.get('JobsName')
                            record_name = z.get('Name')
                            record_ammount = z.get('Ammount')
                            record_ammountexe = z.get('AmmountExecuted')
                            record_date = z.get('DateToExecute')
                            record_dateexe = z.get('DateExecuted')
                            temp = str(record_jobsname)+ " -> " + str(record_name) + ":\n" + str(record_ammount) \
                                   + " /" + str(record_ammountexe) + "; " + str(record_date)
                            record_txt = record_txt + temp
                            display = display + (temp,)
                        else:
                            display = display + ("",)
                        break
                if not found:
                    display = display + ("",)
            TimeSummary_entry_element_table.insert(parent='', index=int(j), iid=int(j), values=(display))
        found = True
        print(TimeOrderTreview)
        print(DatesToDisplay)
        GUI_Summary_save_to_txt(TimeOrderPipePortSummaryPerDate_Final, TimeOrderTreview, DatesToDisplay)

    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break

def GUI_TimeSummary_DatePlus():
    GUI_trace_function("GUI_TimeSummary_DatePlus")
    global DateShift
    global DatesToDisplay
    DateShift = DateShift + 1
    DatesToDisplay = [GUI_TimePlan_GetTimeString(-1 + DateShift),
                      GUI_TimePlan_GetTimeString(0 + DateShift),
                      GUI_TimePlan_GetTimeString(1 + DateShift),
                      GUI_TimePlan_GetTimeString(2 + DateShift),
                      GUI_TimePlan_GetTimeString(3 + DateShift),
                      GUI_TimePlan_GetTimeString(4 + DateShift),
                      GUI_TimePlan_GetTimeString(5 + DateShift)]
    TimeSummary_entry_element_table.heading(1, text=DatesToDisplay[
        0])  # language_DataTable.get("Monday").get(language_Select))
    TimeSummary_entry_element_table.heading(2, text=DatesToDisplay[
        1])  # language_DataTable.get("Tuesday").get(language_Select))
    TimeSummary_entry_element_table.heading(3, text=DatesToDisplay[
        2])  # language_DataTable.get("Wednesday").get(language_Select))
    TimeSummary_entry_element_table.heading(4, text=DatesToDisplay[
        3])  # language_DataTable.get("Thursday").get(language_Select))
    TimeSummary_entry_element_table.heading(5, text=DatesToDisplay[
        4])  # language_DataTable.get("Friday").get(language_Select))
    TimeSummary_entry_element_table.heading(6, text=DatesToDisplay[
        5])  # language_DataTable.get("Saturday").get(language_Select))
    TimeSummary_entry_element_table.heading(7, text=DatesToDisplay[
        6])  # language_DataTable.get("Sunday").get(language_Select))
    GUI_TimePlan_Update()

def GUI_TimeSummary_DateMinus():
    GUI_trace_function("GUI_TimeSummary_DateMinus")
    global DateShift
    global DatesToDisplay
    DateShift = DateShift - 1
    DatesToDisplay = [GUI_TimePlan_GetTimeString(-1 + DateShift),
                      GUI_TimePlan_GetTimeString(0 + DateShift),
                      GUI_TimePlan_GetTimeString(1 + DateShift),
                      GUI_TimePlan_GetTimeString(2 + DateShift),
                      GUI_TimePlan_GetTimeString(3 + DateShift),
                      GUI_TimePlan_GetTimeString(4 + DateShift),
                      GUI_TimePlan_GetTimeString(5 + DateShift)]
    TimeSummary_entry_element_table.heading(1, text=DatesToDisplay[
        0])  # language_DataTable.get("Monday").get(language_Select))
    TimeSummary_entry_element_table.heading(2, text=DatesToDisplay[
        1])  # language_DataTable.get("Tuesday").get(language_Select))
    TimeSummary_entry_element_table.heading(3, text=DatesToDisplay[
        2])  # language_DataTable.get("Wednesday").get(language_Select))
    TimeSummary_entry_element_table.heading(4, text=DatesToDisplay[
        3])  # language_DataTable.get("Thursday").get(language_Select))
    TimeSummary_entry_element_table.heading(5, text=DatesToDisplay[
        4])  # language_DataTable.get("Friday").get(language_Select))
    TimeSummary_entry_element_table.heading(6, text=DatesToDisplay[
        5])  # language_DataTable.get("Saturday").get(language_Select))
    TimeSummary_entry_element_table.heading(7, text=DatesToDisplay[
        6])  # language_DataTable.get("Sunday").get(language_Select))
    GUI_TimePlan_Update()

def GUI_Job_search():
    GUI_trace_function('GUI_Job_search')
    # ToDo
    # need to create popup window with table
    # Read SQL for already available Jobs in database
    # Make available to select data, read one or delete them
    GUI_Job_TopLvl = tk.Toplevel()
    GUI_Job_TopLvl.title('GUI_Job_search')
    Job_TopLvl_treeview_pipes_in_sql_table = ttk.Treeview(GUI_Job_TopLvl, columns=(1, 2, 3), show='headings', height=8)
    Job_TopLvl_button_production_Job_select = tk.Button(GUI_Job_TopLvl,
                                                          text=language_DataTable.get("Select").get(language_Select),
                                                          background="green", width=10,
    command=lambda: GUI_Job_MySQL_search_return_entry(GUI_Job_TopLvl, Job_TopLvl_treeview_pipes_in_sql_table,
    Job_entry_production_job_name_text, Job_entry_production_job_description, Job_entry_element_table))
    Job_TopLvl_button_production_Job_delete = tk.Button(GUI_Job_TopLvl,
                                                          text=language_DataTable.get("DatabaseDelete").get(language_Select),
                                                          background="red", width=15,
    command=lambda: GUI_MySQL_delete_from_database(GUI_Job_TopLvl, Job_TopLvl_treeview_pipes_in_sql_table, db, "job"))

    Job_TopLvl_treeview_pipes_in_sql_table.heading(1, text=language_DataTable.get("Production Job name").get(language_Select))
    Job_TopLvl_treeview_pipes_in_sql_table.heading(2, text=language_DataTable.get("Production Job description").get(language_Select))
    Job_TopLvl_treeview_pipes_in_sql_table.heading(3, text=language_DataTable.get("Elements").get(language_Select))

    Job_TopLvl_treeview_pipes_in_sql_table.grid(row=0, column=0, columnspan=2)
    Job_TopLvl_button_production_Job_select.grid(row=1, column=0)
    Job_TopLvl_button_production_Job_delete.grid(row=1, column=1)

    #for debug
    #ToDo
    #Take data from SQl
    #Add here data from SQL
    DB_data = DB_Select_General(db, "Job", 'JobID', 'Name', 'Description'
        , 'PipelineElementID_1', 'Ammount_1', 'PipelineElementID_2', 'Ammount_2', 'PipelineElementID_3', 'Ammount_3'
        , 'PipelineElementID_4', 'Ammount_4', 'PipelineElementID_5', 'Ammount_5', 'PipelineElementID_6', 'Ammount_6'
        , 'PipelineElementID_7', 'Ammount_7', 'PipelineElementID_8', 'Ammount_8', 'PipelineElementID_9', 'Ammount_9'
        , 'PipelineElementID_10', 'Ammount_10', 'PipelineElementID_11', 'Ammount_11', 'PipelineElementID_12', 'Ammount_12'
        , 'PipelineElementID_13', 'Ammount_13', 'PipelineElementID_14', 'Ammount_14', 'PipelineElementID_15', 'Ammount_15'
        , 'PipelineElementID_16', 'Ammount_16', 'PipelineElementID_17', 'Ammount_17', 'PipelineElementID_18', 'Ammount_18'
        , 'PipelineElementID_19', 'Ammount_19', 'PipelineElementID_20', 'Ammount_20')

    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            elements_description = str(x[5]) + ", " + str(x[6]) + ", " + str(x[7]) + ", " + str(x[8]) + ", " \
                                   + str(x[9]) + ", " + str(x[10]) + ", " + str(x[11]) + ", " + str(x[12])
            Job_TopLvl_treeview_pipes_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                          values=(str(x[1]), str(x[2]), elements_description))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break

    DB_CursorPrint(DB_data)

def GUI_Job_MySQL_search_return_entry(toplvl, treeview, entry_name, entry_description, treeviewsub):
    GUI_trace_function('GUI_MySQL_search_return')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        entry_name.set(treeview_name[0])
        entry_description.delete('1.0', 'end')
        entry_description.insert('1.0', treeview_name[1])
        for item in treeviewsub.get_children():
            treeviewsub.delete(item)
        DB_data = DB_Select_General(db, "Job", 'JobID', 'Name',
        'PipelineElementID_1', 'Ammount_1', 'DateToExecute_1', 'PipelineElementID_2', 'Ammount_2', 'DateToExecute_2', 'PipelineElementID_3', 'Ammount_3', 'DateToExecute_3',
        'PipelineElementID_4', 'Ammount_4', 'DateToExecute_4', 'PipelineElementID_5', 'Ammount_5', 'DateToExecute_5', 'PipelineElementID_6', 'Ammount_6', 'DateToExecute_6',
        'PipelineElementID_7', 'Ammount_7', 'DateToExecute_7', 'PipelineElementID_8', 'Ammount_8', 'DateToExecute_8', 'PipelineElementID_9', 'Ammount_9', 'DateToExecute_9',
        'PipelineElementID_10', 'Ammount_10', 'DateToExecute_10', 'PipelineElementID_11', 'Ammount_11', 'DateToExecute_11', 'PipelineElementID_12', 'Ammount_12', 'DateToExecute_12',
        'PipelineElementID_13', 'Ammount_13', 'DateToExecute_13', 'PipelineElementID_14', 'Ammount_14', 'DateToExecute_14', 'PipelineElementID_15', 'Ammount_15', 'DateToExecute_15',
        'PipelineElementID_16', 'Ammount_16', 'DateToExecute_16', 'PipelineElementID_17', 'Ammount_17', 'DateToExecute_17', 'PipelineElementID_18', 'Ammount_18', 'DateToExecute_18',
        'PipelineElementID_19', 'Ammount_19', 'DateToExecute_19', 'PipelineElementID_20', 'Ammount_20', 'DateToExecute_20')
        datastart = 2
        dataspread = 3
        if not isinstance(DB_data, set):
            for x in DB_data:
                if str(x[1]) == treeview_name[0]:
                    print(x)
                    for j in range(20):
                        if x[datastart] != None:
                            datavalues = ()
                            for i in range(dataspread):
                                datavalues = datavalues + (x[datastart + i],)
                            treeviewsub.insert(parent='', index=j, iid=j, values=datavalues)
                            datastart = datastart + dataspread
        else:
            print('Check MySQL not correct')
            for x in DB_data:
                GUI_trace_function(str(x), 1)
                break

        break
    toplvl.destroy()

def GUI_Job_save():
    GUI_trace_function('GUI_Job_save')
    # ToDo
    # need to save defined data as Job
    # check if similar Job is already in place, if yes popup user with difference view and if accept
    data = GUI_treeview_return(Job_entry_element_table)

    print(' Job name: ' + str(Job_entry_production_job_name_text.get())
    + '\n Job elements: ' + str(data)
    + '\n Job description:' + str(Job_entry_production_job_description.get(1.0, "end-1c")))
    # Name, Description, PipelineElementID_1, Ammount_1...

    i = 0
    data_to_DB = []
    data_to_DB.append(str(Job_entry_production_job_name_text.get()))
    data_to_DB.append(str(Job_entry_production_job_description.get(1.0, "end-1c")))
    for item in Job_entry_element_table.get_children():
        treeview_items = Job_entry_element_table.item(item)
        treeview_name = treeview_items.get('values')
        data_to_DB.append(treeview_name[0])
        data_to_DB.append(treeview_name[1])
        data_to_DB.append(treeview_name[2])
    print(data_to_DB)
    'Need to check if record is in database. '
    'If so make sure that popup will show up. '
    'and acknowledged save to DB as UPDATE'
    response = DB_ExistsRow(db, "job", str(Job_entry_production_job_name_text.get()))
    if response[0][0] > 0:
        DB_Update(db, "job", str(Job_entry_production_job_name_text.get()), data_to_DB)
    else:
        DB_Insert(db, "job", data_to_DB)

def GUI_Element_search():
    GUI_trace_function('GUI_Element_search')
    # ToDo
    # need to create popup window with table
    # Read SQL for already available elements in database
    # Make available to select data, read one or delete them
    GUI_Element_TopLvl = tk.Toplevel()
    GUI_Element_TopLvl.title('GUI_Element_search')
    Element_TopLvl_treeview_pipes_in_sql_table = ttk.Treeview(GUI_Element_TopLvl, columns=(1, 2, 3, 4, 5), show='headings',
                                                           height=8)
    Element_TopLvl_button_production_Job_select = tk.Button(GUI_Element_TopLvl,
                                                             text=language_DataTable.get("Select").get(language_Select),
                                                             background="green", width=10,
    command=lambda: GUI_Element_MySQL_search_return_entry(GUI_Element_TopLvl, Element_TopLvl_treeview_pipes_in_sql_table,
    Element_entry_element_name_text, Element_entry_element_description, Element_entry_pipe_name_text,
    Element_entry_pipe_length_text, Element_entry_port_table))
    Element_TopLvl_button_production_Job_delete = tk.Button(GUI_Element_TopLvl,
                                                             text=language_DataTable.get("DatabaseDelete").get(language_Select),
                                                             background="red", width=15,
    command=lambda: GUI_MySQL_delete_from_database(GUI_Element_TopLvl, Element_TopLvl_treeview_pipes_in_sql_table, db, "element"))

    Element_TopLvl_treeview_pipes_in_sql_table.heading(1, text=language_DataTable.get("Element name").get(language_Select))
    Element_TopLvl_treeview_pipes_in_sql_table.heading(2, text=language_DataTable.get("Element description").get(language_Select))
    Element_TopLvl_treeview_pipes_in_sql_table.heading(3, text=language_DataTable.get("Pipe name").get(language_Select))
    Element_TopLvl_treeview_pipes_in_sql_table.heading(4, text=language_DataTable.get("Pipe length").get(language_Select))
    Element_TopLvl_treeview_pipes_in_sql_table.heading(5, text=language_DataTable.get("Ports").get(language_Select))

    Element_TopLvl_treeview_pipes_in_sql_table.grid(row=0, column=0, columnspan=2)
    Element_TopLvl_button_production_Job_select.grid(row=1, column=0)
    Element_TopLvl_button_production_Job_delete.grid(row=1, column=1)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "element", 'ElementID', 'Name', 'Description', 'PipeName', 'PipeLength',
                                'PortID_1', 'Length_1', 'Angle_1', 'PortID_2', 'Length_2', 'Angle_2'
                                ,'PortID_3', 'Length_3', 'Angle_3','PortID_4', 'Length_4', 'Angle_4'
                                ,'PortID_5', 'Length_5', 'Angle_5','PortID_6', 'Length_6', 'Angle_6'
                                ,'PortID_7', 'Length_7', 'Angle_7','PortID_8', 'Length_8', 'Angle_8'
                                ,'PortID_9', 'Length_9', 'Angle_9','PortID_10', 'Length_10', 'Angle_10'
                                ,'PortID_11', 'Length_11', 'Angle_11','PortID_12', 'Length_12', 'Angle_12'
                                ,'PortID_13', 'Length_13', 'Angle_13','PortID_14', 'Length_14', 'Angle_14'
                                ,'PortID_15', 'Length_15', 'Angle_15','PortID_16', 'Length_16', 'Angle_16'
                                ,'PortID_17', 'Length_17', 'Angle_17','PortID_18', 'Length_18', 'Angle_18'
                                ,'PortID_19', 'Length_19', 'Angle_19','PortID_20', 'Length_20', 'Angle_20')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            ports_description = str(x[5]) + str(x[6]) + str(x[7]) + str(x[8]) + str(x[9]) + str(x[10])+ str(x[11])+ str(x[12])
            Element_TopLvl_treeview_pipes_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                       values=(str(x[1]), str(x[2]), str(x[3]), str(x[4]), ports_description))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Element_MySQL_search_return_entry(toplvl, treeview, entry_name, entry_description, entry_diameter, entry_length, treeviewsub):
    GUI_trace_function('GUI_MySQL_search_return')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        entry_name.set(treeview_name[0])
        entry_description.delete('1.0', 'end')
        entry_description.insert('1.0', treeview_name[1])
        entry_diameter.set(treeview_name[2])
        entry_length.set(treeview_name[3])
        for item in treeviewsub.get_children():
            treeviewsub.delete(item)
        DB_data = DB_Select_General(db, "element", 'ElementID', 'Name',
                                    'PortID_1', 'Length_1', 'Angle_1', 'PortID_2', 'Length_2', 'Angle_2',
                                    'PortID_3', 'Length_3', 'Angle_3', 'PortID_4', 'Length_4', 'Angle_4',
                                    'PortID_5', 'Length_5', 'Angle_5', 'PortID_6', 'Length_6', 'Angle_6',
                                    'PortID_6', 'Length_6', 'Angle_6', 'PortID_7', 'Length_7', 'Angle_7',
                                    'PortID_8', 'Length_8', 'Angle_8', 'PortID_9', 'Length_9', 'Angle_9',
                                    'PortID_10', 'Length_10', 'Angle_10', 'PortID_11', 'Length_11', 'Angle_11',
                                    'PortID_12', 'Length_12', 'Angle_12', 'PortID_13', 'Length_13', 'Angle_13',
                                    'PortID_14', 'Length_14', 'Angle_14', 'PortID_15', 'Length_15', 'Angle_15',
                                    'PortID_16', 'Length_16', 'Angle_16', 'PortID_17', 'Length_17', 'Angle_17',
                                    'PortID_18', 'Length_18', 'Angle_18', 'PortID_19', 'Length_19', 'Angle_19',
                                    'PortID_20', 'Length_20', 'Angle_20')
        datastart = 2
        dataspread = 3
        if not isinstance(DB_data, set):
            for x in DB_data:
                if str(x[1]) == treeview_name[0]:
                    print(x)
                    for j in range(20):
                        if x[datastart] != None:
                            datavalues = ()
                            for i in range(dataspread):
                                datavalues = datavalues + (x[datastart + i],)
                            treeviewsub.insert(parent='', index=j, iid=j, values=datavalues)
                            datastart = datastart + dataspread
        else:
            print('Check MySQL not correct')
            for x in DB_data:
                GUI_trace_function(str(x), 1)
                break

        break
    toplvl.destroy()

def Element_Pipe_search():
    GUI_trace_function('Element_Pipe_search')
    # ToDo
    # need to create popup window with table
    # Read SQL for already available pipes in database
    # Make available to select data, read one or delete them
    GUI_Pipe_TopLvl = tk.Toplevel()
    GUI_Pipe_TopLvl.title('GUI_Pipe_search')
    Pipe_TopLvl_treeview_pipes_in_sql_table = ttk.Treeview(GUI_Pipe_TopLvl, columns=(1, 2, 3, 4, 5), show='headings',
                                                              height=8)
    Pipe_TopLvl_button_production_Job_select = tk.Button(GUI_Pipe_TopLvl,
                                                          text=language_DataTable.get("Select").get(language_Select),
                                                          background="green",
    width=10, command=lambda: GUI_Element_MySQL_pipe_search_return_entry(GUI_Pipe_TopLvl, Pipe_TopLvl_treeview_pipes_in_sql_table,
    Element_entry_pipe_name_text, Element_entry_pipe_length_text))
    Pipe_TopLvl_button_production_Job_delete = tk.Button(GUI_Pipe_TopLvl,
                                                          text=language_DataTable.get("DatabaseDelete").get(language_Select),
                                                          background="red", width=15,
    command=lambda: GUI_MySQL_delete_from_database(GUI_Pipe_TopLvl, Pipe_TopLvl_treeview_pipes_in_sql_table, db, "pipe"))

    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(1, text=language_DataTable.get("Pipe name").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(2, text=language_DataTable.get("Pipe description").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(3, text=language_DataTable.get("Pipe diameter").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(4, text=language_DataTable.get("Pipe thickness").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(5, text=language_DataTable.get("Pipe length").get(language_Select))

    Pipe_TopLvl_treeview_pipes_in_sql_table.grid(row=0, column=0, columnspan=2)
    Pipe_TopLvl_button_production_Job_select.grid(row=1, column=0)
    Pipe_TopLvl_button_production_Job_delete.grid(row=1, column=1)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "pipe", 'PipeID', 'Name', 'Description', 'Diameter', 'Thickness', 'Length')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            Pipe_TopLvl_treeview_pipes_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                       values=(str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5])))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Element_save():
    GUI_trace_function('GUI_Element_save')
    # ToDo
    # need to save defined data as Job
    # check if similar element is already in place, if yes popup user with difference view and if accept
    data = GUI_treeview_return(Element_entry_port_table)

    print(' Element name: ' + str(Element_entry_element_name.get()) + '\n Element diam: ' + str(Element_entry_pipe_name_text.get())
    + '\n Element ports: ' + str(data)
    + '\n Element description:' + str(Element_entry_element_description.get(1.0, "end-1c")))

    i = 0
    data_to_DB = []
    data_to_DB.append(str(Element_entry_element_name.get()))
    data_to_DB.append(str(Element_entry_element_description.get(1.0, "end-1c")))
    data_to_DB.append(str(Element_entry_pipe_name_text.get()))
    data_to_DB.append(str(Element_entry_pipe_length_text.get()))
    for item in Element_entry_port_table.get_children():
        treeview_items = Element_entry_port_table.item(item)
        treeview_name = treeview_items.get('values')
        data_to_DB.append(treeview_name[0])
        data_to_DB.append((treeview_name[1]))
        data_to_DB.append((treeview_name[2]))
        data_to_DB.append("360")

    'Need to check if record is in database. '
    'If so make sure that popup will show up. '
    'and acknowledged save to DB as UPDATE'
    response = DB_ExistsRow(db, "element", str(Element_entry_element_name.get()))
    if response[0][0] > 0:
        DB_Update(db, "element", str(Element_entry_element_name.get()), data_to_DB)
    else:
        DB_Insert(db, "element", data_to_DB)

def GUI_Pipe_search():
    GUI_trace_function('GUI_Pipe_search')
    # ToDo
    # need to create popup window with table
    # Read SQL for already available pipes in database
    # Make available to select data, read one or delete them
    GUI_Pipe_TopLvl = tk.Toplevel()
    GUI_Pipe_TopLvl.title('GUI_Pipe_search')
    Pipe_TopLvl_treeview_pipes_in_sql_table = ttk.Treeview(GUI_Pipe_TopLvl, columns=(1, 2, 3, 4, 5), show='headings',
                                                              height=8)
    Pipe_TopLvl_button_production_Job_select = tk.Button(GUI_Pipe_TopLvl,
                                                          text=language_DataTable.get("Select").get(language_Select),
                                                          background="green",
    width=10, command=lambda: GUI_Pipe_MySQL_search_return_entry(GUI_Pipe_TopLvl, Pipe_TopLvl_treeview_pipes_in_sql_table,
    Pipe_entry_pipe_name_text, Pipe_entry_pipe_description, Pipe_entry_pipe_diameter_text, Pipe_entry_pipe_thickness_text, Pipe_entry_pipe_length_text))
    Pipe_TopLvl_button_production_Job_delete = tk.Button(GUI_Pipe_TopLvl,
                                                          text=language_DataTable.get("DatabaseDelete").get(language_Select),
                                                          background="red", width=15,
    command=lambda: GUI_MySQL_delete_from_database(GUI_Pipe_TopLvl, Pipe_TopLvl_treeview_pipes_in_sql_table, db, "pipe"))

    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(1, text=language_DataTable.get("Pipe name").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(2, text=language_DataTable.get("Pipe description").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(3, text=language_DataTable.get("Pipe diameter").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(4, text=language_DataTable.get("Pipe thickness").get(language_Select))
    Pipe_TopLvl_treeview_pipes_in_sql_table.heading(5, text=language_DataTable.get("Pipe length").get(language_Select))

    Pipe_TopLvl_treeview_pipes_in_sql_table.grid(row=0, column=0, columnspan=2)
    Pipe_TopLvl_button_production_Job_select.grid(row=1, column=0)
    Pipe_TopLvl_button_production_Job_delete.grid(row=1, column=1)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "pipe", 'PipeID', 'Name', 'Description', 'Diameter', 'Thickness', 'Length')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            Pipe_TopLvl_treeview_pipes_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                       values=(str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5])))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Pipe_MySQL_search_return_entry(toplvl, treeview, entry_name, entry_description, entry_diameter, entry_thickness, entry_length):
    GUI_trace_function('GUI_Pipe_MySQL_search_return_entry')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        entry_name.set(treeview_name[0])
        entry_description.delete('1.0', 'end')
        entry_description.insert('1.0', treeview_name[1])
        entry_diameter.set(treeview_name[2])
        entry_thickness.set(treeview_name[3])
        entry_length.set(treeview_name[4])
        break
    toplvl.destroy()

def GUI_Element_MySQL_pipe_search_return_entry(toplvl, treeview, entry_name, entry_length):
    GUI_trace_function('GUI_Element_MySQL_pipe_search_return_entry')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        entry_name.set(treeview_name[0])
        entry_length.set(treeview_name[4])
        break
    toplvl.destroy()

def GUI_Pipe_save():
    GUI_trace_function('GUI_Pipe_save')
    # ToDo
    # need to save defined data as Job
    # check if similar pipe is already in place, if yes popup user with difference view and if accept
    print(' Pipe name: ' + str(Pipe_entry_pipe_name_text.get()) + '\n Pipe diam: ' + str(Pipe_entry_pipe_diameter_text.get())
    + '\n Pipe thickness: ' + str(Pipe_entry_pipe_thickness_text.get()) + '\n Pipe length:' + str(Pipe_entry_pipe_length_text.get())
    + '\n Pipe description:' + str(Pipe_entry_pipe_description.get(1.0, "end-1c")))
    # Name, Description, Diameter, Thickness, Length, PortEndTypePipeSide, PortEndTypeSprinkle

    i = 0
    data_to_DB = []
    data_to_DB.append(str(Pipe_entry_pipe_name_text.get()))
    data_to_DB.append(str(Pipe_entry_pipe_description.get(1.0, "end-1c")))
    data_to_DB.append(str(Pipe_entry_pipe_diameter_text.get()))
    data_to_DB.append(str(Pipe_entry_pipe_thickness_text.get()))
    data_to_DB.append(str(Pipe_entry_pipe_length_text.get()))

    'Need to check if record is in database. '
    'If so make sure that popup will show up. '
    'and acknowledged save to DB as UPDATE'
    response = DB_ExistsRow(db, "pipe", str(Pipe_entry_pipe_name_text.get()))
    if response[0][0] > 0:
        DB_Update(db, "pipe", str(Pipe_entry_pipe_name_text.get()), data_to_DB)
    else:
        DB_Insert(db, "pipe", data_to_DB)

def GUI_Port_search():
    GUI_trace_function('GUI_Port_search')
    # ToDo
    # need to create popup window with table
    # Read SQL for already available ports in database
    # Make available to select data, read one or delete them
    GUI_Port_TopLvl = tk.Toplevel()
    GUI_Port_TopLvl.title('GUI_Port_search')
    Port_TopLvl_treeview_ports_in_sql_table = ttk.Treeview(GUI_Port_TopLvl, columns=(1, 2, 3, 4, 5), show='headings',
                                                           height=8)
    Port_TopLvl_button_port_select = tk.Button(GUI_Port_TopLvl, text=language_DataTable.get("Select").get(language_Select),
                                               background="green",width=10,
    command=lambda: GUI_Port_MySQL_search_return_entry(GUI_Port_TopLvl, Port_TopLvl_treeview_ports_in_sql_table
    , Port_entry_port_name_text, Port_entry_port_description, Port_entry_port_diameter_text, Port_entry_port_thickness_text, Port_entry_port_length_text))
    Port_TopLvl_button_port_delete = tk.Button(GUI_Port_TopLvl,
                                               text=language_DataTable.get("DatabaseDelete").get(language_Select),
                                               background="red", width=15,
    command=lambda: GUI_MySQL_delete_from_database(GUI_Port_TopLvl, Port_TopLvl_treeview_ports_in_sql_table, db, "port"))

    Port_TopLvl_treeview_ports_in_sql_table.heading(1, text=language_DataTable.get("Port name").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(2, text=language_DataTable.get("Port description").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(3, text=language_DataTable.get("Port diameter").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(4, text=language_DataTable.get("Port thickness").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(5, text=language_DataTable.get("Port length").get(language_Select))

    Port_TopLvl_treeview_ports_in_sql_table.grid(row=0, column=0, columnspan=2)
    Port_TopLvl_button_port_select.grid(row=1, column=0)
    Port_TopLvl_button_port_delete.grid(row=1, column=1)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "port", 'PortID', 'Name', 'Description', 'Diameter', 'Thickness', 'Length')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            Port_TopLvl_treeview_ports_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                          values=(str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5])))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Port_MySQL_search_return_entry(toplvl, treeview, entry_name, entry_description, entry_diameter, entry_thickness, entry_length):
    GUI_trace_function('GUI_Port_MySQL_search_return_entry')
    selected_items = treeview.selection()
    for selected_item in selected_items:
        treeview_items = treeview.item(selected_item)
        treeview_name = treeview_items.get('values')
        entry_name.set(treeview_name[0])
        entry_description.delete('1.0', 'end')
        entry_description.insert('1.0', treeview_name[1])
        entry_diameter.set(treeview_name[2])
        entry_thickness.set(treeview_name[3])
        entry_length.set(treeview_name[4])
        break
    toplvl.destroy()

def GUI_Port_save():
    GUI_trace_function('GUI_Port_save')
    # ToDo
    # need to save defined data as Job
    # check if similar port is already in place, if yes popup user with difference view and if accept
    print(' Port name: ' + str(Port_entry_port_name_text.get()) + '\n Port diam: ' + str(Port_entry_port_diameter_text.get())
    + '\n Port thickness: ' + str(Port_entry_port_thickness_text.get()) + '\n Port length:' + str(Port_entry_port_length_text.get())
    + '\n Port description:' + str(Port_entry_port_description.get(1.0, "end-1c")))
    #Name, Description, Diameter, Thickness, Length, PortEndTypePipeSide, PortEndTypeSprinkle

    i = 0
    data_to_DB = []
    data_to_DB.append(str(Port_entry_port_name_text.get()))
    data_to_DB.append(str(Port_entry_port_description.get(1.0, "end-1c")))
    data_to_DB.append(str(Port_entry_port_diameter_text.get()))
    data_to_DB.append(str(Port_entry_port_thickness_text.get()))
    data_to_DB.append(str(Port_entry_port_length_text.get()))

    'Need to check if record is in database. '
    'If so make sure that popup will show up. '
    'and acknowledged save to DB as UPDATE'
    response = DB_ExistsRow(db, "port", str(Port_entry_port_name_text.get()))
    if response[0][0] > 0:
        DB_Update(db, "port", str(Port_entry_port_name_text.get()), data_to_DB)
    else:
        DB_Insert(db, "port", data_to_DB)

def GUI_Job_element_search():
    GUI_trace_function('GUI_Job_element_search')
    # ToDo
    # Add popup window with list of defined elements for selection after clicking add button

    GUI_Element_TopLvl = tk.Toplevel()
    GUI_Element_TopLvl.title('GUI_Job_element_search')
    Element_TopLvl_treeview_ports_in_sql_table = ttk.Treeview(GUI_Element_TopLvl, columns=(1, 2, 3, 4, 5), show='headings',
                                                           height=8)
    columns = ()
    columns = (*columns, 0)
    Element_TopLvl_button_port_select = tk.Button(GUI_Element_TopLvl,
                                                  text=language_DataTable.get("Select").get(language_Select),
                                                  background="green", width=10,
    command=lambda: GUI_MySQL_search_return_treeview(GUI_Element_TopLvl, Element_TopLvl_treeview_ports_in_sql_table,
                                                     Job_entry_element_table,columns, 2))

    Element_TopLvl_treeview_ports_in_sql_table.heading(1, text=language_DataTable.get("Element name").get(language_Select))
    Element_TopLvl_treeview_ports_in_sql_table.heading(2, text=language_DataTable.get("Element description").get(language_Select))
    Element_TopLvl_treeview_ports_in_sql_table.heading(3, text=language_DataTable.get("Pipe name").get(language_Select))
    Element_TopLvl_treeview_ports_in_sql_table.heading(4, text=language_DataTable.get("Pipe length").get(language_Select))
    Element_TopLvl_treeview_ports_in_sql_table.heading(5, text=language_DataTable.get("Ports").get(language_Select))

    Element_TopLvl_treeview_ports_in_sql_table.grid(row=0, column=0)
    Element_TopLvl_button_port_select.grid(row=1, column=0)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "element", 'ElementID', 'Name', 'Description', 'PipeName', 'PipeLength',
                                'PortID_1', 'Length_1', 'Angle_1', 'PortID_2', 'Length_2', 'Angle_2'
                                , 'PortID_3', 'Length_3', 'Angle_3', 'PortID_4', 'Length_4', 'Angle_4'
                                , 'PortID_5', 'Length_5', 'Angle_5', 'PortID_6', 'Length_6', 'Angle_6'
                                , 'PortID_7', 'Length_7', 'Angle_7', 'PortID_8', 'Length_8', 'Angle_8'
                                , 'PortID_9', 'Length_9', 'Angle_9', 'PortID_10', 'Length_10', 'Angle_10'
                                , 'PortID_11', 'Length_11', 'Angle_11', 'PortID_12', 'Length_12', 'Angle_12'
                                , 'PortID_13', 'Length_13', 'Angle_13', 'PortID_14', 'Length_14', 'Angle_14'
                                , 'PortID_15', 'Length_15', 'Angle_15', 'PortID_16', 'Length_16', 'Angle_16'
                                , 'PortID_17', 'Length_17', 'Angle_17', 'PortID_18', 'Length_18', 'Angle_18'
                                , 'PortID_19', 'Length_19', 'Angle_19', 'PortID_20', 'Length_20', 'Angle_20')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            ports_description = str(x[5]) + str(x[6]) + str(x[7]) + str(x[8]) + str(x[9]) + str(x[10]) + str(
                x[11]) + str(x[12])
            Element_TopLvl_treeview_ports_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                              values=(str(x[1]), str(x[2]), str(x[3]), str(x[4]),
                                                                      ports_description))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Element_port_search():
    GUI_trace_function('GUI_Element_port_search')
    # ToDo
    # Add popup window with list of defined elements for selection after clicking add button
    GUI_Port_TopLvl = tk.Toplevel()
    GUI_Port_TopLvl.title('GUI_Element_pipe_search')
    Port_TopLvl_treeview_ports_in_sql_table = ttk.Treeview(GUI_Port_TopLvl, columns=(1, 2, 3, 4), show='headings', height=8)
    columns = ()
    columns = (*columns, 0)
    Port_TopLvl_button_port_select = tk.Button(GUI_Port_TopLvl, text=language_DataTable.get("Select").get(language_Select), background="green", width=10,
    command=lambda: GUI_MySQL_search_return_treeview(GUI_Port_TopLvl, Port_TopLvl_treeview_ports_in_sql_table, Element_entry_port_table,
                                                     columns, 3))

    Port_TopLvl_treeview_ports_in_sql_table.heading(1, text=language_DataTable.get("Port name").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(2, text=language_DataTable.get("Port description").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(3, text=language_DataTable.get("Port diameter").get(language_Select))
    Port_TopLvl_treeview_ports_in_sql_table.heading(4, text=language_DataTable.get("Port thickness").get(language_Select))

    Port_TopLvl_treeview_ports_in_sql_table.grid(row=0, column=0)
    Port_TopLvl_button_port_select.grid(row=1, column=0)

    # for debug
    # ToDo
    # Take data from SQl
    # Add here data from SQL
    DB_data = DB_Select_General(db, "port", 'PortID', 'Name', 'Description', 'Diameter', 'Thickness')
    if not isinstance(DB_data, set):
        for x in DB_data:
            print(x)
            Port_TopLvl_treeview_ports_in_sql_table.insert(parent='', index=int(x[0]), iid=int(x[0]),
                                                       values=(str(x[1]), str(x[2]), str(x[3]), str(x[4])))
    else:
        print('Check MySQL not correct')
        for x in DB_data:
            GUI_trace_function(str(x), 1)
            break
    DB_CursorPrint(DB_data)

def GUI_Element_delete():
    GUI_trace_function('GUI_Element_delete')
    selected_items = Element_entry_port_table.selection()
    for selected_item in selected_items:
        Element_entry_port_table.delete(selected_item)

def GUI_treeview_amount_exchange(treview, columns, *values ):
    GUI_trace_function('GUI_Job_Element_amount_exchange')
    items = treview.selection()
    i = 0
    for value in values:
        for item in items:
            treview.set(item, column=columns[i], value=value.get())
        i += 1

def GUI_Run():
    GUI_trace_function('GUI_Run')
    GUI_MySQL_DatabaseInfo(db)
    root.mainloop()
    DB_Disconnect(db)


root = tk.Tk()

debug_log = True
debug_log_name = "debug" #+ GUI_TimePlan_GetTimeString()

#this is for selection of language
language_Select = "Polski"

#this is for selection of language
language_Storage = ["Polski", "English", "German"]

#this is for storing of names for all languages
language_DataTable = {}
language_DataTable = {
    "Pipe Production Configuration": {"Polski": "Konfiguracja produkcji rur", "English": "Pipe Production Configuration", "German": "Pipe Production Configuration"},
    "TimeSummary": {"Polski": """Podsumowanie
    czasowe""", "English": "TimeSummary", "German": "TimeSummary"},
    "Jobs": {"Polski": "Zlecenia", "English": "Jobs", "German": "Jobs"},
    "Elements": {"Polski": "Elementy/baty", "English": "Elements", "German": "Elements"},
    "Pipes": {"Polski": "Rury", "English": "Pipes", "German": "Pipes"},
    "Ports": {"Polski": "Mufy", "English": "Ports", "German": "Ports"},

    "Refreash": {"Polski": "Odswierz", "English": "Refreash", "German": "Refreash"},
    "DatePlus": {"Polski": "Dodaj dzien", "English": "Date add", "German": "Refreash"},
    "DateMinus": {"Polski": "Odejmij dzien", "English": "Date reverse", "German": "Refreash"},
    "Select": {"Polski": "Wybierz", "English": "Select", "German": "Select"},
    "Search": {"Polski": "Szukaj", "English": "Search", "German": "Search"},
    "Add": {"Polski": "Dodaj", "English": "Add", "German": "Add"},
    "Save": {"Polski": "Zapisz", "English": "Save", "German": "Save"},
    "Delete": {"Polski": "Usun", "English": "Delete", "German": "Delete"},
    "DatabaseDelete": {"Polski": "Usun z bazy danych", "English": "Delete from Database", "German": "Delete from Database"},
    "Change": {"Polski": "Zmien", "English": "Change", "German": "Change"},

    "File": {"Polski": "Plik", "English": "File", "German": "File"},
    "Database": {"Polski": "Baza danych", "English": "Database", "German": "Database"},
    "Settings": {"Polski": "Ustawienia", "English": "Settings", "German": "Settings"},
    "About": {"Polski": "O aplikacji", "English": "About", "German": "About"},
    "Help": {"Polski": "Pomoc", "English": "Help", "German": "Help"},

    "Event log": {"Polski": "Spis wydarzen aplikacji", "English": "Event log", "German": "Event log"},
    "Database name": {"Polski": "Nazwa bazy danych", "English": "Database name", "German": "Database name"},

    "Summary name": {"Polski": "Nazwa planu czasowego", "English": "Time plan name",
                            "German": "Time plan name"},
    "Leftout": {"Polski": "Nie przypisane", "English": "Leftout", "German": "Leftout"},
    "Monday": {"Polski": "Poniedzialek", "English": "Monday", "German": "Monday"},
    "Tuesday": {"Polski": "Wtorek", "English": "Tuesday", "German": "Tuesday"},
    "Wednesday": {"Polski": "Sroda", "English": "Wednesday", "German": "Wednesday"},
    "Thursday": {"Polski": "Czwartek", "English": "Thursday", "German": "Thursday"},
    "Friday": {"Polski": "Piatek", "English": "Friday", "German": "Friday"},
    "Saturday": {"Polski": "Sobota", "English": "Saturday", "German": "Saturday"},
    "Sunday": {"Polski": "Niedziela", "English": "Sunday", "German": "Sunday"},
    "Time plan description": {"Polski": "Opis planu czasowego", "English": "Time plan description",
                                   "German": "Time plan description"},
    "Time plan date to execution": {"Polski": "Data wykonania", "English": "Time plan date to execution",
                                    "German": "Time plan date to execution"},
    "Time plan machine to execution": {"Polski": "Maszyna uzyta do wykonania", "English": "Machine to execution",
                                    "German": "Machine to execution"},

    "Production Job name": {"Polski": "Nazwa zlecenia", "English": "Production Job name", "German": "Production Job name"},
    "Production Job description": {"Polski": "Opis elementu", "English": "Production Job description", "German": "Production Job description"},
    "Element count": {"Polski": "Ilosc elementow/batow", "English": "Element count", "German": "Element count"},
    "Execution date": {"Polski": "Data wykonania", "English": "Execution date", "German": "Execution date"},


    "Element name": {"Polski": "Nazwa elementu/bata", "English": "Element name", "German": "Element name"},
    "Element description": {"Polski": "Opis elementu/bata", "English": "Element description", "German": "Element description"},
    "Port used": {"Polski": "Uzywany port", "English": "Port used", "German": "Port used"},
    "Port distance": {"Polski": "Odleglosc portu", "English": "Port distance", "German": "Port distance"},
    "Port angle": {"Polski": "Kat portu", "English": "Port angle", "German": "Port angle"},


    "Pipe name": {"Polski": "Nazwa rury", "English": "Pipe name", "German": "Pipe name"},
    "Pipe diameter": {"Polski": "Srednica rury", "English": "Pipe diameter", "German": "Pipe diameter"},
    "Pipe thickness": {"Polski": "Grubosc rury", "English": "Pipe thickness", "German": "Pipe thickness"},
    "Bat length": {"Polski": "Dlugosc bata", "English": "Pipe length", "German": "Pipe length"},
    "Pipe length": {"Polski": "Dlugosc rury", "English": "Pipe length", "German": "Pipe length"},
    "Pipe description": {"Polski": "Opis rury", "English": "Pipe description", "German": "Pipe description"},

    "Port name": {"Polski": "Nazwa mufy", "English": "Port name", "German": "Port name"},
    "Port diameter": {"Polski": "Srednica mufy", "English": "Port diameter", "German": "Port diameter"},
    "Port thickness": {"Polski": "Grubosc mufy", "English": "Port thickness", "German": "Port thickness"},
    "Port length": {"Polski": "Dlugosc mufy", "English": "Port length", "German": "Port length"},
    "Port description": {"Polski": "Opis mufy", "English": "Port description", "German": "Port description"},
}

print(language_DataTable.get("Port distance").get(language_Select))

root.title(language_DataTable.get("Pipe Production Configuration").get(language_Select))
root.geometry('{}x{}'.format(1650, 950))
DateShift = -27
DatesToDisplay = [GUI_TimePlan_GetTimeString(-1 + DateShift),
                  GUI_TimePlan_GetTimeString(0 + DateShift),
                  GUI_TimePlan_GetTimeString(1 + DateShift),
                  GUI_TimePlan_GetTimeString(2 + DateShift),
                  GUI_TimePlan_GetTimeString(3 + DateShift),
                  GUI_TimePlan_GetTimeString(4 + DateShift),
                  GUI_TimePlan_GetTimeString(5 + DateShift)]

#ToDo
#Add images to each view
#Recolor all to be mor taimed
#Go with similar icons as in previous production plan

#Logging file of application
#Report for day supplys needed

#Summary should have list of each pipe and port needed per day


#image_background = tk.PhotoImage(file=""".\Data\BP PROJEKT logotyp_small.png""")
#image_label = tk.Label(root, image=image_background)
#image_label.place(x=0, y=0, relwidth=1, relheight=1)
#bg="#006699"
#bg="#5191C1"
#bg="#21C900"

# create all of the main containers
top_frame = tk.Frame(root, bg="#006699", width=450, height=50, pady=3)
center = tk.Frame(root, bg='lavender', width=50, height=40, padx=3, pady=3)
bottom_frame = tk.Frame(root, bg='lavender', width=450, height=45, pady=3)


# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
bottom_frame.grid(row=3, sticky="ew")

# create the widgets for the top frame
top_frame_button_file = tk.Button(top_frame, text=language_DataTable.get("File").get(language_Select),
                                  command=lambda: GUI_dummy_function())
top_frame_button_database = tk.Button(top_frame, text=language_DataTable.get("Database").get(language_Select),
                                      command=lambda: GUI_MySQL_DatabaseSettings())
top_frame_button_settings = tk.Button(top_frame, text=language_DataTable.get("Settings").get(language_Select),
                                      command=lambda: GUI_dummy_function())
top_frame_button_about = tk.Button(top_frame, text=language_DataTable.get("About").get(language_Select),
                                   command=lambda: GUI_dummy_function())
top_frame_button_help = tk.Button(top_frame, text=language_DataTable.get("Help").get(language_Select),
                                  command=lambda: GUI_dummy_function())

top_frame_button_file.grid(row=0, column=0)
top_frame_button_database.grid(row=0, column=1)
top_frame_button_settings.grid(row=0, column=2)
top_frame_button_about.grid(row=0, column=5)
top_frame_button_help.grid(row=0, column=6)

# data for options in application
GUI_MySQL_database_settings_IP_text = tk.StringVar()
GUI_MySQL_database_settings_port_text = tk.StringVar()
GUI_MySQL_database_settings_db_name_text = tk.StringVar()
GUI_MySQL_database_settings_host_name_text = tk.StringVar()
GUI_MySQL_database_settings_host_pass_text = tk.StringVar()

# create the widgets for bootom frame
bottom_frame_label_database_info = tk.Label(bottom_frame,
text=language_DataTable.get("Database name").get(language_Select)+''': pp
IP: x.x.x.x
Port: xxxx
Host: jan''', width=20, padx=1, pady=1)
bottom_frame_label_app_event_log = tk.Label(bottom_frame, text=language_DataTable.get("Event log").get(language_Select),
                                            width=100, height=5, justify='left')
#bottom_frame_button_database_info = tk.Button(bottom_frame, background="pink", text='Save to Database', command=lambda: GUI_dummy_function())
bottom_frame_label_database_info.grid(row=0, column=0)
bottom_frame_label_app_event_log.grid(row=0, column=1)
#bottom_frame_button_database_info.grid(row=0, column=2)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

#Create Frames for given part
ctr_left = tk.Frame(center, bg='lavender', width=100, height=190, padx=1, pady=1)
ctr_right = tk.Frame(center, bg='lavender', width=100, height=190, padx=1, pady=1)
ctr_mid_TimeSummary = tk.Frame(center, bg='lavender', width=250, height=190, padx=3, pady=3)
ctr_mid_Job = tk.Frame(center, bg='lavender', width=250, height=190, padx=3, pady=3)
ctr_mid_Element = tk.Frame(center, bg='lavender', width=250, height=190, padx=3, pady=3)
ctr_mid_Pipe = tk.Frame(center, bg='lavender', width=250, height=190, padx=3, pady=3)
ctr_mid_Port = tk.Frame(center, bg='lavender', width=250, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid_Job.grid(row=0, column=1, sticky="nsew")
#ctr_right.grid(row=0, column=2, sticky="ns")

#Create Buttons for selecting for given part
button_TimeSummary = tk.Button(ctr_left, text=language_DataTable.get("TimeSummary").get(language_Select),
                        background="pink", height=2, width=15, command=lambda: GUI_GoTo_TimeSummary())
button_Jobs = tk.Button(ctr_left, text=language_DataTable.get("Jobs").get(language_Select),
                        background="green", height=2, width=15, command=lambda: GUI_GoTo_Job())
button_Elements = tk.Button(ctr_left, text=language_DataTable.get("Elements").get(language_Select),
                            background="yellow", height=2, width=15, command=lambda: GUI_GoTo_Element())
button_Pipes = tk.Button(ctr_left, text=language_DataTable.get("Pipes").get(language_Select),
                         background="white", height=2, width=15, command=lambda: GUI_GoTo_Pipe())
button_Ports = tk.Button(ctr_left, text=language_DataTable.get("Ports").get(language_Select),
                         background="orange", height=2, width=15, command=lambda: GUI_GoTo_Port())

button_TimeSummary.grid(row=0, column=0, padx=20, pady=10)
button_Jobs.grid(row=1, column=0, padx=20, pady=10)
button_Elements.grid(row=2, column=0, padx=20, pady=10)
button_Pipes.grid(row=3, column=0, padx=20, pady=10)
button_Ports.grid(row=4, column=0, padx=20, pady=10)

# ProjekctSummary
# this should be place for summary of all opened projects for execution,
# their stage, needs, plan for start and supposed end

# TimeSummary
# Is using Plan/Job part of MySQL. It is checking all plans to have some elements to execute. Order them by time execution.
# Goal is to view time summary for all jobs created asign executed

TimeSummary_entry_production_timesummary_name_text = tk.StringVar()
TimeSummary_entry_element_table_amount_text = tk.StringVar()
TimeSummary_button_production_timesummary_refreash = tk.Button(ctr_mid_TimeSummary,
                                                       text=language_DataTable.get("Refreash").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_TimePlan_Update())
TimeSummary_button_production_timesummary_dateplus = tk.Button(ctr_mid_TimeSummary,
                                                       text=language_DataTable.get("DatePlus").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_TimeSummary_DatePlus())
TimeSummary_button_production_timesummary_dateminus = tk.Button(ctr_mid_TimeSummary,
                                                       text=language_DataTable.get("DateMinus").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_TimeSummary_DateMinus())
TimeSummary_entry_element_table_summary = ttk.Treeview(ctr_mid_TimeSummary, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=10)
TimeSummary_entry_element_table = ttk.Treeview(ctr_mid_TimeSummary, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=15)
TimeSummary_entry_production_job_leftouts_table = ttk.Treeview(ctr_mid_TimeSummary,
                                                              columns=(1), show='headings', height=15)
TimeSummary_entry_production_timesummary_element_table_summary_scrollbar = tk.Scrollbar(ctr_mid_TimeSummary, orient="vertical",
                                                                  command=TimeSummary_entry_element_table.yview)
TimeSummary_entry_production_timesummary_element_table_scrollbar = tk.Scrollbar(ctr_mid_TimeSummary, orient="vertical",
                                                                  command=TimeSummary_entry_element_table.yview)
TimeSummary_entry_production_job_leftouts_table_scrollbar = tk.Scrollbar(ctr_mid_TimeSummary, orient="vertical",
                                                                  command=TimeSummary_entry_production_job_leftouts_table.yview)

s=ttk.Style()
s.theme_use('clam')
#style = ttk.Style()
#style.configure('Treeview.Heading', foreground='black')

# Add the rowheight
s.configure('Treeview', rowheight=240)
TimeSummary_entry_production_job_leftouts_table.heading(1, text=language_DataTable.get("Leftout").get(language_Select))

TimeSummary_entry_element_table.heading(1, text=DatesToDisplay[0])#language_DataTable.get("Monday").get(language_Select))
TimeSummary_entry_element_table.heading(2, text=DatesToDisplay[1])#language_DataTable.get("Tuesday").get(language_Select))
TimeSummary_entry_element_table.heading(3, text=DatesToDisplay[2])#language_DataTable.get("Wednesday").get(language_Select))
TimeSummary_entry_element_table.heading(4, text=DatesToDisplay[3])#language_DataTable.get("Thursday").get(language_Select))
TimeSummary_entry_element_table.heading(5, text=DatesToDisplay[4])#language_DataTable.get("Friday").get(language_Select))
TimeSummary_entry_element_table.heading(6, text=DatesToDisplay[5])#language_DataTable.get("Saturday").get(language_Select))
TimeSummary_entry_element_table.heading(7, text=DatesToDisplay[6])#language_DataTable.get("Sunday").get(language_Select))
#TimeSummary_entry_element_table.heading(3, text=language_DataTable.get("Time plan machine to execution").get(language_Select))
#TimeSummary_entry_element_table.heading(3, text="Machine ID")

TimeSummary_entry_element_table_summary.config(yscrollcommand=TimeSummary_entry_production_timesummary_element_table_summary_scrollbar.set)
TimeSummary_entry_production_timesummary_element_table_summary_scrollbar.config(command=TimeSummary_entry_element_table_summary.yview)

TimeSummary_entry_element_table.config(yscrollcommand=TimeSummary_entry_production_timesummary_element_table_scrollbar.set)
TimeSummary_entry_production_timesummary_element_table_scrollbar.config(command=TimeSummary_entry_element_table.yview)

TimeSummary_entry_production_job_leftouts_table.config(yscrollcommand=TimeSummary_entry_production_job_leftouts_table_scrollbar.set)
TimeSummary_entry_production_job_leftouts_table_scrollbar.config(command=TimeSummary_entry_production_job_leftouts_table.yview)

#ToDo
TimeSummary_button_production_timesummary_dateminus.grid(row=0, column=0)
TimeSummary_button_production_timesummary_refreash.grid(row=0, column=1)
TimeSummary_button_production_timesummary_dateplus.grid(row=0, column=2)
TimeSummary_entry_element_table.grid(row=1, column=0, stick='e', columnspan=7, rowspan=3)
TimeSummary_entry_production_timesummary_element_table_scrollbar.grid(row=1, column=7, rowspan=3, sticky='ns')
TimeSummary_entry_element_table_summary.grid(row=4, column=0, stick='e', columnspan=7, rowspan=3)
TimeSummary_entry_production_timesummary_element_table_summary_scrollbar.grid(row=4, column=7, rowspan=3, sticky='ns')
TimeSummary_entry_production_job_leftouts_table.grid(row=1, column=8, stick='w', columnspan=2)
TimeSummary_entry_production_job_leftouts_table_scrollbar.grid(row=1, column=10, rowspan=1, sticky='ns')

#Create Content of given part
#Job is set of elements that machine need to execute.
# Jow contains element names also ammount that should be produced.
# In MySQL also there is place for how many is currently executed and time of execution. This is used for Time plan

Job_entry_production_job_name_text = tk.StringVar()
Job_entry_element_table_amount_text = tk.StringVar()
Job_entry_element_table_date_text = tk.StringVar()
Job_entry_production_job_name_comment = tk.Label(ctr_mid_Job,
text=language_DataTable.get("Production Job name").get(language_Select), width=20, padx=1, pady=1)
Job_entry_production_job_name = tk.Entry(ctr_mid_Job, background="pink", textvariable=Job_entry_production_job_name_text, width=60)
Job_button_production_job_search = tk.Button(ctr_mid_Job, text=language_DataTable.get("Search").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_Job_search())
Job_button_production_job_save = tk.Button(ctr_mid_Job, text=language_DataTable.get("Save").get(language_Select),
                                           background="#21C900", width=10, command=lambda: GUI_Job_save())
Job_entry_production_job_description_comment = tk.Label(ctr_mid_Job, text=language_DataTable.get("Production Job description").get(language_Select), width=20, padx=1, pady=1)
Job_entry_production_job_description = tk.Text(ctr_mid_Job, background="orange", width=30, height=17)
Job_entry_element_table = ttk.Treeview(ctr_mid_Job, columns=(1, 2, 3), show='headings', height=15)
Job_button_production_job_add_element = tk.Button(ctr_mid_Job, text=language_DataTable.get("Add").get(language_Select),
                                                  background="green", width=15, command=lambda: GUI_Job_element_search())
Job_button_production_job_delete_element = tk.Button(ctr_mid_Job, text=language_DataTable.get("Delete").get(language_Select),
                                                     background="red", width=15, command=lambda: GUI_treeview_delete(Job_entry_element_table))
Job_entry_production_job_element_table_scrollbar = tk.Scrollbar(ctr_mid_Job, orient="vertical",
                                                                  command=Job_entry_element_table.yview)

Job_entry_element_table_amount = tk.Entry(ctr_mid_Job, background="white", textvariable=Job_entry_element_table_amount_text,
                                          width=20)
Job_entry_element_table_date = tk.Entry(ctr_mid_Job, background="white", textvariable=Job_entry_element_table_date_text,
                                        width=20)
Job_button_element_table_data_change = tk.Button(ctr_mid_Job, text=language_DataTable.get("Change").get(language_Select),
                                                 background="#5191C1", width=15,
command=lambda: GUI_treeview_amount_exchange(Job_entry_element_table, [2, 3], Job_entry_element_table_amount_text, Job_entry_element_table_date_text))

s=ttk.Style()
s.theme_use('clam')

# Add the rowheight
s.configure('Treeview', rowheight=30)

Job_entry_element_table.heading(1, text=language_DataTable.get("Time plan date to execution").get(language_Select))
Job_entry_element_table.heading(2, text=language_DataTable.get("Element count").get(language_Select))
Job_entry_element_table.heading(3, text=language_DataTable.get("Execution date").get(language_Select))
#Job_entry_element_table.heading(3, text="Machine ID")

Job_entry_element_table.config(yscrollcommand=Job_entry_production_job_element_table_scrollbar.set)
Job_entry_production_job_element_table_scrollbar.config(command=Job_entry_element_table.yview)



Job_entry_production_job_name_comment.grid(row=0, column=0)
Job_entry_production_job_name.grid(row=0, column=1, padx=1, pady=1)
Job_button_production_job_search.grid(row=0, column=5)
Job_button_production_job_save.grid(row=0, column=6)
Job_entry_element_table.grid(row=1, column=0, stick='e', columnspan=2, rowspan=3)
Job_entry_production_job_element_table_scrollbar.grid(row=1, column=2, rowspan=3, sticky='ns')
Job_entry_production_job_description_comment.grid(row=1, column=5, columnspan=2)
Job_entry_production_job_description.grid(row=2, column=5, stick='n', columnspan=2)
Job_entry_element_table_amount.grid(row=4, column=5, stick='n')
Job_entry_element_table_date.grid(row=4, column=6, stick='n')
Job_button_element_table_data_change.grid(row=5, column=5, stick='n')
Job_button_production_job_add_element.grid(row=4, column=0)
Job_button_production_job_delete_element.grid(row=4, column=1)

#Element
#Part to create element that contains one type of pipe and many ports.
# This can be used as type of pipe under sealing
Element_entry_element_name_text = tk.StringVar()
Element_entry_pipe_name_text = tk.StringVar()
Element_entry_pipe_length_text = tk.StringVar()
Element_entry_port_table_edit_distance_text = tk.StringVar()
Element_entry_port_table_edit_angle_text = tk.StringVar()
Element_entry_element_name_comment = tk.Label(ctr_mid_Element,
                                              text=language_DataTable.get("Element name").get(language_Select),
                                              width=20, padx=1, pady=1)
Element_entry_element_name = tk.Entry(ctr_mid_Element, background="white", textvariable=Element_entry_element_name_text,
                                      width=60)
Element_entry_element_description_comment = tk.Label(ctr_mid_Element,
                                                     text=language_DataTable.get("Element description").get(language_Select),
                                                     width=20, padx=1, pady=1)
Element_entry_element_description = tk.Text(ctr_mid_Element, background="orange", width=30, height=10)
Element_button_production_Job_search = tk.Button(ctr_mid_Element,
                                                  text=language_DataTable.get("Search").get(language_Select),
                                                  background="#5191C1", width=10, command=lambda: GUI_Element_search())
Element_button_production_Job_save = tk.Button(ctr_mid_Element, text=language_DataTable.get("Save").get(language_Select),
                                                background="#21C900", width=10,
                                                    command=lambda: GUI_Element_save())
Element_entry_pipe_name_comment = tk.Label(ctr_mid_Element, text=language_DataTable.get("Pipe name").get(language_Select),
                                           width=10, padx=1, pady=1)
Element_entry_pipe_name = tk.Entry(ctr_mid_Element, background="white", textvariable=Element_entry_pipe_name_text,
                                   width=20)
Element_entry_pipe_length_comment = tk.Label(ctr_mid_Element, text=language_DataTable.get("Bat length").get(language_Select),
                                             width=10, padx=1, pady=1)
Element_entry_pipe_length = tk.Entry(ctr_mid_Element, background="white", textvariable=Element_entry_pipe_length_text,
                                     width=10)
Element_entry_port_table = ttk.Treeview(ctr_mid_Element, columns=(1, 2, 3), show='headings', height=15)
Element_button_element_add_element = tk.Button(ctr_mid_Element, text=language_DataTable.get("Add").get(language_Select),
                                               background="green", width=15, command=lambda: GUI_Element_port_search())
Element_button_element_delete_element = tk.Button(ctr_mid_Element, text=language_DataTable.get("Delete").get(language_Select),
                                                  background="red", width=15,
                                                  command=lambda: GUI_treeview_delete(Element_entry_port_table))
Element_entry_production_job_element_table_scrollbar = tk.Scrollbar(ctr_mid_Element)
Element_entry_port_table_edit_distance = tk.Entry(ctr_mid_Element, background="white",
                                                  textvariable=Element_entry_port_table_edit_distance_text, width=20)
Element_entry_port_table_edit_angle = tk.Entry(ctr_mid_Element, background="white",
                                                  textvariable=Element_entry_port_table_edit_angle_text, width=20)
Element_button_port_table_data = tk.Button(ctr_mid_Element, text=language_DataTable.get("Change").get(language_Select),
                                           background="#5191C1", width=15,
command=lambda: GUI_treeview_amount_exchange(Element_entry_port_table, [2, 3],
Element_entry_port_table_edit_distance, Element_entry_port_table_edit_angle))
Element_button_pipe_search = tk.Button(ctr_mid_Element,
                                                  text=language_DataTable.get("Search").get(language_Select),
                                                  background="#5191C1", width=10, command=lambda: Element_Pipe_search())

Element_entry_element_name_comment.grid(row=0, column=0)
Element_entry_element_name.grid(row=0, column=1, columnspan=3)
Element_button_production_Job_search.grid(row=0, column=6)
Element_button_production_Job_save.grid(row=0, column=7)
Element_button_pipe_search.grid(row=1, column=0)
Element_entry_pipe_name_comment.grid(row=1, column=1, stick='e')
Element_entry_pipe_name.grid(row=1, column=2, stick='w')
Element_entry_pipe_length_comment.grid(row=1, column=3, stick='e')
Element_entry_pipe_length.grid(row=1, column=4, stick='w')
Element_entry_port_table.grid(row=2, column=0, stick='w', columnspan=5, rowspan=3)
Element_entry_production_job_element_table_scrollbar.grid(row=2, column=5, rowspan=3, sticky='ns')
Element_entry_element_description_comment.grid(row=1, column=6, columnspan=2)
Element_entry_element_description.grid(row=2, column=6, stick='n', rowspan=3, columnspan=2)
Element_entry_port_table_edit_distance.grid(row=6, column=6, stick='n')
Element_entry_port_table_edit_angle.grid(row=6, column=7, stick='n')
Element_button_port_table_data.grid(row=7, column=6, stick='n')
Element_button_element_add_element.grid(row=6, column=0)
Element_button_element_delete_element.grid(row=6, column=2)

Element_entry_port_table.heading(1, text=language_DataTable.get("Port used").get(language_Select))
Element_entry_port_table.heading(2, text=language_DataTable.get("Port distance").get(language_Select))
Element_entry_port_table.heading(3, text=language_DataTable.get("Port angle").get(language_Select))

Element_entry_port_table.config(yscrollcommand=Element_entry_production_job_element_table_scrollbar.set)
Element_entry_production_job_element_table_scrollbar.config(command=Element_entry_port_table.yview)

#Pipe
Pipe_entry_pipe_name_text = tk.StringVar()
Pipe_entry_pipe_diameter_text = tk.StringVar()
Pipe_entry_pipe_thickness_text = tk.StringVar()
Pipe_entry_pipe_length_text = tk.StringVar()
Pipe_entry_pipe_name_comment = tk.Label(ctr_mid_Pipe, text=language_DataTable.get("Pipe name").get(language_Select),
                                        width=20, padx=1, pady=1)
Pipe_entry_pipe_name = tk.Entry(ctr_mid_Pipe, background="white", textvariable=Pipe_entry_pipe_name_text, width=40)
Pipe_button_production_job_search = tk.Button(ctr_mid_Pipe, text=language_DataTable.get("Search").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_Pipe_search())
Pipe_button_production_job_save = tk.Button(ctr_mid_Pipe, text=language_DataTable.get("Save").get(language_Select),
                                             background="#21C900", width=10, command=lambda: GUI_Pipe_save())
Pipe_entry_pipe_diameter_comment = tk.Label(ctr_mid_Pipe, text=language_DataTable.get("Pipe diameter").get(language_Select),
                                            width=20, padx=1, pady=1)
Pipe_entry_pipe_diameter = tk.Entry(ctr_mid_Pipe, background="white", textvariable=Pipe_entry_pipe_diameter_text,
                                    width=30)
Pipe_entry_pipe_thickness_comment = tk.Label(ctr_mid_Pipe, text=language_DataTable.get("Pipe thickness").get(language_Select),
                                             width=20, padx=1, pady=1)
Pipe_entry_pipe_thickness = tk.Entry(ctr_mid_Pipe, background="white", textvariable=Pipe_entry_pipe_thickness_text,
                                     width=30)
Pipe_entry_pipe_length_comment = tk.Label(ctr_mid_Pipe, text=language_DataTable.get("Pipe length").get(language_Select),
                                          width=20, padx=1, pady=1)
Pipe_entry_pipe_length = tk.Entry(ctr_mid_Pipe, background="white", textvariable=Pipe_entry_pipe_length_text, width=30)
Pipe_entry_pipe_description_comment = tk.Label(ctr_mid_Pipe,
                                               text=language_DataTable.get("Pipe description").get(language_Select),
                                               width=20, padx=1, pady=1)
Pipe_entry_pipe_description = tk.Text(ctr_mid_Pipe, background="orange", width=30, height=10)

Pipe_entry_pipe_name_comment.grid(row=0, column=0)
Pipe_entry_pipe_name.grid(row=0, column=1)
Pipe_button_production_job_search.grid(row=0, column=3)
Pipe_button_production_job_save.grid(row=0, column=4)
Pipe_entry_pipe_diameter_comment.grid(row=1, column=0)
Pipe_entry_pipe_diameter.grid(row=1, column=1, columnspan=2)
Pipe_entry_pipe_thickness_comment.grid(row=2, column=0)
Pipe_entry_pipe_thickness.grid(row=2, column=1, columnspan=2)
#Pipe_entry_pipe_length_comment.grid(row=3, column=0)
#Pipe_entry_pipe_length.grid(row=3, column=1, columnspan=2)
Pipe_entry_pipe_description_comment.grid(row=1, column=3, columnspan=2)
Pipe_entry_pipe_description.grid(row=2, column=3, stick='n', rowspan=5, columnspan=2)

#Port
Port_entry_port_name_text = tk.StringVar()
Port_entry_port_diameter_text = tk.StringVar()
Port_entry_port_thickness_text = tk.StringVar()
Port_entry_port_length_text = tk.StringVar()
Port_entry_port_name_comment = tk.Label(ctr_mid_Port, text=language_DataTable.get("Port name").get(language_Select),
                                        width=20, padx=1, pady=1)
Port_entry_port_name = tk.Entry(ctr_mid_Port, background="white", textvariable=Port_entry_port_name_text, width=40)
Port_button_production_job_search = tk.Button(ctr_mid_Port, text=language_DataTable.get("Search").get(language_Select),
                                               background="#5191C1", width=10, command=lambda: GUI_Port_search())
Port_button_production_job_save = tk.Button(ctr_mid_Port, text=language_DataTable.get("Save").get(language_Select),
                                             background="#21C900", width=10, command=lambda: GUI_Port_save())
Port_entry_port_diameter_comment = tk.Label(ctr_mid_Port,
                                            text=language_DataTable.get("Port diameter").get(language_Select),
                                            width=20, padx=1, pady=1)
Port_entry_port_diameter = tk.Entry(ctr_mid_Port, background="white", textvariable=Port_entry_port_diameter_text,
                                    width=30)
Port_entry_port_thickness_comment = tk.Label(ctr_mid_Port,
                                             text=language_DataTable.get("Port thickness").get(language_Select),
                                             width=20, padx=1, pady=1)
Port_entry_port_thickness = tk.Entry(ctr_mid_Port, background="white", textvariable=Port_entry_port_thickness_text,
                                     width=30)
Port_entry_port_length_comment = tk.Label(ctr_mid_Port, text=language_DataTable.get("Port length").get(language_Select),
                                          width=20, padx=1, pady=1)
Port_entry_port_length = tk.Entry(ctr_mid_Port, background="white", textvariable=Port_entry_port_length_text, width=30)
Pipe_entry_pipe_description_comment = tk.Label(ctr_mid_Port,
                                               text=language_DataTable.get("Port description").get(language_Select),
                                               width=20, padx=1, pady=1)
Port_entry_port_description = tk.Text(ctr_mid_Port, background="orange", width=30, height=10)

Port_entry_port_name_comment.grid(row=0, column=0)
Port_entry_port_name.grid(row=0, column=1)
Port_button_production_job_search.grid(row=0, column=3)
Port_button_production_job_save.grid(row=0, column=4)
Port_entry_port_diameter_comment.grid(row=1, column=0)
Port_entry_port_diameter.grid(row=1, column=1, columnspan=2)
Port_entry_port_thickness_comment.grid(row=2, column=0)
Port_entry_port_thickness.grid(row=2, column=1, columnspan=2)
Port_entry_port_length_comment.grid(row=3, column=0)
Port_entry_port_length.grid(row=3, column=1, columnspan=2)
Pipe_entry_pipe_description_comment.grid(row=1, column=3, columnspan=2)
Port_entry_port_description.grid(row=2, column=3, stick='n', rowspan=5, columnspan=2)

db = DB_Connect()




