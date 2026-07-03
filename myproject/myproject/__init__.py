# Enable PyMySQL as a drop-in replacement for MySQLdb if available
try:
    import pymysql  # type: ignore[import-untyped]
    # Tell Django that we have a supported version of mysqlclient
    pymysql.version_info = (2, 2, 1, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
