Weather App

 Description

A Python-based Weather Application that provides real-time weather information for any city using a weather API.

Features

* Search weather by city name
* Current temperature
* Humidity information
* Wind speed details
* Weather condition display
* Weather history tracking

Technologies Used

* Python
* Requests Library
* Weather API
* File Handling

Project Structure

```text
weather_app/
│
├── app.py
├── config.py
├── requirements.txt
├── weather_history.txt
├── README.md
```

Installation

1. Clone the repository

```bash
git clone https://github.com/ayush18105/synent-task6-weatherapp-aayushrana.git
```

2. Navigate to the project directory

```bash
cd synent-task6-weatherapp-aayushrana
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

Configuration

Add your Weather API key inside `config.py`.

Example:

```python
API_KEY = "YOUR_API_KEY"
```

Run the Application

```bash
python app.py
```

Sample Output

```text
Enter City Name: Surat

Temperature: 32°C
Humidity: 68%
Wind Speed: 12 km/h
Condition: Clear Sky
```

Author

Aayush Rana

Computer Engineering Student

LDRP Institute of Technology & Research
