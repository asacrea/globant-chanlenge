config = {
    "Extract": {
        "DetailedTimeRecordFieldServices":
        {   
            "SharepointRead": {
                "path": "process.factory.extract",
                "parameters": {
                    "load_method": "pd.read_excel({file}, dtype = object, skiprows=6)",
                }
            }
        },
        "EmployeeScheduleFieldServices":
        {   
            "SharepointRead": {
                "path": "process.factory.extract",
                "parameters": {
                    "load_method": "pd.read_excel({file}, dtype = object, skiprows=7)",
                }
            }
        },
        "TeamAligmentFieldServices":
        {   
            "SharepointRead": {
                "path": "process.factory.extract",
                "parameters": {
                    "load_method": "pd.read_excel({file}, dtype = object, sheet_name='Emp. Data', usecols='A:J')",
                }
            }
        }
    },
    "Transform": {
        "departments": {
            "DropDataframeColumns": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": ["Unnamed"],
                    "axis": None
                }
            },
            "FillDataframeNulls": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": []
                }
            },
            "ChangeDataframeColumnsName": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "rename": {
                        "Paid Time (Hours)": "paid_time_hours",
                        "Unpaid Time (Hours)": "unpaid_time_hours",
                        "Total Time (Hours)": "total_time_hours",
                        "Start": "start",
                        "End": "end_",
                        "Activity": "activity",
                        "Employee ID": "employee_id"
                    }
                }
            },
            "ValidateDateColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "date_format": "%Y-%m-%d %H:%M:%S", 
                    "columns": ["start", "end_"],
                    "raise_flag": "",
                    "errors" : "coerce"
                }
            },
            "ValidateTextColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["activity"]
                }
            },
            "ValidateFloatColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["employee_id", "paid_time_hours", "unpaid_time_hours", "total_time_hours"],
                    "errors" : "coerce"
                }
            }
        },
        "hired_employees": {
            "DropDataframeColumns": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": ["Unnamed"],
                    "axis": None
                }
            },
            "FillDataframeNulls": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": []
                }
            },
            "ChangeDataframeColumnsName": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "rename": {
                        "Paid Time (Hours)": "paid_time_hours",
                        "Unpaid Time (Hours)": "unpaid_time_hours",
                        "Total Time (Hours)": "total_time_hours",
                        "Start": "start",
                        "End": "end_",
                        "Activity": "activity",
                        "Employee ID": "employee_id"
                    }
                }
            },
            "ValidateDateColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "date_format": "%Y-%m-%d %H:%M:%S", 
                    "columns": ["start", "end_"],
                    "raise_flag": "",
                    "errors" : "coerce"
                }
            },
            "ValidateTextColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["activity"]
                }
            },
            "ValidateFloatColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["employee_id", "paid_time_hours", "unpaid_time_hours", "total_time_hours"],
                    "errors" : "coerce"
                }
            }
        },
        "jobs": {
            "DropDataframeColumns": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": ["Unnamed"],
                    "axis": None
                }
            },
            "FillDataframeNulls": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "criterias": []
                }
            },
            "ChangeDataframeColumnsName": {
                "path": "process.factory.transform.Dataframe",
                "parameters": {
                    "rename": {
                        "Paid Time (Hours)": "paid_time_hours",
                        "Unpaid Time (Hours)": "unpaid_time_hours",
                        "Total Time (Hours)": "total_time_hours",
                        "Start": "start",
                        "End": "end_",
                        "Activity": "activity",
                        "Employee ID": "employee_id"
                    }
                }
            },
            "ValidateDateColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "date_format": "%Y-%m-%d %H:%M:%S", 
                    "columns": ["start", "end_"],
                    "raise_flag": "",
                    "errors" : "coerce"
                }
            },
            "ValidateTextColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["activity"]
                }
            },
            "ValidateFloatColumns": {
                "path": "process.factory.transform.Validations",
                "parameters": {
                    "columns": ["employee_id", "paid_time_hours", "unpaid_time_hours", "total_time_hours"],
                    "errors" : "coerce"
                }
            }
        }
    },
    "Load": {
        "Load":{ 
            "path":"process.factory.load", 
            "data":{ 
                "Dataframes":[
                    { 
                        'key':'TDSFieldServicesBusinessRules',
                        'bucket':'datalakedsi',
                        'path':'alpha/stage/finance/invoice/glb/tds/field_services/internal/business_rules/',
                        'file_name':'tds_business_rules.csv' 
                    },
                    { 
                        'key':'TDSFieldServicesBillableHours',
                        'bucket':'datalakedsi',
                        'path':'alpha/stage/finance/invoice/glb/tds/field_services/internal/billable_hours/',
                        'file_name':'tds_billable_hours.csv'
                    },
                    {
                        'key':'TDSFieldServicesGetRates',
                        'bucket':'datalakedsi',
                        'path':'alpha/stage/finance/invoice/glb/tds/field_services/internal/billable_hours_rates/',
                        'file_name':'tds_billable_hours_rates.csv'
                    }
                ] 
            }
        }
    }
}