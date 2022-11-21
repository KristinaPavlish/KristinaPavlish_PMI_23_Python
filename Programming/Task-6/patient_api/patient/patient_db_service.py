import json
import re

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user222",
    password="user222",
    database="patient_db"
)


class PatientService:
    # GET /patients
    @staticmethod
    def get_patients():
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_db.patient")
        return json.dumps(cursor.fetchall(), default=str)

    # GET/patients/{patient_id}
    @staticmethod
    def get_by_id(patient_id_to_get):
        cursor = mydb.cursor(dictionary=True)
        try:
            id_to_del = int(patient_id_to_get)
        except Exception as e:
            print(e)
            return "[]"
        cursor.execute("SELECT * FROM patient_db.patient WHERE patient_id =" + str(patient_id_to_get))
        return json.dumps(cursor.fetchall(), default=str)

    # DELETE /patient/{patient_id}
    @staticmethod
    def delete_patient_by_id(patient_id_to_delete):
        cursor = mydb.cursor(dictionary=True)
        try:
            id_to_del = int(patient_id_to_delete)
        except Exception as e:
            print(e)
            return "[]"
        cursor.execute("DELETE FROM patient_db.patient WHERE patient_id =" + str(id_to_del))
        return json.dumps(cursor.fetchall(), default=str)

    # PUT  /patients/{patient_id} -> UPDATE PATIENT(IN BODY SOME MODEL)
    @staticmethod
    def put_patient(patient_id_to_put, patient):
        cursor = mydb.cursor(dictionary=True)
        try:
            id_to_put = int(patient_id_to_put)
        except Exception as e:
            print(e)
            return "[]"
        query = "UPDATE patient_db.patient SET name = " + "'" + patient.name + "'" + ", date = " + "'" + str(
            patient.date) + "'" + ", time = " + "'" + str(patient.time) + "'" + ", duration = " + str(
            patient.duration) + ", doctor_name = " + "'" + patient.doctor_name + "'" + ", department = " + "'" + patient.department + "'" + " WHERE patient_id =" + str(
            patient_id_to_put)
        cursor.execute(query)
        return json.dumps(cursor.fetchall(), default=str)

    # POST /patients/{patient_id} -> CREATE NEW PATIENT(IN BODY SOME MODEL)
    @staticmethod
    def post_patient(patient):
        cursor = mydb.cursor(dictionary=True)
        query = "INSERT INTO patient_db.patient (name, date, time, duration, doctor_name, department) VALUES (%s, %s,%s, %s,%s, %s )"
        val = ("'" + patient.name + "'", str(patient.date), str(patient.time), str(patient.duration),
               "'" + patient.doctor_name + "'", "'" + patient.department + "'")
        cursor.execute(query, val)
        return json.dumps(cursor.fetchall(), default=str)

    @staticmethod
    def validate(data_str):
        data = json.loads(data_str)
        dict_errors = {}
        for i in range(0, len(data)):
            last_elem = data[i]
            if not bool(re.match('[a-zA-Z\s]+$', last_elem["name"].replace("'", ""))):
                dict_errors["name"] = "invalid name"
            if not re.match('[a-zA-Z\s]+$', last_elem["doctor_name"].replace("'", "")):
                dict_errors["doctor_name"] = "invalid doctor name"
            if not re.match('[a-zA-Z\s]+$', last_elem["department"].replace("'", "")):
                dict_errors["department"] = "invalid department"
            if len(dict_errors) != 0:
                dict_errors["status"] = 400
                raise ValueError(str(dict_errors))
            print(str(dict_errors))
        return data



