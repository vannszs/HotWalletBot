<h1 align="center">
  <br>
  <a href="https://github.com/your-username/your-repository"><img src="https://static.herewallet.app/intro.35bf1b5e.png" alt="HotWallet Automation Bot" width="200"></a>
  <br>
  HotWallet Automation Bot
  <br>
</h1>

<h4 align="center">Automate your interactions with the HotWallet web application using this Python script powered by Selenium.</h4>


<a align="center" href="https://ibb.co/y6qSHfp"><img src="https://i.ibb.co/Wkftmx0/Screenshot-2024-02-07-152813.png" alt="Screenshot-2024-02-07-152813" border="0"></a>

## ⚡️ Key Features

* **Seed Input**: Reads the seed from the `seed.txt` file. If the file is empty, prompts the user for input and saves it to `seed.txt`.
* **Initial Login**: Enters the seed, handles login, and navigates through the initial steps.
* **Periodic Check**: Periodically checks if the condition "Full" appears on a specific page. If true, waits for 2 hours before checking again.
* **Automated Claim**: Performs a series of automated clicks on specific elements based on predefined XPaths.

## 🚀 How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) (which comes with [pip](https://pypi.org/project/pip/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/your-username/your-repository

# Go into the repository
$ cd your-repository

# Install dependencies
$ pip install -r requirements.txt

# Run the script
$ python your_script.py
