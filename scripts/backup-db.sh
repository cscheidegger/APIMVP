
#!/bin/bash
set -e

# Configuration
BACKUP_DIR="/app/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/proteuslab_backup_${TIMESTAMP}.sql"

# Ensure backup directory exists
mkdir -p ${BACKUP_DIR}

# Create backup
echo "Creating database backup..."
pg_dump -h postgres -U postgres -d proteuslab > ${BACKUP_FILE}

# Compress backup
echo "Compressing backup..."
gzip ${BACKUP_FILE}

# Clean up old backups (keep last 7)
echo "Cleaning up old backups..."
ls -tp ${BACKUP_DIR}/*.sql.gz | grep -v '/$' | tail -n +8 | xargs -I {} rm -- {}

echo "Backup completed: ${BACKUP_FILE}.gz"
