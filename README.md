

---

# My First Bedrock Project 🚀

A simple Python project demonstrating how to use **Amazon Bedrock** to generate text with a large language model.

---

## 🧠 About The Project

This project serves as a foundational example for building **generative AI applications** on AWS.
It uses the `boto3` library to authenticate with **Amazon Bedrock** and invoke a pre-trained language model — such as **Anthropic’s Claude** — to answer a text prompt.

### ✨ Key Features

* **Secure Authentication**: Uses environment variables for credential management.
* **Simple API Call**: Demonstrates an easy way to invoke a Bedrock model.
* **Error Handling**: Includes a `try...except` block for handling common exceptions.

### 🛠️ Built With

* Python 3.10+
* Boto3 (AWS SDK for Python)
* Amazon Bedrock

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### ✅ Prerequisites

* An AWS account
* AWS credentials with Bedrock access permissions
* Access to a Bedrock model (e.g., `anthropic.claude-3-sonnet-20240229-v1:0`) — request access via the AWS Management Console

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. **Create a Python virtual environment** and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install boto3
   ```

---

## 🔐 Configuration

Set your **AWS credentials** as environment variables.
👉 **Never hardcode them** in your scripts.

### On macOS/Linux:

```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
export AWS_SESSION_TOKEN="YOUR_SESSION_TOKEN"
```

### On Windows (Command Prompt):

```cmd
set AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
set AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
set AWS_SESSION_TOKEN=YOUR_SESSION_TOKEN
```

> 💡 Tip: You can also use **PowerShell** with `$env:` syntax:
>
> ```powershell
> $env:AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
> $env:AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
> $env:AWS_SESSION_TOKEN="YOUR_SESSION_TOKEN"
> ```

---

## ▶️ Usage

To run the text generation script, execute the following command in the same terminal session where you set your credentials:

```bash
python3 text_generator.py
```

---

Would you like me to also include a **sample `text_generator.py` script** that demonstrates how to call the Bedrock model using `boto3`?
It’ll make your project immediately runnable.
