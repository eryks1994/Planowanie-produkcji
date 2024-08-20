from Support.Database.dbfunc import *

def PP_Create_Tables(db):
    db = DB_Connect()
    DB_CreateTable(db, "Plan",
                   "PlanID INT PRIMARY KEY AUTO_INCREMENT",
                   "Name VARCHAR(100)",
                   "Description TEXT",
                   "PipelineElementID_1 INT","Ammount_1 INT",
                   "PipelineElementID_2 INT","Ammount_2 INT",
                   "PipelineElementID_3 INT","Ammount_3 INT",
                   "PipelineElementID_4 INT","Ammount_4 INT",
                   "PipelineElementID_5 INT","Ammount_5 INT",
                   "PipelineElementID_6 INT","Ammount_6 INT",
                   "PipelineElementID_7 INT","Ammount_7 INT",
                   "PipelineElementID_8 INT","Ammount_8 INT",
                   "PipelineElementID_9 INT","Ammount_9 INT",
                   "PipelineElementID_10 INT","Ammount_10 INT",
                   "PipelineElementID_11 INT","Ammount_11 INT",
                   "PipelineElementID_12 INT","Ammount_12 INT",
                   "PipelineElementID_13 INT","Ammount_13 INT",
                   "PipelineElementID_14 INT","Ammount_14 INT",
                   "PipelineElementID_15 INT","Ammount_15 INT",
                   "PipelineElementID_16 INT","Ammount_16 INT",
                   "PipelineElementID_17 INT","Ammount_17 INT",
                   "PipelineElementID_18 INT","Ammount_18 INT",
                   "PipelineElementID_19 INT","Ammount_19 INT",
                   "PipelineElementID_20 INT","Ammount_20 INT")

    DB_CreateTable(db, "Element",
                   "ElementID INT PRIMARY KEY AUTO_INCREMENT",
                   "Name VARCHAR(100)",
                   "Description TEXT",
                   "Length DOUBLE",
                   "PipeID INT",
                   "PortID_1 INT", "Length_1 DOUBLE",
                   "PortID_2 INT", "Length_2 DOUBLE",
                   "PortID_3 INT", "Length_3 DOUBLE",
                   "PortID_4 INT", "Length_4 DOUBLE",
                   "PortID_5 INT", "Length_5 DOUBLE",
                   "PortID_6 INT", "Length_6 DOUBLE",
                   "PortID_7 INT", "Length_7 DOUBLE",
                   "PortID_8 INT", "Length_8 DOUBLE",
                   "PortID_9 INT", "Length_9 DOUBLE",
                   "PortID_10 INT", "Length_10 DOUBLE",
                   "PortID_11 INT", "Length_11 DOUBLE",
                   "PortID_12 INT", "Length_12 DOUBLE",
                   "PortID_13 INT", "Length_13 DOUBLE",
                   "PortID_14 INT", "Length_14 DOUBLE",
                   "PortID_15 INT", "Length_15 DOUBLE",
                   "PortID_16 INT", "Length_16 DOUBLE",
                   "PortID_17 INT", "Length_17 DOUBLE",
                   "PortID_18 INT", "Length_18 DOUBLE",
                   "PortID_19 INT", "Length_19 DOUBLE",
                   "PortID_20 INT", "Length_20 DOUBLE")

    DB_CreateTable(db, "Pipe",
                   "PipeID INT PRIMARY KEY AUTO_INCREMENT",
                   "Name VARCHAR(100)",
                   "Description TEXT",
                   "Diameter DOUBLE",
                   "Thickness DOUBLE",
                   "Length DOUBLE",
                   "PipeEndTypeStart INT",
                   "PipeEndTypeFinish INT")

    DB_CreateTable(db, "Port",
                   "PortID INT PRIMARY KEY AUTO_INCREMENT",
                   "Name VARCHAR(100)",
                   "Description TEXT",
                   "Diameter DOUBLE",
                   "Thickness DOUBLE",
                   "Length DOUBLE",
                   "PortEndTypePipeSide INT",
                   "PortEndTypeSprinklerSide INT")

def PP_Pull_ProductionPlans(db, PPID):
    mycursor = db.cursor()
    DB_Select_Specific(db, "ProductionPlan", "ProductionPlanID =" + PPID)

    return mycursor


