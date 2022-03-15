class BaseDriver:
    def __init__(obj, type):
        self.obj = obj
        self.type = type

    def save(self):
        raise NotImplementedError()

    def load(self):
        raise NotImplementedError()

class CsvDriver:
    def save(self, fname):
        import pandas as pd
        assert isinstance(self.obj, pd.DataFrame)

        self.obj.to_csv(fname)

    def load(self, fname):
        import pandas as pd
        return pd.read_csv(fname)


class FeatherDriver:
    def save(self, fname):
        import pandas as pd
        assert isinstance(self.obj, pd.DataFrame)

        self.obj.to_feather(fname)

    def load(self, fname):
        import pandas as pd
        return pd.read_feather(fname)


class JoblibDriver:
    def save(self, fname):
        import joblib

        joblib.dump(obj, fname)

    def load(self, fname):
        import joblib

        return joblib.load(open(fname, "rb"))
