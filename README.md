
# WordFinder - Terminal Word Search Tool 🚀

WordFinder is a colorful, handy, and robust Python application that lets you quickly and easily search for words and find their meanings right in your terminal.

---

## Features

- **Fast and responsive** word searching
- Colorful and readable terminal interface (uses the `rich` library)
- Works with a database in `dataset.parquet` format
- User-friendly warnings on empty inputs and faulty file issues
- Easy exit with `Ctrl+C` or commands like `q/exit`
- Clean, simple, and extensible codebase

---

## Requirements

- Python 3.8+
- Pandas
- Rich
- PyArrow (for reading Parquet files)

---

## Installation

```bash
pip install pandas rich pyarrow
```

---

## Usage

1. Clone or download the project:
    ```bash
    git clone https://github.com/hakankygsz/wordfinder.git
    cd wordfinder3000
    ```

2. Place your `dataset.parquet` file inside the project folder.

3. Run the application:
    ```bash
    python word_search.py
    ```

4. Type your word in the terminal and instantly see the meanings!

5. To exit, type `q`, `exit`, `quit` or press `Ctrl+C`.

---

## Dataset Creation (Optional)

If you don't have a ready dataset, you can create one using this small script:

```python
import pandas as pd

data = {
    'word': ['apple', 'banana', 'orange', 'grape', 'lemon'],
    'meaning': ['Elma', 'Muz', 'Portakal', 'Üzüm', 'Limon']
}

df = pd.DataFrame(data)
df.to_parquet('dataset.parquet')
```

---

## Contact

For any questions, suggestions, or contributions, reach me at [hakankaygusuzdev@gmail.com](mailto:hakankaygusuzdev@gmail.com).

---

## License

MIT License © 2025 Hakan

---

🚀 Don't get lost in the word world, explore it with **wordfinder**!
