from dal.databases.base_database import BaseDataBase
import mysql.connector
from dynaconf import settings


class SqlDataBase(BaseDataBase):
    def __init__(self, logger):
        super().__init__()
        self.__logger = logger

    def connect(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as err:
            self.__logger.error(
                "error when tried to connect to db: {}".format(err))

    @staticmethod
    def dict_to_conditions(conditions_dict):
        if(conditions_dict == {}):
            return ''
        return ' AND ' + ' AND '.join(["{key} = '{value}'".format(
            key=key, value=value) for key, value in conditions_dict.items()]).strip()

    def create(self, table_name, object_to_create):
        cursor = self.connection.cursor()

        sql = "INSERT INTO {table_name} ({keys}) VALUES ({values})".format(
            table_name=table_name,
            keys=', '.join(object_to_create.keys()).strip(),
            values=", ".join(["%({key})s".format(key=key) for key in object_to_create.keys()])).strip()

        cursor.execute(sql, object_to_create)
        cursor.close()

        self.connection.commit()

    def __joinner_pointing_on_me(self, table_name, identifaction, keys_to_get=None):
        res = {}

        cursor = self.connection.cursor()
        cursor.execute("SELECT TABLE_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_NAME = '{table_name}' and REFERENCED_TABLE_NAME IS NOT NULL".format(
            table_name=table_name))

        tables_pointing_table_name = cursor.fetchall()

        for row in tables_pointing_table_name:
            # row[0] = table that point my table_name
            res.update(self.__joinner_pointing_on(
                row[0], identifaction, table_name))

        cursor.close()
        return res


    def __joinner_pointing_on(self, table_name, identifaction, main_table=None):
        result = {}
        cursor = self.connection.cursor()

        cursor.execute("SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table_name}' and REFERENCED_TABLE_NAME IS NOT NULL".format(
            table_name=table_name))

        result_set = cursor.fetchall()
        # main_item_id in this case post_id
        if main_table is not None:
            main_item_id = [row for row in result_set if main_table in row][0][0]

        for row in result_set:
            # row[1] - table that table_name pointing on
            # we dont want to get the data of the main table every time
            if(main_table is None):
                main_item_id = row[2]

            if(row[1] == main_table):
                continue
            
            cursor.execute(
                "SELECT \
                * \
                FROM {table_name} \
                INNER JOIN {refernce_table_name} ON {table_name}.{column_name} = {refernce_table_name}.{refernce_column_name} {conditions}".format(
                    table_name=table_name,
                    conditions=' AND {identifaction}'.format(
                    identifaction = table_name + '.' + main_item_id + '=' + identifaction),
                    column_name=row[0],
                    refernce_table_name=row[1],
                    refernce_column_name=row[2]
                ))

            columns = cursor.description
            result.update(({table_name: [{columns[index][0]:column for index, column in enumerate(
                value)} for value in cursor.fetchall()]}))

        cursor.close()
        return result

    def read(self, table_name, identifaction, keys_to_get=None):
        result = {}

        result.update(self.__joinner_pointing_on_me(table_name, identifaction))
        result.update(self.__joinner_pointing_on(table_name, identifaction))

        return result

    def delete(self, table_name, conditions_dict):
        cursor = self.connection.cursor()

        sql = "DELETE FROM {table_name} WHERE {conditions}".format(
            table_name=table_name,
            conditions=SqlDataBase.dict_to_conditions(conditions_dict)
        )

        cursor.execute(sql)
        cursor.close()

        self.connection.commit()

    def update(self, table_name, conditions, object_to_update):
        pass
