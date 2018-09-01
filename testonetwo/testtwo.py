#! /usr/bin/env python3

import re
import csv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

db = 'django_test'
mregex = re.compile(r'\w|\s')


def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        titles = next(reader)
        data = [row for row in reader]

    return titles, data


def clean(string):
    return '_'.join(''.join(
        re.findall(mregex, string.lower())).split())


def map_titles(titles):
    data = {}
    for title in titles:
        data[title] = clean(str(title))

conn = psycopg2.connect(user='postgres', password='secretive',
                        host='localhost')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS {}'.format(db))
cursor.execute('CREATE DATABASE {}'.format(db))

management_sql = """
                    CREATE TABLE management_category(
                        id      INT PRIMARY KEY NOT NULL,
                        name    VARCHAR(20)     NOT NULL
                    )
                """

variety_sql = """
                CREATE TABLE variety(
                    id      INT PRIMARY KEY NOT NULL,
                    name    VARCHAR(30)     NOT NULL
                )
            """

farmer_sql = """
                CREATE TABLE farmer(
                    id      INT PRIMARY KEY NOT NULL,
                    name    VARCHAR         NOT NULL
                )
            """

crop_sql = """
            CREATE TABLE crop(
                id      INT PRIMARY KEY NOT NULL,
                name    VARCHAR         NOT NULL
            )
            """

cropping_sql = """
            CREATE TABLE cropping_system(
                id      INT PRIMARY KEY NOT NULL,
                name    VARCHAR         NOT NULL
            )
            """

data_sql = """
        CREATE TABLE {}(
            id                      INT PRIMARY KEY NOT NULL,
            farmer_id               INT             NOT NULL,
            management_category_id  INT             NOT NULL,
            variety_id              INT             NOT NULL,
            crop_id                 INT             NOT NULL,
            cropping_system_id      INT             NOT NULL,
            plot_size               VARCHAR         NOT NULL,
            spacing                 VARCHAR         NOT NULL,
            harvesting_date         DATETIME        NOT NULL,
            sampling_date           DATETIME        NOT NULL,
            stand_count             INT                     ,
            
            FOREIGN KEY farmer_id REFERENCES farmer(id),
            FOREIGN KEY management_category_id REFERENCES management_category(id),
            FOREIGN KEY variety_id REFERENCES variety(id),
            FOREIGN KEY crop_id REFERENCES crop(id),
            FOREIGN KEY cropping_system_id REFERENCES cropping_system(id),
        )
"""
