# Video Streaming Website

This is a video streaming website built using the Flask framework. It allows users to watch episodes of shows from a MySQL database. The website provides a simple and intuitive interface for browsing and watching content.

## Features

- Browse and view available shows.
- Watch episodes of selected shows.
- Navigate between episodes using next and previous buttons.
- Dynamic URL routing for accessing specific shows and episodes.

## Setup

### Requirements

- Python 3.x
- Flask
- MySQL database
- `mysql-connector-python`
- `flask-sitemap`

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/guyoverclocked/FlaskVideoStreamer
   ```
2. Install the required packages:
```sh
pip install flask mysql-connector-python flask-sitemap
```
3. Set up the MySQL database with the necessary tables and data.
4. Update the database connection details in app.py (user, password, host, database).

## Usage
Run the application:
```sh
python app.py
```
The application will be accessible at http://localhost:5000.

## File Structure
-  app.py: The main Flask application file.
-  templates/: Directory containing HTML templates (index.html, home.html, player.html).
-  static/: Directory containing static files (CSS, JavaScript, images).

## License
This project is licensed under the MIT License.
```sh
Feel free to update the database connection details, file paths, and other configurations as per your requirements. Let me know if there's anything else you'd like to add or modify! 
```


