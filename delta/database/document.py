
class Document(object):
    ID      =   "SELECT * FROM DOCUMENT WHERE %s LIKE ID AND "\
            +   "TIME > %s LIMIT %s;"

    TYPE    =   "SELECT * FROM DOCUMENT where %s LIKE TYPE AND "\
            +   "TIME > %s LIMIT %s;"

    REGULAR =   "SELECT * FROM DOCUMENT WHERE TIME > %s LIMIT %s;"

    def request(cursor, request):
        limit = request.limit
        if limit is None:
            limit = 10000

        try:
            if request.id is not None:
                cursor.execute( Document.ID
                              , (request.id, request.date, limit))

                return request.set_payload(cursor.fetchall())
            elif request.type is not None:
                cursor.execute( Document.TYPE
                              , (request.type, request.date, limit))

                return request.set_payload(cursor.fetchall())
            else:
                cursor.execute( Document.REGULAR
                              , (request.date, limit))

                return request.set_payload(self.cursor.fetchall())

        except Exception as e:
            print(e)
            """Add error handling."""
            print("Failed to get requested document: {}".format(str(e)))
            sys.exit(1)

        return request
