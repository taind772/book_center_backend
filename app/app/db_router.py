DATA_MODELS = ['document', 'author', 'user']


class Router:
    @staticmethod
    def db_for_read(self, model, **hints):
        return 'db' if app_label(model) in DATA_MODELS else None

    @staticmethod
    def db_for_write(self, model, **hints):
        return 'db' if app_label(model) in DATA_MODELS else None

    @staticmethod
    def allow_migrate(self, db, app_label_name, model_name=None, **hints):
        # with open('log/db.log', 'a') as log:
        #     log.write(f'{db}-{app_label}-{db == "db" if app_label in DATA_MODELS else db == "default"}\n')
        if app_label_name in DATA_MODELS:
            return db == 'db'
        else:
            return db == 'default'


def app_label(model):
    return model._meta.app_label
