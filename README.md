# 🔐 Password Manager

A simple and secure desktop password manager built with Python and Tkinter. Generate strong passwords, store them safely, and retrieve them easily!

## ✨ Features

- **Strong Password Generation**: Creates secure passwords with letters, numbers, and symbols
- **Local Storage**: Passwords saved locally in JSON format
- **Search Functionality**: Quickly find saved passwords by website
- **Auto-copy**: Generated passwords are automatically copied to clipboard
- **User-friendly GUI**: Clean and intuitive interface

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

### Required Libraries

```bash
pip install pyperclip
```

*Note: `tkinter` and `json` come pre-installed with Python*

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add a logo image named `logo.png` to the project directory (optional)

4. Run the application:
```bash
python password_manager.py
```

## 🎯 How to Use

1. **Generate Password**: Click "Generate Password" to create a strong password
2. **Save Password**: Enter website name, email, and password, then click "Add"
3. **Search Password**: Enter website name and click "Search" to retrieve saved credentials
4. **Auto-fill Email**: Default email is pre-filled (you can change it in the code)

## 📁 File Structure

```
password-manager/
├── password_manager.py    # Main application file
├── logo.png              # Application logo (optional)
├── data.json             # Password storage (created automatically)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🔒 Security Notes

- Passwords are stored locally in JSON format
- **Important**: This is a basic implementation for learning purposes
- For production use, consider:
  - Encrypting the JSON file
  - Using a master password
  - Implementing additional security measures

## 🛠️ Customization

- **Change default email**: Edit line 96 in `password_manager.py`
- **Modify password strength**: Adjust ranges in the `password_generator()` function
- **Update UI colors**: Modify the `fg` and `bg` parameters in the UI setup section

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- Logo image must be present or code will throw an error
- No master password protection
- Data stored in plain text

## 🔮 Future Enhancements

- [ ] Master password protection
- [ ] Data encryption
- [ ] Password strength indicator
- [ ] Export/import functionality
- [ ] Dark mode theme
- [ ] Cross-platform packaging

---

⭐ **If you found this project helpful, please give it a star!** ⭐
