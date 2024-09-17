# 📥 Instagram Video Upload & Download 📤

A Python script to **download** videos from any Instagram account and **upload** them to your own account using `Instaloader` and `Instagrapi`.

## 🚀 Features

- **Download Videos**: Fetch all videos from a specified Instagram user 📸.
- **Upload Videos**: Post downloaded videos to your Instagram account 📤.
- **Retry Failed Uploads**: Automatically retry uploads that failed 🚀.
- **Account Status Check**: Optional function to verify account status (if applicable) ✅.

## 🛠 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/instagram-video-upload-download.git
    cd instagram-video-upload-download
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:

    Copy `.env.example` to `.env` and update it with your Instagram credentials and user ID:

    ```bash
    cp .env.example .env
    ```

5. **Run the Script**:

    ```bash
    python instaloader_instagrapi_script.py
    ```

## 💡 Usage

1. **Update `instaloader_instagrapi_script.py`**:
    - Replace placeholders in the `.env` file with your Instagram username, password, and target user ID.

2. **Run the Script**:
    - Ensure you have the necessary permissions and that your Instagram account is not restricted.

## 🤝 Contributing

Contributions are welcome! Please submit a pull request with your changes.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Instaloader](https://github.com/instaloader/instaloader) for video downloading 🎥.
- [Instagrapi](https://github.com/adw0rd/instagrapi) for video uploading 📤.
