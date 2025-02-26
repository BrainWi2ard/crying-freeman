# Data Extraction App

This project demonstrates a comprehensive data extraction solution using advanced web scraping techniques, regex validation, adversarial attacks, variable analysis, and more. It extracts data from various sources, performs fuzzy matching to validate the information, and ensures compliance with GDPR and CCPA regulations.

## Features
- Advanced web scraping using `requests`, `BeautifulSoup`, `Selenium`, `Scrapy`, and `Regex`
- Regex validation for CVV, PAN, debit/credit cards, ISIN, SSN, VIN, Driver's ID, etc.
- Adversarial attacks (Data poisoning, Evasion attacks, Model inversion, Model stealing, Privacy attacks, Abuse attacks)
- Fuzzy matching with `fuzzywuzzy`
- Configurable data sources and user input
- Saving extracted information as PDF/DOC files
- Robust error handling and rate limiting

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/BrainWi2ard/crying-freeman.git
    cd crying-freeman
    ```

2. **Set Up Virtual Environment (optional but recommended):**

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Libraries:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download Models:**

    ```sh
    python download_models.py
    ```

## Usage

1. **Run the Program:**

    ```sh
    python main.py
    ```

2. **Access the UI:**

    ```sh
    python ui/app.py
    ```

    Open your browser and go to `http://127.0.0.1:5000/`.

## Configuration

Edit the `config.py` file to update user input and data source URLs.
