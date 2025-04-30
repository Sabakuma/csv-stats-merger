# csv-stats-merger
When merging csv stats.

# CSV Merger

A simple Python script to merge CSV files from different folders based on a specified filename. The script reads all CSV files with the given name in the current directory's subfolders, adds the source folder name as a new column, and saves the merged result into a new CSV file.

## Features

- Prompts the user for a CSV filename (e.g., `xxxxxx.csv`).
- Merges all matching CSV files found in subfolders.
- Adds a new column indicating the source folder for each row.
- Saves the merged data into a new CSV file.

## Requirements

- Python 3.x
- pandas library

You can install the required library using pip:

```bash
pip install pandas
```

## Usage

1. Clone the repository or download the script.
2. Navigate to the directory containing the script.
3. Run the script:

```bash
python csv_merger.py
```

4. When prompted, enter the filename of the CSV you want to merge (e.g., `data.csv`).
5. The merged file will be saved as `data_merged.csv` in the current directory.

## Example

If you have the following folder structure:

```
.
├── folder1
│   └── data.csv
├── folder2
│   └── data.csv
└── folder3
    └── data.csv
```

After running the script and entering `data.csv`, the output will be a merged CSV file with an additional column named `source_folder` indicating the folder from which each row originated.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
