class Information_DB:
    def __init__(self, dsn, name, desc, db_name, user, pw, selected=False):
        self.dsn = dsn
        self.name = name
        self.desc = desc
        self.db_name = db_name
        self.user = user
        self.pw = pw
        self.selected = selected

    def __str__(self):
        return f"{self.dsn} ({self.desc})"
