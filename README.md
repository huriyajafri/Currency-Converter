# Currency Converter Application

#### Video Demo: https://youtu.be/pQlVxWAWNeo?feature=shared

#### Description:
The Currency Converter Application is a Python-based GUI tool designed to facilitate quick and easy currency conversions. Built using the Tkinter library for the graphical interface and the `requests` library for fetching real-time exchange rates, this application provides an intuitive user experience.

### Project Overview

The main purpose of this project is to provide users with a simple and efficient way to convert amounts between different currencies. The application fetches the latest exchange rates from a public API and performs conversions based on user input.

### Application Features
- **Real-time Exchange Rates:** The application fetches up-to-date exchange rates from the ExchangeRate-API, ensuring accurate conversions.
- **Intuitive User Interface:** The GUI is designed with user-friendliness in mind, making it easy for users of all backgrounds to use the application without any prior knowledge.
- **Validation:** The application includes input validation to ensure users provide valid amounts and select valid currencies, enhancing the overall reliability of the tool.

### Files and Their Functions

- **project.py:** This is the core file of the project, containing the main application logic. It includes functions for fetching available currencies, getting exchange rates, performing conversions, and validating user inputs. The GUI is also constructed in this file, leveraging Tkinter for the interface.
- **test_project.py:** This file contains unit tests for the application functions. Using the `pytest` framework , it tests the accuracy and reliability of the core functions without depending on real-time data from the API.
- **requirements.txt:** This file lists the dependencies required to run the project, including `requests`, `pytest`, and `Pillow` for image processing.
- **README.md:** The file you are currently reading, providing an overview and detailed description of the project.

### Design Choices

#### User Interface
The user interface is designed using Tkinter to provide a simple and intuitive layout. A background image is used to enhance the visual appeal of the application. Key design choices include:

- **Label and Entry Placement:** Labels and entry fields are positioned to be easily accessible and readable, with sufficient spacing to avoid a cluttered appearance.
- **Font Choices:** Fonts are chosen for readability, with different font sizes to distinguish between headings, labels, and entry fields.

#### Functionality
- **Real-time Data:** By using a public API for exchange rates, the application ensures that users always get the most current conversion rates.
- **Input Validation:** Input validation is implemented to handle common user errors, such as non-numeric values or unsupported currencies, providing appropriate error messages.

### Conclusion

The Currency Converter Application is a practical tool designed to simplify currency conversions with a user-friendly interface and reliable functionality. Through careful design and robust testing, it aims to offer a seamless experience for users needing quick and accurate currency conversions.

By leveraging Python's libraries and adhering to best practices in software development, this project demonstrates how a seemingly simple application can provide significant utility through thoughtful design and implementation.

### Future Enhancements
- **Additional Currencies:** Expanding the list of supported currencies to cover a wider range of international currencies.
- **Historical Data:** Including the ability to view historical exchange rates for users interested in trends over time.
- **Enhanced UI:** Further refining the user interface for better accessibility and aesthetics.

This project reflects a commitment to creating useful tools through clear, maintainable code and an emphasis on user experience. Feel free to explore the codebase, provide feedback, and contribute to its development.
