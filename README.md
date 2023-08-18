

# Hospital Management System - Project Description

### The repository for the project is available at https://github.com/frediff/HMS

## HMS 

#### System Description

This project is a web application for a hospital management system. The system registers patients, schedules appointments with doctors, maintains patient information about diagnostics tests and treatments, maintains information about doctors/healthcare professionals, and stores admit/discharge information about the patients.

#### Intended users

- ***Front Desk Operators***: Registers/admits/discharges patients
- ***Data Entry Operators***: Enters patient data about tests and treatments
- ***Doctors***: Query patient information
- ***Database Administrators***: Add/delete users

#### Functionalities

The system supports the following workflow:

> ###### Patient registration/discharge and doctor appointment/test scheduling
>
> Information about new patients can be registered. One can schedule appointments based on availability and priority. Furthermore, it notifies doctors about the appointments in a dashboard. Assignment of rooms for admitted patients is done based on available room capacity. The system preserves information about discharged patients. Nevertheless, it updates the room occupancy accordingly. The workflow also supports scheduling tests and treatments prescribed by doctors.

> ###### Patient data entry
>
> All a patient's health information, including test results and treatments administered, can be recorded.

> ###### Doctor dashboard
>
> The application displays all the records of patients a doctor treats on a dashboard. Doctors may also query for any patient information. The doctor should be able to record drugs/treatments prescribed to a patient. Operators can send automated email reports to a doctor about the health information of patients treated by him/her every week. Emailing high-priority events is done in an emergency manner.

> ###### Database Administration
>
> Will be able to add/delete new users. A data security policy is present with suitable access control.

#### Tech Stack

> BACK-END
>
> - SQLite
> - Django Framework
> - Python3

> FRONT-END
>
> - HTML
> - CSS
> - Java-Script



#### Contributors

- Subham Ghosh (Roll No.: 20CS10065)
- Anubhav Dhar (Roll No.: 20CS30004)
- Aritra Mitra (Roll No.: 20CS30006)
