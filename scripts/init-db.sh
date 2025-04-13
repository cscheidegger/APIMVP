
#!/bin/bash
set -e

# Initialize database if needed
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Create extensions if not exists
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    
    -- Ensure the database is set up correctly for the application
    -- Most schema creation will be handled by Alembic migrations
    CREATE TABLE IF NOT EXISTS alembic_version (
        version_num VARCHAR(32) NOT NULL PRIMARY KEY
    );
EOSQL

echo "Database initialization complete."
