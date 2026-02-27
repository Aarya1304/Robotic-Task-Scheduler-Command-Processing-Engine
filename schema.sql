-- =====================================================
-- Smart Lab Equipment Automation Simulator
-- Database Schema
-- =====================================================

-- Table to store machine command history
CREATE TABLE IF NOT EXISTS machine_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Command sent to machine (START, STOP, CALIBRATE)
    command TEXT NOT NULL,

    -- Machine response (ACK, ERROR, etc.)
    status TEXT NOT NULL,

    -- Timestamp for traceability
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Optional index to improve lookup performance
CREATE INDEX IF NOT EXISTS idx_machine_logs_command
ON machine_logs(command);