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

    # GET /patients?elem_to_search=&limit=&offset=
    @staticmethod
    def search_without_sort(lim, offs, elem_to_search):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_db.patient WHERE "
                       "patient_id LIKE '%" + str(elem_to_search) + "%'" +
                       " OR name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR date LIKE '%" + str(elem_to_search) + "%'" +
                       " OR time LIKE '%" + str(elem_to_search) + "%'" +
                       " OR duration LIKE '%" + str(elem_to_search) + "%'" +
                       " OR doctor_name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR department LIKE '%" + str(elem_to_search) + "%'" +
                       " LIMIT " + str(offs) + ", " + str(lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?elem_to_search=&sort=&limit=&offset=
    @staticmethod
    def search_sort(lim, offs, sort, elem_to_search):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_db.patient WHERE "
                       "patient_id LIKE '%" + str(elem_to_search) + "%'" +
                       " OR name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR date LIKE '%" + str(elem_to_search) + "%'" +
                       " OR time LIKE '%" + str(elem_to_search) + "%'" +
                       " OR duration LIKE '%" + str(elem_to_search) + "%'" +
                       " OR doctor_name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR department LIKE '%" + str(elem_to_search) + "%'" +
                       "ORDER BY " + str(sort) + " ASC" +
                       " LIMIT " + str(offs) + ", " + str(lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?elem_to_search=&sort_by_desc=&limit=&offset=
    @staticmethod
    def search_sort_desc(lim, offs, sort_by_desc, elem_to_search):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_db.patient WHERE "
                       "patient_id LIKE '%" + str(elem_to_search) + "%'" +
                       " OR name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR date LIKE '%" + str(elem_to_search) + "%'" +
                       " OR time LIKE '%" + str(elem_to_search) + "%'" +
                       " OR duration LIKE '%" + str(elem_to_search) + "%'" +
                       " OR doctor_name LIKE '%" + str(elem_to_search) + "%'" +
                       " OR department LIKE '%" + str(elem_to_search) + "%'" +
                       "ORDER BY " + str(sort_by_desc) + " DESC" +
                       " LIMIT " + str(offs) + ", " + str(lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?sort=&sort_by_desc=&limit=&offset=
    @staticmethod
    def get_patients(lim, offs, sort, sort_by_desc):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient_db.patient ORDER BY " + str(sort) + " ASC, " + str(
            sort_by_desc) + " DESC" + " LIMIT " + str(offs) + ", " + str(lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?sort=&limit=&offset=
    @staticmethod
    def get_patients_order_by(lim, offs, sort):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM patient_db.patient ORDER BY " + str(sort) + " ASC" + " LIMIT " + str(offs) + ", " + str(lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?sort_by_decs=&limit=&offset=
    @staticmethod
    def get_patients_order_by_desc(lim, offs, sort):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM patient_db.patient ORDER BY " + str(sort) + " DESC" + " LIMIT " + str(offs) + ", " + str(
                lim))
        return json.dumps(cursor.fetchall(), default=str)

    # GET /patients?limit=&offset=
    @staticmethod
    def get_patients_without_any_order(lim, offs):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM patient_db.patient " + "LIMIT " + str(offs) + ", " + str(lim))
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
    def count_patient():
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(patient_id) FROM patient_db.patient")
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
