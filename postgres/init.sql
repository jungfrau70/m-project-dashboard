SELECT 'CREATE DATABASE mytestdb'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mytestdb')\gexec