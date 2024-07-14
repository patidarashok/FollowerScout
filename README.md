# Follower Scout

Follower Scout is a powerful tool designed to filter Instagram followers based on custom criteria. With an intuitive interface built using CustomTkinter, users can easily select a file of usernames and filter followers by specifying minimum and maximum follower counts. The tool uses `requests` and `BeautifulSoup` to fetch follower counts directly from Instagram profiles.

## Features

- **File Selection:** Select a text file containing Instagram usernames.
- **Custom Filtering:** Filter users based on a specified range of follower counts.
- **Immediate Saving:** Save filtered users to a text file instantly.
- **User-Friendly Interface:** Intuitive and attractive UI built with CustomTkinter.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Canyildiz1386/follower-scout.git
   cd follower-scout
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Select a text file containing Instagram usernames.

3. Specify the minimum and maximum follower counts for filtering.

4. Save the filtered users to a new text file.

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- customtkinter

## Example

```plaintext
Select File: users.txt
Min Followers: 100
Max Followers: 1000

Filtered users saved to filtered_users.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Demo Video

<video width="320" height="240" controls>
  <source src="https://github.com/Canyildiz1386/FollowerScout/blob/master/FollowerScout.mkv" type="video/mkv">
  Your browser does not support the video tag.
</video>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [can.yildiz.1386@gmail.com](mailto:can.yildiz.1386@gmail.com).

---


### Future Plans

- Add multi-threading support for faster processing.
- Implement more advanced filtering options.
- Enhance UI with more customization options.

---

Developed with ❤️ by [Canyildiz1386](https://github.com/Canyildiz1386)

