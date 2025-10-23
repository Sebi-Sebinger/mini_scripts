# Time Tracking Scripts

A simple shell-based time tracking system for the command line.

## Description

These scripts allow you to track working time for different jobs/projects and generate reports:

- **`time_tracker`**: Main script for time tracking with timer functions
- **`time_summary`**: Script for calculating monthly summaries

## Installation

1. Copy both scripts to a directory of your choice
2. Make them executable:
   ```bash
   chmod +x time_tracker time_summary
   ```
3. Optional: Add directory to PATH or copy scripts to `/usr/local/bin/`

## Configuration

The data directory can be customized via the `TIMETRACKING_DIR` environment variable:

```bash
export TIMETRACKING_DIR="/path/to/your/timedata"
```

**Default**: `~/.timetracking/`

## Usage

### Start time tracking
```bash
./time_tracker
```

### Timer mode functions
- `s` - Start timer
- `p` - Pause/resume timer  
- `e` - End timer and save time
- `u` - Show timer status
- `h` - Show help

### Monthly summary
```bash
./time_summary [job_name]
```

Without parameters, all jobs are evaluated; with a parameter, only the specified job.

## Data Structure

The scripts create the following files in the data directory:

```
~/.timetracking/
├── jobs.txt                    # List of all jobs
├── Monthly-Summary.txt         # Monthly evaluations
├── Job_Name_1.txt              # Time entries for Job 1
└── Job_Name_2.txt              # Time entries for Job 2
```

## Features

- ✅ Job management (create, delete, list)
- ✅ Timer with start/pause/stop functionality
- ✅ Automatic rounding to quarter hours
- ✅ Monthly evaluation
- ✅ Real-time display of running time
- ✅ Persistent data storage

## System Requirements

- zsh Shell
- Standard Unix tools (date, awk, bc, sed, grep)
- Linux/macOS/WSL

## License

These scripts are available under a free license.