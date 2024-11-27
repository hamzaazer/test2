# Student Management System

A comprehensive student management system built with Python and Flet, featuring:

- Student information management
- Attendance tracking
- Grade management
- Mobile-friendly interface
- Offline-first data storage

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Building Mobile App

The application can be built for Android using GitHub Actions. The workflow will automatically:

1. Build the application when code is pushed to main branch
2. Create a release with the APK file
3. Upload the APK as a release asset

To build manually:

```bash
flet build apk
```

## Features

- Student Management
  - Add/Edit/Delete students
  - Track academic details
  - Organize by class and group

- Attendance Tracking
  - Mark daily attendance
  - View attendance history
  - Generate reports

- Grade Management
  - Record and track grades
  - Calculate averages
  - Track performance over time

## License

MIT License