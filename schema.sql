-- =====================================================
-- Robotic Task Scheduler & Command Engine
-- Database Schema
-- =====================================================

-- Task lifecycle tracking table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Robotic command (MOVE_ARM, PICK_OBJECT, ROTATE, etc.)
    command TEXT NOT NULL,

    -- Execution status (PENDING, RUNNING, COMPLETED, FAILED)
    status TEXT NOT NULL,

    -- Priority for scheduling
    priority INTEGER DEFAULT 1,

    -- Retry counter
    retry_count INTEGER DEFAULT 0,

    -- Timestamp tracking
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Index to optimize status-based filtering
CREATE INDEX IF NOT EXISTS idx_tasks_status
ON tasks(status);

-- Index to optimize priority scheduling
CREATE INDEX IF NOT EXISTS idx_tasks_priority
ON tasks(priority);