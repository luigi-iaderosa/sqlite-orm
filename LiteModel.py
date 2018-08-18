import copy

class BusinessKey:
    def __init__(self):
        self.keySet = {}


    def addKeyValue(self,key,value):
        self.keySet[key] = value


from SqliteOp import SqliteOp
from DBConnections import DBConnections
class LiteModel:

    table = ''
    columns = []
    protectedColumns = []
    fillableColumns = []

    entityValues = {}  # dictionary
    argumentString = ''

    def __init__(self, key=None):

        def _formatArgumentString(columns):
            columnsLength = len(columns)
            columnsSqlString = '('
            for i in range(0, columnsLength):
                columnsSqlString = columnsSqlString + '?'
                if i < columnsLength - 1:
                    columnsSqlString = columnsSqlString + ','
                i = i + 1
            columnsSqlString = columnsSqlString+')'
            return columnsSqlString

        self.fillableColumns = list(set(self.columns) - set(self.protectedColumns))
        self.argumentString = _formatArgumentString(self.fillableColumns)

        if isinstance(key, BusinessKey):
            data = self.searchByParams(key)

            for i in range(0, len(self.columns)):
                self.entityValues[self.columns[i]] = data[0][i]
                i = i + 1

        else:
            if key is not None:
                raise ValueError('you must use a <LiteModel::BusinessKey> type, or None!')
            else:
                self.entityValues = {}



    def save(self):
        def _formatColumnListForSave(entityValues):
            columnsSqlString = '('
            columnsLength = len(entityValues.keys())
            i = 0
            for column in entityValues.keys():
                columnsSqlString = columnsSqlString + column
                if i < columnsLength - 1:
                    columnsSqlString = columnsSqlString + ','
                    i = i + 1
            columnsSqlString = columnsSqlString+')'
            return columnsSqlString

        def _formatColumnValuesForSave(entityValues):
            return list(entityValues.values())

        columnsSqlString = _formatColumnListForSave(self.entityValues)
        args = _formatColumnValuesForSave(self.entityValues)

        sql = "insert into "+self.table+" "+columnsSqlString+" VALUES "+self.argumentString
        sqliteOp = SqliteOp(DBConnections.connection())

        data = sqliteOp.executeDBEdit(sql, args)

    def update(self):
        raise Exception('Unimplemented!')  # TODO: implement update

    def delete(self):
        raise Exception('Unimplemented!')  # TODO: implement delete

    # TODO: a good idea to extend this method with query arguments, like sorting (ASC,DESC)
    def searchByParams(self, key):
        sql = "select * from " + self.table + " where "
        keySetItems = key.keySet.items()
        keySetItemsLength = len(keySetItems)
        i = 0
        args = []
        for k, v in keySetItems:
            args.append(str(v))
            sql = sql + k + ' = ?'
            if i < keySetItemsLength - 1:
                sql = sql + ' and '
                i = i + 1
        sqliteOp = SqliteOp(DBConnections.connection())
        data = sqliteOp.executeDBInterrogation(sql, args)
        if len(data) == 0:
            return None
        else:
            return self.tupleDBCollectionToEntityCollection(data)

    def tupleToEntity(self, tuple):

        instance = self.__class__()
        rangeColumns = len(instance.columns)
        for i in range(0, rangeColumns):
            instance.entityValues[instance.columns[i]] = tuple[i]
        return instance

    def tupleDBCollectionToEntityCollection(self, data):
        entityCollection = []
        i = 0
        for d in data:
            nextToPut = self.tupleToEntity(d)
            entityCollection.insert(i, nextToPut)
            i = i + 1
        return entityCollection

    def search(self, bk, queryArgs = []):
        if not isinstance(bk, BusinessKey):
            raise ValueError('you must use a <LiteModel::BusinessKey> type, or None!')
        data = self.searchByParams(bk)
        return data


    def print(self):
        for x, y in self.entityValues.items():
            print('['+x+': '+str(y)+']')
