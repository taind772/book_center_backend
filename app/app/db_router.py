DATA_MODELS = ['myapi']

class Router:
    def db_for_read(self, model, **hints):
        return 'db' if app_label(model) in DATA_MODELS else None

    def db_for_write(self, model, **hints):
        return 'db' if app_label(model) in DATA_MODELS else None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return False if db in DATA_MODELS else True


def app_label(model):
  return model._meta.app_label