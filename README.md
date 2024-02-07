# 🚀 HotWallet Wallet Automation Bot

Welcome to the Telegram Wallet Automation Bot repository! This Python script, empowered by Selenium, automates interactions with the HotWallet web application.

## 📝 Description

Experience the convenience of automation! This script handles various tasks, from entering a seed and managing login to claiming rewards based on specific conditions, all utilizing Selenium's capabilities to manipulate the Telegram wallet web interface.

## ⚙️ Installation and Setup

1. **Clone Repository**: Clone this repository to your local machine.
2. **Python and Libraries**: Ensure Python is installed and run `pip install selenium.
3. **Browser Setup**: Configure ChromeDriver and set its path in the `driver_path` variable.
4. **Run Script**: Execute the Python script via terminal or command prompt.

## ⭐ Features

| Features               | Description                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------|
| 🌱 Seed Input           | Reads the seed from the `seed.txt` file. If the file is empty, prompts the user for input and saves it to `seed.txt`.                        |
| 🌐 Initial Login        | Enters the seed, handles login, and navigates through the initial steps.                           |
| 🔄 Periodic Check       | Periodically checks if the condition "Full" appears on a specific page. If true, waits for 2 hours before checking again.|
| 🛒 Automated Claim     | Performs a series of automated clicks on specific elements based on predefined XPaths.               |

## 📄 License

This project is licensed under the MIT License. For details, refer to the [LICENSE](LICENSE) file.

## 🤝 Contributing

Contributions are welcomed! Fork the repository, make your changes, and create a pull request.

## 📞 Contact

For inquiries or support, feel free to reach out via email or open an issue in the repository.

## 🙌 Acknowledgements

- [OpenAI](https://github.com/openai) for providing inspiration for automation endeavors.
- Tutorial sources and online communities that contributed to the development of these scripts.
