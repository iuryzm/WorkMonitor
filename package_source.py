import os
import zipfile

def package_source():
    output_filename = "WorkMonitor_Source.zip"
    
    # Files and directories to include
    includes = [
        'core',
        'ui',
        'tests',
        'main.py',
        'WorkMonitor.spec',
        'requirements.txt',
        'README.md',
        'LICENSE',
        'CHANGELOG.md',
        'build_linux.sh',
        'build_windows.bat'
    ]
    
    # Files to exclude specifically (if they happen to be in the root check)
    excludes = [
        'work_log.csv',
        'settings.json',
        output_filename
    ]

    print(f"Creating {output_filename}...")
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in includes:
            if not os.path.exists(item):
                print(f"Warning: {item} not found, skipping.")
                continue
                
            if os.path.isfile(item):
                zipf.write(item)
                print(f"Added file: {item}")
            elif os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    # Remove __pycache__ from traversal
                    if '__pycache__' in dirs:
                        dirs.remove('__pycache__')
                    
                    for file in files:
                        if file.endswith('.pyc') or file == '.DS_Store':
                            continue
                        
                        file_path = os.path.join(root, file)
                        # Archive names should be relative to project root
                        zipf.write(file_path)
    
    print(f"\nSuccessfully created {output_filename}!")

if __name__ == "__main__":
    package_source()
